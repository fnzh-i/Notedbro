"""Local content scan for publish and ship. No network calls."""

import getpass
import os
import re
from pathlib import Path

import workspace_map

IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".bmp"}
EMAIL = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
PHONE = re.compile(r"(?<![\w.-])(?:\+?\d{1,3}[ .-])?\(?\d{3}\)?[ .-]\d{3}[ .-]\d{4}(?![\w.-])")
SAMPLE_TERMS = {"SAMPLE-EMPLOYER", "SAMPLE-CLIENT", "SAMPLE-NAME"}
MIN_TERMS = 3
LOCAL_LINE = "Scan ran locally. Nothing was sent anywhere."
MAINTAINER_MESSAGE = (
    "Maintainer only: fnsh publish builds a public copy from a private vault. "
    "You don't need it. To share a change, use fnsh ship."
)
DENYLIST_MESSAGE = "Edit your denylist first. It still has the sample words."
SHORT_DENYLIST = "Edit your denylist first. It needs at least three terms that are not samples."
PRIVATE_PREFIXES = (
    ".notedbro-local/",
    ".claude/settings.local.json",
    ".claude/hooks/notedbro.py",
    "Personal/",
    "Plans/",
    "Skill files/",
    ".obsidian/",
    "_Scripts/host-restore/",
)
KNOWN_PRIVATE_TOP = {
    "Personal", "Work", "Collaboration", "Hackathons", "Research", "Plans",
    "Skill files", ".obsidian",
    ".notedbro-local",
}
PUBLIC_REPO = "https://github.com/fnzh-i/Notedbro"
PUBLIC_API = "https://api.github.com/repos/fnzh-i/Notedbro"
ALLOWED_URL = re.compile(
    "(?:" + re.escape(PUBLIC_REPO) + "|" + re.escape(PUBLIC_API) + ")"
    + r"[A-Za-z0-9/._#?=&-]*"
)


def token_patterns():
    """Built at runtime so this file does not contain a live secret shape."""
    ghp = "gh" + "p_"
    sk = "s" + "k-"
    akia = "AK" + "IA"
    header = "-----BEGIN " + "PRIVATE KEY-----"
    return (
        (re.compile(re.escape(ghp) + r"[A-Za-z0-9]{8,}"), "token", ghp),
        (re.compile(re.escape(sk) + r"[A-Za-z0-9]{8,}"), "token", sk),
        (re.compile(re.escape(akia) + r"[A-Z0-9]{8,}"), "token", akia),
        (re.compile(re.escape(header)), "private key", "key"),
    )


def mask(value, prefix):
    if prefix == "key":
        return "-----BEGIN ****"
    shown = value[: len(prefix)]
    return shown + "****"


def term_pattern(term):
    body = r"\s+".join(re.escape(part) for part in term.split())
    if term.endswith("-"):
        return re.compile(r"(?<![A-Za-z0-9_])" + body)
    return re.compile(r"(?<![A-Za-z0-9_])" + body + r"(?![A-Za-z0-9_])", re.I)


def read_terms(path):
    path = Path(path)
    if not path.is_file():
        return []
    terms = []
    for line in path.read_text(errors="replace").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            terms.append(line)
    return terms


def denylist_problems(path):
    """Refuse a missing, still-sample, or too-short denylist. Does not create anything."""
    path = Path(path)
    if not path.is_file():
        return [DENYLIST_MESSAGE]
    terms = read_terms(path)
    if any(term in SAMPLE_TERMS for term in terms):
        return [DENYLIST_MESSAGE]
    real = [term for term in terms if term not in SAMPLE_TERMS]
    if len(real) < MIN_TERMS:
        return [SHORT_DENYLIST]
    return []


def maintainer_ready(vault, denylist):
    if not Path(denylist).is_file():
        return False
    found = workspace_map.load_map(vault)
    if not found.get("maintainer"):
        return False
    return any(rule == "notedbro" and folder for _project, rule, folder in found.get("ships", []))


def map_terms(vault):
    found = workspace_map.load_map(vault)
    if not found["path"] or Path(found["path"]).name != "Workspace map.md":
        return []
    terms = []
    if found["company"]:
        terms.append(found["company"])
    if found["ticket_key"]:
        terms.append(found["ticket_key"] + "-")
    terms += [name for _path, name, _area in found["workspaces"]]
    terms += found["projects"]
    terms += [name for name in found["param_sets"] if name not in ("main", "example")]
    return terms


def iter_files(root):
    root = Path(root)
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(name for name in dirnames if name != ".git")
        for name in sorted(filenames):
            yield Path(dirpath) / name


def _line_hits(text, terms, home, login, product_name, allow_product):
    patterns = []
    seen = set()
    for term in terms:
        if term and term.lower() not in seen:
            seen.add(term.lower())
            patterns.append((term, term_pattern(term)))
    hits = []
    for number, line in enumerate(text.splitlines(), start=1):
        kinds = []
        for match in EMAIL.finditer(line):
            kinds.append("email (" + mask(match.group(0), match.group(0)[:2]) + ")")
        if PHONE.search(line):
            kinds.append("phone")
        if home and home in line:
            kinds.append("home folder")
        if login.search(line):
            kinds.append("login name")
        if product_name and not allow_product and re.search(
            r"(?<![A-Za-z0-9_])" + re.escape(product_name) + r"(?![A-Za-z0-9_])", line
        ):
            kinds.append(f"{product_name} outside the title")
        for pattern, label, prefix in token_patterns():
            for match in pattern.finditer(line):
                kinds.append(f"{label} ({mask(match.group(0), prefix)})")
        for term, pattern in patterns:
            if pattern.search(line):
                kinds.append(f"denylist ({term})")
        for kind in kinds:
            hits.append((number, kind))
    return hits


def scan(root, terms, product="", allow_product_paths=(), allowed_url=None):
    """Return 'path:line: kind' lines. Images are not text-scanned."""
    home = str(Path.home())
    login_name = getpass.getuser()
    login = re.compile(
        r"(?<![A-Za-z0-9_-])" + re.escape(login_name) + r"(?![A-Za-z0-9_-])"
    )
    allowed = set(allow_product_paths)
    hits = []
    for path in iter_files(root):
        rel = path.relative_to(root).as_posix()
        if path.suffix.lower() in IMAGE_SUFFIXES:
            continue
        try:
            text = path.read_bytes().decode("utf-8", errors="replace")
        except OSError:
            hits.append(f"{rel}: unreadable")
            continue
        if allowed_url is None:
            allowed_url = ALLOWED_URL
        text = allowed_url.sub("", text)
        allow = rel in allowed or rel.startswith("assets/") or rel.startswith("_Scripts/")
        for number, kind in _line_hits(text, terms, home, login, product, allow):
            hits.append(f"{rel}:{number}: {kind}")
    return hits


def scan_text(text, terms, allowed_url=None):
    """Scan one string. Returns 'line: kind' hits."""
    if allowed_url is None:
        allowed_url = ALLOWED_URL
    text = allowed_url.sub("", text)
    return [f"{number}: {kind}" for number, kind in _line_hits(
        text, terms, str(Path.home()), re.compile(
            r"(?<![A-Za-z0-9_-])" + re.escape(getpass.getuser()) + r"(?![A-Za-z0-9_-])"
        ), None, True
    )]


def scan_text_hits(text, terms):
    return [term for term in terms if term_pattern(term).search(text)]


def manifest_path(vault):
    return Path(vault) / "_Scripts" / "starter-manifest.txt"


def read_manifest(vault):
    path = manifest_path(vault)
    files, dirs = [], []
    if not path.is_file():
        return files, dirs
    for line in path.read_text(errors="replace").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.endswith("/"):
            dirs.append(line)
        else:
            files.append(line)
    return files, dirs


def rel_path(rel):
    """Drop a ./ prefix only. Do not strip leading dots from .gitignore."""
    while rel.startswith("./"):
        rel = rel[2:]
    return rel


def in_manifest(rel, files, dirs):
    rel = rel_path(rel)
    if rel in files:
        return True
    return any(rel.startswith(folder) for folder in dirs)


def is_private_path(rel):
    rel = rel_path(rel)
    if rel == "Workspace map.md":
        return True
    return any(rel == prefix[:-1] or rel.startswith(prefix) for prefix in PRIVATE_PREFIXES)
