# Notedbro 1.1.0 implementation report

## What changed

Added reliable onboarding and deterministic migration: explicit private-template setup, host-specific instructions, project-local Claude settings, v1.0.0 checksum comparison, safe version promotion, static legacy-hook checks, and serialized session filing. Generated configuration is private, and CI jobs are restricted to the upstream repository. Codex JSONL records are normalized so manual filing captures the request and recognized file edits.

## Reason

Fresh users could follow incomplete instructions, miss hooks, or believe configuration was working before a session was verified. Existing users needed a deterministic comparison with released files and clear handling of old global hooks.

## Files touched

Setup, migration and documentation validators; hook restoration and filing; publication, synchronization and shipping rules; starter manifests, examples, version and bootstrap; CI; README, setup, daily-use, security, contribution and release guides.

## Files not touched

User notes, maps, preferences, parameters, existing company/project instructions, global Claude configuration, and published GitHub releases. Remote archive installation remains deferred.

## Validation

Passed locally on macOS with Python 3.9.6:

- All 24 onboarding/migration integration tests, including empty-home setup, idempotence, custom configuration preservation, unsafe paths, inherited-CI guard regression, web-only behavior, exported-release setup, and execution of the README command block against a local private-copy fixture.
- Concurrent legacy/local hook delivery, replay without duplicate notes/index/Daily entries, and failure recovery.
- Codex transcript parsing with request, model, recognized edit, and Daily output.
- Historical manifest verification against all 75 files of the pinned v1.0.0 commit; the runtime manifest covers every shipped runtime file.
- Documentation link/path checks, collaboration/file-session/provenance validators, structural starter validation, all six existing script self-checks, and git diff whitespace validation.

## Remaining release gates

The code is a release candidate. GitHub's Template repository setting remains disabled and must be enabled before promoting the private-template journey. Upstream macOS/Linux CI, actual Claude/Cursor hook delivery, a real Codex manual-filing walkthrough, and a private-template-copy test still require recording. Claude and Cursor executables were not available in this local environment. No remote settings, branches, pull requests, tags, or releases were changed.

Customized runtime files are preserved and flagged. Version promotion requires the shipped runtime bytes; unresolved custom runtime changes must be reviewed before finishing migration. This is deliberately stricter than trusting a version label.

## CI follow-up: deterministic publication fixtures

Reproduced the exported-release smoke failure with the hosted account name: the privacy scanner interpreted ordinary CI expressions and documentation mentioning that account as private login-name disclosures. The original failing assertion was the exported tree's content scan, not setup or migration.

The exported-release test and publication self-check now use a synthetic fixture identity and home directory. The smoke test always simulates the hosted account first, so local runs cover this regression. Scan failures print every finding, and a separate regression test confirms both tree and text scans still reject planted home paths and login names. Production privacy scanning is unchanged.

Files touched: `_Scripts/check-onboarding`, `_Scripts/publish`, the regenerated `_Scripts/release-runtime.sha256`, and this report. No user content, host configuration, workflow permissions, historical checksums, or production scanner rules changed.

Validation on macOS/Python 3.9.6: all 24 onboarding tests passed, including a separate full-suite run simulating the hosted account; all repository validators and six script self-checks passed; all 75 historical hashes verified. The hosted Actions matrix still needs a rerun after this local commit is pushed.

## Release evidence

Record evidence without inferring one environment from another:

| Gate | Commit | Environment/version | Result | Evidence |
|---|---|---|---|---|
| Clean release check | Current PR candidate | macOS, Python 3.9.6 | Passed | 24 full-checkout onboarding tests; 75 historical and 31 runtime files; clean-export validators and self-checks |
| GitHub matrix | Pending | macOS, Ubuntu, Windows; Python 3.9 and 3.15 | Pending | Actions run URL |
| Claude first session | Pending | Installed Claude version | Pending | Concise observed result |
| Cursor first session | Pending | Installed Cursor version | Pending | Concise observed result |
| Codex manual filing | Pending | Installed Codex version | Pending | Concise observed result |
| Web paste/save | Pending | Browser and version | Pending | Concise observed result |
| Private template copy | Pending | Authorized private repository | Pending | Repository or run URL |
