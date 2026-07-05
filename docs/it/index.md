# Issuebeam

**[← Sito web (issuebeam.github.io)](https://issuebeam.github.io/it/)** · Documentazione

**Issuebeam** collega **agenti AI di coding** a **GitHub Issues** con una CLI Python stdlib e file di istruzioni nel repository. Funziona su **Windows, macOS e Linux** con Cursor, Claude Code, Copilot e altro.

!!! info "Documentazione bilingue"
    Questa documentazione è disponibile anche in **inglese**. Usa il selettore lingua in alto.

## Cosa fa

| Livello | Descrizione |
|---------|-------------|
| **CLI** | `scripts/github_issue.py` — crea, elenca, commenta, chiude, importa issue |
| **Regole agente** | `AGENTS.md`, regola Cursor, istruzioni Copilot, `CLAUDE.md`, … |
| **GitHub** | Backlog ufficiale con label, template web, `Fixes #N` nelle PR |

## A chi serve

Sviluppi con **vibe coding** (LLM, iterazione rapida) e perdi bug e task sepolti in chat. Issuebeam sposta lo stato operativo su GitHub Issues — non su markdown sparsi.

**Non solo Cursor.** La stessa CLI funziona ovunque; cambia solo il percorso del file istruzioni per IDE.

## Avvio rapido

```bash
python -c "from pathlib import Path; Path('tracker/github_repo').write_text('myorg/my-app\n')"
python scripts/github_issue.py labels --apply
python scripts/github_issue.py create "Test setup" --labels task
python scripts/github_issue.py list
```

Dettagli: [Panoramica](getting-started/overview.md) · [Token](getting-started/token.md) · [Piattaforme](platforms/overview.md)

## Adotta nel tuo repo

```bash
python scripts/adopt.py --target ../my-repo --repo myorg/my-app
```

Copia CLI, label, template e file istruzioni per più piattaforme.

## Mappa documentazione

| Sezione | Contenuto |
|---------|-----------|
| [Per iniziare](getting-started/overview.md) | Problema, architettura, setup |
| [Piattaforme](platforms/overview.md) | Cursor, Claude Code, Copilot, altro |
| [Riferimento CLI](cli/commands.md) | Tutti i comandi |
| [Flusso agente](agent/natural-language.md) | Frasi in linguaggio naturale |
| [Riferimento](reference/faq.md) | FAQ, sicurezza, troubleshooting |

## Anteprima e pubblicazione docs

```bash
pip install -r docs/requirements.txt
mkdocs serve
```

Anteprima su http://127.0.0.1:8000 — pubblicazione: `python scripts/publish_docs.py`, poi `git push` nel repo gemello `issuebeam.github.io`. **Nessuna GitHub Action.**

## Licenza

MIT — Copyright © 2026 [Antonio Trento](https://antoniotrento.net). Vedi [LICENSE](https://github.com/issuebeam/issuebeam/blob/main/LICENSE).
