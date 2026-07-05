# GitHub token

You need a **Personal Access Token** with permission to read and write issues on the target repository.

Issuebeam runs on **Windows, macOS, and Linux** — only the way you export `GITHUB_TOKEN` changes. The CLI is the same everywhere: `python scripts/github_issue.py`.

## Classic token

1. GitHub → **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**
2. **Generate new token (classic)**
3. Minimum scope: **`repo`** (or Issues-only with fine-grained on a single repo)
4. Copy the token — shown **once**

## Fine-grained token (recommended for teams)

1. **Personal access tokens** → **Fine-grained tokens** → **Generate new token**
2. **Repository access:** only the project repo (e.g. `myorg/my-app`)
3. **Permissions → Issues:** Read and write
4. No other permissions required

## Where to store the token

| Method | Works on | Pros | Cons |
|--------|----------|------|------|
| **`GITHUB_TOKEN` env var** | Win · Mac · Linux | Works in terminals and AI agents | Must restart IDE/shell after change |
| **`.secrets/github_token`** | All | Gitignored, simple, portable | Local file — never commit |
| **`.env`** | All | Convenient in dev | Risk of accidental commit (gitignored) |

**Never** paste the token in agent chat, public issues, or commits.

## Set `GITHUB_TOKEN` (recommended)

=== "Windows"

1. Open **Environment Variables** → **User variables** → **New…**
2. Name: `GITHUB_TOKEN` — Value: `github_pat_...`
3. OK on all dialogs
4. **Restart your IDE** (Cursor, VS Code, …) or open a new terminal

**Extra:** if the IDE terminal still misses the variable, issuebeam also reads the **Windows user registry** (same value as above) — no extra setup.

=== "macOS"

**Terminal / CLI agents** — add to `~/.zshrc` or `~/.bashrc`:

```bash
export GITHUB_TOKEN=github_pat_...
```

Then `source ~/.zshrc` (or open a new terminal).

**GUI apps (Cursor, VS Code launched from Dock)** — user env vars from the shell are not always inherited. Options:

- Launch the IDE from a terminal: `cursor .` or `code .`
- Or use `.env` / `.secrets/github_token` in the project (see below)

=== "Linux"

**Shell** — add to `~/.bashrc`, `~/.zshrc`, or use [direnv](https://direnv.net/) in the repo:

```bash
export GITHUB_TOKEN=github_pat_...
```

**systemd user session** (optional, for GUI tools):

```ini
# ~/.config/environment.d/github.conf
GITHUB_TOKEN=github_pat_...
```

Log out and back in. Alternatively use `.env` or `.secrets/github_token`.

## Alternative: `.env` or `.secrets/` (all OS)

**`.env`** at repo root (gitignored):

```
GITHUB_REPO=myorg/my-app
GITHUB_TOKEN=github_pat_...
```

**`.secrets/github_token`** — one line, gitignored:

```bash
mkdir -p .secrets
printf '%s\n' 'github_pat_...' > .secrets/github_token
chmod 600 .secrets/github_token   # macOS / Linux
```

## Verify

```bash
python -c "import os; print('OK' if os.environ.get('GITHUB_TOKEN') else 'MISSING')"
```

Then (after [repository slug](repository.md) is set):

```bash
python scripts/github_issue.py list
```

## Token resolution order (CLI)

The script reads the token automatically:

1. `GITHUB_TOKEN` in the current process environment
2. **Windows only:** user env var from registry (helps IDE terminals)
3. `.env` in repo root
4. `.secrets/github_token`

## Optional: `GITHUB_REPO` in the environment

Same methods as `GITHUB_TOKEN` — useful if you always work on one repo:

```bash
export GITHUB_REPO=myorg/my-app
```
