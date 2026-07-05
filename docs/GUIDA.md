# Guida issuebeam

Guida completa per colleghi che sviluppano con **Cursor** e **vibe coding** e vogliono tracciare bug e task su **GitHub Issues** senza perdere il filo in chat.

---

## 1. Cos'è e perché

### Il problema

Con LLM e iterazione rapida succede spesso:

- Un bug viene discusso in chat e poi **dimenticato**
- Un task viene «fatto mentalmente» ma **non compare** nel backlog del team
- Si aprono file markdown ovunque (`TODO.md`, `bugs.txt`, note in cartelle random)
- Nessuno sa cosa è **aperto**, **in corso** o **chiuso**

### La soluzione

**issuebeam** collega la chat Cursor a **GitHub Issues** con:

1. **`scripts/github_issue.py`** — CLI Python (solo stdlib) per creare, commentare, chiudere issue
2. **Regola Cursor** (`.cursor/rules/github-issues.mdc`) — l'agente **esegue lo script da solo**, non chiede a te di incollare comandi
3. **Template GitHub** — form web per chi apre issue dal browser
4. **`adopt.py`** — copia tutto in un progetto esistente in un minuto

GitHub Issues diventa la **fonte di verità**. I markdown locali restano per piani dettagliati e archivio, non per lo stato operativo.

---

## 2. Token GitHub

Serve un **Personal Access Token** con permesso di leggere e scrivere le issue del repository.

### Classic token (semplice)

1. GitHub → **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**
2. **Generate new token (classic)**
3. Scope minimo: **`repo`** (oppure solo **Issues** se usi fine-grained sul singolo repo)
4. Copia il token — lo vedi **una sola volta**

### Fine-grained token (consigliato per team)

1. **Personal access tokens** → **Fine-grained tokens** → **Generate new token**
2. **Repository access:** solo il repo del progetto (es. `myorg/my-app`)
3. **Permissions → Issues:** Read and write
4. Nessun altro permesso necessario per questo tool

### Dove mettere il token

| Metodo | Pro | Contro |
|--------|-----|--------|
| **Variabile utente Windows `GITHUB_TOKEN`** | Funziona in Cursor, terminale, agent | Va impostata una volta per macchina |
| **File `.secrets/github_token`** | Gitignored, facile per chi non usa env | File locale da non committare |
| **File `.env`** | Comodo in dev | Rischio commit accidentale (è in `.gitignore`) |

**Mai** incollare il token in chat Cursor, in issue pubbliche o in commit.

---

## 3. Setup variabili utente Windows

Metodo consigliato per chi lavora su Windows con Cursor.

### Interfaccia grafica

1. Cerca **「Modifica variabili d'ambiente relative al sistema」** o **「Variabili d'ambiente」**
2. Nella sezione **Variabili utente** → **Nuova…**
3. Nome: `GITHUB_TOKEN` — Valore: `github_pat_...` (il token)
4. OK su tutte le finestre
5. **Riavvia Cursor** (o almeno il terminale integrato) per caricare la variabile

### Verifica da terminale

```cmd
python -c "import os; t=os.environ.get('GITHUB_TOKEN',''); print('OK' if t else 'MANCANTE', len(t))"
```

Se stampa `MANCANTE` ma hai impostato la variabile utente, lo script legge anche dal **registry Windows** — prova:

```cmd
python scripts/github_issue.py list
```

(dopo aver configurato il repo, vedi §4)

### Opzionale: anche `GITHUB_REPO` in variabili utente

Utile se lavori sempre sullo stesso repo:

- Nome: `GITHUB_REPO`
- Valore: `myorg/my-app`

---

## 4. Configurare il repository

Lo script deve sapere **quale repo** GitHub usare (`owner/nome`).

**Opzione A — file locale (consigliata dopo adopt):**

```cmd
echo myorg/my-app> tracker\github_repo
```

**Opzione B — `.env`:**

```
GITHUB_REPO=myorg/my-app
GITHUB_TOKEN=github_pat_...
```

**Opzione C — override una tantum:**

```cmd
python scripts/github_issue.py --repo myorg/my-app list
```

---

## 5. Adottare in un progetto esistente

Dalla cartella **issuebeam** (o dopo aver clonato questo repo):

```cmd
python scripts/adopt.py --target ..\my-repo --repo myorg/my-app
```

Cosa fa `adopt.py`:

| Azione | Dettaglio |
|--------|-----------|
| Copia | `scripts/github_issue.py`, `tracker/*`, `.github/ISSUE_TEMPLATE/*`, `.cursor/rules/github-issues.mdc` |
| Crea | `tracker/github_repo` con lo slug indicato |
| Crea | `tracker/import-manifest.json` dall'esempio (se mancante) |
| Crea | `.secrets/.gitkeep` |

Con `--force` sovrascrive file già presenti.

Poi nel progetto adottato:

```cmd
cd ..\my-repo
python scripts/github_issue.py labels --apply
python scripts/github_issue.py list
```

Apri la cartella in **Cursor** — la regola `github-issues.mdc` è già attiva (`alwaysApply: true`).

---

## 6. Comandi CLI

Tutti i comandi si eseguono dalla **root del progetto** (dove c'è `scripts/`).

### Label

Definite in `tracker/labels.yml`. Prima volta sul repo:

```cmd
python scripts/github_issue.py labels
python scripts/github_issue.py labels --apply
```

### Elenco issue

```cmd
python scripts/github_issue.py list
python scripts/github_issue.py list --state closed --limit 50
```

### Creare issue

```cmd
python scripts/github_issue.py create "Titolo breve" --body "Descrizione in **markdown**" --labels bug,priority-high,area-frontend
```

Body da file:

```cmd
python scripts/github_issue.py create "Bug Safari" --body-file descrizione.md --labels bug
```

### Commento

```cmd
python scripts/github_issue.py comment 42 --body "Fix applicato in commit abc123"
```

### Chiusura

```cmd
python scripts/github_issue.py close 42
python scripts/github_issue.py close 42 --reason "Duplicato di #40"
python scripts/github_issue.py close-batch 10 11 12 --reason "Backlog non prioritario"
```

### Import batch (migrazione da tracker locale)

```cmd
copy tracker\import-manifest.example.json tracker\import-manifest.json
REM modifica import-manifest.json con le tue issue
python scripts/github_issue.py import --dry-run
python scripts/github_issue.py import --apply
```

Nel body di ogni voce importata, usa **`Legacy ID:`** per evitare duplicati al re-import:

```markdown
**Legacy ID:** `BUG-001`
```

---

## 7. Frasi da usare in Cursor chat

L'agente con la regola attiva capisce queste richieste (italiano o inglese):

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

Non serve ricordare la sintassi CLI — descrivi il lavoro in linguaggio naturale.

---

## 8. Convenzioni label

| Label | Quando usarla |
|-------|----------------|
| `bug` | Comportamento errato, regressione |
| `enhancement` | Nuova funzionalità, miglioramento UX |
| `task` | Lavoro pianificato con DoD |
| `documentation` | Solo documentazione |
| `priority-high` | Blocca release o flusso critico |
| `priority-medium` | Importante ma non bloccante |
| `priority-low` | Nice-to-have, backlog |
| `area-frontend` | UI, client, browser |
| `area-backend` | API, servizi, database |
| `area-infra` | CI, Docker, deploy, monitoring |
| `area-docs` | README, guide, sito |
| `imported` | Migrato da tracker precedente |

Personalizza `tracker/labels.yml` e riesegui `labels --apply`.

---

## 9. Sicurezza

### Da fare

- Token solo in variabili utente, `.env` (gitignored) o `.secrets/github_token`
- `.gitignore` include `.secrets/` e `.env`
- Fine-grained token limitato al singolo repository
- Ruotare il token se esposto accidentalmente

### Da non fare

- **Mai** incollare il token in chat Cursor o in issue GitHub
- **Mai** committare `tracker/github_repo` con dati sensibili (contiene solo lo slug, ma è gitignored per flessibilità locale)
- **Mai** condividere screenshot con token visibile
- **Mai** usare script PowerShell in questo stack (antivirus / policy team) — solo Python

### SSL su Windows

Se vedi errori certificato SSL verso `api.github.com`:

```cmd
pip install -r requirements-optional.txt
```

Installa `truststore` che usa il trust store di Windows.

---

## 10. Commit e pull request

Quando una PR risolve un'issue, nel messaggio di commit:

```
fix(auth): handle Safari redirect after login

Fixes #42
```

GitHub chiude automaticamente l'issue al merge (se il repo ha l'opzione attiva).

Varianti: `Closes #42`, `Refs #42` (riferimento senza chiusura automatica).

---

## 11. Struttura file

```
progetto/
├── scripts/
│   ├── github_issue.py      # CLI principale
│   └── adopt.py             # Copia skeleton (solo in repo issuebeam)
├── tracker/
│   ├── labels.yml
│   ├── github_repo          # slug (locale, gitignored)
│   ├── import-manifest.json # batch import (gitignored)
│   └── README.md
├── .github/ISSUE_TEMPLATE/  # Form web GitHub
├── .cursor/rules/
│   └── github-issues.mdc    # Istruzioni agente
├── .secrets/
│   └── github_token         # opzionale, gitignored
└── docs/
    └── GUIDA.md             # questo file
```

---

## 12. Troubleshooting

| Sintomo | Soluzione |
|---------|-----------|
| `ERRORE: token GitHub non trovato` | Imposta `GITHUB_TOKEN` (§2–3) o crea `.secrets/github_token` |
| `ERRORE: repository GitHub non configurato` | Crea `tracker/github_repo` o `GITHUB_REPO` in `.env` |
| HTTP 401 | Token scaduto o revocato — generane uno nuovo |
| HTTP 404 | Slug repo errato o token senza accesso al repo |
| HTTP 403 | Permessi insufficienti — Issues read/write |
| SSL certificate error | `pip install truststore` (requirements-optional.txt) |
| L'agente non esegue lo script | Verifica che `.cursor/rules/github-issues.mdc` esista e `alwaysApply: true` |

---

## 13. Origine

Questo skeleton è un **estratto generalizzato** del sistema di tracking usato nel progetto **[Qwibo](https://github.com/qwibo/qwibo)** (trascrizione audio + riassunto LLM).

Da Qwibo sono stati rimossi:

- Label e template specifici del prodotto (ASR, Electron, Docker Qwibo)
- Path `data/.secrets/` → sostituito con `.secrets/`
- Variabile `QWIBO_GITHUB_REPO` → `GITHUB_REPO` + file `tracker/github_repo`

Mantenuti:

- CLI stdlib senza dipendenza da `gh`
- Lettura token da registry Windows (ideale per Cursor agent)
- Import manifest con Legacy ID anti-duplicati
- Regola agente «esegui lo script, non delegare all'utente»

---

## 14. Licenza

MIT — Copyright (c) 2026 Antonio Trento. Vedi [LICENSE](../LICENSE).

Per domande sul setup in team, apri una issue su [issuebeam](https://github.com/issuebeam/issuebeam) o contatta chi ha introdotto il tool nel progetto.
