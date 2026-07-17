# Security

## Do

- Store token in user env vars, `.env` (gitignored), or `.secrets/github_token`
- Ensure `.gitignore` includes `.secrets/` and `.env`
- Use fine-grained tokens scoped to a single repository
- Rotate the token if accidentally exposed

## Don't

- **Never** paste the token in agent chat or GitHub issues
- **Never** commit tokens or share screenshots with tokens visible
- **Never** use PowerShell scripts in this stack (antivirus / team policy) — Python only

## SSL / corporate proxy

If you see SSL certificate errors toward `api.github.com` (common on **Windows** with corporate AV/proxy, sometimes elsewhere):

```bash
pip install -r requirements-optional.txt
```

Installs optional `truststore` (uses the OS trust store on Windows).

## Token resolution order (CLI)

The CLI reads the token automatically:

1. `.env` at repo root (`GITHUB_TOKEN=...`)
2. `GITHUB_TOKEN` in process environment (all OS)
3. `.secrets/github_token`
4. **Windows only:** user env var from registry (fallback)

The agent should run the script directly — not ask the user to paste tokens or commands when configured.
