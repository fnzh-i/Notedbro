# Contributing

Pull requests go to https://github.com/fnzh-i/Notedbro.

1. Clone public Notedbro for development and branch from `main`. Personal users should create a private template copy using the setup guide. One change per pull request.
2. Change only shared files: the shared notes, `AGENTS.md`, `CLAUDE.md`, the repo docs, `Hosts/`, `_Templates/`, `_Scripts/`, `.github/`, and `assets/`.
3. Never `git add -f` a note. If git ignores a file, it stays on your machine.
4. Use the example vocabulary: `Example`, `EX-NNN`, `Work/Example/`. Real names, employers, ticket keys, and paths go in your own `Workspace map.md`.
5. Run `python3 _Scripts/check-release` from a full checkout. It verifies historical Git state and a clean tracked-files export, so ignored local files cannot affect the release candidate.
6. If you change `How this vault works.md`, `Prefixes.md`, or `Parameters.md`, run `python3 _Scripts/build-bootstrap` and commit `_Config/bootstrap.md` with it.
7. Add one dated line to `CHANGELOG.md` in the same pull request.
8. Fill in the pull request checklist. The first item is "no personal data in this change".

Conduct: see [CODE_OF_CONDUCT](CODE_OF_CONDUCT.md).

For onboarding, hooks, migrations, publication, or shipping, document how the branch was reconciled with `origin/main`; identify retained main behavior, retained branch behavior, and intentional differences. Keep historical checksums pinned to the released v1.0.0 commit. Regenerate runtime checksums after the final script change as described in [Maintainer guide](Maintainer%20guide.md).

Every CI job is guarded to fnzh-i/Notedbro. Template copies show skipped workflows and use no validation runner. Contributors can deliberately adapt this condition in their own development repository. Preserve the guard in upstream changes.
