# Design

Cerebro is the starter kit. The vault it sets up is called Brain. This page explains three choices: living versus temporal notes, prefixes, and one card per chat.

## Living and temporal notes
A living note is current truth. A project note, a hub, `Prefixes.md`, and `Parameters.md` are living: you edit them in place, and they say what is true now. A temporal note is a record of one moment. A session, a decision, a daily note, and a commit note are temporal: they are written once, dated, and left alone.

The split keeps both kinds honest. A living note never grows a history section that drifts out of date, because the history lives in temporal notes that link back to it. A temporal note never needs updating, because it only claims what was true on its date. `check-vault` enforces the split: temporal notes sit in a record folder (`Sessions/`, `Daily/`, `Decisions/`, `Commits/`), and nothing else does.

Each area (`Work/<Company>/`, `Personal/`, `Collaboration/`, `Research/`, `Hackathons/`) is self-contained. Its notes link to each other and to the shared notes, not across areas. That keeps one company's work from leaking into another's, and lets you share or delete an area as a unit.

## Prefixes
Agents differ in what they remember and how they start. A prefix is a short phrase, such as `fnsh brain`, `fnsh update`, or `fnsh check`, with one fixed meaning written down in `Prefixes.md`. Every host reads the same table, so the same words do the same thing in Cursor, Claude Code, Codex, and a web chat.

Prefixes are explicit on purpose. The agent does not guess when to file, load, or publish; you say it, or a hook runs it. Each prefix has one exact reply, so you can tell at a glance whether it worked. Dash codes (`fnsh -bp`) combine actions without adding new words.

## One card per chat
Every chat that changed something gets one session note: what was asked, what changed, and links to the project. The filer writes it from the transcript, locally by default, with an optional cheap model call. The note is small on purpose. It is a card you can scan, not a transcript.

Cards make the vault useful to the next chat. `fnsh load <host>` reads the newest cards instead of whole transcripts, so a new agent picks up where the last one stopped without loading old conversations. The daily note gets one line per chat, so a day reads as a list of cards.

## What stays private
Shared files carry only example names. Real folders, projects, and ticket keys live in `Workspace map.md`, which git ignores. Publishing builds the public tree from an include list, scans the whole tree for private terms, and stops before anything is replaced if one is found.
