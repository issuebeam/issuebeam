# FAQ

## What is Issuebeam?

A lightweight skeleton that connects AI coding agents to GitHub Issues. The agent runs a Python CLI to create, comment, and close issues — no `gh` CLI, no PowerShell scripts.

## Is it Cursor-only?

**No.** Cursor is the best-tested path, but the same CLI works with Claude Code, GitHub Copilot, Windsurf, Cline, Gemini CLI, Codex CLI, Aider, and manual use. See [Platforms](../platforms/overview.md).

## Do I need the gh CLI?

No. Issuebeam uses stdlib Python (`urllib`) against the GitHub REST API. You need Python and a PAT with Issues read/write.

## How does the agent know to use it?

Instruction files in the repo: `AGENTS.md` (universal), `.cursor/rules/` for Cursor, `CLAUDE.md` for Claude Code, `.github/copilot-instructions.md` for Copilot. The agent runs `python scripts/github_issue.py` directly.

## Can I adopt it into an existing project?

Yes: `python scripts/adopt.py --target ../my-repo --repo myorg/my-app`

## Where does the token live?

Prefer Windows user env var `GITHUB_TOKEN`. Alternatives: `.env` (gitignored) or `.secrets/github_token`. Never commit tokens or paste them in chat.

## Can I use it without any AI agent?

Yes. The CLI is fully usable by humans — many teams start with CLI + labels, then add agent rules.

## How do I publish these docs?

```cmd
pip install -r docs/requirements.txt
scripts\publish_docs.bat
cd ..\issuebeam.github.io
git push
```

Site: [issuebeam.github.io/docs](https://issuebeam.github.io/docs/)
