# Token GitHub

Serve un **Personal Access Token** con permesso di leggere e scrivere le issue del repository target.

## Classic token

1. GitHub → **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**
2. **Generate new token (classic)**
3. Scope minimo: **`repo`** (oppure solo Issues con fine-grained sul singolo repo)
4. Copia il token — lo vedi **una sola volta**

## Fine-grained token (consigliato per team)

1. **Personal access tokens** → **Fine-grained tokens** → **Generate new token**
2. **Repository access:** solo il repo del progetto (es. `myorg/my-app`)
3. **Permissions → Issues:** Read and write
4. Nessun altro permesso necessario

## Dove mettere il token

| Metodo | Pro | Contro |
|--------|-----|--------|
| **Variabile utente Windows `GITHUB_TOKEN`** | Funziona in IDE, terminale, agent | Va impostata una volta per macchina |
| **File `.secrets/github_token`** | Gitignored, facile | File locale — mai committare |
| **File `.env`** | Comodo in dev | Rischio commit accidentale (gitignored) |

**Mai** incollare il token in chat con l'agente, issue pubbliche o commit.

## Variabile utente Windows (consigliata)

1. Apri **Variabili d'ambiente** (sezione utente)
2. **Nuova…** → Nome: `GITHUB_TOKEN` — Valore: `github_pat_...`
3. OK su tutte le finestre
4. **Riavvia l'IDE** (Cursor, VS Code, …) o il terminale integrato

### Verifica

```cmd
python -c "import os; t=os.environ.get('GITHUB_TOKEN',''); print('OK' if t else 'MANCANTE', len(t))"
```

Se `MANCANTE` ma hai impostato la variabile utente, lo script legge anche il **registry Windows** — prova:

```cmd
python scripts/github_issue.py list
```

(dopo aver configurato lo slug)

### Opzionale: `GITHUB_REPO` in variabili utente

Utile se lavori sempre sullo stesso repo:

- Nome: `GITHUB_REPO`
- Valore: `myorg/my-app`
