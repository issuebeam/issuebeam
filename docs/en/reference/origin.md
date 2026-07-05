# Origin

Issuebeam is a **generalized extract** of the tracking system used in the [Qwibo](https://github.com/qwibo/qwibo) project (audio transcription + LLM summarization).

## Removed from Qwibo context

- Product-specific labels and templates (ASR, Electron, Docker)
- Path `data/.secrets/` → replaced with `.secrets/`
- Variable `QWIBO_GITHUB_REPO` → `GITHUB_REPO` + `tracker/github_repo`

## Kept

- Stdlib CLI without `gh` dependency — **Windows, macOS, Linux**
- Token from env, `.env`, `.secrets/`, and on Windows optional registry read for IDE agents
- Multi-platform instructions (`AGENTS.md` + Cursor/Copilot/Claude rules)
- Import manifest with Legacy ID anti-duplicates
- Agent rule: *run the script, don't delegate to the user*

## Name

*Issuebeam* evokes a beam connecting chat to the tracker — a direct bridge between conversation and the official backlog.

MIT — Copyright © 2026 [Antonio Trento](https://antoniotrento.net).
