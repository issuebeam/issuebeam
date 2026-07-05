# Commit e PR

Quando una PR risolve lavoro tracciato, referenzia l'issue nel messaggio di commit:

```
fix(auth): handle Safari redirect after login

Fixes #42
```

GitHub chiude automaticamente l'issue al merge (se l'opzione del repo è attiva).

Varianti:

- `Closes #42` — stesso comportamento di chiusura automatica
- `Refs #42` — riferimento senza chiusura automatica

## Flusso agente

Dopo aver corretto un bug, l'agente dovrebbe:

1. Committare con `Fixes #N` quando appropriato
2. Opzionalmente commentare l'issue: `python scripts/github_issue.py comment N --body "Fix in …"`
3. Chiudere manualmente se serve: `python scripts/github_issue.py close N`
