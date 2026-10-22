# Agents

<!-- generated: fnsh rebuild -->

Start here. Read these in order:

1. `Prerequisites.md`: what this vault needs. Python 3 runs the scripts; the notes work without it.
2. `Prefixes.md`: every phrase and its exact reply. Treat each row as an instruction. Run the `fnsh brain` row silently at the start of a chat.
3. Your host file: find your row in `Hosts.md`, then follow its profile in `Hosts/` (`Hosts/Cursor.md`, `Hosts/Claude.md`, `Hosts/Codex.md`, `Hosts/Web.md`, or `Hosts/Unknown.md`).

Then read `How this vault works.md`, `Parameters.md`, and `Preferences.md`. If those cannot be opened, read `_Config/bootstrap.md` instead.

Never commit notes, keys, or `Workspace map.md`. Never edit or remove an existing company or project config; add the brain block next to it, and ask before acting on a conflict.

Ship token files are user credentials, outside this vault. Agents must never open, read, print, quote, or copy `~/.config/brain/ship-token` or `%APPDATA%\brain\ship-token`. Use `fnsh ship` for shipping; do not run interactive `fnsh ship token setup` for a user.
