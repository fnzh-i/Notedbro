## What changed

## Runtime reconciliation
- `origin/main` behavior retained:
- Branch behavior retained:
- Intentional differences:

## Checklist
- [ ] No personal data in this change.
- [ ] Only shared files changed; no note was added with `git add -f`.
- [ ] `python3 _Scripts/check-vault` prints `Vault ok.`
- [ ] The `_Scripts/check-*` scripts I touched pass.
- [ ] `_Scripts/release-runtime.sha256` was regenerated after the final runtime edit.
- [ ] `python3 _Scripts/check-release` passed from a full checkout and clean tracked export.
- [ ] `_Config/bootstrap.md` was rebuilt if a rules file changed.
- [ ] One dated line was added to `CHANGELOG.md`.

## Reviewer checkpoint
- [ ] No current runtime behavior was replaced by a stale overlay.
- [ ] Privacy exclusions and Windows UTF-8/LF behavior are preserved.
- [ ] Runtime files and their checksum manifest changed atomically.
