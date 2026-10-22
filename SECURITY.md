# Security

## Reporting a problem
Report a vulnerability through GitHub private vulnerability reporting: open the Security tab of https://github.com/fnzh-i/Notedbro and choose "Report a vulnerability". Do not open a public issue for it.

## Supported versions
Only `main` is supported. Fixes land there.

## Scope
The scripts run on your own machine, against your own vault. They make no network calls except the optional filer model call set in `Parameters.md`. They write only inside the vault, or in the folders under `~/.local/share/brain` and `~/.config/brain`.

Never commit notes, keys, or `Workspace map.md`.
