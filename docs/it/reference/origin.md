# Origine

Issuebeam è un **estratto generalizzato** del sistema di tracking usato nel progetto [Qwibo](https://github.com/qwibo/qwibo) (trascrizione audio + riassunto LLM).

## Rimosso dal contesto Qwibo

- Label e template specifici del prodotto (ASR, Electron, Docker)
- Path `data/.secrets/` → sostituito con `.secrets/`
- Variabile `QWIBO_GITHUB_REPO` → `GITHUB_REPO` + `tracker/github_repo`

## Mantenuto

- CLI stdlib senza dipendenza da `gh`
- Lettura token da registry Windows (ideale per agenti in IDE)
- Istruzioni multi-piattaforma (`AGENTS.md` + regole Cursor/Copilot/Claude)
- Import manifest con Legacy ID anti-duplicati
- Regola agente: *esegui lo script, non delegare all'utente*

## Nome

*Issuebeam* evoca un raggio che collega la chat al tracker — un ponte diretto tra conversazione e backlog ufficiale.

MIT — Copyright © 2026 [Antonio Trento](https://antoniotrento.net).
