"""Offline release comparison. Hash raw bytes; never infer stock content from version labels."""
import hashlib
from pathlib import Path, PurePosixPath
import shlex
import subprocess

BASE_COMMIT = "3183f11e60a48e8e7dbce4ef8e28267a5031862c"
SOURCE = Path(__file__).resolve().parent.parent
PROTECTED = {"Parameters.md", "Preferences.md", "Workspace map.md", "Index.md", "AGENTS.md", "CLAUDE.md", ".gitignore"}
EXECUTABLES = {"setup", "check-migration", "check-onboarding", "check-docs", "guard", "upgrade", "file-session", "load-host", "check-vault", "build-views", "build-bootstrap", "build-runtime-manifest"}


def read_manifest(path):
    hashes = {}
    for line in Path(path).read_text().splitlines():
        if not line or line.startswith("#"):
            continue
        checksum, rel = line.split("  ", 1)
        parts = PurePosixPath(rel).parts
        if len(checksum) != 64 or any(ch not in "0123456789abcdef" for ch in checksum) or not parts or rel.startswith("/") or ".." in parts or "\\" in rel or rel != PurePosixPath(rel).as_posix() or rel in hashes:
            raise ValueError(f"Invalid manifest entry: {line}")
        hashes[rel] = checksum
    return hashes


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def safe(root, rel):
    path = Path(root) / rel
    if any(item.is_symlink() for item in (path, *list(path.parents)[:len(PurePosixPath(rel).parts) - 1])):
        return False
    return True


def release_files(source=SOURCE):
    from publish_scan import read_manifest as starter_manifest, is_private_path, in_manifest
    files, dirs = starter_manifest(source)
    result = {}
    for path in Path(source).rglob("*"):
        rel = path.relative_to(source).as_posix()
        if ".git" in path.parts or "__pycache__" in path.parts or is_private_path(rel):
            continue
        if path.is_file() and not path.is_symlink() and in_manifest(rel, files, dirs):
            result[rel] = path
    return result


def compare(target, source=SOURCE):
    target, source = Path(target).resolve(), Path(source).resolve()
    if not target.is_dir():
        raise ValueError(f"Migration target does not exist: {target}")
    old = read_manifest(source / "_Scripts/migrations/v1.0.0.sha256")
    current = release_files(source)
    rows = []
    for rel in sorted(set(old) | set(current)):
        path, candidate = target / rel, current.get(rel)
        if not safe(target, rel) or path.is_symlink():
            state = "unknown"
        elif not path.exists():
            state = "missing"
        elif not path.is_file():
            state = "unknown"
        else:
            try:
                seen = sha(path)
                state = "already current" if candidate and seen == sha(candidate) else "stock v1.0.0" if seen == old.get(rel) else "modified"
            except OSError:
                state = "unknown"
        private = rel in PROTECTED or rel.startswith(("Personal/", "Work/", "Collaboration/", "Research/", "Hackathons/"))
        mode = bool(candidate and candidate.parent.name == "_Scripts" and candidate.name in EXECUTABLES and path.is_file() and not path.is_symlink() and not path.stat().st_mode & 0o111)
        rows.append({"path": rel, "state": state, "copy": candidate is not None and state in ("stock v1.0.0", "missing") and not private and rel != "_Scripts/notedbro-version", "mode": mode})
    # Unknown scripts must be reviewed rather than silently treated as release files.
    scripts = target / "_Scripts"
    if scripts.is_dir() and not scripts.is_symlink():
        for path in scripts.rglob("*"):
            rel = path.relative_to(target).as_posix()
            if path.is_file() and rel not in old and rel not in current and "__pycache__" not in path.parts and "host-restore" not in path.parts:
                rows.append({"path": rel, "state": "unknown", "copy": False, "mode": False})
    return rows


def runtime_problems(target, source=SOURCE):
    problems = []
    hashes = read_manifest(Path(source) / "_Scripts/release-runtime.sha256")
    for rel, expected in hashes.items():
        if rel == "_Scripts/notedbro-version":
            continue
        path = Path(target) / rel
        if not safe(target, rel) or not path.is_file() or path.is_symlink() or sha(path) != expected:
            problems.append(f"Runtime migration required: {rel}")
    return problems


def verify_baseline(source=SOURCE):
    hashes = read_manifest(Path(source) / "_Scripts/migrations/v1.0.0.sha256")
    tree = subprocess.run(["git", "-C", str(source), "ls-tree", "-r", "--name-only", BASE_COMMIT], capture_output=True, text=True, check=True)
    if set(tree.stdout.splitlines()) != set(hashes):
        raise ValueError("Historical manifest does not cover the released tree exactly")
    for rel, expected in hashes.items():
        data = subprocess.run(["git", "-C", str(source), "show", f"{BASE_COMMIT}:{rel}"], capture_output=True, check=True).stdout
        if hashlib.sha256(data).hexdigest() != expected:
            raise ValueError(f"Historical checksum differs: {rel}")
    return len(hashes)


def report(target, source=SOURCE):
    rows = compare(target, source)
    for row in rows:
        print(f"{row['state']}: {row['path']}" + (" (executable permission missing)" if row["mode"] else ""))
    print("\nEligible commands after making the backup described in Migration 1.1.0.md:")
    for row in rows:
        if row["copy"]:
            dest = Path(target).resolve() / row["path"]
            print(f"mkdir -p {shlex.quote(str(dest.parent))}")
            print(f"cp -p {shlex.quote(str(Path(source) / row['path']))} {shlex.quote(str(dest))}")
        if row["mode"] and row["state"] in ("stock v1.0.0", "already current"):
            print(f"chmod u+x {shlex.quote(str(Path(target).resolve() / row['path']))}")
    print("Version promotion is last: run the 1.1.0 setup from the extracted release with BRAIN_VAULT set to the existing installation.")
    return 1 if any(row["state"] in ("modified", "unknown") for row in rows) else 0
