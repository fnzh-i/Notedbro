---
type: registry
tags: [registry]
---
# Hosts

After the start step, match your fingerprint to one row and follow it. To support a new app or model, add one row. If nothing matches, use the unknown row.

| Host | Profile note | Session folder | Transcript source | Host tag | Auto-file |
|---|---|---|---|---|---|
| claude | Hosts/Claude | by project, else Personal/Chats/Sessions | ~/.claude/projects | host/claude | hook |
| cursor | Hosts/Cursor | by project, else Personal/Chats/Sessions | local Cursor transcript path | host/cursor | hook |
| codex | Hosts/Codex | by project, else Personal/Chats/Sessions | ~/.codex | host/codex | manual |
| chatgpt | Hosts/Web | Personal/Chats/Sessions | none | host/chatgpt | none |
| claude-ai | Hosts/Web | Personal/Chats/Sessions | none | host/claude-ai | none |
| gemini | Hosts/Web | Personal/Chats/Sessions | none | host/gemini | none |
| unknown | Hosts/Unknown | Personal/Chats/Sessions | none | host/unknown | none |

Session filing also derives `ai/` and normalized `model/` tags from the recorded model. See [[Graph colors]].
