"""Read and manage Ship's one user-owned credential outside the vault."""

import ctypes
import getpass
import os
import stat
import sys
import tempfile
import warnings
from pathlib import Path


def token_path():
    if sys.platform == "win32":
        appdata = os.environ.get("APPDATA")
        if not appdata:
            raise RuntimeError("APPDATA is unavailable; cannot locate the Ship token file.")
        return Path(appdata) / "brain" / "ship-token"
    return Path.home() / ".config" / "brain" / "ship-token"


def _inside(path, vault):
    root = Path(vault).resolve()
    target = path.resolve(strict=False)
    return target == root or root in target.parents


def _reparse(path):
    try:
        info = path.lstat()
    except FileNotFoundError:
        return False
    return path.is_symlink() or bool(getattr(info, "st_file_attributes", 0) & 0x400)


def _win_sid_and_descriptor(handle):
    """Return current SID, owner SID, and effective allow-ACE SIDs for a handle."""
    from ctypes import wintypes

    adv = ctypes.WinDLL("advapi32", use_last_error=True)
    kernel = ctypes.WinDLL("kernel32", use_last_error=True)
    kernel.GetCurrentProcess.restype = wintypes.HANDLE
    kernel.CloseHandle.argtypes = [wintypes.HANDLE]
    kernel.LocalFree.argtypes = [ctypes.c_void_p]
    kernel.LocalFree.restype = ctypes.c_void_p
    token = wintypes.HANDLE()
    adv.OpenProcessToken.argtypes = [wintypes.HANDLE, wintypes.DWORD, ctypes.POINTER(wintypes.HANDLE)]
    adv.OpenProcessToken.restype = wintypes.BOOL
    if not adv.OpenProcessToken(kernel.GetCurrentProcess(), 0x0008, ctypes.byref(token)):
        raise RuntimeError("cannot verify Windows token-file ownership.")
    try:
        needed = wintypes.DWORD()
        adv.GetTokenInformation.argtypes = [wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p, wintypes.DWORD, ctypes.POINTER(wintypes.DWORD)]
        adv.GetTokenInformation.restype = wintypes.BOOL
        adv.GetTokenInformation(token, 1, None, 0, ctypes.byref(needed))
        buf = ctypes.create_string_buffer(needed.value)
        if not adv.GetTokenInformation(token, 1, buf, needed, ctypes.byref(needed)):
            raise RuntimeError("cannot verify Windows token-file ownership.")
        current = ctypes.c_void_p.from_buffer(buf).value
        owner = ctypes.c_void_p()
        dacl = ctypes.c_void_p()
        descriptor = ctypes.c_void_p()
        adv.GetSecurityInfo.argtypes = [wintypes.HANDLE, ctypes.c_int, wintypes.DWORD,
            ctypes.POINTER(ctypes.c_void_p), ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p),
            ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p)]
        adv.GetSecurityInfo.restype = wintypes.DWORD
        status = adv.GetSecurityInfo(handle, 1, 0x5, ctypes.byref(owner), None,
                                     ctypes.byref(dacl), None, ctypes.byref(descriptor))
        if status or not dacl.value:
            raise RuntimeError("cannot verify Windows token-file permissions.")
        adv.EqualSid.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
        adv.EqualSid.restype = wintypes.BOOL
        if not adv.EqualSid(current, owner):
            raise RuntimeError("Ship token path must be owned by the current user.")
        count = ctypes.c_ushort.from_address(dacl.value + 4).value
        adv.GetAce.argtypes = [ctypes.c_void_p, wintypes.DWORD, ctypes.POINTER(ctypes.c_void_p)]
        adv.GetAce.restype = wintypes.BOOL
        allowed = []
        for index in range(count):
            ace = ctypes.c_void_p()
            if not adv.GetAce(dacl, index, ctypes.byref(ace)):
                raise RuntimeError("cannot verify Windows token-file permissions.")
            ace_type = ctypes.c_ubyte.from_address(ace.value).value
            flags = ctypes.c_ubyte.from_address(ace.value + 1).value
            if ace_type not in (0, 1):
                raise RuntimeError("Ship token file has an unsupported Windows access rule.")
            if ace_type == 0:
                allowed.append((ace.value + 8, flags))
        return _sid_string(current, adv), [(_sid_string(sid, adv), flags) for sid, flags in allowed]
    finally:
        kernel.CloseHandle(token)
        if "descriptor" in locals() and descriptor.value:
            kernel.LocalFree(descriptor)


def _sid_string(sid, adv):
    from ctypes import wintypes
    result = wintypes.LPWSTR()
    adv.ConvertSidToStringSidW.argtypes = [ctypes.c_void_p, ctypes.POINTER(wintypes.LPWSTR)]
    adv.ConvertSidToStringSidW.restype = wintypes.BOOL
    if not adv.ConvertSidToStringSidW(ctypes.c_void_p(sid), ctypes.byref(result)):
        raise RuntimeError("cannot verify Windows token-file permissions.")
    try:
        return result.value
    finally:
        kernel = ctypes.WinDLL("kernel32")
        kernel.LocalFree.argtypes = [ctypes.c_void_p]
        kernel.LocalFree.restype = ctypes.c_void_p
        kernel.LocalFree(result)


def _win_check(path, directory=False, repair=False):
    from ctypes import wintypes

    kernel = ctypes.WinDLL("kernel32", use_last_error=True)
    kernel.CloseHandle.argtypes = [wintypes.HANDLE]
    kernel.CreateFileW.argtypes = [wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD,
        ctypes.c_void_p, wintypes.DWORD, wintypes.DWORD, wintypes.HANDLE]
    kernel.CreateFileW.restype = wintypes.HANDLE
    flags = 0x00200000 | (0x02000000 if directory else 0)  # OPEN_REPARSE_POINT, BACKUP_SEMANTICS
    handle = kernel.CreateFileW(str(path), 0x00020000, 0x7, None, 3, flags, None)
    if handle == ctypes.c_void_p(-1).value:
        raise RuntimeError("cannot verify Windows token-file permissions.")
    try:
        if _reparse(path):
            raise RuntimeError("Ship token path is a link or reparse point; remove it manually.")
        try:
            current, allowed = _win_sid_and_descriptor(handle)
        except RuntimeError as error:
            if "owned by" in str(error):
                raise RuntimeError(f"Ship token path must be owned by you; run takeown /f \"{path}\" in Command Prompt.") from None
            raise
        if repair:
            return
        for sid, flags in allowed:
            if sid == current:
                continue
            if sid in ("S-1-5-18", "S-1-5-32-544") and flags & 0x10:
                continue
            raise RuntimeError("Ship token path grants access to another user; run py _Scripts/ship token setup to replace it safely.")
    finally:
        kernel.CloseHandle(handle)


def _win_secure(path, directory=False):
    """Set the current user as owner and sole effective ACL entry in-process."""
    from ctypes import wintypes

    adv = ctypes.WinDLL("advapi32", use_last_error=True)
    kernel = ctypes.WinDLL("kernel32", use_last_error=True)
    kernel.GetCurrentProcess.restype = wintypes.HANDLE
    kernel.CloseHandle.argtypes = [wintypes.HANDLE]
    kernel.LocalFree.argtypes = [ctypes.c_void_p]
    kernel.LocalFree.restype = ctypes.c_void_p
    token = wintypes.HANDLE()
    adv.OpenProcessToken.argtypes = [wintypes.HANDLE, wintypes.DWORD, ctypes.POINTER(wintypes.HANDLE)]
    adv.OpenProcessToken.restype = wintypes.BOOL
    if not adv.OpenProcessToken(kernel.GetCurrentProcess(), 0x0008, ctypes.byref(token)):
        raise RuntimeError("cannot secure the Windows Ship token file.")
    try:
        needed = wintypes.DWORD()
        adv.GetTokenInformation.argtypes = [wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p, wintypes.DWORD, ctypes.POINTER(wintypes.DWORD)]
        adv.GetTokenInformation.restype = wintypes.BOOL
        adv.GetTokenInformation(token, 1, None, 0, ctypes.byref(needed))
        buf = ctypes.create_string_buffer(needed.value)
        if not adv.GetTokenInformation(token, 1, buf, needed, ctypes.byref(needed)):
            raise RuntimeError("cannot secure the Windows Ship token file.")
        sid = _sid_string(ctypes.c_void_p.from_buffer(buf).value, adv)
    finally:
        kernel.CloseHandle(token)
    # Set owner and DACL together.  A newly created directory can inherit an
    # unexpected owner from a CI temporary directory, so DACL-only repair is
    # insufficient before token bytes are written.
    sddl = "O:" + sid + "D:P(A;" + ("OICI" if directory else "") + ";FA;;;" + sid + ")"
    descriptor = ctypes.c_void_p()
    adv.ConvertStringSecurityDescriptorToSecurityDescriptorW.argtypes = [wintypes.LPCWSTR, wintypes.DWORD, ctypes.POINTER(ctypes.c_void_p), ctypes.c_void_p]
    adv.ConvertStringSecurityDescriptorToSecurityDescriptorW.restype = wintypes.BOOL
    if not adv.ConvertStringSecurityDescriptorToSecurityDescriptorW(sddl, 1, ctypes.byref(descriptor), None):
        raise RuntimeError("cannot secure the Windows Ship token file.")
    try:
        adv.SetFileSecurityW.argtypes = [wintypes.LPCWSTR, wintypes.DWORD, ctypes.c_void_p]
        adv.SetFileSecurityW.restype = wintypes.BOOL
        if not adv.SetFileSecurityW(str(path), 0x5, descriptor):
            raise RuntimeError("cannot secure the Windows Ship token file.")
    finally:
        kernel.LocalFree(descriptor)


def validate_path(path, vault, *, existing=False, repair=False):
    path = Path(path)
    if _inside(path, vault):
        raise RuntimeError("Ship token file must be outside the vault.")
    if _reparse(path) or _reparse(path.parent) or _reparse(path.parent.parent):
        raise RuntimeError("Ship token path is a link or reparse point; remove it manually.")
    if existing and not path.exists():
        return False
    if path.exists() and not path.is_file():
        raise RuntimeError("Ship token path must be a regular file.")
    if path.parent.exists():
        if not path.parent.is_dir():
            raise RuntimeError("Ship token folder is not a directory.")
        if sys.platform == "win32":
            _win_check(path.parent, directory=True, repair=repair)
        else:
            info = path.parent.stat()
            if info.st_uid != os.getuid():
                raise RuntimeError("Ship token folder must be owned by you; run chown \"$USER\" ~/.config/brain.")
            if not repair and stat.S_IMODE(info.st_mode) != 0o700:
                raise RuntimeError("Ship token folder needs mode 0700; run chmod 700 ~/.config/brain.")
    if not path.exists():
        return False
    if sys.platform == "win32":
        _win_check(path, repair=repair)
    else:
        info = path.stat()
        if info.st_uid != os.getuid():
            raise RuntimeError("Ship token file must be owned by you; run chown \"$USER\" ~/.config/brain/ship-token.")
        if not repair and stat.S_IMODE(info.st_mode) != 0o600:
            raise RuntimeError("Ship token file needs mode 0600; run chmod 600 ~/.config/brain/ship-token.")
    return True


def read_token(path, vault):
    if not validate_path(path, vault, existing=True):
        return None
    if sys.platform == "win32":
        import msvcrt
        from ctypes import wintypes
        kernel = ctypes.WinDLL("kernel32", use_last_error=True)
        kernel.CloseHandle.argtypes = [wintypes.HANDLE]
        kernel.CreateFileW.argtypes = [wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD,
            ctypes.c_void_p, wintypes.DWORD, wintypes.DWORD, wintypes.HANDLE]
        kernel.CreateFileW.restype = wintypes.HANDLE
        handle = kernel.CreateFileW(str(path), 0x80020000, 0x7, None, 3, 0x00200000, None)
        if handle == ctypes.c_void_p(-1).value:
            raise RuntimeError("Ship token file could not be opened safely.")
        if _reparse(path):
            kernel.CloseHandle(handle)
            raise RuntimeError("Ship token path is a link or reparse point; remove it manually.")
        try:
            descriptor = msvcrt.open_osfhandle(handle, os.O_RDONLY | os.O_BINARY)
        except OSError:
            kernel.CloseHandle(handle)
            raise
    else:
        descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
    try:
        info = os.fstat(descriptor)
        if not stat.S_ISREG(info.st_mode):
            raise RuntimeError("Ship token path must be a regular file.")
        if sys.platform != "win32" and (info.st_uid != os.getuid() or stat.S_IMODE(info.st_mode) != 0o600):
            raise RuntimeError("Ship token file permissions changed; run chmod 600 ~/.config/brain/ship-token.")
        if info.st_size > 4096:
            raise RuntimeError("Ship token file is too large.")
        token = os.read(descriptor, 4097).decode("utf-8").strip()
    finally:
        os.close(descriptor)
    if not token:
        raise RuntimeError("Ship token file is empty; run the token setup command.")
    if any(char.isspace() for char in token):
        raise RuntimeError("Ship token file is malformed; run the token setup command.")
    return token


def setup(path, vault, validate, confirm=input, prompt=getpass.getpass):
    path = Path(path)
    exists = validate_path(path, vault, existing=True, repair=True)
    original_entry = path.lstat() if exists else None
    if exists:
        try:
            answer = confirm("Replace the existing Ship token file? [y/N] ")
        except (EOFError, KeyboardInterrupt):
            return "Ship token unchanged."
        if answer.strip().lower() != "y":
            return "Ship token unchanged."
    if not path.parent.exists():
        path.parent.mkdir(parents=True, mode=0o700)
        if sys.platform == "win32":
            _win_secure(path.parent, directory=True)
        else:
            path.parent.chmod(0o700)
    elif sys.platform == "win32":
        _win_secure(path.parent, directory=True)
    else:
        path.parent.chmod(0o700)
    validate_path(path, vault, repair=True)
    if prompt is getpass.getpass and not sys.stdin.isatty():
        raise RuntimeError("Ship token setup requires an interactive terminal with hidden input.")
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("error", getpass.GetPassWarning)
            token = prompt("GitHub Ship token: ").strip()
    except getpass.GetPassWarning:
        raise RuntimeError("Could not hide token input; use an interactive terminal.") from None
    except (EOFError, KeyboardInterrupt):
        return "Ship token unchanged."
    if not token or any(char.isspace() for char in token):
        raise RuntimeError("Ship token is empty or malformed.")
    account, expiry = validate(token)
    fd, temp_name = tempfile.mkstemp(prefix=".ship-token-", dir=str(path.parent))
    temp = Path(temp_name)
    try:
        if sys.platform == "win32":
            _win_secure(temp)
            _win_check(temp)
        else:
            os.fchmod(fd, 0o600)
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            fd = -1
            stream.write(token)
            stream.flush()
            os.fsync(stream.fileno())
        validate_path(path, vault, existing=True, repair=True)
        if path.exists() != exists:
            raise RuntimeError("Ship token destination changed during setup; nothing was replaced.")
        if original_entry is not None:
            current = path.lstat()
            if (current.st_dev, current.st_ino) != (original_entry.st_dev, original_entry.st_ino):
                raise RuntimeError("Ship token destination changed during setup; nothing was replaced.")
        os.replace(temp, path)
    finally:
        if fd >= 0:
            os.close(fd)
        temp.unlink(missing_ok=True)
    return f"Ship token saved for {account}. Expiry: {expiry or 'unknown'}."


def remove(path, vault, confirm=input):
    path = Path(path)
    if not validate_path(path, vault, existing=True, repair=True):
        return "No managed Ship token file exists."
    try:
        answer = confirm("Remove the managed Ship token file? [y/N] ")
    except (EOFError, KeyboardInterrupt):
        return "Ship token unchanged."
    if answer.strip().lower() != "y":
        return "Ship token unchanged."
    validate_path(path, vault, existing=True, repair=True)
    path.unlink()
    return "Managed Ship token file removed. Other configured credential sources may still be available."
