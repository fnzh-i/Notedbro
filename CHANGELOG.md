# Changelog

One dated line per pull request, newest first. Written in the pull request; sync never writes it.

- 2026-10-22 — Added portable Ship token setup and status, repository validation, safe PR recovery, and Windows checks.
- 2026-10-21 — Let `fnsh ship` create PRs with a securely supplied token or authenticated gh, and stop before push when a matching open PR exists.
- 2026-10-19 — Distinguished an unpublished release from a GitHub connection failure in `fnsh upgrade check`, and restored direct execution for `upgrade` and `guard`.
- 2026-10-19 — Generalized the shipped preferences and parameters into public starter defaults and linked the plan, ticket, and commit templates to them.
- 2026-10-19 — Presented the included preferences and parameters as usable public starter defaults that each user can keep, edit, or remove.
- 2026-10-19 — Renamed Cerebro to Notedbro to give the project a warmer, more natural, and more approachable identity. The new name better reflects its conversational role: helping AI assistants take note of the context that matters and carry it into future work.
- 2026-10-19 — Added GitHub Actions CI for repository validators and script self-checks on Python 3.9 and 3.15.
- 2026-10-19 — Single-folder starter kit. `fnsh ship`, `fnsh guard`, and `fnsh upgrade` for users. `fnsh publish` and `fnsh sync` are maintainer-only and never push.
- 2026-10-18 — Centered README header with logo and screenshot in `assets/branding/`. Publish copies that folder and skips binary images when scanning for private terms.
- 2026-10-18 — First public release: shared notes, templates, scripts, five starter hubs, and the repo docs.
