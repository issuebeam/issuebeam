# Piattaforme supportate

Issuebeam **non è legato a Cursor**. Se il tuo agente legge file nel repo ed esegue comandi shell, funziona.

## Confronto rapido

| Piattaforma | File istruzioni | Accesso shell |
|-------------|-----------------|---------------|
| [Cursor](cursor.md) | `.cursor/rules/github-issues.mdc` | Sì |
| [Claude Code](claude-code.md) | `CLAUDE.md`, `AGENTS.md` | Sì |
| [GitHub Copilot](copilot.md) | `.github/copilot-instructions.md`, `AGENTS.md` | Sì |
| [Altri agenti](other-agents.md) | `AGENTS.md` o equivalente | Sì |
| Manuale | — | Esegui tu la CLI |

## Stessa CLI ovunque

| Livello | Dipende dalla piattaforma? |
|---------|----------------------------|
| `scripts/github_issue.py` | No |
| Token, slug, label | No |
| File istruzioni agente | Sì — cambia il percorso |

## Team misti

Puoi includere **tutti** i file istruzioni in un repo — non vanno in conflitto:

- Cursor legge `.cursor/rules/`
- Claude Code legge `CLAUDE.md`
- Copilot legge `copilot-instructions.md`
- Tutti puntano alla stessa CLI e convenzioni

## Quale file usare

| Usi… | File minimi |
|------|-------------|
| Solo Cursor | `.cursor/rules/github-issues.mdc` |
| Solo Claude Code | `AGENTS.md` + `CLAUDE.md` |
| Solo Copilot | `AGENTS.md` + `.github/copilot-instructions.md` |
| Team misto | Tutti i precedenti |

`adopt.py` copia automaticamente il set comune.
