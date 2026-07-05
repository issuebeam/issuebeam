# Other agents

Copy **`AGENTS.md`** into the format your tool expects.

## Platform reference

| Platform | Instruction file | Setup |
|----------|------------------|-------|
| **Windsurf** | `.windsurfrules` | `copy AGENTS.md .windsurfrules` |
| **Cline** | `.clinerules` or custom instructions | Paste `AGENTS.md` in Cline settings |
| **Continue.dev** | `.continue/rules` or YAML config | Reference `AGENTS.md` in config |
| **Gemini CLI** | `GEMINI.md` | `copy AGENTS.md GEMINI.md` |
| **OpenAI Codex CLI** | `AGENTS.md` | Included by adopt — run from repo root |
| **Aider** | `CONVENTIONS.md` or `/read AGENTS.md` | Load at session start |
| **Custom / CI** | `AGENTS.md` in system prompt | Grant scoped shell tool |

## Manual use (no AI)

No agent required:

```cmd
python scripts/github_issue.py create "Bug: login redirect" --labels bug
python scripts/github_issue.py list
```

Many teams adopt issuebeam for **CLI + labels + templates** first, then add agent rules per IDE.

## Custom agents and CI

Any automation that runs Python can use issuebeam without an LLM:

```cmd
python scripts/github_issue.py create "CI: flaky test on main" --labels bug,area-infra
```

For custom LLM agents:

- Put `AGENTS.md` in system prompt or RAG context
- Grant a shell tool scoped to the repo
- Never pass the token through the model — use env vars only
