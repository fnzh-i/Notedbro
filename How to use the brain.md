---
tags: [meta]
---
# How to use the brain

Notedbro supplies the kit; Brain is your folder of Markdown context. Setup instructions are in [[How to set up]]. A session card saves the useful result of a chat, not the entire conversation.

## Everyday use

For local hosts, send these phrases in the **AI chat**:

| Phrase | Purpose |
|---|---|
| fnsh brain | Check loaded instructions and report host/model/profile |
| fnsh update | Ask the local agent to save or update this chat's session card |
| fnsh check | Ask the agent to run structural checks |

Claude automatically files on SessionEnd when started at Brain's root. Cursor files through supported hooks after its user rule is installed. Codex uses manual filing. Browser chats require you to provide context and save the returned card yourself.

## Your first useful card

In a connected local chat, send fnsh brain, then ask: “Create a short checklist for my sample project and save it as a Markdown file.” After the change, send fnsh update; for Claude also exit the session normally to verify its hook.

With no configured project routing, the card appears under Personal/Chats/Sessions. Its sections should describe the request and the saved file:

```markdown
## Asked
Create a short checklist for my sample project.

## Changed
Created a Markdown checklist covering the next project steps.
```

The full card also records host, model, date, conversation identifier, and a transcript path when available. The local filer adds the card to its session index and adds one Daily entry when work changed.

For a browser chat, upload only the context needed, request a card in the session-template format, and save it yourself. There is no automatic index or Daily update in that manual workflow.

## Continue in a later chat

Give the new chat access to the relevant project or session card and ask it to continue from that context. Brain is not automatic semantic search, and fnsh brain does not load all historical conversations. Local fnsh load can recall recent cards for a host and restore supported missing configuration; see [[Prefixes]] for its precise behavior.

## Find and customize

Start at [[Index]]. Review [[Preferences]] for style and [[Parameters]] for standing rules and values. Setup creates a minimal private map; project routing and the complete example are described in [[Advanced configuration]].

Setup generates Decisions and sessions.canvas. It begins empty and updates as local sessions and decisions are filed. Open it in Obsidian if desired. Graph colors are optional manual settings; see [[Graph colors]]. The repository screenshot shows an established, customized installation.

## Ship pull-request transport

Ship uses `NOTEDBRO_SHIP_TOKEN` if you set it, then your managed token file (`~/.config/brain/ship-token` on macOS/Linux or `%APPDATA%\brain\ship-token` on Windows), then the OS credential store, then authenticated `gh`. It ignores `GITHUB_TOKEN` and `GH_TOKEN`, including when invoking `gh`. An unsafe, unreadable, empty, invalid, or expired selected token stops Ship without falling back to another identity.

Set up or renew the managed token with `python3 _Scripts/ship token setup` on macOS/Linux or `py _Scripts/ship token setup` on Windows (`python` also works when installed). This interactive command hides input, validates the token with GitHub, confirms before replacing an existing token, and saves it outside the vault with restricted permissions. `token status` shows the selected source, account, and available expiry date. `token remove` confirms before deleting only the managed file. Agents must not run setup because you must paste the token yourself. For an optional OS store, use macOS Keychain (`security add-generic-password -s notedbro-ship -a github -w`, with `-U` before `-w` for renewal), Linux Secret Service (`secret-tool store --label=Notedbro-Ship service notedbro-ship account github`), or Windows Credential Manager through Python `keyring` when installed.

Use a fine-grained GitHub token limited to repositories you ship, with Pull requests read/write. Contents write is not needed for Ship API calls; Git push uses separate Git credentials. Choose an expiry suitable for you and renew using `token setup` when needed. Ship warns five days before an expiry date GitHub provides, and reports an authentication failure with the current OS's renewal command. When GitHub provides no expiry date, status says `unknown`.

The token is used only for in-process Python `urllib` calls to GitHub's API. It is never passed in command arguments or a child-process environment. Git commits are local; `git push` uses your SSH or Git credential helper. Ship writes a token only to the managed file during your interactive setup, never to the vault, Workspace map, `report.md`, previews, recovery records, logs, Git configuration, commits, or PR text.

Each `## Ship` row needs a `Repository` value (`owner/repo`). Before any API request, Ship confirms that origin's fetch and push destinations match that value. Before preview and again before pushing, Ship confirms account and repository access and checks for an open PR with the same head and configured base. An existing PR is reported by URL without a push. Preview shows source, account, repository, title, body, head, base, and public-repository confirmation when applicable. After a yes, Ship creates the PR with explicit head, base, title, and body from `report.md` and stops. If a push succeeds but PR creation fails, Ship reports the pushed branch and a sanitized error. A new preview verifies the remote commit and can open the PR after another yes without pushing again. Review-change pushes to the same work branch require an explicit request and the usual destination checks.

## More commands

The full phrase reference is [[Prefixes]]. Backups, project routing, shipping, and upgrade limitations are covered in [[Advanced configuration]]. Publication and synchronization belong to [[Maintainer guide]]. Recovery and removal steps are in [[Troubleshooting]].

## Revisions
- 2026-10-20 — documented host limits, first-session verification, and manual web usage for 1.1.0.
