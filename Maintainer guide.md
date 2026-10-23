# Maintainer guide

This page is for maintaining public Notedbro. Personal users need only [setup](How%20to%20set%20up.md) and [daily use](How%20to%20use%20the%20brain.md).

## Publishing and synchronization

fnsh publish builds a public starter tree from the manifest and scans it locally. It does not push. fnsh sync fetches merged changes into explicitly shared paths; scheduled synchronization does not replace scripts.

The private workspace map must explicitly enable the maintainer role and shipping rule. Keep example maintainer settings inactive for normal users. Generated local Claude settings, hooks, backups, locks, notes, maps, and host snapshots must be excluded even if mistakenly added to an include list.

New shared guides must be in the starter manifest and synchronization allowlist. Generated bootstrap content must follow its sources.

## Checks

Run in Terminal from a full development checkout:

```bash
python3 _Scripts/check-release
```

The release checker verifies the runtime manifest, historical Git baseline, and all onboarding tests in the full checkout. It then copies only tracked working-tree files into a temporary clean export and runs documentation, onboarding, repository validators, and every script self-check there. Ignored local files such as `report.md` are never copied. CI runs this gate on macOS/Linux and runs the portable validators plus Ship and publish checks natively on Windows. Every validation job remains guarded to github.repository == 'fnzh-i/Notedbro'.

## Checksum provenance

Verify the historical manifest against the pinned v1.0.0 Git commit before release. Never regenerate historical hashes from an installed folder. Include that manifest inside the release.

After the final script change, run python3 _Scripts/build-runtime-manifest to regenerate _Scripts/release-runtime.sha256 from raw bytes of shipped runtime files, excluding checksum manifests, bytecode, and private snapshots. Entries are sorted. `--check` lists missing, unexpected, and mismatched runtime paths. Verify the manifest against an exported release candidate. It detects incomplete runtime migration; it is not a signed release-authenticity guarantee.

## Release 1.1.0 gate

Before promotion:

1. Pass all automated checks, including private generated files, duplicate delivery, old-hook detection, checksums, and customized migration.
2. Exercise Claude and Cursor using their real installed versions; save the versions and first-session results in the release report.
3. Verify Codex manual filing and web paste/save behavior.
4. Enable **Settings → General → Template repository** on GitHub, then test **Use this template → Private** in an authorized test copy.
5. Verify upstream CI passes and a private template copy skips the jobs.
6. Merge the reviewed code, then tag that merged commit v1.1.0 and publish a stable release with the migration guide.

The release report must record the commit, operating system, Python version, command or host tested, result, and evidence link or concise observation for every macOS, Ubuntu, Windows, Claude, Cursor, Codex, web, and private-template-copy gate. Unverified rows remain explicitly marked `Pending`; local checks must not be presented as hosted CI or real-host evidence.

Publishing a release, changing repository settings, and pushing code use the established human-controlled workflow. Local automated checks cannot substitute for those actual-host and GitHub checks.
