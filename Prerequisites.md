# Prerequisites

For automated local setup:

- Git: verify in Terminal with `git --version`.
- Python 3.9 or later: verify with `python3 --version`.
- One installed local tool: Claude Code, Cursor, or Codex.
- A GitHub account to create the recommended private template copy.

Any Markdown editor works. Obsidian is optional. Browser-only users can read and manually fill the Markdown templates without running scripts.

Install Git from [git-scm.com](https://git-scm.com/downloads) and Python from [python.org](https://www.python.org/downloads/), or use your operating system's package manager. Finish prerequisites before the quick start.

macOS is the primary local environment. Portable setup, migration, and filing are covered by macOS/Linux CI. Native Windows and WSL are unverified; LaunchAgent scheduling requires macOS. CI cannot prove that every installed AI-host version emits the expected events: complete the actual-host verification in the setup guide.

Optional encrypted backups require age and zstd. On macOS install them in Terminal with `brew install age zstd`. Installing dependencies uses the network.

Scripts discover Brain from their installed folder, or BRAIN_VAULT when explicitly supplied. Generated hooks remember the selected location. If you move Brain, rerun setup and review legacy-hook findings. The default instructions use ~/Documents/Brain.
