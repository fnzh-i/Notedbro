---
type: registry
tags: [registry]
---
# Prefixes

A prefix is a short phrase I say to an agent. Every prefix starts with the marker `fnsh` as a plain first word, with no colon, followed by a space. A phrase counts only when it is at the start of a message or on a line of its own. A phrase inside a normal sentence is ignored. Matching is case-insensitive for the marker, actions, sets, and letters. If nothing matches, ignore the line.

To add a prefix: add one row. Nothing else needs editing. Keep Phrase short and unique. Read means notes to open first. Reply is the exact reply, or "none". KEY means the tracker's letters. NNN means any number.

## Order of precedence

Step 0: if the line does not start with `fnsh`, skip to rule 4 (alias check). Otherwise read the word after `fnsh` and walk this list top to bottom. The first rule that matches wins, and nothing below it is tried.

1. **Dash word.** A word starting with `-` is a letters chain. Read it by the Codes rules.
2. **Full action word.** A word that exactly equals an action word runs that solo prefix.
3. **Parameter set.** A word that equals a set name, followed by `params`, runs `<set> params`. A set may also be followed by a dash word, as in `fnsh example -bp`, and then applies to `p` only. If that dash word has no `p`, drop the set, still run the letters, and name the set in the reply.
4. **Alias.** An old phrase on its own line maps to the new phrase. See Temporary aliases.
5. **Anything else.** Ignore the line as normal text.

Argument words (a host, a scope, a ticket) are never checked against this list.

## Solo prefixes

A message with one action is a solo prefix. Solo prefixes keep working beside the dash codes. A solo line holds one action: words after its arguments are ignored, so `fnsh load cursor update` is a load of cursor and nothing else. Use a dash word to combine actions.

| Phrase | Read | Action | Reply |
|---|---|---|---|
| fnsh brain | How this vault works, Parameters, _Templates/Session, Hosts, Preferences | Fingerprint yourself without asking: host (cursor, claude, codex, chatgpt, claude-ai, gemini, or unknown), model, conversation id if the app gives one. If the app gives no id, set conversation to <host>-<date>-<time>-<first 8 chars of a hash of the first message>. Match your host to one row in [[Hosts]] and read that row's Profile note. Keep host, model, profile, session folder, and tags for the session note. Never guess the host. Use unknown, not a guess. This runs silently at the start of every chat. It also runs `_Scripts/guard` quietly. If the vault cannot be read, stay silent, write unknown for host, model, and profile, and note "vault unreadable" in the session note. Only when the message says brain: reply with the line below, or if you cannot read the vault, reply Brain unavailable: <host> / <model> and tell me to paste the filled template after a turn that changed something. A host that cannot open those notes reads `_Config/bootstrap.md`. | Brain ready: <host> / <model> / <profile> (only when the message says brain; otherwise no reply) |
| fnsh update | How this vault works, _Templates/Session | Manual backup for the automatic filing. Write or update today's Daily when the chat changed something. File or update this chat's session note using the stored fingerprint. Put the transcript path on it and do not copy the transcript in. | none |
| fnsh <set> params | That set's note in the Parameter sets table below | Use that set instead of asking me to paste it. The set is the word before `params`. If the set is not in the table or in `Workspace map.md`, list the known sets and load nothing. | none |
| fnsh params | Parameters | Bare form: use the Parameters note (the set named `main` in the table). | none |
| fnsh prefs | Preferences | Apply the rows in Preferences whose scope matches this chat, for the rest of the chat. | none |
| fnsh remember | Preferences | Append one row to the Preferences table from what I just said: Area, Preference in my words, Scope (default all hosts), and today's date as Added. Never change or delete another row. Record the new row in this chat's session note under prefixes. The reply is allowed even when a preference says to stay silent about the vault, because I asked for it. On a host with no disk access, give me the row to paste. I can fix a badly phrased row by editing it. | Saved to Preferences: <preference> |
| fnsh load <host> | that host's profile, Parameters, that host's skill hub, the newest matching session notes | Only when I say it, after that app, harness, or model setup was deleted or reinstalled. It does not run on its own, and the silent start does not call it. Host is cursor, claude, codex, chatgpt, claude-ai, or gemini. The same line may add all, company <name>, or project <name>. all reads the same cards as a bare load and does not raise the cap. company <name> is one Work/<Company>/ area. project <name> must match one project note title or one slug. If more than one matches, list the titles and load no cards. Do not reuse a filer alias. Cards only: Asked and Changed, no transcript. Cap is load_sessions. The reply shows n of total. Scope filters cards only. Run _Scripts/load-host for that host. It restores missing personal files and leaves a file that is already there, even when empty or broken. A dangling symlink is missing. If nothing is missing, still read the cards. unknown asks which host and restores nothing. On a fresh unit, run _Scripts/load-host from a terminal, or paste the block in Hosts/Web, before this phrase is recognized. If the vault cannot be read, use the unavailable reply. | Loaded <host> [<scope>]: <n> of <total> sessions through <date>. Restored: <names>. Nothing to restore when nothing was missing. Bare load omits the scope brackets. No match: Loaded <host> [<scope>]: 0 sessions. No match. Vault unreadable: Brain unavailable: <host>. |
| fnsh ticket <KEY>-NNN | Index, that ticket's note | Read both before other work. KEY is the letters the company's tracker uses. NNN is any number. The key and number come from the phrase. This does not rename notes already filed as EX-NNN. | none |
| fnsh config | AGENTS.md, CLAUDE.md, .cursor/rules, and any file I name, in the project root, plus Hosts | Read those files and use them for anything the brain is silent on. Record the files you read in the session note. | none |
| fnsh wins | none | For any conflict between the brain and a company config in this chat, follow the brain without asking. | none |
| fnsh plan save <name>, fnsh plan load <name>, fnsh plan list | _Templates/Plan | Save, load, or list one shared plan at `Plans/<name>.md`. The name is one token of lowercase letters, digits, and hyphens. Uppercase is lowercased. Anything else is not a name. This is a full word, not a dash letter. A combined start is two lines. Words after the name are ignored. `save <name>` fills Core Goal, The Issue / Root Cause, and Action Items from the plan already settled in this chat. Do not invent one. Each action item must serve the Core Goal and follow from the cause. `host`, `model`, and `date` come from the fingerprint. Add `host/`, `ai/`, and normalized `model/` tags using [[Graph colors]]. `date` is YYYY-MM-DD. The first save omits History. Saving the same name replaces those three sections, updates `host`, `model`, `date`, and provenance tags, and moves the previous three into History, newest first. A history entry is `### <date> — <host> / <model>` and then those three sections. Do not copy History into itself. `load <name>` reads that note and uses it as the working plan for the rest of the chat. Before doing an item, check it against the Core Goal and the cause. Name an item that serves neither, and skip it. Edits stay in the chat until the same name is saved again. A missing file loads nothing. `list` shows saved plans, newest first, by the `date` in the note. A host that cannot write the vault does not claim a save. It gives the filled note to paste. A host that cannot read the folder cannot list or load, unless the note is pasted in the message. | Saved plan: <name>. Loaded plan: <name>. List lines are `<name> — <date>`, or `Plans: none`. Unknown name, or a missing file: `No plan named <name>.` then the list, and load nothing. No subcommand, or a subcommand other than save, load, or list: do nothing and reply the three forms. Save with no name: `Name the plan.` No settled plan: `No plan to save.` No disk on save: `Paste into Plans/<name>.md:` and the note. |

| fnsh check | How this vault works | Run `_Scripts/check-vault`. It stays offline. It runs `_Scripts/guard` quietly first. A host that cannot run the script says so and does not claim a result. | `Vault ok. Cerebro v<version>.` using `_Scripts/cerebro-version`, or one problem per line. If the script cannot be run: `Cannot run check.` |
| fnsh shadow | How this vault works, Parameters | Run `_Scripts/shadow`. No extra word builds a surface folder and a new encrypted copy of the live vault. `open` decrypts and unpacks the newest copy into the open folder. `close` deletes that folder. `list` prints each copy's description, newest first. A daily LaunchAgent runs the script and builds only when the newest copy is `shadow_every_days` old or older. Copies older than `shadow_keep_days` are deleted only after the new copy checks out. A failed build deletes nothing. The key is `~/.config/brain/shadow.key`. The script prints the public recipient only. This is a full word, not a dash letter. | `Surface: <path>. Shadow: <path>.` Surface left unchanged: problem lines, then `Surface withheld. Shadow: <path>.` `Shadow open: <path>.` `Shadow closed.` List prints each description, newest first, or `Shadows: none.` No copy to open: `No shadow to open.` Missing age or zstd: `Cannot run shadow.` |
| fnsh guard | none | Run `_Scripts/guard`. It compares the top of the vault with `_Scripts/starter-manifest.txt` and records unknown paths in the `.gitignore` block. It never deletes files. This is a full word, not a dash letter. | `Nothing new. All unknown paths are already private.` or one summary line, then `Ran locally. Nothing was sent anywhere.` |
| fnsh ship | Workspace map | Ship the current project by its `## Ship` rule. `fnsh ship <project>` names one. `fnsh ship yes` applies the last preview. `fnsh ship yes public` is the second yes when the repo is public. `branch-pr` is for everyone. The `cerebro` rule is maintainer-only. It never pushes `main`. This is a full word, not a dash letter. | Preview lines, then `Ship? yes to push.` On success: the pull request URL, or the compare URL. `Ship withheld: <reason>.` |
| fnsh upgrade | none | `check` prints the local version and the latest release and writes nothing. With no subcommand, show the changed starter files and wait for `fnsh upgrade yes`. It never sends vault data. `check` is its one subcommand. This is a full word, not a dash letter. | `Your Cerebro is v<old>, latest is v<new>. Run fnsh upgrade.` or `Cerebro is up to date (v<version>).` Offline: `Cannot reach GitHub. Try again later.` |
| fnsh rebuild <host> | Hosts | Run `_Scripts/rebuild <host>`. Host is cursor, claude, codex, web, chatgpt, claude-ai, gemini, unknown, or all. It restores that host's profile in `Hosts/` and its harness file: CLAUDE.md for claude, AGENTS.md for codex. all adds `_Config/bootstrap.md`. The clean copy comes from git HEAD, else the publish checkout; AGENTS.md and CLAUDE.md are generated. It prints a preview first, creates only missing files, and overwrites only with `--force`, after a dated backup in `~/.local/share/brain/backups`. It never touches notes or Personal/. A scheduled run only prints the preview. `fnsh check` prints this line when a host or harness file is missing or damaged. Self-check: `_Scripts/rebuild self-check`. This is a full word, not a dash letter. | `Preview:` and one line per file, then `Rebuilt: <files>.` or `Nothing to rebuild.` Unknown host: the usage line. |

## Maintainer

Only needed if you keep a private vault and a public copy. `fnsh check` does not suggest these to anyone else.

| Phrase | Read | Action | Reply |
|---|---|---|---|
| fnsh publish | How this vault works | Run `_Scripts/publish`. It copies the manifest into a temp folder outside the vault, writes the generated files, then scans the whole tree and runs check-vault on it. A hit leaves the previous folder untouched. A clean run swaps the tree into `~/.local/share/brain/publish` and keeps its `.git`. It never commits or pushes. It refuses unless the denylist, a `cerebro` ship row, and `maintainer: yes` are all present. Self-check: `_Scripts/publish self-check`. This is a full word, not a dash letter. | `Published: ~/.local/share/brain/publish` Withheld: one `path:line: kind` line per hit, then `Scan ran locally. Nothing was sent anywhere.` and `Publish withheld.` Missing setup: `Maintainer only: fnsh publish builds a public copy from a private vault. You don't need it. To share a change, use fnsh ship.` |
| fnsh sync | none | Run `_Scripts/sync`. It fetches `origin/main` in the publish checkout, stops if the checkout is dirty, and fast-forwards. It copies changed shared files into the live vault. A hand run also copies `_Scripts/`. The scheduled run copies nothing when a script changed, and it skips when the guard finds an unknown path. It never pushes. Same maintainer setup as publish. Self-check: `_Scripts/sync self-check`. This is a full word, not a dash letter. | `Synced: <sha>.` `Sync waiting: scripts changed` `Sync withheld:` then the paths or the reason. |

## Parameter sets

Parameters are modular. Each set is one row. `fnsh params` uses `main`. `fnsh <set> params` uses that set's note. To add a set: add one row. A set name must not equal an action word.

| Set | Note | Use for |
|---|---|---|
| main | Parameters | General facts I would otherwise paste |
| example | Example Parameters | Example work |

`main params` is the same as bare `params`. Sets listed in `Workspace map.md` also work, and they are read before this table.

## Codes

A dash word is one short word that stands for several actions: `fnsh -bp`. Each letter is one action. To add a code: add one row. A letter must be unique.

| Letter | Action | Argument |
|---|---|---|
| l | load | host, then optional scope |
| b | brain | none |
| p | params | optional set, written before the dash word |
| f | prefs | none |
| r | remember | none |
| c | config | none |
| w | wins | none |
| t | ticket | one <KEY>-NNN token |
| u | update | none |

Examples:

- `fnsh -bp` runs brain, then params. `fnsh -bpf` adds prefs. `fnsh -bpfu` ends by filing the session.
- `fnsh example -bp` runs brain, then the example params set.
- `fnsh -bpt ABC-123` runs brain, params, then that ticket.
- `fnsh -lb cursor` restores the cursor host, then runs brain.

Rules:

1. A dash word contains only the dash and letters from the table. Any other character means the line is ignored.
2. Run order is fixed, whatever the typed order: `l` first, then `b`, then the rest left to right, `u` last. A repeated letter runs once.
3. Arguments follow the dash word and match the argument-taking letters in the order those letters appear.
4. An unknown letter stops the chain at that letter. Run the letters before it. The reply says what ran, which letter stopped it, and asks what was meant.
5. A ticket token that is not `<KEY>-NNN` is an unknown argument. Stop there and name it.
6. The reply is one message from each action's Reply, in run order. A Reply of none adds nothing. When `b` ran, it starts with `Brain ready: <host> / <model> / <profile>`.
7. If one action fails, the rest still run, and the reply names the failed one.
8. `l` never runs unless written. The silent start runs brain only, with no reply.
9. A load scope ends only at a word that exactly equals a full action word. Single letters never end a scope.
10. A word without a dash is never read as letters, so `fnsh bp` is ignored.

A repeated combination can trigger the offer to save it as a setup. The count uses the normalized chain: dash letters in run order, repeats dropped, `main` dropped, any set kept. A solo line counts as its one-action chain and is stored in the same form as the dash chain for counting, so `fnsh brain` and `fnsh -b` both count as `fnsh -b`. The session note still stores the phrase as written. When that chain has appeared in 3 separate chats, the next chat offers once: "You keep using <chain>. Save it as a setup?" Yes appends one row under Setups: the normalized chain and today's date. No adds it to Declined in [[Preferences]].

## Setups

Saved chains. A row is the normalized chain and the date it was saved. Delete a row when you no longer want it offered.

| Chain | Added |
|---|---|

## Temporary aliases

An alias line ignores the rest of the line and is never mixed into a chain. Delete a row when you no longer need it.

| Old phrase | Maps to |
|---|---|
| use brain | fnsh brain |
| update the brain | fnsh update |
| use my parameters | fnsh params |
| use my preferences | fnsh prefs |
| remember this | fnsh remember |
| use my example parameters | fnsh example params |
| load <host> | fnsh load <host> |
| ticket <KEY>-NNN | fnsh ticket <KEY>-NNN |
| use company config | fnsh config |
| brain wins | fnsh wins |

## Templates

The notes the prefixes write start from these. To add a template: add the file and one row. `fnsh check` reports a template missing from this table.

| Template | Used for |
|---|---|
| _Templates/Session | one card per chat, written by `fnsh update` and the filer |
| _Templates/Plan | `fnsh plan save` |
| _Templates/Daily | one day in an area |
| _Templates/Decision | one choice and its reasoning |
| _Templates/Ticket | one tracker ticket, `EX-NNN` |
| _Templates/Project | a project hub |
| _Templates/Area | a company or area hub |
| _Templates/Commit | one commit |
| _Templates/Question | one open question |
| _Templates/Skill | one skill card |
| _Templates/Workspace map | the example private map, published as `Workspace map.example.md` |

## Revisions
- 2026-10-17 — added fnsh plan: save, load, and list a note in Plans/.
- 2026-10-18 — added fnsh check, and pointed a host with no tools at `_Config/bootstrap.md`.
- 2026-10-18 — added fnsh shadow: build, open, close, and list.
- 2026-10-18 — added fnsh publish, fnsh sync, fnsh rebuild, and the Templates table.
- 2026-10-19 — added fnsh guard, fnsh ship, and fnsh upgrade. Publish and sync are maintainer-only.
