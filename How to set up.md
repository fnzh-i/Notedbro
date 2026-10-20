# How to set up

These instructions configure Notedbro 1.1.0. Read [Prerequisites](Prerequisites.md) first. Migrating an existing folder? Start with [Migration 1.1.0](Migration%201.1.0.md).

## Create a private copy

1. On [Notedbro](https://github.com/fnzh-i/Notedbro), select **Use this template → Create a new repository**.
2. Select **Private**, name the copy Brain, and create it.
3. Open the private copy's **Code** menu and copy its clone URL.
4. Open Terminal. Replace YOUR-ACCOUNT in this command with the owner of your copy:

```bash
mkdir -p ~/Documents
git clone https://github.com/YOUR-ACCOUNT/Brain.git ~/Documents/Brain
cd ~/Documents/Brain
```

If GitHub asks you to authenticate, use your configured credential manager or SSH URL; an account password is not a Git HTTPS credential. Follow [GitHub authentication guidance](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github).

If the Brain folder already exists, stop and inspect it. Never clone over or delete an existing installation.

## Run setup for your tool

**Terminal, from Brain's root** (the folder containing AGENTS.md and _Scripts):

```bash
python3 _Scripts/setup codex
```

Choose `claude`, `cursor`, or `web` instead where appropriate. Setup prepares a private map, privacy rules, a canvas, and the selected host. A successful command still requires the real-session check below. Repeating the command is safe and should report unchanged local files.

### Codex

Setup adds a marked block to the default `~/.codex/AGENTS.md`, preserving surrounding instructions. This is a global instruction file: future Codex chats can see the reference, but still need permission/access to Brain. Custom CODEX_HOME or an overriding AGENTS.override.md requires manual configuration of the active instruction file.

Open Brain as the local project or explicitly grant the chat access to it. Start a new chat and send `fnsh brain`. Expect `Brain ready: codex / <model> / Hosts/Codex`; unknown model metadata may be reported honestly.

After a small task that changes a file, send `fnsh update`. Codex filing is manual. Confirm a session card and its transcript path; a missing transcript must be reported rather than invented.

See [OpenAI's instruction-loading description](https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide).

### Claude Code

Setup merges the hook into `.claude/settings.local.json` within Brain. Shared project settings and global Claude settings are preserved. Local settings and the generated hook stay untracked.

**Terminal:**

```bash
cd ~/Documents/Brain
claude
```

Start at **Brain's root**, not Brain/Projects/x or another repository. Subfolder launch behavior is not part of the 1.1.0 guarantee. Trust the project and inspect hook configuration using your installed Claude Code's hook controls.

**AI chat:** send `fnsh brain`, complete a small file-changing task, then exit the session normally. The SessionEnd hook should create exactly one card. Restart Claude after configuration changes.

An old global hook can also run. Setup reports whether it reaches this upgraded filer or needs migration. Resolve every migration finding before calling setup complete.

### Cursor

**Terminal:**

```bash
python3 _Scripts/setup cursor
```

Setup creates or merges hook configuration in the default user configuration directory. Custom hook files are preserved.

Open **Cursor Settings → Rules → User Rules**. Copy only the marked block from Hosts/Web.md into your user rule, preserving existing rules. Replace the default Brain path with the full path to your installation if it differs. Start a new chat with access to Brain.

**AI chat:** send `fnsh brain`, perform a small file-changing task, and allow the chat to finish. Verify one card. Hook event availability depends on the installed Cursor version; failure to create a card means the integration remains unverified.

### Web chats

**Terminal:**

```bash
python3 _Scripts/setup web
```

Expect:

```text
Local files prepared. Web workflow is manual.
No browser connection or automatic filing was configured.
```

In the browser, paste/upload the relevant rules and context you want to share. A filesystem path alone gives a browser chat no access to local files. Do not paste the local-host block into custom instructions and expect automatic access.

Ask: “Summarize this session as a Markdown card with Asked and Changed sections. Return the text for me to save.” Save the returned card using the session template under Personal/Chats/Sessions. Use host chatgpt, claude-ai, or gemini and leave the transcript empty when none exists.

## Verify the first session

For local hosts, inspect Personal/Chats/Sessions. Without project routing, a qualifying conversation should create one card. Check Asked, Changed, host, conversation ID, and transcript path. A change-making session should also have one Daily entry and one session-index entry.

For web use, open the card you saved manually. This verifies the manual workflow only.

**Terminal:**

```bash
python3 _Scripts/check-vault
```

Configured files should print `Vault ok. Notedbro v1.1.0.`. A fresh unconfigured starter prints a setup warning. This structural check does not prove that your host delivered a hook event.

## Optional editor and customization

In Obsidian select **Open folder as vault** and choose Brain. Open Index.md or the generated Decisions and sessions.canvas. Other Markdown editors work too.

Review Preferences.md and Parameters.md before serious work: their shipped defaults include commit-only behavior and a required change report. To add projects later, use [Advanced configuration](Advanced%20configuration.md). Keep an independent backup of ignored content.
