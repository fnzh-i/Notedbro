# Prerequisites

Required:
- Git
- Python 3 (for the scripts only; the notes work without it)
- On Windows, use `py _Scripts/<script>` (or `python _Scripts/<script>`); on macOS/Linux, use `python3 _Scripts/<script>`.
- Obsidian or another markdown editor

Optional:
- Cursor, Claude Code, or Codex, to file chats automatically or with `fnsh update`
- age and zstd, for `fnsh shadow` encrypted backups (`brew install age zstd`)

The scripts default to `~/Documents/Brain`. To use a clone somewhere else, set `BRAIN_VAULT` to its path, for example `export BRAIN_VAULT=~/notes/Brain`. The Cursor and Claude hooks call `~/Documents/Brain/_Scripts/file-session`, so cloning to `~/Documents/Brain` is the simplest choice.
