---
tags: [meta]
---
# Terms

What the words and tags in this vault mean. Filing, names, and habits stay in [[How this vault works]]. Start at [[Index]].

## How a note is put together
- **Frontmatter** is the block between `---` at the top. It holds `tags` and, when the note needs them, `status`, `date`, `hash`, `hosts`, `source`, `kind`, or `conversation`.
- **Body** is the short record: what it is, what changed, what is next.
- **Wiki link** is `[[Note name]]`. The name is the file name without `.md`. Moving the file does not break the link.
- **Backlink** is the reverse. A session links its project. The project does not have to link every session back. Obsidian lists those on the project.
- **Tag** groups notes for a filter. A `[[link]]` is what connects one note to another.

A filed note carries a type tag and an area tag. A project tag is added when the note belongs to a project. A skill card carries a host tag for each host it runs on.

## Terms

| Term | Means |
|---|---|
| Vault | This folder. Long-term memory for work and personal projects. |
| Area | One self-contained part of the vault. Its notes link to each other, and to [[Index]] to go home. A question may also link the code project it belongs to. |
| Hub | The note that opens an area or a host: a company hub such as `Example`, [[Personal]], [[Collaboration]], [[Research]], [[Hackathons]], and the skill hubs `Skills`, `Claude skills`, `Codex skills`, `Cursor skills`. |
| Project | One codebase or effort, with its own note, `Sessions/`, sometimes `Commits/`, and sometimes tickets. |
| Description | The repo README on a project note. Goal stays one or two lines. No README means Goal is the description. |
| Ticket | One tracker issue assigned to me. Files are `EX-NNN.md`, using the key in `Workspace map.md`. The prefix is `fnsh ticket <KEY>-NNN`. Closed unless that ticket is being continued. |
| Decision | A choice worth keeping: context, options, the choice, and why. |
| Daily | One note for one day's work in one area. |
| Session | One chat. It links its project, question, or event, and the next session. |
| Session list | The note that lists one project's sessions in date order, for example `Example website sessions`. |
| Commit | One commit worth keeping. It links its project and the next commit. A message that is only `Initial commit` or `Update logs` is left out. |
| Living | A note whose current text is the truth, such as Parameters, Prefixes, Hosts, a hub, a project, a skill card, a ticket, or a plan. A plan's History section is the earlier text. |
| Temporal | A record written once: a session card, a daily note, a decision, or a commit. Tagged `temporal`, and left in its project or area folder. A session list or a commit list is living. |
| Commit list | The note that lists one project's commits, oldest first, for example `Example iOS commits`. |
| Question | One research or thesis question under `Research/`. |
| Hackathon | One event under `Hackathons/`, kept apart from personal projects. |
| Skill card | A short note in `Skills/`. It says when to use the skill, which hosts it runs on, and the path to the master. The card is not the skill. |
| Master | The real skill text. One folder in `Skill files/`, with its `SKILL.md`. That folder is a git repo and the copy that matters. |
| Host | An app that can run a skill: Claude, Cursor, or Codex. |
| Parameters | Standing rules for any model, in [[Parameters]]. An area may point its own checklist at them. |
| Revisions | A dated line on a note that was changed in a real way. On a ticket: `- YYYY-MM-DD — reopened: what I revised (branch · commit)`. The line stays after the ticket goes back to closed. |
| Template | A blank in `_Templates/`. It has the type tag only. Area and project tags are added when the note is filed. |

## Tags

Order in the frontmatter: type, then `temporal` on a record, then area, then project or host.

`[ticket, example, example-portal]` is a ticket, in Example, on Example Portal.

### Type

One type per note. This is what the note is.

| Tag | Note |
|---|---|
| `area` | An area hub. |
| `project` | A project note. |
| `question` | A research or thesis question. |
| `hackathon` | One hackathon event. |
| `ticket` | One tracker ticket. |
| `decision` | One decision. |
| `daily` | One day's work. |
| `session` | One chat, or the list of chats for a project. |
| `commit` | One commit, or the list of commits for a project. |
| `skill` | One skill card. |
| `plan` | One shared plan in `Plans/`. Type-only. No area tag. |
| `meta` | A note about the vault itself: [[Index]], [[How this vault works]], this note, [[Parameters]]. |

### Area

Taken from the folder.

| Tag | Folder |
|---|---|
| `example` | `Work/Example/`. Each company area is its own folder under `Work/`. |
| `personal` | `Personal/` |
| `collaboration` | `Collaboration/` |
| `research` | `Research/` |
| `hackathon` | `Hackathons/` |
| `claude` | `Claude/` |
| `skills` | `Skills/` |

[[Index]], [[How this vault works]], this note, and files still in `_Templates/` stay type-only. A note in `Plans/` is type-only too. A template gets its area tag, and its project tag when it has one, once it is filed.

### Project

The project note's name, lowercased, with spaces turned into hyphens.

| Project | Tag |
|---|---|
| Example Portal | `example-portal` |
| Example website | `example-website` |
| Example iOS | `example-ios` |
| Cursor | `cursor` |

The list of real project tags lives in `Workspace map.md`, which is not shared.

A note in two projects gets both tags. A company-wide decision has the area tag only. Write the slug on its own: `example-portal`.

### Host

On a skill card only. One tag per app that runs that skill.

| Tag | App |
|---|---|
| `claude` | Claude |
| `codex` | Codex |
| `cursor` | Cursor |

`[skill, skills, claude]` is a skill card, in `Skills/`, that runs on Claude.

## Same word, two jobs

| Word | As a type or area | As a project or host |
|---|---|---|
| `hackathon` | Type on an event note. Area on the [[Hackathons]] hub and on notes under `Hackathons/`. | — |
| `claude` | Area on notes in `Claude/`. | Host on a skill card that runs on Claude. |
| `cursor` | — | Project on notes for the `Cursor` project. Host on a skill card that runs in Cursor. |
| `skill` / `skills` | `skill` is the type of a card. `skills` is the area of `Skills/`. | — |

Read the slot. Type comes first, area second, project or host after that.

## Status

| Value | Where | Means |
|---|---|---|
| `active` | Area, project, question, hackathon, skill card | Current. |
| `closed` | Ticket | Default. The work is not being continued. |
| `reopened` | Ticket | This ticket is being continued right now. It goes back to `closed` at hand-off. The Revisions line stays. |

## Other frontmatter

| Field | Means |
|---|---|
| `date` | The day of a daily, decision, session, or commit. `YYYY-MM-DD`. |
| `hash` | On a commit note. The short git hash. |
| `hosts` | On a skill card. The same hosts as the host tags. |
| `source` | Path to that skill's master `SKILL.md`. Open this file and follow it. |
| `kind` | On a question. `research` or `thesis`. |
| `conversation` | The chat id, on a session note. Used so the same chat is not filed twice. |
| `host` | The app that ran the chat: `cursor`, `claude`, `codex`, `chatgpt`, `claude-ai`, `gemini`, or `unknown`. |
| `model` | The model name the app reported. |
| `profile` | Path to the host profile note, for example `Hosts/Cursor`. |
| `transcript` | Path to the raw chat on disk. The note stores the path, not a copy. |
| `truncated` | `true` when the filer sent only the newest part of the transcript to the model. Omit when false. |
| `configs_read` | Project instruction files opened for `fnsh config`. Omit when empty. |
| `conflicts` | Company rules that disagreed with the brain. The chat model writes these. The filer only copies them. Omit when empty. |
| `prefixes` | Prefixes I typed in that chat. A silent start does not count. Omit when empty. |
| `filer` | Who wrote the session card: `local`, or `model` when a model wrote it. |
| `filer_error` | Why the model card was not used. Omit when empty. |
| `filed_turns` | How many user turns were in the transcript when the note was filed. |
| `repeats` | Asks that also appeared in other chats, with the chat count. The filer writes this. Omit when empty. `offered` is set when this chat asked to save one. |
| `private` | On a project note, `true` means the repo is private. The session is still filed, tagged `private`, and recalled. |

## Words

| Word | Means |
|---|---|
| Prefix | A row in [[Prefixes]]. It starts with `fnsh`, then an action or a dash word. It counts only at the start of a message or on its own line. |
| Preference | A row in [[Preferences]]. An area, a preference, a scope, and the date added. |
| Profile | The Hosts row matched at the start step. It sets the tags and the folder for that chat's note. |
| Auto-file | Whether a host files its own session. `hook`, `manual`, or `none`. |
| Brain block | The text between `brain:start` and `brain:end` markers. It is the only part of a shared config the brain may write. |
| Conflict | A brain rule and a company or project rule that would make the agent do different things. Always ask first. |
| host | Set by the fingerprint at the start step. `unknown` is allowed. |
| model | Set by the fingerprint at the start step. `unknown` is allowed. |
| private | A tag on a session note whose project says `private: true`. The note is still filed and recalled. |
| secret | A tag, or `secret: true`. The note stays in the live vault. The surface leaves it out. |
| employee | A tag, or `employee: true`. The note holds employee personal data. The surface leaves it out. |
| Surface | The generated folder with secrets removed. The shareable copy. `~/.local/share/brain/surface`. |
| Shadow | An encrypted full copy of the live vault. `fnsh shadow` builds one. `fnsh shadow open` unpacks the newest. |
| host tag | `host/<host>`, for example `host/cursor`. It does not collide with a project tag or a skill host tag. |
| Load | The prefix `fnsh load <host>`. It restores a wiped host and reads that host's cards. It runs only when I say it. |
| Snapshot | A copy of a personal host file in `_Scripts/host-restore/`. Kept out of git and out of Sync. |

## Revisions
- 2026-10-17 — added the plan type. Plans notes are type-only.
- 2026-10-18 — added the Collaboration hub and area tag.
- 2026-10-18 — living notes and the temporal tag. Infrastructure folders start with `_`.
- 2026-10-18 — surface, shadow, secret, and employee.
- 2026-10-18 — shared text uses the Example / EX- vocabulary. Real project tags moved to `Workspace map.md`.
