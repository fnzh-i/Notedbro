---
tags: [meta]
---
# How to use the brain

## What the brain is
- The brain is this vault, `~/Documents/Brain`. It is a record of chats with any agent, model, or app, for work and for personal projects. It is not a diary and not a copy of the transcript.
- One chat becomes one short card: host, model, project, what was asked, what changed, and the path to the raw transcript. The transcript stays on disk.
- Cursor, Claude Code, Codex, and web chats (ChatGPT, Claude.ai, Gemini) use the same notes. [[Prefixes]] is what I say. [[Hosts]] is which app this is. [[How this vault works]] is how the notes are organised.
- The vault stays quiet outside itself. It is not mentioned in repo files, commits, pull requests, Jira, or an end-of-day note unless I ask about it.

## What to say
A phrase starts with `fnsh`. It counts only at the start of a message or on its own line. The order of precedence is in [[Prefixes]]. A dash word mixes several actions: `fnsh -bp` is brain, then params.

- `fnsh brain` — reply `Brain ready: <host> / <model> / <profile>`. The same check already runs silently when the vault can be read. It replies only when the message says brain.
- `fnsh update` — write today's Daily if something changed, and file the session note. Use this in Codex and in web chats.
- `fnsh params` — open [[Parameters]]. `fnsh example params` — open the `example` set. Your own sets are listed in `Workspace map.md`.
- `fnsh load <host>` — only after that app was deleted or reinstalled. Optional: `all`, `company <name>`, or `project <name>`. Reads the newest cards and restores missing personal files. It does not run on its own.
- `fnsh ticket <KEY>-NNN` — read [[Index]] and that ticket's note first. KEY is the tracker's letters. Any number works. Notes already filed as EX-NNN keep that name.
- `fnsh config` — read the project instruction files. `fnsh wins` — follow the brain for a conflict in this chat, without asking.
- `fnsh prefs` — apply the rows in [[Preferences]] whose scope matches this chat.
- `fnsh remember` — append one row to [[Preferences]]. The reply is `Saved to Preferences: <preference>`.
- `fnsh plan save <name>` — write `Plans/<name>.md`. `fnsh plan load <name>` reads it as the working plan. `fnsh plan list` shows saved plans, newest first. It is its own line.
- `fnsh check` — run `_Scripts/check-vault` and list problems. A clean run says `Vault ok. Cerebro v<version>.` It stays offline.
- `fnsh shadow` — build a surface folder and an encrypted shadow copy. `fnsh shadow open` unpacks the newest copy. `fnsh shadow close` deletes that unpacked copy. `fnsh shadow list` prints the copies, newest first. It is its own line.
- `fnsh guard` — record unknown top-level paths as private. It is its own line.
- `fnsh ship` — open a pull request for the current project, after a preview and a yes. `fnsh ship <project>` names one. It never pushes `main`.
- `fnsh upgrade check` — compare the local version with the latest release. `fnsh upgrade` replaces the starter-kit scripts after a yes.
- `fnsh rebuild <host>` — restore a missing host or harness file. `fnsh check` prints this line when one is missing.

## Maintainer
Only needed if you keep a private vault and a public copy.

- `fnsh publish` — build the public starter kit and scan it. A hit withholds it. It never pushes.
- `fnsh sync` — copy merged pull requests from the publish checkout into the shared files here. A scheduled run waits when a script changed.

## What happens on its own
Claude and Cursor file through `_Scripts/file-session`. Codex is manual. ChatGPT, Claude.ai, and Gemini do not file themselves. Paste the block in [[Hosts/Web]] into that site's custom instructions, then say `fnsh update`. A short chat with nothing on disk is skipped unless a prefix was typed. A project with `private: true` is still filed and tagged `private`. When the same ask reaches 3 chats, the next chat offers once to save it as a preference or a parameter.

## Graph
- Open the graph. Color follows the note type: hubs light, decisions amber, sessions blue, tickets teal, days green, Northwind commits rose, Northwind projects coral, other commits purple, other projects orange, skills slate, questions yellow, hackathons magenta, meta gray. Clear the search box for the whole vault. Filter `path:"Work/Example"` for one area.
- `Decisions and sessions` is the canvas. Each card shows the note: Choice and Reasoning, or Asked and Changed.

## Where the note goes
Under the project when the working directory or a ticket in the first message matches one. Otherwise `Personal/Chats`. Web and unknown always go to `Personal/Chats/Sessions`. Today's Daily gets one line for that conversation id.

## When something disagrees
A company rule and a brain rule are raised first. `fnsh wins` is the only time the brain is followed without asking. To remove the brain from a host, delete the text between `<!-- brain:start -->` and `<!-- brain:end -->`, and delete the hook line. `fnsh load <host>` may write personal host files when I say it. Hooks and the filer still do not edit config.

## Where the details live
- [[Index]]
- [[How this vault works]]
- [[Prefixes]]
- [[Preferences]]
- [[Hosts]]
- [[Parameters]]
- [[Terms]]
- [[_Templates/Session]]
- `Brain logs.base` — the session list view
- `_Config/bootstrap.md` — one generated page when the separate notes cannot be opened. Do not edit it by hand.

## Revisions
- 2026-10-17 — added fnsh plan under What to say.
- 2026-10-18 — added fnsh check, and the generated bootstrap page.
- 2026-10-18 — added fnsh shadow.
- 2026-10-18 — added fnsh publish, fnsh sync, and fnsh rebuild.
- 2026-10-19 — added fnsh guard, fnsh ship, and fnsh upgrade. Publish and sync moved under Maintainer.
