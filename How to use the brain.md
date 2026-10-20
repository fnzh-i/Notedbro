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

## More commands

The full phrase reference is [[Prefixes]]. Backups, project routing, shipping, and upgrade limitations are covered in [[Advanced configuration]]. Publication and synchronization belong to [[Maintainer guide]]. Recovery and removal steps are in [[Troubleshooting]].

## Revisions
- 2026-10-20 — documented host limits, first-session verification, and manual web usage for 1.1.0.
