# Notedbro

<p align="center">
  <img src="assets/branding/notedbro.png" alt="Notedbro" width="238">
</p>

A starter kit for Brain: a Markdown vault that gives your AI agents—Cursor, Claude Code, Codex, and web chats—a memory that outlives the chat. Each session ends with one short note, so you can always recall it later.

It is just an Obsidian template. There is nothing to install and no database, so it also works with ChatGPT, Claude, and Gemini.

[How to set up](How%20to%20set%20up.md) · [Prerequisites](Prerequisites.md) · [Contributing](CONTRIBUTING.md) · [Design](DESIGN.md)

<p align="center">
  <a href="https://github.com/fnzh-i/Notedbro/actions/workflows/ci.yml"><img src="https://github.com/fnzh-i/Notedbro/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
</p>

<p align="center">
  <img src="assets/branding/screenshot.png" alt="Screenshot">
</p>

A fork of a public repository is public. Keep real notes in a private copy.

`fnsh upgrade check` and `fnsh upgrade` contact GitHub. `fnsh ship` fetches from Git and checks GitHub authentication and existing pull requests during preview; it pushes files only after confirmation.

## Why I built it

About a month ago, I lost an AI chat session. It expired, and I couldn't remember what was in it. The decisions, fixes, and reasoning were all gone. I built Brain so that never happens to me again, and I'm sharing it so it doesn't happen to you either.

## Benefits

- **Memory that outlives your chats.** Every session leaves a short note, so you can recall it later even after the chat expires.
- **Works with any AI.** It is plain Markdown in Obsidian, so you aren't locked into one tool.
- **No install, no database.** Open the folder in Obsidian and run `fnsh brain` at the start of a chat.
- **Light and fast.** The vault stays small and loads quickly, even after months of sessions.
- **Private by default.** Your notes stay on your machine.
- **Safe to share.** Built-in checks help keep personal information and secrets out of anything you publish.

## Why it doesn't store whole conversations

Saving every full chat would make the vault grow quickly and become heavy. I want Brain to stay light for people who have limited storage.

Instead, `fnsh update` writes a short session note—what was asked and what changed—and stores only the path to the transcript. You keep the useful summary in your vault, while the full chat stays wherever your AI tool keeps it.

## Make it yours

Brain is a starting point, not a fixed system. You can configure it however you want:

- Review `Preferences.md` for response style and behavior, and `Parameters.md` for standing rules, limits, paths, and other values. The entries shipped with the starter kit are my usable defaults; keep, edit, or remove any of them to make Brain yours.
- Edit `Prefixes.md` to add, rename, or remove `fnsh` commands.
- Change what a session note contains, such as more detail, less detail, or different headings.
- Add your own folders for projects, school, or work. Unknown folders are treated as private by default.
- If you want full transcripts, you can configure your own Brain to keep them. The default stays light.

## About the content scan

The scan runs only on your machine. It looks for things like API keys, emails, phone numbers, and your home-folder path so you don't accidentally publish them.

It does not collect, copy, store, or send anything: no tokens, personal information, logs, or network calls. When it finds something, it shows you the file and line on your own screen and stops.

It exists for your safety, and you stay in control. The content scan sends nothing. Ship checks GitHub authentication and existing pull requests during preview; files leave your computer only after you review the preview and say yes.

`fnsh ship` and `fnsh guard` only protect actions performed through `fnsh`. Plain `git push` and `git add -f` are outside their reach.

## First steps

1. Open the folder in Obsidian.
2. Copy `Workspace map.example.md` to `Workspace map.md` and fill it in.
3. Run `fnsh brain`.

Using an existing project? You don't need a new vault. Make a project note for it, and its sessions will collect there.

- [Prerequisites](Prerequisites.md): what to install
- [How to set up](How%20to%20set%20up.md): clone to the first `Brain ready`
- [Security](SECURITY.md): how to report a problem privately
- [Contributing](CONTRIBUTING.md): pull-request rules
- [Design](DESIGN.md): why it is built this way

Pull requests go to https://github.com/fnzh-i/Notedbro.

## What is in the repo

- **Shared notes:** `How this vault works.md`, `How to use the brain.md`, `Prefixes.md`, `Parameters.md`, `Preferences.md`, `Hosts.md`, `Hosts/`, `Terms.md`, and `Graph colors.md`. These contain the rules every agent reads.
- **`AGENTS.md`:** where an agent starts. `CLAUDE.md` points to it.
- **`_Templates/`:** one template for each note type, including sessions, decisions, tickets, daily notes, and areas.
- **`_Scripts/`:** the session filer, `check-vault`, shadow backup, publish, sync, and rebuild scripts. They use Python 3 and require no packages.
- **`_Config/`:** the generated bootstrap page. Do not edit it by hand.
- **`Workspace map.example.md`:** copy it to `Workspace map.md` and add your real folders, projects, and ticket key.
- **Hub notes:** `Work/Example/Example.md`, `Collaboration/Collaboration.md`, `Hackathons/Hackathons.md`, `Research/Research.md`, `Personal/Personal.md`, and `Personal/Chats/Chats.md`. Other files under `Personal/` belong to the user and are not included in the starter kit.

## What not to commit

- Your notes. `.gitignore` ignores everything under the five areas except the hub notes. Never use `git add -f` to add a note.
- `Workspace map.md`, keys, `.env` files, or shadow copies.
- Anything containing your name, employer, email address, or phone number.
