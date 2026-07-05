# Labels

Conventions in `tracker/labels.yml`. Customize and re-run `labels --apply`.

| Label | When to use |
|-------|-------------|
| `bug` | Wrong behavior, regression |
| `enhancement` | New feature, UX improvement |
| `task` | Planned work with definition of done |
| `documentation` | Docs only |
| `priority-high` | Blocks release or critical flow |
| `priority-medium` | Important but not blocking |
| `priority-low` | Nice-to-have, backlog |
| `area-frontend` | UI, client, browser |
| `area-backend` | API, services, database |
| `area-infra` | CI, Docker, deploy, monitoring |
| `area-docs` | README, guides, site |
| `imported` | Migrated from previous tracker |

For imported issues, include **`Legacy ID:`** in the body (e.g. `BUG-001`) and a link to the local markdown file.

Apply to GitHub:

```cmd
python scripts/github_issue.py labels --apply
```
