# Claude Code

Claude Code (estensione VS Code, CLI o desktop) legge **`CLAUDE.md`** e **`AGENTS.md`** dalla root del repository.

## Setup

1. Esegui [adopt](../getting-started/adopt.md) — copia `CLAUDE.md` e `AGENTS.md`.
2. Apri la **root del repository** in VS Code (non una cartella padre).
3. Installa l'estensione Claude Code o usa la CLI.
4. Imposta `GITHUB_TOKEN` ([guida token](../getting-started/token.md)).

## Verifica

Chiedi: *«Crea un'issue GitHub [Bug] Test da Claude»* — Claude deve eseguire lo script Python.

## Suggerimenti VS Code

- I comandi shell nel terminale integrato ereditano le variabili utente dopo il riavvio dell'IDE.
- Se Claude chiede comandi manuali, rimanda a **AGENTS.md**.

## Memoria progetto (opzionale)

Aggiungi nelle impostazioni progetto Claude:

> Per bug e task, usa `python scripts/github_issue.py` secondo AGENTS.md. GitHub Issues è la fonte di verità.

## Troubleshooting

| Problema | Soluzione |
|----------|-----------|
| Directory sbagliata | Apri la root dove c'è `scripts/` |
| L'agente non esegue lo script | Verifica che `AGENTS.md` sia nel contesto |
| Token mancante | Riavvia VS Code dopo la variabile d'ambiente |
