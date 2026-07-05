# issuebeam

**GitHub Issues from Cursor/LLM chat — for vibe coders.**

---

## IT — Perché esiste

Stai sviluppando con **vibe coding** (Cursor, LLM, iterazione rapida) e perdi il filo di bug, task e idee sparse in chat? **issuebeam** è uno skeleton leggero che collega la chat all'**issue tracker ufficiale su GitHub**: l'agente crea e aggiorna issue con un comando Python, senza `gh` CLI e senza script PowerShell.

- CLI stdlib (`urllib`) + token da env / Windows / `.env` / `.secrets/`
- Regola Cursor (`alwaysApply`) che obbliga l'agente a usare lo script
- Template issue GitHub generici (bug, evolutiva, task)
- `adopt.py` per copiare tutto in un progetto esistente in un colpo solo

**Guida completa per il team:** [docs/GUIDA.md](docs/GUIDA.md) · **Sito:** [issuebeam.github.io](https://issuebeam.github.io)

---

## EN — Why it exists

You ship with **vibe coding** (Cursor, LLMs, fast iteration) and lose track of bugs and tasks buried in chat? **issuebeam** is a minimal skeleton that wires chat to **GitHub Issues**: the agent creates and updates issues via a Python CLI — no `gh` CLI, no PowerShell scripts.

- Stdlib CLI + token from env / Windows user vars / `.env` / `.secrets/`
- Cursor rule (`alwaysApply`) so the agent runs the script directly
- Generic GitHub issue templates
- `adopt.py` to copy the skeleton into any repo

**Full team guide (Italian):** [docs/GUIDA.md](docs/GUIDA.md) · **Site:** [issuebeam.github.io](https://issuebeam.github.io)

---

## Quick start

### 1. Token GitHub

Create a Personal Access Token with **Issues: read & write** on your repo.  
Store it as Windows user env var `GITHUB_TOKEN`, or in `.secrets/github_token` (one line, gitignored).

### 2. Repository slug

```cmd
echo myorg/my-app> tracker\github_repo
```

Or in `.env`:

```
GITHUB_REPO=myorg/my-app
GITHUB_TOKEN=github_pat_...
```

### 3. Labels + first issue

```cmd
python scripts/github_issue.py labels --apply
python scripts/github_issue.py create "Test issue from vibe tracker" --labels task
python scripts/github_issue.py list
```

### 4. Adopt into another project

```cmd
python scripts/adopt.py --target ..\my-repo --repo myorg/my-app
```

### 5. Optional: Windows SSL (corporate proxy / antivirus)

```cmd
pip install -r requirements-optional.txt
```

---

## Structure

| Path | Role |
|------|------|
| `scripts/github_issue.py` | CLI: list, create, comment, close, labels, import |
| `scripts/adopt.py` | Copy skeleton into another repo |
| `tracker/` | Labels, manifest, repo slug config |
| `.github/ISSUE_TEMPLATE/` | GitHub web forms |
| `.cursor/rules/github-issues.mdc` | Agent instructions |
| `docs/GUIDA.md` | Full Italian guide |

---

## Origin

Extracted and generalized from the [Qwibo](https://github.com/qwibo/qwibo) project tracker. MIT licensed — Antonio Trento, 2026.

Repository: [github.com/issuebeam/issuebeam](https://github.com/issuebeam/issuebeam)
