# Advanced configuration

Complete [setup](How%20to%20set%20up.md) and save one session before adding complexity. The minimal workspace map is enough for personal use.

## Preferences and parameters

Preferences.md stores scoped response behavior. Parameters.md stores standing rules and values, including Git behavior, filing thresholds, and the optional filer model. Read the defaults; change only what you intend.

The full phrase reference is [Prefixes](Prefixes.md). Type fnsh phrases in your AI chat. Terminal examples below invoke Python scripts.

## Projects and routing

Keep the minimal Workspace map.md private. Copy individual sections you need from [the advanced example](Workspace%20map.advanced.example.md), rather than activating every example.

Create a project note from _Templates/Project.md, for example Personal/My project/My project.md, with tags project, personal, and my-project. Create its parent folders first. Add a Workspaces row mapping the actual code directory to My project and area personal. A map row alone does not create the project note.

For company work, create Work/Example/Example.md from the area template, then project notes under its Projects folder. Replace Example with your own company only in private files. Shared projects use Collaboration/Project. Project aliases and ticket-key routing are optional.

## Views

Setup creates Decisions and sessions.canvas. Local filing refreshes it. To rebuild in Terminal:

```bash
python3 _Scripts/build-views
```

Obsidian graph configuration is personal. Open Graph view → settings → Groups and add the filters/colors described in [Graph colors](Graph%20colors.md). Add groups individually, preserve existing settings, and put AI groups before note-type groups. No graph configuration is automatically overwritten.

## Backups

Ignored notes, Workspace map.md, local settings, and host snapshots are not backed up by pushing your private repository. Use an independent filesystem backup.

Optional fnsh shadow builds an encrypted snapshot using age and zstd. Keep its private key separately and test recovery. macOS LaunchAgent scheduling is macOS-only; see the script's usage before installing a schedule. Dependency installation can access the network.

## Ship and updates

fnsh ship uses explicit project rules and the configured base (`staging` by default; `main` only when explicitly selected). It requires a complete root `report.md` for the commit and pull-request title and body. It scans selected files, confirms the GitHub account and repository, checks for a matching open pull request before any push, and previews the exact head, base, and PR text before confirmation. Public confirmation is a separate step. A dedicated Ship token handles GitHub API calls, or authenticated `gh` is used when no Ship token is available; Git push uses ordinary Git credentials. See [How to use the brain](How%20to%20use%20the%20brain.md) for token handling and credential-store details. Plain git push bypasses these checks. Keep maintainer rules disabled in personal copies.

fnsh upgrade check reads GitHub metadata. Automatic remote archive installation is incomplete in 1.1.0. Use [Migration 1.1.0](Migration%201.1.0.md). The existing local-source upgrade machinery covers scripts and supporting unit files, not your customized rules, templates, or notes.

See [Maintainer guide](Maintainer%20guide.md) for publication and synchronization.
