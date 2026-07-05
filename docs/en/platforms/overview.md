# Supported platforms

Issuebeam is **not tied to Cursor**. If your agent can read repo files and run shell commands, it works.

## Quick comparison

| Platform | Instruction file(s) | Shell access |
|----------|---------------------|--------------|
| [Cursor](cursor.md) | `.cursor/rules/github-issues.mdc` | Yes |
| [Claude Code](claude-code.md) | `CLAUDE.md`, `AGENTS.md` | Yes |
| [GitHub Copilot](copilot.md) | `.github/copilot-instructions.md`, `AGENTS.md` | Yes |
| [Other agents](other-agents.md) | `AGENTS.md` or platform equivalent | Yes |
| Manual | — | You run CLI |

## Same CLI everywhere

| Layer | Platform-specific? |
|-------|-------------------|
| `scripts/github_issue.py` | No |
| Token, slug, labels | No |
| Agent instruction file | Yes — path differs |

## Mixed teams

You can ship **all** instruction files in one repo — they do not conflict:

- Cursor reads `.cursor/rules/`
- Claude Code reads `CLAUDE.md`
- Copilot reads `copilot-instructions.md`
- All point to the same CLI and conventions

## Choosing files

| You use… | Minimum files |
|----------|----------------|
| Cursor only | `.cursor/rules/github-issues.mdc` |
| Claude Code only | `AGENTS.md` + `CLAUDE.md` |
| Copilot only | `AGENTS.md` + `.github/copilot-instructions.md` |
| Mixed team | All of the above |

`adopt.py` copies the common set automatically.
