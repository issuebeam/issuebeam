# Token GitHub

Serve un **Personal Access Token** con permesso di leggere e scrivere le issue del repository target.

Issuebeam funziona su **Windows, macOS e Linux** — cambia solo il modo in cui esporti `GITHUB_TOKEN`. La CLI è identica ovunque: `python scripts/github_issue.py`.

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

| Metodo | Funziona su | Pro | Contro |
|--------|-------------|-----|--------|
| **Variabile `GITHUB_TOKEN`** | Win · Mac · Linux | Terminale e agenti AI | Riavvia IDE/shell dopo la modifica |
| **`.secrets/github_token`** | Tutti | Gitignored, semplice, portabile | File locale — mai committare |
| **`.env`** | Tutti | Comodo in dev | Rischio commit accidentale (gitignored) |

**Mai** incollare il token in chat con l'agente, issue pubbliche o commit.

## Imposta `GITHUB_TOKEN` (consigliato)

=== "Windows"

1. Apri **Variabili d'ambiente** → **Variabili utente** → **Nuova…**
2. Nome: `GITHUB_TOKEN` — Valore: `github_pat_...`
3. OK su tutte le finestre
4. **Riavvia l'IDE** (Cursor, VS Code, …) o apri un nuovo terminale

**Extra:** se il terminale dell'IDE non vede ancora la variabile, issuebeam legge anche il **registry utente Windows** (stesso valore) — nessun setup aggiuntivo.

=== "macOS"

**Terminale / agenti CLI** — aggiungi a `~/.zshrc` o `~/.bashrc`:

```bash
export GITHUB_TOKEN=github_pat_...
```

Poi `source ~/.zshrc` (o nuovo terminale).

**App GUI (Cursor, VS Code dal Dock)** — le variabili della shell non sempre arrivano alle app avviate dal launcher. Opzioni:

- Avvia l'IDE dal terminale: `cursor .` o `code .`
- Oppure usa `.env` / `.secrets/github_token` nel progetto (sotto)

=== "Linux"

**Shell** — aggiungi a `~/.bashrc`, `~/.zshrc`, o usa [direnv](https://direnv.net/) nel repo:

```bash
export GITHUB_TOKEN=github_pat_...
```

**Sessione utente systemd** (opzionale, per tool GUI):

```ini
# ~/.config/environment.d/github.conf
GITHUB_TOKEN=github_pat_...
```

Logout e login. In alternativa `.env` o `.secrets/github_token`.

## Alternativa: `.env` o `.secrets/` (tutti i SO)

**`.env`** nella root del repo (gitignored):

```
GITHUB_REPO=myorg/my-app
GITHUB_TOKEN=github_pat_...
```

**`.secrets/github_token`** — una riga, gitignored:

```bash
mkdir -p .secrets
printf '%s\n' 'github_pat_...' > .secrets/github_token
chmod 600 .secrets/github_token   # macOS / Linux
```

## Verifica

```bash
python -c "import os; print('OK' if os.environ.get('GITHUB_TOKEN') else 'MANCANTE')"
```

Poi (dopo lo [slug repository](repository.md)):

```bash
python scripts/github_issue.py list
```

## Ordine di lettura token (CLI)

Lo script legge il token automaticamente:

1. `.env` nella root del repo (`GITHUB_TOKEN=...`)
2. `GITHUB_TOKEN` nell'ambiente del processo corrente
3. `.secrets/github_token`
4. **Solo Windows:** variabile utente da registry (fallback se la shell IDE non eredita le variabili)

**Perché `.env` prima:** su Windows gli IDE spesso ereditano un `GITHUB_TOKEN` obsoleto dalle variabili utente. Il token del progetto in `.env` deve avere priorità.

## Opzionale: `GITHUB_REPO` nell'ambiente

Stessi metodi di `GITHUB_TOKEN` — utile se lavori sempre sullo stesso repo:

```bash
export GITHUB_REPO=myorg/my-app
```
