# Risoluzione problemi

| Sintomo | Soluzione |
|---------|-----------|
| `ERRORE: token GitHub non trovato` | Imposta `GITHUB_TOKEN` o crea `.secrets/github_token` |
| `ERRORE: repository GitHub non configurato` | Crea `tracker/github_repo` o `GITHUB_REPO` in `.env` |
| HTTP 401 | Token scaduto o revocato — generane uno nuovo |
| HTTP 404 | Slug repo errato o token senza accesso |
| HTTP 403 | Permessi insufficienti — Issues read/write |
| Errore certificato SSL | `pip install -r requirements-optional.txt` (truststore) |
| L'agente non esegue lo script | Aggiungi file istruzioni per la piattaforma — vedi [Piattaforme](../platforms/overview.md) |
| Chiede comandi da incollare | Rafforza `AGENTS.md`: eseguire lo script direttamente |
| Funziona in Cursor, non in Copilot | Controlla `.github/copilot-instructions.md` e `AGENTS.md` |
| Funziona in terminale, non in agente | Abilita permessi shell/terminale nell'agente |
| Directory sbagliata | Apri la root del repo dove c'è `scripts/` |

## Verifica setup

```bash
python -c "import os; print('token:', 'OK' if os.environ.get('GITHUB_TOKEN') else 'MANCANTE')"
cat tracker/github_repo
python scripts/github_issue.py list
```

## Aiuto

Apri una issue su [github.com/issuebeam/issuebeam](https://github.com/issuebeam/issuebeam/issues).
