# Migrate v1.0.0 to v1.1.0

This procedure uses a separate extracted 1.1.0 release. Remote version checking does not install it. End active AI sessions before migration.

## 1. Obtain the release and back up

Download the 1.1.0 source archive from [Releases](https://github.com/fnzh-i/Notedbro/releases) and extract it beside, not over, your existing Brain. Before release publication, maintainers use an exported release candidate.

In Terminal, make a backup outside the installation. Choose an unused backup destination:

```bash
cp -pR ~/Documents/Brain ~/Documents/Brain-before-1.1.0
```

Back up relevant user configuration separately: ~/.claude, ~/.cursor, and ~/.codex if present. Keep those backups private. A private Git remote does not include ignored files.

## 2. Compare known bytes

Change into the extracted 1.1.0 folder. Replace the target below if yours differs:

```bash
python3 _Scripts/check-migration ~/Documents/Brain
```

The shipped _Scripts/migrations/v1.0.0.sha256 records raw-byte hashes from released commit 3183f11e60a48e8e7dbce4ef8e28267a5031862c. The checker works offline.

- stock v1.0.0: exact historical content.
- already current: exact supplied 1.1.0 content.
- modified: differs from both.
- missing: no installed file.
- unknown: unsafe, unrecognized, symlink, or otherwise unresolved.

Executable permissions are checked separately. Exit status 1 means review is needed; stock files awaiting replacement are listed explicitly.

## 3. Apply only eligible replacements

Review and run the printed mkdir/cp/chmod commands after making your backup. They reference the separate release source and your existing installation. Keep the files unchanged between comparison and copying; rerun the comparison if anything changes.

Protected notes, maps, preferences, parameters, instruction files, and .gitignore are never bulk-copied. Modified or unknown files get no automatic replacement command. Manually merge required script changes and preserve customization. Host instruction-path repairs and privacy additions are handled by setup.

The version file is deliberately held back. Readiness requires the exact shipped runtime checksums; modified runtime files require resolving the merge against the release, not merely changing the version label.

## 4. Configure and finish verification

While still in the extracted release folder, run its setup against the existing installation:

```bash
BRAIN_VAULT=~/Documents/Brain python3 _Scripts/setup claude
```

Use cursor, codex, or web for your tool. Running the release's setup ensures its checksum baseline verifies the target. It refuses version promotion if runtime files or legacy hooks remain unresolved.

For Claude, resolve each legacy-global-hook finding using [Troubleshooting](Troubleshooting.md). A hook pointing to an old filer elsewhere must be removed or updated. Global settings are not edited automatically. Two wrappers reaching the same upgraded filer share duplicate protection; a separate old copy does not.

After setup:

```bash
cd ~/Documents/Brain
python3 _Scripts/setup claude
python3 _Scripts/check-vault
```

The second setup run should change nothing. Start the actual host using [the setup guide](How%20to%20set%20up.md), complete a qualifying session, and inspect one note, one index entry, and one Daily entry.

Keep the original backup until verification passes. Record unresolved customizations. Structural checks alone do not verify real host events.

## Shared documentation and workflows

Review modified shared files individually. Preserve company/project instructions and user defaults. Remove or adapt inherited CI in old private copies; 1.1.0 guards upstream validation jobs to fnzh-i/Notedbro. The printed eligible replacement list includes the stock workflow.

Manually customized instructions must retain or receive the corrected _Templates/Session.md and _Scripts/file-session paths. Setup repairs recognized marked blocks with backups.
