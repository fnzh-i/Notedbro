# How to set up

Read [Prerequisites](Prerequisites.md) first.

1. **Clone** the repo into place:
   `git clone https://github.com/fnzh-i/Notedbro ~/Documents/Brain`
2. **Copy the example map:**
   `cp "Workspace map.example.md" "Workspace map.md"`, then replace the example company, ticket key, and folders with yours. Git ignores `Workspace map.md`.
3. **Review your defaults:** `Preferences.md` controls response style and behavior. `Parameters.md` holds standing rules, limits, paths, and other values. The starter kit includes the maintainer's usable defaults; keep, edit, or remove any entry.
4. **Check the vault:** `python3 _Scripts/check-vault`. Expect `Vault ok.` If a host or harness file is missing, it prints the `fnsh rebuild <host>` line to run.
5. **Pick a host:**
   - Cursor or Claude Code: run `python3 _Scripts/load-host cursor` (or `claude`) once from a terminal. After that, `fnsh load <host>` works in chat. It adds the filing hook and the brain block, and leaves existing files alone.
   - Codex: manual. Paste the block between `<!-- brain:start -->` and `<!-- brain:end -->` in `Hosts/Web.md` into `~/.codex/AGENTS.md`, then say `fnsh update` after a turn that changed something.
   - ChatGPT, Claude.ai, or Gemini: paste the same block from `Hosts/Web.md` into the site's custom instructions.
6. **Say `fnsh brain`** in a new chat. Expect `Brain ready: <host> / <model> / <profile>`.
7. **Add your areas:** copy `_Templates/Area.md` into `Work/<Company>/<Company>.md` for each company, and set the same name in `Workspace map.md`.
8. **Learn the phrases:** `Prefixes.md` lists them all. `fnsh check` runs the vault check. `fnsh update` files the chat by hand.
9. **Keep private data out of tracked notes.** Real notes go under the five areas, which git ignores. Real folders, projects, and ticket keys go in `Workspace map.md`.
