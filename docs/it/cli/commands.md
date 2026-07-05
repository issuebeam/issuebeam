# Comandi

Esegui tutti i comandi dalla **root del progetto** (dove c'è `scripts/`). Stessa CLI su **Windows, macOS e Linux**.

## Label

Definite in `tracker/labels.yml`. Prima volta sul repo:

```bash
python scripts/github_issue.py labels
python scripts/github_issue.py labels --apply
```

## Elenco issue

```bash
python scripts/github_issue.py list
python scripts/github_issue.py list --state closed --limit 50
```

## Creare issue

```bash
python scripts/github_issue.py create "Titolo breve" --body "Descrizione in **markdown**" --labels bug,priority-high,area-frontend
```

Da file:

```bash
python scripts/github_issue.py create "Bug Safari" --body-file descrizione.md --labels bug
```

## Commento

```bash
python scripts/github_issue.py comment 42 --body "Fix applicato in commit abc123"
```

## Chiusura

```bash
python scripts/github_issue.py close 42
python scripts/github_issue.py close 42 --reason "Duplicato di #40"
python scripts/github_issue.py close-batch 10 11 12 --reason "Backlog non prioritario"
```

## Import batch (migrazione da tracker locale)

```bash
cp tracker/import-manifest.example.json tracker/import-manifest.json
# modifica import-manifest.json
python scripts/github_issue.py import --dry-run
python scripts/github_issue.py import --apply
```

Includi **`Legacy ID:`** nel body di ogni voce importata per evitare duplicati:

```markdown
**Legacy ID:** `BUG-001`
```

## Override slug repo

```bash
python scripts/github_issue.py --repo myorg/my-app list
```
