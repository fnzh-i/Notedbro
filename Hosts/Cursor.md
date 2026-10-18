---
tags: [meta]
---
# Cursor

Profile for [[Hosts]]. Shared rules stay in [[How this vault works]].

- Auto-file: hook. The stop hook calls `Scripts/file-session`.
- That hook fires after every reply. The filer refiles only after `refile_min_new_turns` new turns.
- Transcript: the local Cursor transcript path, passed in by the hook.
- `~/.cursor/hooks/brain-reminder.py` is shared. Only the session stub and the old reminder are removed.
- `fnsh load cursor` restores a missing `hooks.json` entry and a missing hook file. A hook file that is already there is left as it is. The in-app user rule is not a file here. When the hook is restored, paste the block in [[Hosts/Web]] into that rule.
- At the start step, apply [[Preferences]] rows whose scope matches this chat. If that note cannot be read, apply no rows and stay silent.
