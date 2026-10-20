---
tags: [meta]
---
# How this vault works

My long-term memory for work and personal projects. Start at [[Index]]. What the words and tags mean: [[Terms]].

A host that cannot open the separate notes reads `_Config/bootstrap.md`. That file is generated. Do not edit it by hand.

## Private: never mentioned outside this vault
- Claude uses this vault **silently**. It never mentions Obsidian, this vault, "Brain" or these notes in:
  - repo files, docs, change reports and manual test templates
  - commit messages, PR titles or bodies, Jira comments, Devs announcements
  - EOD summaries, or any other chat reply
- Exception: only when I ask about the vault myself.

## Layout
```
Brain/
├─ Index.md                 home: one link per area
├─ How this vault works.md
├─ Prefixes.md              phrases I say, and what each one does
├─ Plans/                   one shared plan per file. fnsh plan save writes it
├─ Preferences.md           standing preferences, applied by scope
├─ Hosts.md                 one row per app. Profiles live in Hosts/
├─ Parameters.md            standing rules and filer limits
├─ Workspace map.md         private: working folders, projects, ticket key. Not shared, not in git.
├─ _Config/bootstrap.md     generated from the rules, prefixes, and parameters. Do not edit by hand.
├─ _Scripts/file-session     writes a session note and one Daily line
├─ _Scripts/load-host        restores personal files for a wiped host
├─ _Scripts/host-restore/    snapshots of those files. Not in git. Not synced.
├─ _Templates/               shared templates (Area, Project, Question, Ticket, Decision, Daily, Skill, Commit, Session, Plan)
├─ Skill files/             git repo: one master copy of each skill. Source of truth. Hidden from the graph.
├─ Skills/                  short cards that point at Skill files/
│  ├─ Skills.md             hub
│  ├─ Claude/Claude skills.md
│  ├─ Codex/Codex skills.md
│  └─ Cursor/Cursor skills.md
├─ Claude/                  how my Claude Code setup works
├─ Work/
│  └─ <Company>/            one folder per OJT / internship
│     ├─ <Company>.md       area hub: projects, open tickets, rules, days, people
│     ├─ Projects/<Project>/  project note (+ copy of the repo's CLAUDE.md)
│     ├─ Tickets/           EX-NNN.md (tickets assigned to me; the key is in Workspace map.md)
│     ├─ Decisions/         YYYY-MM-DD-short-title.md
│     └─ Daily/             one note per work day
├─ Personal/
│  ├─ Chats/Sessions/       web chats, unknown hosts, and local chats with no project
│  └─ <Project>/            same idea, smaller
│     └─ Commits/           one note per commit worth keeping
├─ Collaboration/          projects built with friends or other collaborators
│  ├─ Collaboration.md      area hub
│  ├─ Daily/                YYYY-MM-DD Collaboration.md
│  └─ <Project>/            project note, Sessions/, and other project notes
├─ Research/
│  └─ <Question>/           one question or thesis, optional link to a project
└─ Hackathons/
   └─ <Event>/              one hackathon, kept apart from personal projects
```

## Living and temporal
- A living note's current text is the truth. Parameters, Prefixes, Preferences, Hosts, hubs, project notes, skill cards, tickets, and plans are living.
- A plan stays one note. The current Core Goal, cause, and action items are the truth. The History section is the earlier text.
- A temporal note is written once as a record: a session card, a daily note, a decision, or a commit. It stays in its project or area folder and has the tag `temporal` beside its type tag. A session list or a commit list is living. It sits next to the project note.

## Areas stay separate
- Each area links **only to its own notes** (plus [[Index]] to go home). That keeps every area easy to read and change on its own.
- Exception: a question note may link to the code project it belongs to.
- To see one area in the graph, filter it: `path:"Work/Example"`. Clear the search box for the whole vault.
- Graph colors use `ai/` tags on session cards and plans: GPT green, Claude terracotta, Grok blue, Gemini violet, and unknown gray. `host/` and `model/` tags remain available for filtering, and tag nodes are visible. See [[Graph colors]]. Other notes keep their type colors: hubs light, decisions amber, session indexes blue, tickets teal, days green, Northwind commits rose, Northwind projects coral, other commits purple, other projects orange, skills slate, questions yellow, hackathons magenta, plans indigo, meta gray. The first matching group wins; _Templates are excluded. The text for decisions and sessions is on the `Decisions and sessions` canvas, which `_Scripts/build-views` writes.

## Tickets: closed unless continued
- Every ticket note is `status: closed` by default. Nothing keeps a hand-made "open tickets" list, because those go stale.
- When I continue a ticket in a session, its note gets `status: reopened` for that work and a dated line under `## Revisions`: `- YYYY-MM-DD — reopened: what I revised (branch · commit)`. When the work is handed off, the status goes back to `closed`; the Revisions line stays as the record.
- The same applies when I revise any other note substantially: add a dated line under its `## Revisions` (create the section if missing).

## Naming
| Note | Name |
|---|---|
| Area hub | `<Company>.md`, e.g. `Example.md` |
| Project | `<Project>.md` in `Projects/<Project>/` |
| Ticket | `EX-NNN.md` |
| Decision | `YYYY-MM-DD-short-title.md` |
| Daily (company in `Workspace map.md`) | `YYYY-MM-DD.md` |
| Daily (any other area) | `YYYY-MM-DD <Area>.md`, e.g. `2026-10-20 Personal.md`, so day links never clash |
| Question | `<Question>.md` in `Research/<Question>/` |
| Hackathon | `<Event>.md` in `Hackathons/<Event>/` |
| Session | `YYYY-MM-DD <project, question, or event> <short title>.md` in that note's `Sessions/` |
| Commit | `YYYY-MM-DD <hash> <short title>.md` in that project's `Commits/` |
| Commit list | `<Project> commits`, for example `Example iOS commits` |
| Skill card | skill name, e.g. `animate`. Add the host only when two masters share a name (`Claude pdf`, `Codex pdf`) |
| Skill hub | `Skills`, `Claude skills`, `Codex skills`, `Cursor skills` |

## Links and tags
- Link with `[[Note name]]`, e.g. `[[EX-101]]`. Moving a note between folders doesn't break its links.
- Link upward: a Daily note links its tickets, a ticket links its project and decisions, a session links its project and the next session, and a commit links its project and the next commit. Backlinks fill in the reverse.
- Type and area are required. Further tags are fine.
- Type: `area`, `project`, `question`, `hackathon`, `ticket`, `decision`, `daily`, `session`, `commit`, `skill`, `plan`, `meta`, or `registry`. A note in `Plans/` is type-only. Its type is `plan`.
- Area comes from the folder: `Work/Example/` is `example`, `Personal/` is `personal`, `Collaboration/` is `collaboration`, `Research/` is `research`, `Hackathons/` is `hackathon`, `Claude/` is `claude`, `Skills/` is `skills`.
- A skill card also gets a host tag for each host it runs on: `claude`, `codex`, `cursor`.
- When a note belongs to a project, add that project's tag: the project note's name, lowercased, spaces turned into hyphens (`Example Portal` → `example-portal`, `Example iOS` → `example-ios`). A note in two projects gets both. Do not nest it under `project/`. Tags group and filter; `[[links]]` are what connect notes.
- Session cards and plans record provenance as `host/<host>`, `ai/<family>`, and `model/<normalized-model>`. The `host` and `model` properties keep the original values; tags are derived from them. Unknown values are explicit. `_Scripts/sync-provenance-tags` checks drift by default and updates it with `--apply`.
- [[Index]], this note, and _Templates stay type-only. Add the area tag, and the project tag when there is one, when a template is filed into a folder.

## Starting a new area
1. Create `Work/<Company>/` (or `Personal/<Project>/`, or `Collaboration/<Project>/` for shared projects).
2. Add the hub note from _Templates → Area, then the subfolders you need.
3. Add one line for it in [[Index]].

## Skills
- `Skill files/` is a git repo and the only copy that matters. Each skill is one folder with its `SKILL.md` and any files that skill tells you to read.
- A card in `Skills/` has three things: when to use it, which hosts it runs on, and the path to the master `SKILL.md`. The model opens that file and follows it. Do not paste the skill into the card. Git is the history and the backup.
- User skill folders point at the master (`~/.cursor/skills/<name>`, `~/.claude/skills/<name>`, `~/.codex/skills/<name>`). Deleting one of those does not change the card.
- Do not replace folders an app overwrites: Claude `skills/synced/`, Cursor `skills-cursor/`, Codex `.system/`, Codex plugin caches. If an update replaces one of those, copy it again from `Skill files/`.
- Same name, same instructions: one master, and the card lists every host. Same name, different instructions: two masters, and the note title includes the host.
- If a master is not in `Skill files/`, add a read-only Fallback section at the bottom of that card with the skill text. Do not add it while the master is in git.

## Project description
- Goal stays one or two lines.
- If the repo has a README, copy it under `## Description` on the project note. Drop the README title line. Leave out a line that is only a key, token, or password.
- If there is no README, Goal is the description. Do not add an empty Description section.

## Prefixes
- [[Prefixes]] is the list of phrases I say. A phrase starts with `fnsh`. It counts only at the start of a message or on its own line. The order of precedence decides which rule matches.
- `fnsh brain` is the start step. It runs silently at the start of every chat where the vault can be read. It replies only when the message says brain. If the vault cannot be read and the message says brain, the reply is `Brain unavailable: <host> / <model>`.
- `fnsh update` is the manual backup. It writes today's Daily when the chat changed something, and files the session note from the stored fingerprint. The transcript path goes on the note. The transcript itself stays on disk.
- `fnsh check` runs `_Scripts/check-vault` and lists problems. A clean run says the vault is ok. A host that cannot run the script says so and does not claim a result.
- `fnsh config` reads the project files it names. `fnsh wins` is the only time a conflict is resolved without asking.
- `fnsh load <host>` is only for a host whose app, harness, or model setup was deleted or reinstalled. It runs only when I say it. The silent start does not call it. Optional scope on the same line: `all`, `company <name>`, or `project <name>`. `all` does not raise the cap. A project name must match one note title or one slug. A company name must match one `Work/<Company>/` area. Cards only, capped by `load_sessions`. Scope filters cards. The restore is for the whole host.
- `fnsh ticket <KEY>-NNN` reads [[Index]] and that ticket's note. KEY is the tracker's letters. Notes already filed as `EX-NNN.md` keep that name.
- `fnsh prefs` applies the rows in [[Preferences]] whose scope matches this chat.
- `fnsh remember` appends one row to [[Preferences]]. It does not change or delete another row. The reply is allowed even when a preference says to stay silent about the vault, because I asked for it.
- A dash word mixes actions. `fnsh -bp` runs brain, then params. Run order is `l`, then `b`, then the rest left to right, with `u` last.
- `fnsh params` uses a parameter set from [[Prefixes]].
- `fnsh plan` saves, loads, and lists a note in `Plans/`. It is a full word, so it is its own line. Saving the same name keeps the old text under History.

## Sessions
- A session note is a short card: host, model, project, what I asked, what changed, and the path to the raw transcript. It is not a copy of the chat.
- [[Hosts]] decides the profile, the session folder, the transcript source, the host tag, and whether filing is a hook, manual, or none.
- File new notes for shared projects under `Collaboration/<Project>/`; keep personal and company work in their existing areas. Which working folder files into which project is listed in `Workspace map.md`.
- Local hosts file under the project. If there is no project, they file under `Personal/Chats/Sessions`. Web and unknown always file there.
- `_Scripts/file-session` writes the note. It is idempotent on conversation id. It skips a short chat unless I typed a prefix. A second run updates the same note and the same Daily line. After a note is filed, it refreshes that host's snapshot in `_Scripts/host-restore/`. A failed snapshot still leaves the note in place.
- A project with `private: true` is still filed. The session note gets the tag `private` and is recalled like any other session.
- `_Scripts/file-session` counts the same ask across session notes and stores it under `repeats` on the note it files. It does not edit [[Preferences]] or [[Parameters]].

## Preferences
- [[Preferences]] is the list of standing preferences. The start step reads it and applies the rows whose scope matches this chat. If the note cannot be read, apply no rows, stay silent, and do not reply with an error. The chat continues.
- Scope is `all hosts`, a host name from [[Hosts]], a project name, or a company name.
- The project is found from the working directory name, or from the ticket in the first message, the same way a session note finds its project. The company is the `Work/<Company>/` area that project belongs to. Match a row to a project by note title or slug, the same way `fnsh load <host> project <name>` does. If the project or company cannot be decided, apply only the `all hosts` rows and the rows for this host. Never guess. A personal project has no company, so a company row does not apply there.
- My current message beats a stored preference. After that, the narrower scope wins, then the newer date. A project beats a company, because the project sits inside that company. A project beats a host. A host beats `all hosts`. A company beats `all hosts`. A company and a host are not nested; if those two clash, ask. If it is still unclear, ask.
- A company or project config still wins by default. A conflict is raised first. See Coexistence.
- A preference is added only when I say `fnsh remember`, answer the repeat prompt, or edit the note myself.
- At the start of the next chat, read the newest session note's `repeats`. When `chats` is 3 or more, ask once: "You keep asking for <ask>. Save it as a preference or a parameter?" Options are Preference, Parameter, and No. Do not offer an ask that is already a preference or a parameter, is under Declined, or has `offered` on any session note. A style or behavior ask is a preference. A value or setting (a number, a limit, a path, a name) is a parameter: one bare `key: value` line in [[Parameters]], not a numbered rule. If you cannot tell, ask which. Nothing is saved without my answer. No adds the ask to Declined. Preference appends one row. Parameter adds one line and changes nothing else.

## Coexistence
- Never delete, overwrite, or reorder a company or repo instruction file. Append a marked block only: `<!-- brain:start -->` through `<!-- brain:end -->`.
- Personal files I own (`~/.claude/CLAUDE.md`, and my Cursor user rule) may have old vault steps removed once.
- To remove the brain, delete the text between the markers, and delete the hook line.
- Hooks never edit config files. The filer never edits config files. It may write inside `_Scripts/host-restore/` after a session is filed.
- `_Scripts/load-host` restores supported missing files. Claude uses only Brain's `.claude/settings.local.json` and the generated local hook; start Claude at Brain's root. Shared and global settings are preserved. Recognized obsolete paths can be repaired with backups. Custom or malformed configuration requires review. Local settings, generated hooks, `.notedbro-local/`, and `_Scripts/host-restore/` remain private and must never be published.
- A company rule and a brain rule in conflict are raised with me first. The brain wins only when I say `fnsh wins`. Asking about a conflict is allowed.
- Stay silent about the vault in repo files, commits, pull requests, Jira, end-of-day notes, and chat replies, unless I ask about it.

## Surface and shadow
- The live vault is the working copy. It stays as it is.
- `fnsh shadow` writes a surface folder and an encrypted shadow copy. Share the surface folder only. Do not share the live vault.
- The surface leaves out `Personal/`, `_Scripts/host-restore/`, notes tagged `secret` or `employee` (`secret: true` or `employee: true` too), and lines that are only a key, token, or password. It is one folder, replaced on each build: `~/.local/share/brain/surface`.
- Each shadow copy is the full vault, compressed with zstd, then encrypted with age. Copies live in `~/.local/share/brain/shadow/` as `shadow-YYYY-MM-DD-HHMM.age`, with a matching `.txt` description. `fnsh shadow list` prints those descriptions, newest first.
- `fnsh shadow open` unpacks the newest copy into `~/.local/share/brain/open`. That folder is temporary. `fnsh shadow close` deletes it.
- A daily job checks once. It builds a new copy when the newest is `shadow_every_days` old or older (30). After that copy checks out, copies older than `shadow_keep_days` (90) are deleted. A failed build deletes nothing. `fnsh shadow` builds immediately and restarts the 30-day timer.
- The private key is `~/.config/brain/shadow.key`. It is not in the vault, not in git, and not in host-restore. Losing it loses the copies. The live vault can build new ones.
- A monthly copy can be up to 30 days behind the live vault. That matters only if the live vault is lost. Run `fnsh shadow` before big changes when you want a fresher backup.

## Publish, sync, and rebuild
- `fnsh publish` is maintainer-only. It builds the public starter kit in `~/.local/share/brain/publish` from the starter manifest. It writes a starter Index, the hub notes including `Personal/Personal.md` and `Personal/Chats/Chats.md`, `Workspace map.example.md`, `.gitignore`, and `_Config/bootstrap.md`. Then it scans the whole tree and runs check-vault on it. Any hit withholds the publish and leaves the previous folder as it was. It never commits or pushes. It refuses unless the denylist, a `notedbro` ship row, and `maintainer: yes` are all set. Other files under `Personal/` are never included.
- The scan flags emails, phone numbers, my home folder and login name, the terms in `~/.config/brain/publish-denylist`, and the names in `Workspace map.md`. Terms match whole words. A term ending in `-` is a case-sensitive prefix.
- `fnsh sync` brings merged pull requests from that checkout into the live vault. It copies shared files only, and never the live Index, `Workspace map.md`, hubs, notes, Skill files, `.obsidian`, or host-restore. A scheduled run never copies a script. A file changed on both sides is withheld. The last synced commit is in `~/.config/brain/sync-sha`.
- `fnsh rebuild <host>` restores a missing host profile or harness file. It overwrites only with `--force`, after a dated backup.
- Each script has a self-check: `python3 _Scripts/<name> self-check` for publish, sync, rebuild, and shadow.

## Habits
- New note: Cmd+P → "Templates: Insert template". The Daily-note button creates company days.
- Keep notes short; use bullets.
- Always paste keys, passwords or employee personal data.
- Claude writes here too: Daily summaries, ticket status, decisions.

## Search
Keyword search is enough. Revisit semantic search when keyword search misses a note that exists, or the vault passes about 1,000 notes. Count content notes only, not files under `Skill files/`. Do not build it before then.

## Revisions
- 2026-10-20 — added 1.1.0 local Claude setup, backed-up instruction repair, and private generated configuration.
- 2026-10-17 — added Plans/, the plan type, and fnsh plan.
- 2026-10-18 — added Collaboration for shared projects and per-project routing.
- 2026-10-18 — graph colors prioritize recorded host/model, AI family, and host, with gray for session cards lacking provenance.
- 2026-10-18 — replaced property-based graph colors with AI-family tags and visible provenance tag nodes.
- 2026-10-18 — living and temporal notes, infrastructure folders, bootstrap, and the vault check.
- 2026-10-18 — surface folder and encrypted shadow copies.
- 2026-10-18 — added publish, sync, and rebuild.
- 2026-10-18 — shared text uses the Example / EX- vocabulary. Real folders, projects, and the ticket key moved to `Workspace map.md`.
