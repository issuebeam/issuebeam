# Repository slug

The CLI must know which GitHub repo to use (`owner/name`).

Resolution order:

| Priority | Source |
|----------|--------|
| 1 | `GITHUB_REPO` environment variable |
| 2 | `.env` → `GITHUB_REPO=owner/repo` |
| 3 | `tracker/github_repo` — one line (created by `adopt.py`) |

## Option A — local file (recommended after adopt)

```cmd
echo myorg/my-app> tracker\github_repo
```

## Option B — `.env`

```
GITHUB_REPO=myorg/my-app
GITHUB_TOKEN=github_pat_...
```

## Option C — one-time override

```cmd
python scripts/github_issue.py --repo myorg/my-app list
```

## First commands

After token and slug are set:

```cmd
python scripts/github_issue.py labels --apply
python scripts/github_issue.py list
```
