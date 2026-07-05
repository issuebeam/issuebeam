# Commands

Run all commands from the **project root** (where `scripts/` lives).

## Labels

Defined in `tracker/labels.yml`. First time on a repo:

```cmd
python scripts/github_issue.py labels
python scripts/github_issue.py labels --apply
```

## List issues

```cmd
python scripts/github_issue.py list
python scripts/github_issue.py list --state closed --limit 50
```

## Create issue

```cmd
python scripts/github_issue.py create "Short title" --body "Markdown **description**" --labels bug,priority-high,area-frontend
```

From file:

```cmd
python scripts/github_issue.py create "Safari bug" --body-file description.md --labels bug
```

## Comment

```cmd
python scripts/github_issue.py comment 42 --body "Fix applied in commit abc123"
```

## Close

```cmd
python scripts/github_issue.py close 42
python scripts/github_issue.py close 42 --reason "Duplicate of #40"
python scripts/github_issue.py close-batch 10 11 12 --reason "Deprioritized backlog"
```

## Import batch (migrate from local tracker)

```cmd
copy tracker\import-manifest.example.json tracker\import-manifest.json
REM edit import-manifest.json
python scripts/github_issue.py import --dry-run
python scripts/github_issue.py import --apply
```

Include **`Legacy ID:`** in each imported body to prevent duplicates on re-import:

```markdown
**Legacy ID:** `BUG-001`
```

## Override repo slug

```cmd
python scripts/github_issue.py --repo myorg/my-app list
```
