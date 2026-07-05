# Slug repository

La CLI deve sapere **quale repo** GitHub usare (`owner/nome`).

Ordine di risoluzione:

| Priorità | Sorgente |
|----------|----------|
| 1 | Variabile d'ambiente `GITHUB_REPO` |
| 2 | `.env` → `GITHUB_REPO=owner/repo` |
| 3 | `tracker/github_repo` — una riga (creato da `adopt.py`) |

## Opzione A — file locale (consigliata dopo adopt)

Cross-platform (Python 3):

```bash
python -c "from pathlib import Path; Path('tracker/github_repo').write_text('myorg/my-app\n')"
```

## Opzione B — `.env`

```
GITHUB_REPO=myorg/my-app
GITHUB_TOKEN=github_pat_...
```

## Opzione C — override una tantum

```bash
python scripts/github_issue.py --repo myorg/my-app list
```

## Primi comandi

Dopo token e slug:

```bash
python scripts/github_issue.py labels --apply
python scripts/github_issue.py list
```

Uguale su **Windows, macOS e Linux**.
