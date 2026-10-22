---
tags: [meta, claude]
---
# Claude

Profile for [[Hosts]]. Shared rules stay in [[How this vault works]].

- Run python3 _Scripts/setup claude in Terminal from Brain's root.
- Auto-file: project-local SessionEnd hook in .claude/settings.local.json.
- Start Claude at Brain's root, containing AGENTS.md and _Scripts. Subfolder launches and other repositories are outside the 1.1.0 support promise.
- Shared .claude/settings.json and global settings are preserved.
- The generated .claude/hooks/notedbro.py calls _Scripts/file-session with this Brain destination.
- Transcript: the session JSONL path supplied by Claude Code.
- Reinstallation through fnsh load claude uses the same local configuration and reports unresolved legacy global hooks.
- Two hook calls share duplicate protection only when they reach the same upgraded filer and Brain folder.
- Apply matching Preferences rows silently.
