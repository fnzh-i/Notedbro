# Notedbro 1.1.0 release candidate

Status: awaiting upstream CI, actual-host smoke checks, GitHub template enablement, and release approval.

## Changes

- Private-template onboarding with explicit host capabilities and manual web use.
- Idempotent setup, project-local Claude settings, repaired v1.0.0 paths, and preservation of customization.
- Historical checksum comparison, gated version promotion, and static legacy-hook destination checks.
- Serialized session filing for duplicate delivery to the same upgraded implementation.
- Private generated settings and CI guards for template copies.

## Compatibility and installation

macOS is the primary local platform; portable workflows are covered by macOS/Linux CI. Native Windows/WSL are unverified. Claude must start at Brain's root. Cursor needs its user-rule step. Codex and web saving are manual.

Read [Migration 1.1.0](Migration%201.1.0.md) before updating. Remote archive installation is incomplete; upgrade check reads version metadata only. Ignored content requires independent backups.

Do not mark this candidate ready for beginner promotion until the release gates in [Maintainer guide](Maintainer%20guide.md) are recorded.
