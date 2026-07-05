# Adopt into a project

From the **issuebeam** folder (or after cloning this repo):

```bash
python scripts/adopt.py --target ../my-repo --repo myorg/my-app
```

Use `--force` to overwrite existing files. Works on **Windows, macOS, and Linux**.

## What `adopt.py` copies

| Item | Purpose |
|------|---------|
| `scripts/github_issue.py` | CLI |
| `tracker/*` | Labels, examples, slug file |
| `.github/ISSUE_TEMPLATE/*` | Web forms |
| `.github/copilot-instructions.md` | GitHub Copilot |
| `.cursor/rules/github-issues.mdc` | Cursor |
| `AGENTS.md`, `CLAUDE.md` | Universal / Claude Code rules |

## What it creates

- `tracker/github_repo` with your slug
- `tracker/import-manifest.json` from example (if missing)
- `.secrets/.gitkeep`

## After adopt

```bash
cd ../my-repo
python scripts/github_issue.py labels --apply
python scripts/github_issue.py list
```

Open the folder in your **AI agent**:

| Platform | Instruction file |
|----------|------------------|
| Cursor | `.cursor/rules/github-issues.mdc` |
| Claude Code | `CLAUDE.md` + `AGENTS.md` |
| Copilot | `.github/copilot-instructions.md` + `AGENTS.md` |
| Other | See [Platforms](../platforms/overview.md) |

Full documentation: [issuebeam.github.io/docs](https://issuebeam.github.io/docs/)
