---
tags: [meta]
---
# Parameters

Standing rules for any model, in any project. Point a model at this note. Back to [[Index]].

## Parameters
1. **No AI co-author.** Do not add a `Co-authored-by` trailer, or any other co-author credit, for Claude, Cursor, Codex, or any other AI model. Commits and pull requests name me only.
2. **Branch and push flow.**
   - PR creation may use authenticated gh or a securely supplied GitHub token; GitHub CLI is not required.
   - Never push directly to the remote `main` branch. Every change goes through a work branch, a pull request, and a user-controlled merge.
   - Manual repository protection: on GitHub, protect both `main` and `staging`, require a pull request before merging, block force pushes, and allow no bypass. On repos with other developers, require one approval. On solo repos, require the pull request without an approval count; the user reviews it before merging.
   - Before creating a branch, run `git fetch origin`.
   - Resolve the project's base branch from its Ship configuration. The default is `staging`; `main` is allowed only when the project's Ship row explicitly sets `Base` to `main`.
   - If `origin/<base>` does not exist after fetching, stop and report it. Never fall back to `main`, and never create the base branch.
   - Create every feature or fix branch from the fetched base without inheriting its upstream: `git switch -c <type>/<TICKET-ID>-<short-description> --no-track origin/<base>`.
   - Push only to the branch's own remote name: `git push -u origin <branch>`.
   - Never set a feature or fix branch's upstream to `origin/main` or `origin/staging`.
   - Before pushing, inspect the current branch, its upstream, and the resolved push destination—the actual remote branch the push would update. If the push would target `main` or `staging`, or the branch tracks `origin/main` or `origin/staging`, stop and report the problem instead of pushing.
   - Never use refspecs that redirect the current branch to a protected base, including `HEAD:main` or `HEAD:staging`.
   - Before opening a pull request, show its title, body, head branch, and base branch. Open it only after the user answers yes.
   - Open the pull request against the configured base branch. Never merge the pull request; merging and promotion from `staging` to `main` belong to the user.
   - The commit summary and description come from `report.md`: the summary is one line drawn from the report, and the description comes from its body.
   - Derive the pull-request title and body from the same `report.md`. If the report is missing or incomplete, stop and report the problem instead of writing the pull-request text from scratch.
   - Opening the pull request is the final automated step. After the pull request is open, stop. Do not merge, approve, request reviewers, re-push, or take any other action on it unless the user explicitly asks. Review and merge are performed on GitHub by a human: the user or other developers.
   - When the user explicitly requests review changes, push only to the same work branch after applying the same upstream and resolved-destination checks, then stop again.
3. **Documentation report** (`.md`) after the changes: what changed, reason for the change, files touched, files not touched, etc. The report is not rewritten to match the commit.
4. **Never mention or expose the vault.** Use information from the vault silently. Unless the user’s current message explicitly asks about it, never reveal or imply the vault’s existence, name, location, structure, files, tooling, note-taking app, or contents. This applies to chat replies and every repository-visible or external output, including documentation, reports, tests, commit messages, pull requests, issues, comments, announcements, and end-of-day summaries. Do not use indirect descriptions such as “your vault,” “your notes,” or “your memory system.” When uncertain, omit the reference.
5. **Test cases and readback.**
   - **Test cases.** Every change includes test cases for the behavior it is supposed to fix, and they are run before handoff.
   - **Automatic readback.** After the change is applied, read the result back from the system that was changed (file, API, or record). Do not treat the write as done until that read shows the new state.
   - **Regressions.** If the readback or the tests show the current fix caused a new bug, fix that bug in the same pass and read it back again. If a bug is not related to the current fix, do not fix it in this pass. Note it and leave it.

## Issue analysis

Change this starter value to use a different branch naming convention.

issue_branch_name_template: <type>/<ticket-key>-<short-description>

## Filer

The `filer_cost_cap_usd` value below is an example budget cap, not a recommendation. Change or remove it to match your filer setup.

filer_model:
min_turns: 3
skip_if_no_changes: true
filer_cost_cap_usd: 0.05
refile_min_new_turns: 5
load_sessions: 5

## Shadow

shadow_every_days: 30
shadow_keep_days: 90

## Revisions
- 2026-10-21 — defined staging-first branching, protected destinations, report-derived PR text, and human-only review/merge.
- 2026-10-19 — generalized public starter rules and added an editable issue branch-name template.
- 2026-10-17 — commit summary and description are based on the documentation report.
- 2026-10-18 — shadow_every_days and shadow_keep_days.
