# Panoramica

## Il problema

Con LLM e iterazione rapida succede spesso:

- Un bug discusso in chat viene **dimenticato**
- Un task resta «mentale» ma **non compare** nel backlog del team
- File markdown sparsi (`TODO.md`, `bugs.txt`) moltiplicano la confusione
- Nessuno sa cosa è **aperto**, **in corso** o **chiuso**

## La soluzione

Issuebeam collega la **chat dell'agente AI** a **GitHub Issues** con:

1. **`scripts/github_issue.py`** — CLI Python stdlib
2. **Istruzioni agente** — file letti dall'LLM (`AGENTS.md`, regola Cursor, Copilot, Claude, …)
3. **Template GitHub** — form web per aprire issue dal browser
4. **`adopt.py`** — copia lo skeleton in qualsiasi repo con un comando

GitHub Issues diventa la **fonte di verità**. I markdown locali restano per piani dettagliati e archivio — non per lo stato operativo.

## Architettura

```
Tu in chat  →  Agente AI (legge AGENTS.md)  →  github_issue.py  →  GitHub Issues
```

Requisiti per ogni piattaforma:

- Python 3 (**Windows, macOS, Linux**)
- `GITHUB_TOKEN` con Issues read/write
- Slug in `tracker/github_repo` o `GITHUB_REPO`
- Istruzioni agente: *esegui lo script, non delegare all'utente*

## Prossimi passi

1. [Token GitHub](token.md)
2. [Slug repository](repository.md)
3. [Adotta in un progetto](adopt.md) (opzionale)
4. [Scegli la piattaforma](../platforms/overview.md)
