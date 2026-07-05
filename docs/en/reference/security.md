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

1. `GITHUB_TOKEN` in process environment (all OS)
2. **Windows only:** user env var from registry (helps IDE terminals)
3. `.env` at repo root
4. `.secrets/github_token`

The agent should run the script directly — not ask the user to paste tokens or commands when configured.
