# Adotta in un progetto

Dalla cartella **issuebeam** (o dopo aver clonato questo repo):

```cmd
python scripts/adopt.py --target ..\my-repo --repo myorg/my-app
```

Usa `--force` per sovrascrivere file già presenti.

## Cosa copia `adopt.py`

| Elemento | Scopo |
|----------|-------|
| `scripts/github_issue.py` | CLI |
| `tracker/*` | Label, esempi, file slug |
| `.github/ISSUE_TEMPLATE/*` | Form web |
| `.github/copilot-instructions.md` | GitHub Copilot |
| `.cursor/rules/github-issues.mdc` | Cursor |
| `AGENTS.md`, `CLAUDE.md` | Regole universali / Claude Code |

## Cosa crea

- `tracker/github_repo` con il tuo slug
- `tracker/import-manifest.json` dall'esempio (se mancante)
- `.secrets/.gitkeep`

## Dopo l'adozione

```cmd
cd ..\my-repo
python scripts/github_issue.py labels --apply
python scripts/github_issue.py list
```

Apri la cartella nel **tuo agente AI**:

| Piattaforma | File istruzioni |
|-------------|-----------------|
| Cursor | `.cursor/rules/github-issues.mdc` |
| Claude Code | `CLAUDE.md` + `AGENTS.md` |
| Copilot | `.github/copilot-instructions.md` + `AGENTS.md` |
| Altro | Vedi [Piattaforme](../platforms/overview.md) |

Documentazione completa: [issuebeam.github.io/docs/it](https://issuebeam.github.io/docs/it/)
