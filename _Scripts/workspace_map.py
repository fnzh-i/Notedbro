"""Read Workspace map.md: the private folders, projects, and ticket key.

Falls back to Workspace map.example.md, then to an empty map. Shared notes
and scripts carry no real names; everything real is read from here.
"""
import os
import re

MAP_NAME = "Workspace map.md"
EXAMPLE_NAME = "Workspace map.example.md"
_CACHE = {}


def empty_map():
    return {
        "path": "",
        "company": "",
        "ticket_key": "",
        "workspace": "",
        "daily_date_only": True,
        "workspaces": [],
        "project_aliases": {},
        "projects": [],
        "param_sets": {},
        "prefix_aliases": [],
        "maintainer": False,
        "ships": [],
    }


def map_path(vault):
    for name in (MAP_NAME, EXAMPLE_NAME):
        path = os.path.join(vault, name)
        if os.path.isfile(path):
            return path
    return ""


def sections(text):
    found = {}
    current = None
    for line in text.splitlines():
        heading = re.match(r"^##\s+(.+?)\s*$", line)
        if heading:
            current = heading.group(1).strip().lower()
            found[current] = []
        elif current is not None:
            found[current].append(line)
    return found


def table_rows(lines):
    rows = []
    for line in lines:
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [cell.strip().strip("`") for cell in line.strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells if cell):
            continue
        rows.append(cells)
    return rows[1:]


def list_items(lines):
    return [line.strip()[2:].strip().strip("`") for line in lines if line.strip().startswith("- ")]


def expand(path):
    return os.path.normpath(os.path.expanduser(path)) if path else ""


def parse(text):
    found = empty_map()
    parts = sections(text)
    for item in list_items(parts.get("company", [])):
        key, _, value = item.partition(":")
        key = key.strip().lower()
        value = value.strip().strip("`")
        if key == "name":
            found["company"] = value
        elif key == "ticket key":
            found["ticket_key"] = value.upper()
        elif key == "workspace":
            found["workspace"] = expand(value)
        elif key == "daily":
            found["daily_date_only"] = value.lower() != "date and company"
    for row in table_rows(parts.get("workspaces", [])):
        if len(row) >= 3 and row[0] and row[1]:
            found["workspaces"].append((expand(row[0]), row[1], row[2].lower()))
    for row in table_rows(parts.get("project aliases", [])):
        if len(row) >= 2 and row[0] and row[1]:
            found["project_aliases"][row[0].lower()] = row[1]
    found["projects"] = [item for item in list_items(parts.get("extra projects", [])) if item]
    for row in table_rows(parts.get("parameter sets", [])):
        if len(row) >= 2 and row[0]:
            found["param_sets"][row[0].lower()] = row[1]
    for row in table_rows(parts.get("prefix aliases", [])):
        if len(row) >= 2 and row[0] and row[1]:
            found["prefix_aliases"].append((row[0].lower(), row[1]))
    for item in list_items(parts.get("maintainer", [])):
        key, _, value = item.partition(":")
        if key.strip().lower() == "maintainer" and value.strip().lower() == "yes":
            found["maintainer"] = True
    for row in table_rows(parts.get("ship", [])):
        if len(row) >= 3 and row[0] and row[1]:
            base = row[3].strip().lower() if len(row) >= 4 and row[3] else "staging"
            found["ships"].append((row[0], row[1].strip().lower(), expand(row[2]), base))
    return found


def load_map(vault):
    path = map_path(vault)
    if not path:
        return empty_map()
    try:
        stamp = os.stat(path).st_mtime_ns
    except OSError:
        return empty_map()
    cached = _CACHE.get(path)
    if cached and cached[0] == stamp:
        return cached[1]
    with open(path, encoding="utf-8") as handle:
        found = parse(handle.read())
    found["path"] = path
    _CACHE[path] = (stamp, found)
    return found
