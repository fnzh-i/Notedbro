---
tags: [meta]
---
# Graph colors

Session cards and plans use three independent provenance tags derived from their recorded properties:

- `host/codex` says where the work ran.
- `ai/gpt` says which AI family the model belongs to.
- `model/gpt-6-1-sol` is the normalized exact model for filtering.

The original `host` and `model` properties remain the source of truth. Tag values are lowercase, and punctuation or spaces in model names become hyphens. The family comes only from the model name; it is never guessed from the host. Missing or unrecognized values use `unknown`.

| AI tag | Note color |
|---|---|
| `ai/gpt` | green (`#10B981`) |
| `ai/claude` | terracotta (`#D97757`) |
| `ai/grok` | blue (`#0EA5E9`) |
| `ai/gemini` | violet (`#A78BFA`) |
| `ai/unknown` | gray (`#94A3B8`) |

The AI group appears before the note-type groups, so it determines a session card or plan's color. Host and exact-model tags are filters rather than competing colors. Visible tag nodes use Obsidian's shared theme color; native Graph view does not assign each tag node the color of its matching notes.

`_Scripts/file-session` adds all three tags to new session cards. `fnsh plan save` applies the same tags to plans. `_Scripts/sync-provenance-tags` reports missing, stale, or conflicting tags; `_Scripts/sync-provenance-tags --apply` replaces only provenance tags and keeps all other tags in their original order. Apply mode backs up each changed file before replacing it.

## Change report — 2026-10-18

- Changed: provenance tag generation, session filing, plan instructions and templates, existing session/plan cards, graph groups, and tag-node display.
- Reason: a tag gives each provenance dimension one stable meaning and makes host, AI family, and exact model independently searchable.
- Files not touched: recorded host/model values, session bodies, project/area tags, model selection, host profiles, graph layout and force settings.
- Validation: filer, collaboration, and migration checks passed; a second migration check reported zero drift; all 63 migrated files differed from their backups only on the tags line; every card has exactly one `host/`, `ai/`, and `model/` tag; the graph retained all 14 original type groups and its force settings. Native Obsidian readback showed the five AI tag groups, visible tag nodes, and matching `ai/gpt` results with normalized model tags.
- Version control: the working folder has no Git repository, so no commit was created.

## Revisions
- 2026-10-18 — added the first property-based provenance palette.
- 2026-10-18 — replaced it with host, AI-family, and exact-model tags.
