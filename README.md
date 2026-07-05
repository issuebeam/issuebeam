# issuebeam

**GitHub Issues from AI agent chat — for vibe coders.**

Works with **Cursor, Claude Code, GitHub Copilot, Windsurf, Cline, Gemini CLI, Codex CLI**, and any agent that can read repo instructions and run shell commands.

---

## IT — Perché esiste

Stai sviluppando con **vibe coding** (LLM, iterazione rapida) e perdi il filo di bug, task e idee sparse in chat? **issuebeam** collega **qualsiasi agente AI** all'**issue tracker ufficiale su GitHub**: l'agente crea e aggiorna issue con un comando Python, senza `gh` CLI e senza script PowerShell.

- CLI stdlib (`urllib`) + token da env / Windows / `.env` / `.secrets/`
- **Regole agente multi-piattaforma** — Cursor, Claude Code, Copilot, e altro via `AGENTS.md`
- Template issue GitHub generici (bug, evolutiva, task)
- `adopt.py` per copiare tutto in un progetto esistente in un colpo solo

**Guide:** [issuebeam.github.io/docs/it](https://issuebeam.github.io/docs/it/) (MkDocs IT/EN) · **Sito:** [issuebeam.github.io](https://issuebeam.github.io)

---

## EN — Why it exists

You ship with **vibe coding** (LLMs, fast iteration) and lose track of bugs and tasks buried in chat? **issuebeam** wires **any AI agent** to **GitHub Issues**: the agent creates and updates issues via a Python CLI — no `gh` CLI, no PowerShell scripts.

- Stdlib CLI + token from env / Windows user vars / `.env` / `.secrets/`
- **Multi-platform agent rules** — Cursor, Claude Code, Copilot, and more via `AGENTS.md`
- Generic GitHub issue templates
- `adopt.py` to copy the skeleton into any repo

**Guides:** [issuebeam.github.io/docs](https://issuebeam.github.io/docs/) (MkDocs IT/EN) · **Marketing site:** [issuebeam.github.io](https://issuebeam.github.io)

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

### 5. Wire your AI agent

| Platform | Instruction file |
|----------|------------------|
| Cursor | `.cursor/rules/github-issues.mdc` |
| Claude Code | `CLAUDE.md` + `AGENTS.md` |
| GitHub Copilot | `.github/copilot-instructions.md` + `AGENTS.md` |
| Other | See [docs](https://issuebeam.github.io/docs/platforms/overview/) |

### 6. Optional: Windows SSL (corporate proxy / antivirus)

```cmd
pip install -r requirements-optional.txt
```

### 7. Documentation (MkDocs IT/EN)

```cmd
pip install -r docs/requirements.txt
mkdocs serve
```

Publish to [issuebeam.github.io/docs](https://issuebeam.github.io/docs/): `scripts\publish_docs.bat`

---

## Structure

| Path | Role |
|------|------|
| `scripts/github_issue.py` | CLI: list, create, comment, close, labels, import |
| `scripts/adopt.py` | Copy skeleton into another repo |
| `tracker/` | Labels, manifest, repo slug config |
| `.github/ISSUE_TEMPLATE/` | GitHub web forms |
| `AGENTS.md` | Universal agent instructions |
| `CLAUDE.md` | Claude Code pointer |
| `.cursor/rules/github-issues.mdc` | Cursor rule (`alwaysApply`) |
| `.github/copilot-instructions.md` | GitHub Copilot workspace instructions |
| `docs/en/`, `docs/it/` | MkDocs sources (published to issuebeam.github.io/docs/) |
| `mkdocs.yml` | MkDocs + i18n config |

---

## Origin

Extracted and generalized from the [Qwibo](https://github.com/qwibo/qwibo) project tracker. MIT licensed — Antonio Trento, 2026.

Repository: [github.com/issuebeam/issuebeam](https://github.com/issuebeam/issuebeam)
