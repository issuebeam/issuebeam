# GitHub Copilot

Copilot uses **workspace instructions**:

```
.github/copilot-instructions.md
AGENTS.md
```

## Setup

1. [Adopt](../getting-started/adopt.md) issuebeam — both files are included.
2. Enable Copilot Chat with **agent / edit** and terminal capabilities in VS Code.
3. Configure [token](../getting-started/token.md) and [repository slug](../getting-started/repository.md).

## Visual Studio

Same `copilot-instructions.md` pattern when Copilot workspace context is enabled. The solution folder must be the repo root where `scripts/` lives.

## Verify

In Copilot Chat: *"Track this bug on GitHub using our issuebeam CLI"*.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Works in Cursor, not Copilot | Check `.github/copilot-instructions.md` exists |
| Agent won't run commands | Enable terminal permissions in Copilot settings |
| Wrong repo | Open solution at repository root |
