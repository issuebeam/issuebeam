# Commands

Run all commands from the **project root** (where `scripts/` lives). Same CLI on **Windows, macOS, and Linux**.

## Labels

Defined in `tracker/labels.yml`. First time on a repo:

```bash
python scripts/github_issue.py labels
python scripts/github_issue.py labels --apply
```

## List issues

```bash
python scripts/github_issue.py list
python scripts/github_issue.py list --state closed --limit 50
```

## Create issue

```bash
python scripts/github_issue.py create "Short title" --body "Markdown **description**" --labels bug,priority-high,area-frontend
```

From file:

```bash
python scripts/github_issue.py create "Safari bug" --body-file description.md --labels bug
```

## Edit issue

Update title, body, and/or labels on an existing issue. At least one flag is required.  
`--labels` **replaces** the full label set (empty string clears all labels).

```bash
python scripts/github_issue.py edit 42 --title "New title"
python scripts/github_issue.py edit 42 --body "Updated **markdown** body"
python scripts/github_issue.py edit 42 --body-file updated.md
python scripts/github_issue.py edit 42 --labels task,priority-low,area-docs
python scripts/github_issue.py edit 42 --title "Retitled" --labels bug,priority-high
```

## Comment

```bash
python scripts/github_issue.py comment 42 --body "Fix applied in commit abc123"
```

## Close

```bash
python scripts/github_issue.py close 42
python scripts/github_issue.py close 42 --reason "Duplicate of #40"
python scripts/github_issue.py close-batch 10 11 12 --reason "Deprioritized backlog"
```

## Import batch (migrate from local tracker)

```bash
cp tracker/import-manifest.example.json tracker/import-manifest.json
# edit import-manifest.json
python scripts/github_issue.py import --dry-run
python scripts/github_issue.py import --apply
```

Include **`Legacy ID:`** in each imported body to prevent duplicates on re-import:

```markdown
**Legacy ID:** `BUG-001`
```

## Override repo slug

```bash
python scripts/github_issue.py --repo myorg/my-app list
```
