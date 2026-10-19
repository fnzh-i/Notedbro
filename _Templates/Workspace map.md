---
tags: [meta]
---
# Workspace map (example)

Copy `Workspace map.example.md` to `Workspace map.md` and replace the example values with yours. The scripts read `Workspace map.md` first and fall back to this file. `Workspace map.md` is ignored by git, so your real folders, projects, and ticket key stay on your machine.

## Company
- name: Example
- ticket key: EX
- workspace: ~/Code/example
- daily: date only

Company notes live in `Work/Example/`. `daily: date only` names company days `YYYY-MM-DD.md`; `daily: date and company` adds the company name.

## Workspaces
Working folders that file into a named project, longest path first.

| Path | Project | Area |
|---|---|---|
| ~/Code/example-website | Example website | personal |
| ~/Code/example-ios | Example iOS | personal |

## Project aliases
| Alias | Project |
|---|---|
| example-web | Example website |

## Extra projects
- Example website
- Example iOS

## Parameter sets
Extra `fnsh <set> params` sets, read before the table in Prefixes.md.

| Set | Note | Use for |
|---|---|---|

## Prefix aliases
| Phrase | Maps to |
|---|---|

## Routing
- Shared projects go under `Collaboration/<Project>/` with the tags `collaboration, <project-slug>`.

## Maintainer
Leave this out unless you keep a private vault and a public copy.

- maintainer: no

## Ship
| Project | Rule | Folder |
|---|---|---|
| Example kit | notedbro | ~/.local/share/brain/publish |
| Example website | branch-pr | ~/Code/example-website |

## Project tags
| Project | Tag |
|---|---|
| Example Portal | example-portal |
| Example website | example-website |
| Example iOS | example-ios |
