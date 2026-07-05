# Issuebeam

**[← Main website (issuebeam.github.io)](https://issuebeam.github.io/en/)** · Documentation

**Issuebeam** wires **AI coding agents** to **GitHub Issues** with a stdlib Python CLI and repository instruction files. Works on **Windows, macOS, and Linux** with Cursor, Claude Code, GitHub Copilot, and more.

!!! info "Bilingual documentation"
    This site is also available in **Italiano**. Use the language selector in the top navigation bar.

## What it does

| Layer | Description |
|-------|-------------|
| **CLI** | `scripts/github_issue.py` — create, list, comment, close, import issues |
| **Agent rules** | `AGENTS.md`, Cursor rule, Copilot instructions, `CLAUDE.md`, … |
| **GitHub** | Official backlog with labels, web templates, `Fixes #N` in PRs |

## Who this is for

You ship with **vibe coding** (LLMs, fast iteration) and lose track of bugs and tasks buried in chat. Issuebeam moves operational status to GitHub Issues — not scattered markdown files.

**Not Cursor-only.** The same CLI runs everywhere; only the instruction file path changes per IDE.

## Quick start

```bash
python -c "from pathlib import Path; Path('tracker/github_repo').write_text('myorg/my-app\n')"
python scripts/github_issue.py labels --apply
python scripts/github_issue.py create "Setup test" --labels task
python scripts/github_issue.py list
```

Details: [Overview](getting-started/overview.md) · [Token](getting-started/token.md) · [Platforms](platforms/overview.md)

## Adopt into your repo

```bash
python scripts/adopt.py --target ../my-repo --repo myorg/my-app
```

Copies CLI, labels, templates, and agent instruction files for multiple platforms.

## Documentation map

| Section | Content |
|---------|---------|
| [Getting started](getting-started/overview.md) | Problem, architecture, setup |
| [Platforms](platforms/overview.md) | Cursor, Claude Code, Copilot, others |
| [CLI reference](cli/commands.md) | All commands |
| [Agent workflow](agent/natural-language.md) | Natural language phrases |
| [Reference](reference/faq.md) | FAQ, security, troubleshooting |

## Build docs locally

```bash
pip install -r docs/requirements.txt
mkdocs serve
```

Preview at http://127.0.0.1:8000 — publish with `python scripts/publish_docs.py`, then `git push` in sibling repo `issuebeam.github.io`. **No GitHub Actions.**

## License

MIT — Copyright © 2026 [Antonio Trento](https://antoniotrento.net). See [LICENSE](https://github.com/issuebeam/issuebeam/blob/main/LICENSE).
