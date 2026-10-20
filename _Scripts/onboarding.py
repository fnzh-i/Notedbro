"""Local setup primitives shared by setup, restoration, and migration checks."""
import ast
import hashlib
import json
import os
from pathlib import Path
import re
import shlex
import subprocess
import tempfile

START = "<!-- brain:start -->"
END = "<!-- brain:end -->"
PRIVATE = ("/.claude/settings.local.json", "/.claude/hooks/notedbro.py", "/.notedbro-local/", "/Workspace map.md", "/_Scripts/host-restore/")
MINIMAL_MAP = """---
tags: [meta]
---
# Workspace map

Personal use is ready. Unmatched chats go to Personal/Chats/Sessions.
Add project routing later using Workspace map.advanced.example.md.

## Workspaces
| Path | Project | Area |
|---|---|---|

## Maintainer
- maintainer: no
"""


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def safe_destination(path):
    path = Path(path).absolute()
    if any(part.is_symlink() for part in (path, *path.parents)):
        raise ValueError(f"Symlink destination requires manual review: {path}")
    return path


def tracked(root, path):
    try:
        rel = Path(path).absolute().relative_to(Path(root).absolute())
    except ValueError:
        return False
    result = subprocess.run(["git", "-C", str(root), "ls-files", "--error-unmatch", "--", str(rel)], capture_output=True)
    return result.returncode == 0


def write(root, path, text, events, private=False):
    path = safe_destination(path)
    if private and tracked(root, path):
        rel = path.relative_to(root).as_posix()
        raise ValueError(f"Tracked private destination: {rel}. Before rerunning, use git rm --cached -- {shlex.quote(rel)}. Existing history is unaffected.")
    data = text.encode() if isinstance(text, str) else text
    old = path.read_bytes() if path.exists() else None
    if old == data:
        return
    if old is not None:
        token = hashlib.sha256(str(path).encode() + old).hexdigest()
        backup = safe_destination(Path(root) / ".notedbro-local" / "backups" / token / path.name)
        backup.parent.mkdir(parents=True, mode=0o700, exist_ok=True)
        if not backup.exists():
            backup.write_bytes(old)
            backup.chmod(0o600)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=".notedbro-", dir=str(path.parent))
    try:
        with os.fdopen(fd, "wb") as out:
            out.write(data)
        if old is not None:
            os.chmod(temporary, path.stat().st_mode & 0o777)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
    if path.read_bytes() != data:
        raise ValueError(f"Readback failed: {path}")
    events.append(f"{'Repaired' if old is not None else 'Created'}: {path}")


def ignore_rules(root, events):
    path = Path(root) / ".gitignore"
    if not path.is_file():
        raise ValueError(".gitignore is missing. Restore the shipped ignore file before running setup; no personal files were prepared.")
    text = path.read_text()
    missing = [item for item in PRIVATE if item not in text.splitlines()]
    if missing:
        write(root, path, text.rstrip() + "\n" + "\n".join(missing) + "\n", events)


def corrected(text):
    text = re.sub(r"(?<![\w/])Templates/Session\.md", "_Templates/Session.md", text)
    return re.sub(r"(?<![\w/])Scripts/file-session", "_Scripts/file-session", text)


def map_readiness(root):
    import workspace_map
    found = workspace_map.load_map(root)
    samples = found["company"] == "Example" or found["ticket_key"] == "EX" or any("/Code/example" in path for path, _, _ in found["workspaces"])
    return ["Example routing is still active in Workspace map.md. Replace or remove the example company, ticket, and workspace sections, then rerun setup."] if samples else []


def instruction_block(root):
    text = (Path(root) / "Hosts" / "Web.md").read_text()
    if START not in text or END not in text:
        raise ValueError("Hosts/Web.md is missing the marked instruction block")
    block = text[text.index(START):text.index(END) + len(END)]
    return corrected(block).replace("~/Documents/Brain/", str(Path(root).resolve()) + "/") + "\n"


def install_instructions(root, path, events):
    text = path.read_text() if path.exists() else ""
    if text.count(START) != text.count(END) or text.count(START) > 1:
        raise ValueError(f"Malformed instruction markers: {path}")
    if START in text:
        # Repair only recognized defects in the existing block; retain custom instructions.
        a, b = text.index(START), text.index(END) + len(END)
        block = corrected(text[a:b]).replace("~/Documents/Brain/", str(Path(root).resolve()) + "/")
        updated = text[:a] + block + text[b:]
    else:
        updated = text.rstrip() + "\n\n" + instruction_block(root)
    write(root, path, updated.lstrip("\n"), events)


def wrapper(root, host):
    return (
        '#!/usr/bin/env python3\n"""Generated Notedbro hook; personal configuration."""\n'
        'import os\nimport subprocess\nimport sys\n'
        f'BRAIN_ROOT = {str(Path(root).resolve())!r}\n'
        f'FILER = {str(Path(root).resolve() / "_Scripts" / "file-session")!r}\n'
        'if __name__ == "__main__":\n'
        '    env = dict(os.environ, BRAIN_VAULT=BRAIN_ROOT)\n'
        f'    raise SystemExit(subprocess.run([sys.executable, FILER, "--hook", {host!r}], input=sys.stdin.read(), text=True, env=env).returncode)\n'
    )


def read_settings(path):
    if not path.exists():
        return {}
    obj = json.loads(path.read_text())
    if not isinstance(obj, dict) or not isinstance(obj.get("hooks", {}), dict):
        raise ValueError(f"Malformed hook configuration: {path}")
    return obj


def wrapper_shape(text):
    tree = ast.parse(text)
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name) and node.targets[0].id in ("FILER", "BRAIN_ROOT"):
            node.value = ast.Constant(value="PATH")
    return ast.dump(tree, include_attributes=False)


def generated_wrapper(text, root, host):
    try:
        return wrapper_shape(text) == wrapper_shape(wrapper(root, host))
    except SyntaxError:
        return False


def install_claude(root, events):
    root = Path(root).resolve()
    ignore_rules(root, events)
    path = root / ".claude" / "settings.local.json"
    safe_destination(path)
    if tracked(root, path):
        raise ValueError(".claude/settings.local.json is tracked. Run git rm --cached -- .claude/settings.local.json before setup. Check history separately.")
    obj = read_settings(path)
    hooks = obj.setdefault("hooks", {})
    entries = hooks.setdefault("SessionEnd", [])
    if not isinstance(entries, list):
        raise ValueError(f"SessionEnd must be a list: {path}")
    hook = root / ".claude" / "hooks" / "notedbro.py"
    if hook.exists() and not generated_wrapper(hook.read_text(), root, "claude"):
        raise ValueError(f"Custom hook at generated destination requires manual review: {hook}")
    command = "python3 -I " + shlex.quote(str(hook))
    if any(not isinstance(item, dict) or not isinstance(item.get("hooks", []), list) for item in entries):
        raise ValueError(f"Malformed SessionEnd hook entry: {path}")
    known = [item for item in entries if any(h.get("command") == command for h in item.get("hooks", []) if isinstance(h, dict))]
    if not known:
        entries.append({"hooks": [{"type": "command", "command": command, "timeout": 45}]})
    elif len(known) > 1:
        raise ValueError(f"Duplicate local Notedbro hook entries: {path}; retain one before rerunning")
    write(root, hook, wrapper(root, "claude"), events, private=True)
    write(root, path, json.dumps(obj, indent=2) + "\n", events, private=True)


def _literal(node, home):
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == "expanduser" and len(node.args) == 1:
        return _literal(node.args[0], home)
    raise ValueError("dynamic path")


def expand_home(raw, home):
    if raw == "~":
        return str(home)
    return str(home / raw[2:]) if raw.startswith("~/") else raw


def inspect_hook(command, root, home):
    """Conservative static inspection. Never execute a hook to discover its target."""
    tokens = shlex.split(command)
    overrides = {}
    if tokens[:1] == ["env"]:
        tokens.pop(0)
    while tokens and "=" in tokens[0]:
        key, val = tokens.pop(0).split("=", 1)
        if key != "BRAIN_VAULT":
            raise ValueError("unrecognized environment assignment")
        overrides[key] = val
    if not tokens or Path(tokens[0]).name not in ("python", "python3"):
        raise ValueError("unrecognized hook command")
    args = tokens[1:]
    if args[:1] == ["-I"]:
        args.pop(0)
    if not args:
        raise ValueError("missing wrapper")
    target = Path(expand_home(args[0], home))
    if not target.is_absolute():
        raise ValueError("relative legacy wrapper needs manual review")
    target = target.resolve(strict=True)
    effective = None
    if target.name == "file-session" and args[1:] == ["--hook", "claude"]:
        filer = target
    elif len(args) == 1:
        tree = ast.parse(target.read_text())
        source = Path(__file__).with_name("load-host").read_text()
        legacy_template = next(node.value.value for node in ast.parse(source).body if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "THIN_HOOK" for t in node.targets))
        allowed = (legacy_template.format(kind="Session-end", hook="claude"), wrapper(root, "claude"))
        if wrapper_shape(target.read_text()) not in [wrapper_shape(item) for item in allowed]:
            raise ValueError("custom wrapper cannot be verified statically")
        values = {}
        for node in tree.body:
            if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                key = node.targets[0].id
                if key in ("FILER", "BRAIN_ROOT"):
                    values[key] = _literal(node.value, home)
        filer = Path(expand_home(values["FILER"], home)).resolve(strict=True)
        effective = values.get("BRAIN_ROOT")
    else:
        raise ValueError("unrecognized hook arguments")
    destination = Path(expand_home(effective or overrides.get("BRAIN_VAULT") or os.environ.get("BRAIN_VAULT") or str(filer.parent.parent), home)).resolve()
    expected = Path(root).resolve() / "_Scripts" / "file-session"
    if filer != expected.resolve() or destination != Path(root).resolve():
        raise ValueError(f"legacy filer {filer}; destination {destination}; must target {expected} and {root}")
    # An explicit marker plus current release checksum is required, not the filename.
    manifest = Path(__file__).with_name("release-runtime.sha256")
    if not manifest.is_file():
        raise ValueError("release runtime checksums missing")
    expected_hash = next((line.split("  ", 1)[0] for line in manifest.read_text().splitlines() if line.endswith("  _Scripts/file-session")), None)
    if not expected_hash or digest(filer) != expected_hash:
        raise ValueError(f"legacy hook reaches an old or modified filer: {filer}")
    return f"Duplicate delivery protected: {target} -> {filer}"


def legacy_hooks(root, home):
    issues, protected = [], []
    config_home = Path(os.environ.get("CLAUDE_CONFIG_DIR", str(Path(home) / ".claude")))
    paths = list(dict.fromkeys([config_home / "settings.json", Path(home) / ".claude/settings.json", Path(root) / ".claude/settings.json", Path(root) / ".claude/settings.local.json"]))
    for path in paths:
        if not path.exists():
            continue
        try:
            obj = read_settings(path)
            for event, entries in obj.get("hooks", {}).items():
                if not isinstance(entries, list):
                    raise ValueError(f"{event} must be a list")
                for entry in entries:
                    for hook in entry.get("hooks", []):
                        command = hook.get("command", "")
                        if not any(word in command.lower() for word in ("brain", "notedbro", "file-session")):
                            continue
                        try:
                            verified = inspect_hook(command, root, Path(home))
                            if path != Path(root) / ".claude/settings.local.json":
                                protected.append(verified)
                        except (ValueError, OSError, KeyError, SyntaxError) as error:
                            issues.append(f"Legacy hook migration required in {path} ({event}): {command}\n  {error}. Remove only this Notedbro entry or update its wrapper to the current filer; rerun setup.")
        except (ValueError, OSError, AttributeError) as error:
            issues.append(f"Cannot inspect legacy settings {path}: {error}")
    return issues, protected
