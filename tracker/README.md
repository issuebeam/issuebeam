# Tracker — GitHub Issues (issuebeam)

**GitHub Issues** è la **fonte di verità** per bug, task e evolutive del progetto.

I file markdown locali (piani, note, post-mortem) restano **riferimento e archivio**. Lo stato operativo (aperto / in corso / chiuso) vive su GitHub.

---

## Configurazione repository

Lo script risolve `owner/repo` in questo ordine:

| Priorità | Sorgente |
|----------|----------|
| 1 | Variabile `GITHUB_REPO` nella sessione |
| 2 | File `.env` → `GITHUB_REPO=owner/repo` |
| 3 | File `tracker/github_repo` — una riga (creato da `adopt.py`) |

Override una tantum: `python scripts/github_issue.py --repo owner/repo list`

---

## Token GitHub

Lo script legge il token **automaticamente** (l'agente Cursor non deve chiedere comandi manuali):

| Priorità | Sorgente |
|----------|----------|
| 1 | Variabile `GITHUB_TOKEN` nella sessione corrente |
| 2 | **Variabili utente Windows** (funziona anche nel terminale Cursor) |
| 3 | File `.env` nella root: `GITHUB_TOKEN=github_pat_...` |
| 4 | File `.secrets/github_token` — una riga, gitignored |

**Setup consigliato:** token in Variabili utente Windows.

**Alternativa file:**

```cmd
mkdir .secrets 2>nul
copy tracker\github_token.example .secrets\github_token
notepad .secrets\github_token
```

Incolla il token su una riga, salva. **Mai** committare quel file.

---

## Uso con Cursor chat

Quando segnali un bug o chiedi un task, l'agente può creare o aggiornare issue GitHub:

- *«Apri issue per il bug del form login»*
- *«Crea task GitHub per dark mode»*
- *«Commenta issue #42 con il fix applicato»*

L'agente esegue `python scripts/github_issue.py ...` (vedi regola `.cursor/rules/github-issues.mdc`).

Guida completa: [docs/GUIDA.md](../docs/GUIDA.md) · Sito: [issuebeam.github.io](https://issuebeam.github.io)

---

## Comandi

### Label (prima import o setup repo)

```cmd
python scripts/github_issue.py labels
python scripts/github_issue.py labels --apply
```

### Import issue da manifest

Copia l'esempio se serve:

```cmd
copy tracker\import-manifest.example.json tracker\import-manifest.json
python scripts/github_issue.py import --dry-run
python scripts/github_issue.py import --apply
```

Salta duplicati se trova lo stesso **Legacy ID** nel body.

### Creare issue manualmente

```cmd
python scripts/github_issue.py create "Titolo breve" --body "Descrizione markdown" --labels bug,priority-high,area-frontend
```

### Elencare issue

```cmd
python scripts/github_issue.py list
python scripts/github_issue.py list --state closed --limit 50
```

### Commento e chiusura

```cmd
python scripts/github_issue.py comment 12 --body "Fix in PR #99"
python scripts/github_issue.py close 12
python scripts/github_issue.py close-batch 10 11 12 --reason "Duplicati"
```

---

## Struttura cartella

| File | Ruolo |
|------|--------|
| `labels.yml` | Definizione label GitHub |
| `import-manifest.example.json` | Esempio batch import |
| `import-manifest.json` | Manifest reale (gitignored, copia da example) |
| `github_repo` | Slug repo (gitignored, creato da adopt) |
| `github_repo.example` | Template slug |
| `github_token.example` | Template token (non usare in produzione) |

---

## Commit e PR

Nei commit e nelle PR che risolvono lavoro tracciato, referenzia l'issue:

```
fix(auth): handle Safari redirect loop

Fixes #NN
```
