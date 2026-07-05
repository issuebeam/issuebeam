# Commits and PRs

When a PR resolves tracked work, reference the issue in the commit message:

```
fix(auth): handle Safari redirect after login

Fixes #42
```

GitHub closes the issue automatically on merge (if the repo option is enabled).

Variants:

- `Closes #42` — same auto-close behavior
- `Refs #42` — reference without auto-close

## Agent workflow

After fixing a bug, the agent should:

1. Commit with `Fixes #N` when appropriate
2. Optionally comment on the issue: `python scripts/github_issue.py comment N --body "Fixed in …"`
3. Close manually if needed: `python scripts/github_issue.py close N`
