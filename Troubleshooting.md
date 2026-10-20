# Troubleshooting and uninstall

## Setup cannot find files

In Terminal, change to the Brain folder containing AGENTS.md and _Scripts before running setup. Quote paths containing spaces. Use python3 --version to verify Python 3.9 or later. If the folder already exists, inspect it before cloning anything.

## A map is missing or still contains examples

Run the setup command for your host. It creates a minimal map when missing and preserves an existing map. Review your existing map manually if it contains Example values; setup does not rewrite your routing.

check-vault validates structure. A starter can be structurally valid while setup is incomplete; the output explicitly distinguishes those cases.

## Invalid settings or a tracked local file

If .gitignore is missing, restore the shipped ignore file before rerunning setup. Setup stops before preparing personal files in that case.

Setup reports malformed JSON instead of replacing it. Back up the file and repair its JSON syntax, preserving other keys.

If .claude/settings.local.json is tracked, review it and run this in Terminal before setup:

```bash
git rm --cached -- .claude/settings.local.json
```

This stops future tracking but does not erase previous commits. Review repository history separately if it contained sensitive values. Keep the explicit ignore rule.

## No session was saved

Claude: start at Brain's root, inspect the local SessionEnd configuration, restart Claude after changes, complete a task that changes a file, and exit normally. A short unchanged chat can intentionally be skipped.

Cursor: install the user rule and check that your version delivers hook events. Codex: send fnsh update and ensure filesystem access is granted. Browser chats: save the returned card yourself.

A missing transcript should be reported honestly. A fallback card is not evidence that the transcript was parsed successfully.

## Legacy global Claude hook

Setup prints the exact settings file, command, and resolved destination where possible. Back up that settings file. Open its hooks → SessionEnd list and remove only the Notedbro command shown. If its entry has other commands, retain them. Keep every unrelated hook and key.

If intentionally retaining a legacy wrapper, it must reach this installation's upgraded filer and destination. A wrapper pointing to another or old installation remains a migration blocker. Setup never executes arbitrary hook commands to inspect them.

Rerun setup and verify one session produces one note. Duplicate protection does not extend to a separate old filer.

## Access and remote problems

Private GitHub clones need account authentication via credentials or SSH. GitHub account passwords do not authenticate Git HTTPS operations. An HTTPS remote URL alone cannot prove repository visibility; verify Private in GitHub.

fnsh upgrade check reports metadata only. Use the migration guide to install a release.

## Uninstall

End active sessions and back up Brain and host configuration.

- Claude: remove only the Notedbro command from Brain's .claude/settings.local.json. Preserve other local settings. Remove the generated .claude/hooks/notedbro.py after no hook references it. Also inspect any reported legacy global entry.
- Cursor: remove only Notedbro's entries from the user's hooks.json, its generated wrapper after references are gone, and the marked user-rule block.
- Codex: remove only the marked block from the active global AGENTS.md.
- Browser: remove pasted custom instructions if you added any.

Keep your notes, maps, transcripts, encryption keys, and backups. You can continue reading the Markdown files without Notedbro. Do not delete .claude/settings.json or whole configuration directories.
