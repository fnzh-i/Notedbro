---
tags: [meta]
---
# Parameters

Standing rules for any model, in any project. Point a model at this note. Back to [[Index]].

## Parameters
1. **No AI co-author.** Do not add a `Co-authored-by` trailer, or any other co-author credit, for Claude, Cursor, Codex, or any other AI model. Commits and pull requests name me only.
2. **Git.** Double-check you're on a local feature branch, not `main` or `origin/main`. **Commit only.** No push, no PR (I do those). This is a starter default: change it if you want the agent to push branches or open pull requests. The one exception is `fnsh ship` followed by yes: that prefix may commit, push the feature branch, and open a pull request. It still never pushes `main`. The commit message has a summary and a description, both based on the documentation report. The summary is one line drawn from the report. The description is drawn from the report body: what changed, the reason, files touched, and files not touched.
3. **Documentation report** (`.md`) after the changes: what changed, reason for the change, files touched, files not touched, etc. The report is not rewritten to match the commit.
4. **Keep the vault out of outputs.** Do not mention the vault, its notes, or the note-taking app in reports, test templates, commits, pull requests, issue trackers, announcements, end-of-day summaries, or other outputs unless the user asks about them.
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
- 2026-10-19 — generalized public starter rules and added an editable issue branch-name template.
- 2026-10-17 — commit summary and description are based on the documentation report.
- 2026-10-18 — shadow_every_days and shadow_keep_days.
