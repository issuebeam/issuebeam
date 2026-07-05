# issuebeam

**GitHub Issues from AI agent chat — for vibe coders.**

Works on **Windows, macOS, and Linux** with **Cursor, Claude Code, GitHub Copilot, Windsurf, Cline, Gemini CLI, Codex CLI**, and any agent that can read repo instructions and run shell commands.

---

## IT — Perché esiste

Stai sviluppando con **vibe coding** (LLM, iterazione rapida) e perdi il filo di bug, task e idee sparse in chat? **issuebeam** collega **qualsiasi agente AI** all'**issue tracker ufficiale su GitHub**: l'agente crea e aggiorna issue con un comando Python, senza `gh` CLI e senza script PowerShell.

- CLI stdlib (`urllib`) — **Windows, macOS, Linux**
- Token da env, `.env`, `.secrets/` (su Windows anche lettura opzionale da registry)
- **Regole agente multi-piattaforma** — Cursor, Claude Code, Copilot, e altro via `AGENTS.md`
- Template issue GitHub generici (bug, evolutiva, task)
- `adopt.py` per copiare tutto in un progetto esistente in un colpo solo

**Guide:** [issuebeam.github.io/docs/it](https://issuebeam.github.io/docs/it/) (MkDocs IT/EN) · **Sito:** [issuebeam.github.io](https://issuebeam.github.io)

---

## EN — Why it exists

You ship with **vibe coding** (LLMs, fast iteration) and lose track of bugs and tasks buried in chat? **issuebeam** wires **any AI agent** to **GitHub Issues**: the agent creates and updates issues via a Python CLI — no `gh` CLI, no PowerShell scripts.

- Stdlib CLI — **Windows, macOS, Linux**
- Token from env, `.env`, `.secrets/` (on Windows, optional registry read for IDE terminals)
- **Multi-platform agent rules** — Cursor, Claude Code, Copilot, and more via `AGENTS.md`
- Generic GitHub issue templates
- `adopt.py` to copy the skeleton into any repo

**Guides:** [issuebeam.github.io/docs](https://issuebeam.github.io/docs/) (MkDocs IT/EN) · **Marketing site:** [issuebeam.github.io](https://issuebeam.github.io)

---

## Quick start

### 1. GitHub token

Create a Personal Access Token with **Issues: read & write** on your repo.

Set `GITHUB_TOKEN` in your environment (see [token guide](https://issuebeam.github.io/docs/getting-started/token/) for Windows, macOS, and Linux), or use `.secrets/github_token` (one line, gitignored).

### 2. Repository slug

```bash
python -c "from pathlib import Path; Path('tracker/github_repo').write_text('myorg/my-app\n')"
```

Or in `.env`:

```
GITHUB_REPO=myorg/my-app
GITHUB_TOKEN=github_pat_...
```

### 3. Labels + first issue

```bash
python scripts/github_issue.py labels --apply
python scripts/github_issue.py create "Test issue from vibe tracker" --labels task
python scripts/github_issue.py list
```

### 4. Adopt into another project

```bash
python scripts/adopt.py --target ../my-repo --repo myorg/my-app
```

### 5. Wire your AI agent

| Platform | Instruction file |
|----------|------------------|
| Cursor | `.cursor/rules/github-issues.mdc` |
| Claude Code | `CLAUDE.md` + `AGENTS.md` |
| GitHub Copilot | `.github/copilot-instructions.md` + `AGENTS.md` |
| Other | See [docs](https://issuebeam.github.io/docs/platforms/overview/) |

### 6. Optional: SSL / corporate proxy

If you see certificate errors toward `api.github.com` (common on Windows with corporate AV):

```bash
pip install -r requirements-optional.txt
```

### 7. Documentation (MkDocs IT/EN)

```bash
pip install -r docs/requirements.txt
mkdocs serve
```

Publish to [issuebeam.github.io/docs](https://issuebeam.github.io/docs/): `python scripts/publish_docs.py`

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
