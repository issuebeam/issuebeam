# Cursor

**Best-tested path.** Issuebeam ships with:

```
.cursor/rules/github-issues.mdc   # alwaysApply: true
```

## Setup

1. Clone issuebeam or run `adopt.py` into your repo.
2. Configure [token](../getting-started/token.md) and [repository slug](../getting-started/repository.md).
3. Open the folder in Cursor — the rule is active immediately.

## Verify

In chat: *"List open GitHub issues"* → agent should run `python scripts/github_issue.py list`.

## Notes

- Works in Agent mode and integrated terminal.
- `GITHUB_TOKEN` from Windows user env is read via registry.
- Italian phrases like *«apri issue per…»* are documented in the rule file.
- This rule is Cursor-specific; other platforms use `AGENTS.md` — see [overview](overview.md).

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Agent asks you to paste commands | Point to `AGENTS.md`: execute script directly |
| Rule not applied | Check `alwaysApply: true` in `.mdc` front matter |
| Token not found | Restart Cursor after setting `GITHUB_TOKEN` |
