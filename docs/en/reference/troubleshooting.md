# Troubleshooting

| Symptom | Solution |
|---------|----------|
| `ERRORE: token GitHub non trovato` / token not found | Set `GITHUB_TOKEN` or create `.secrets/github_token` |
| `ERRORE: repository GitHub non configurato` / repo not configured | Create `tracker/github_repo` or `GITHUB_REPO` in `.env` |
| HTTP 401 | Token expired or revoked — generate a new one |
| HTTP 404 | Wrong repo slug or token has no access |
| HTTP 403 | Insufficient permissions — Issues read/write required |
| SSL certificate error | `pip install -r requirements-optional.txt` (truststore) |
| Agent never runs the script | Add instruction file for your platform — see [Platforms](../platforms/overview.md) |
| Agent asks user to paste commands | Strengthen `AGENTS.md`: execute script directly |
| Works in Cursor, not Copilot | Check `.github/copilot-instructions.md` and `AGENTS.md` |
| Works in terminal, not in agent | Enable shell/terminal permissions in agent settings |
| Wrong working directory | Open repository root where `scripts/` lives |

## Verify setup

```bash
python -c "import os; print('token:', 'OK' if os.environ.get('GITHUB_TOKEN') else 'MISSING')"
cat tracker/github_repo
python scripts/github_issue.py list
```

## Get help

Open an issue on [github.com/issuebeam/issuebeam](https://github.com/issuebeam/issuebeam/issues).
