# Security

## Reporting a problem
Report a vulnerability through GitHub private vulnerability reporting: open the Security tab of https://github.com/fnzh-i/Notedbro and choose "Report a vulnerability". Do not open a public issue for it.

## Supported versions
Fixes land on main. Release 1.1.0 remains a candidate until the verification gates in Maintainer guide.md pass.

## Scope
Setup, structural checks, migration comparison, scanning, and view generation run locally. Upgrade checks request GitHub release metadata. Ship fetches/pushes Git data and can create a GitHub pull request after confirmation; maintainer sync fetches GitHub changes. An explicitly configured filer model sends cleaned user-message excerpts to Anthropic. Backup dependency installation may download through Homebrew.

Setup writes selected host configuration: local Claude settings inside Brain, Cursor user hook files, or marked Codex global instructions. Backups and lock files stay in the ignored .notedbro-local folder. Existing unrelated settings are preserved. Local storage does not prevent an AI host from sending context it reads to its provider.

Generated .claude/settings.local.json and the local hook are ignored and excluded from publication. Shared .claude/settings.json is preserved. Ignoring a file does not remove it from prior Git history. The content scanner remains active and detects common sensitive patterns, not every possible secret.

Never commit notes, keys, or `Workspace map.md`.
