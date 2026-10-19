# Contributing

Pull requests go to https://github.com/fnzh-i/Notedbro.

1. Branch from `main`. One change per pull request.
2. Change only shared files: the shared notes, `AGENTS.md`, `CLAUDE.md`, the repo docs, `Hosts/`, `_Templates/`, `_Scripts/`, `.github/`, and `assets/`.
3. Never `git add -f` a note. If git ignores a file, it stays on your machine.
4. Use the example vocabulary: `Example`, `EX-NNN`, `Work/Example/`. Real names, employers, ticket keys, and paths go in your own `Workspace map.md`.
5. Run `python3 _Scripts/check-vault` and the `_Scripts/check-*` scripts you touched. All must pass.
6. If you change `How this vault works.md`, `Prefixes.md`, or `Parameters.md`, run `python3 _Scripts/build-bootstrap` and commit `_Config/bootstrap.md` with it.
7. Add one dated line to `CHANGELOG.md` in the same pull request.
8. Fill in the pull request checklist. The first item is "no personal data in this change".

Conduct: see [CODE_OF_CONDUCT](CODE_OF_CONDUCT.md).
