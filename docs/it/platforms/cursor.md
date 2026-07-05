# Cursor

Percorso **più testato**. Issuebeam include:

```
.cursor/rules/github-issues.mdc   # alwaysApply: true
```

## Setup

1. Clona issuebeam o esegui `adopt.py` nel tuo repo.
2. Configura [token](../getting-started/token.md) e [slug repository](../getting-started/repository.md).
3. Apri la cartella in Cursor — la regola è subito attiva.

## Verifica

In chat: *«Elenca le issue GitHub aperte»* → l'agente deve eseguire `python scripts/github_issue.py list`.

## Note

- Funziona in modalità Agent e terminale integrato su tutti i SO.
- Su **Windows**, `GITHUB_TOKEN` da variabile utente può essere letto anche via registry se la shell IDE non lo eredita.
- Frasi italiane come *«apri issue per…»* sono documentate nella regola.
- Questa regola è specifica per Cursor; altre piattaforme usano `AGENTS.md` — vedi [panoramica](overview.md).

## Troubleshooting

| Problema | Soluzione |
|----------|-----------|
| L'agente chiede comandi da incollare | Rimanda a `AGENTS.md`: eseguire lo script direttamente |
| Regola non applicata | Controlla `alwaysApply: true` nel front matter `.mdc` |
| Token non trovato | Riavvia Cursor dopo `GITHUB_TOKEN` |
