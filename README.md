<p align="center">
  <img src="assets/branding/cerebro.png" alt="Cerebro" width="238">
</p>

<p align="center">
  A starter kit for Brain: a markdown vault that your AI agents (Cursor, Claude Code, Codex, and web chats) read for your rules, and file one short note into after each chat.
</p>

<p align="center">
  <a href="https://github.com/fnzh-i/Cerebro/actions/workflows/ci.yml"><img src="https://github.com/fnzh-i/Cerebro/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
</p>

<p align="center">
  <a href="How%20to%20set%20up.md">How to set up</a> ·
  <a href="Prerequisites.md">Prerequisites</a> ·
  <a href="CONTRIBUTING.md">Contributing</a> ·
  <a href="DESIGN.md">Design</a>
</p>

<p align="center">
  <img src="assets/branding/screenshot.png" alt="Screenshot">
</p>

---

A fork of a public repository is public. Keep real notes in a private copy.

Only `fnsh upgrade check` and `fnsh upgrade` use the network.

**About the content scan.** The scan runs only on your machine. It looks for things like API keys, emails, phone numbers and your home folder path so you don't accidentally publish them. It does not collect, copy, store, or send anything: no tokens, no personal information, no logs, no network calls. When it finds something, it shows you the file and line on your own screen and stops. It exists for your safety, and you stay in control: nothing leaves your computer until you review the preview and say yes.

`fnsh ship` and `fnsh guard` only protect actions made through `fnsh`. Plain `git push` and `git add -f` are outside their reach.

## First steps
1. Open the folder in Obsidian.
2. Copy `Workspace map.example.md` to `Workspace map.md` and fill it in.
3. Run `fnsh brain`.

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
- **Hub notes**: `Work/Example/Example.md`, `Collaboration/Collaboration.md`, `Hackathons/Hackathons.md`, `Research/Research.md`, `Personal/Personal.md`, and `Personal/Chats/Chats.md`. Other files under `Personal/` are yours. They are not in the starter kit.

## What not to commit
- Your notes. `.gitignore` ignores everything under the five areas except the hub notes. Never `git add -f` a note.
- `Workspace map.md`, keys, `.env`, and shadow copies.
- Anything with your name, employer, email, or phone number.
