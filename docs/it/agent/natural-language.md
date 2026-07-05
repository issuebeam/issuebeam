# Linguaggio naturale

Con le istruzioni agente attive (`AGENTS.md`, regola Cursor, Copilot, …) descrivi il lavoro in linguaggio naturale — non serve ricordare la sintassi CLI.

| Tu dici | L'agente fa |
|---------|-------------|
| *«Apri issue per il bug del login su Safari»* | `create` con label `bug` |
| *«Traccia bug: API restituisce 500 su /users»* | verifica duplicati, poi `create` |
| *«Crea task GitHub per dark mode»* | `create` con label `task` |
| *«Elenca le issue aperte»* | `list` |
| *«Commenta issue #15: fix in PR #99»* | `comment 15` |
| *«Chiudi issue #8, risolto»* | `close 8` |
| *«Importa le issue dal manifest»* | `import --dry-run` poi `--apply` |
| *«Applica le label sul repo»* | `labels --apply` |

Funziona anche in inglese:

| You say | Agent does |
|---------|------------|
| *"Open an issue for the Safari login bug"* | `create` with `bug` label |
| *"List open issues"* | `list` |

## File istruzioni

| Piattaforma | File |
|-------------|------|
| Universale | `AGENTS.md` |
| Cursor | `.cursor/rules/github-issues.mdc` |
| Claude Code | `CLAUDE.md` |
| Copilot | `.github/copilot-instructions.md` |

Vedi [Piattaforme](../platforms/overview.md) per il setup completo.
