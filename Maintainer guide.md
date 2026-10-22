# Maintainer guide

This page is for maintaining public Notedbro. Personal users need only [setup](How%20to%20set%20up.md) and [daily use](How%20to%20use%20the%20brain.md).

## Publishing and synchronization

fnsh publish builds a public starter tree from the manifest and scans it locally. It does not push. fnsh sync fetches merged changes into explicitly shared paths; scheduled synchronization does not replace scripts.

The private workspace map must explicitly enable the maintainer role and shipping rule. Keep example maintainer settings inactive for normal users. Generated local Claude settings, hooks, backups, locks, notes, maps, and host snapshots must be excluded even if mistakenly added to an include list.

New shared guides must be in the starter manifest and synchronization allowlist. Generated bootstrap content must follow its sources.

## Checks

Run in Terminal from a full development checkout:

```bash
python3 _Scripts/check-onboarding
python3 _Scripts/check-docs
python3 _Scripts/check-migration verify-baseline
python3 _Scripts/check-collaboration
python3 _Scripts/check-file-session
python3 _Scripts/check-provenance-tags
python3 _Scripts/check-vault
```

Also run existing script self-checks. CI runs portable checks on macOS/Linux and guards every validation job to github.repository == 'fnzh-i/Notedbro'. Inherited template workflows can show skipped runs; they allocate no validation runner. A contributor can deliberately adapt that condition for another repository.

## Checksum provenance

Verify the historical manifest against the pinned v1.0.0 Git commit before release. Never regenerate historical hashes from an installed folder. Include that manifest inside the release.

After changing scripts, run python3 _Scripts/build-runtime-manifest to regenerate _Scripts/release-runtime.sha256 from raw bytes of shipped runtime files, excluding checksum manifests, bytecode, and private snapshots. Entries are sorted. Verify the manifest against an exported release candidate. It detects incomplete runtime migration; it is not a signed release-authenticity guarantee.

## Release 1.1.0 gate

Before promotion:

1. Pass all automated checks, including private generated files, duplicate delivery, old-hook detection, checksums, and customized migration.
2. Exercise Claude and Cursor using their real installed versions; save the versions and first-session results in the release report.
3. Verify Codex manual filing and web paste/save behavior.
4. Enable **Settings → General → Template repository** on GitHub, then test **Use this template → Private** in an authorized test copy.
5. Verify upstream CI passes and a private template copy skips the jobs.
6. Merge the reviewed code, then tag that merged commit v1.1.0 and publish a stable release with the migration guide.

Publishing a release, changing repository settings, and pushing code use the established human-controlled workflow. Local automated checks cannot substitute for those actual-host and GitHub checks.
