# Overview

## The problem

With LLMs and fast iteration:

- Bugs discussed in chat are **forgotten**
- Tasks stay "mental" but never appear in the team backlog
- Scattered markdown files (`TODO.md`, `bugs.txt`) multiply
- Nobody knows what is **open**, **in progress**, or **closed**

## The solution

Issuebeam connects **AI agent chat** to **GitHub Issues** with:

1. **`scripts/github_issue.py`** — stdlib Python CLI
2. **Agent instructions** — files the LLM reads (`AGENTS.md`, Cursor rule, Copilot, Claude, …)
3. **GitHub templates** — web forms for browser-based issue creation
4. **`adopt.py`** — copy the skeleton into any repo in one command

GitHub Issues becomes the **source of truth**. Local markdown stays for detailed plans and archives — not operational status.

## Architecture

```
You in chat  →  AI agent (reads AGENTS.md)  →  github_issue.py  →  GitHub Issues
```

Requirements for any platform:

- Python 3
- `GITHUB_TOKEN` with Issues read/write
- Repo slug in `tracker/github_repo` or `GITHUB_REPO`
- Agent instructions: *run the script, don't delegate to the user*

## Next steps

1. [GitHub token](token.md)
2. [Repository slug](repository.md)
3. [Adopt into a project](adopt.md) (optional)
4. [Choose your platform](../platforms/overview.md)
