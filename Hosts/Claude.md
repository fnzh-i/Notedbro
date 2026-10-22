---
tags: [meta, claude]
---
# Claude

Profile for [[Hosts]]. Shared rules stay in [[How this vault works]].

- Auto-file: hook. The session-end hook calls `Scripts/file-session`. The per-reply Stop hook does not.
- Transcript: the jsonl path under `~/.claude/projects`, passed in by the hook.
- The old stop-hook reminder is removed. The filer writes the session note and the Daily line.
- `fnsh load claude` restores a missing `CLAUDE.md`, `settings.json`, or hook file. A file that is already there only gains the brain block or the `SessionEnd` hook when that piece is absent.
- At the start step, apply [[Preferences]] rows whose scope matches this chat. If that note cannot be read, apply no rows and stay silent.
