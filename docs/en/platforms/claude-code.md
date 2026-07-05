# Claude Code

Claude Code (VS Code extension, CLI, or desktop) reads **`CLAUDE.md`** and **`AGENTS.md`** from the repository root.

## Setup

1. Run [adopt](../getting-started/adopt.md) — copies `CLAUDE.md` and `AGENTS.md`.
2. Open the **repository root** in VS Code (not a parent folder).
3. Install Claude Code extension or use the CLI.
4. Set `GITHUB_TOKEN` ([token guide](../getting-started/token.md)).

## Verify

Ask: *"Create a GitHub issue titled [Bug] Test from Claude"* — Claude should execute the Python script.

## VS Code tips

- Shell commands run from integrated terminal inherit user env vars after IDE restart.
- If Claude asks you to run commands manually, remind it to follow **AGENTS.md**.

## Optional project memory

Add to Claude project settings:

> For bugs and tasks, use `python scripts/github_issue.py` per AGENTS.md. GitHub Issues is the source of truth.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Wrong working directory | Open repo root where `scripts/` lives |
| Agent doesn't run script | Ensure `AGENTS.md` is in context |
| Token missing | Restart VS Code after env var change |
