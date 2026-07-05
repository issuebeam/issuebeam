# GitHub token

You need a **Personal Access Token** with permission to read and write issues on the target repository.

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

| Method | Pros | Cons |
|--------|------|------|
| **Windows user env `GITHUB_TOKEN`** | Works in IDE terminals and agents | Set once per machine |
| **`.secrets/github_token`** | Gitignored, simple | Local file — never commit |
| **`.env`** | Convenient in dev | Risk of accidental commit (gitignored) |

**Never** paste the token in agent chat, public issues, or commits.

## Windows user variable (recommended)

1. Open **Environment Variables** (user section)
2. **New…** → Name: `GITHUB_TOKEN` — Value: `github_pat_...`
3. OK on all dialogs
4. **Restart your IDE** (Cursor, VS Code, …) or integrated terminal

### Verify

```cmd
python -c "import os; t=os.environ.get('GITHUB_TOKEN',''); print('OK' if t else 'MISSING', len(t))"
```

If `MISSING` but you set the user variable, the script also reads **Windows registry** — try:

```cmd
python scripts/github_issue.py list
```

(after configuring the repo slug)

### Optional: `GITHUB_REPO` in user variables

Useful if you always work on the same repo:

- Name: `GITHUB_REPO`
- Value: `myorg/my-app`
