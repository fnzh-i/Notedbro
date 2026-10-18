# Cerebro

A starter kit for Brain: a markdown vault that your AI agents (Cursor, Claude Code, Codex, and web chats) read for your rules, and file one short note into after each chat.

- [Prerequisites](Prerequisites.md): what to install
- [How to set up](How%20to%20set%20up.md): clone to first `Brain ready`
- [SECURITY](SECURITY.md): how to report a problem privately
- [CONTRIBUTING](CONTRIBUTING.md): pull request rules
- [DESIGN](DESIGN.md): why it is built this way

Pull requests go to https://github.com/fnzh-i/Cerebro.

## What is in the repo
- **Shared notes**: `How this vault works.md`, `How to use the brain.md`, `Prefixes.md`, `Parameters.md`, `Preferences.md`, `Hosts.md`, `Hosts/`, `Terms.md`, and `Graph colors.md`. These are the rules every agent reads.
- **`AGENTS.md`**: where an agent starts. `CLAUDE.md` points at it.
- **`_Templates/`**: one template per note type (session, decision, ticket, daily, area, and more).
- **`_Scripts/`**: the session filer, `check-vault`, the shadow backup, publish, sync, and rebuild. They use Python 3 and need no packages.
- **`_Config/`**: the generated bootstrap page. Do not edit it by hand.
- **`Workspace map.example.md`**: copy it to `Workspace map.md` and fill in your real folders, projects, and ticket key.
- **Five hubs**: `Work/Example/`, `Personal/`, `Collaboration/`, `Hackathons/`, and `Research/`. Each holds only its hub note.

## What not to commit
- Your notes. `.gitignore` ignores everything under the five areas except the hub notes. Never `git add -f` a note.
- `Workspace map.md`, keys, `.env`, and shadow copies.
- Anything with your name, employer, email, or phone number.
