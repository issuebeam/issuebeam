# Label

Convenzioni in `tracker/labels.yml`. Personalizza e riesegui `labels --apply`.

| Label | Quando usarla |
|-------|----------------|
| `bug` | Comportamento errato, regressione |
| `enhancement` | Nuova funzionalità, miglioramento UX |
| `task` | Lavoro pianificato con DoD |
| `documentation` | Solo documentazione |
| `priority-high` | Blocca release o flusso critico |
| `priority-medium` | Importante ma non bloccante |
| `priority-low` | Nice-to-have, backlog |
| `area-frontend` | UI, client, browser |
| `area-backend` | API, servizi, database |
| `area-infra` | CI, Docker, deploy, monitoring |
| `area-docs` | README, guide, sito |
| `imported` | Migrato da tracker precedente |

Per issue importate, includi **`Legacy ID:`** nel body (es. `BUG-001`) e link al file markdown locale.

Applica su GitHub:

```bash
python scripts/github_issue.py labels --apply
```
