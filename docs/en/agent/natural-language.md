# Natural language

With agent instructions active (`AGENTS.md`, Cursor rule, Copilot, …) describe work in plain language — no need to memorize CLI syntax.

| You say | Agent does |
|---------|------------|
| *"Open an issue for the Safari login bug"* | `create` with `bug` label |
| *"Track bug: API returns 500 on /users"* | check duplicates, then `create` |
| *"Create GitHub task for dark mode"* | `create` with `task` label |
| *"List open issues"* | `list` |
| *"Comment on issue #15: fix in PR #99"* | `comment 15` |
| *"Close issue #8, resolved"* | `close 8` |
| *"Import issues from manifest"* | `import --dry-run` then `--apply` |
| *"Apply labels on the repo"* | `labels --apply` |

Italian works too:

| Tu dici | L'agente fa |
|---------|-------------|
| *«Apri issue per il bug del login su Safari»* | `create` con label `bug` |
| *«Elenca le issue aperte»* | `list` |
| *«Chiudi issue #8, risolto»* | `close 8` |

## Instruction files

| Platform | File |
|----------|------|
| Universal | `AGENTS.md` |
| Cursor | `.cursor/rules/github-issues.mdc` |
| Claude Code | `CLAUDE.md` |
| Copilot | `.github/copilot-instructions.md` |

See [Platforms](../platforms/overview.md) for full setup.
