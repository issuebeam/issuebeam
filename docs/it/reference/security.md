# Sicurezza

## Da fare

- Token solo in variabili utente, `.env` (gitignored) o `.secrets/github_token`
- `.gitignore` include `.secrets/` e `.env`
- Token fine-grained limitato al singolo repository
- Ruotare il token se esposto accidentalmente

## Da non fare

- **Mai** incollare il token in chat con l'agente o in issue GitHub
- **Mai** committare token o condividere screenshot con token visibile
- **Mai** usare script PowerShell in questo stack (antivirus / policy team) — solo Python

## SSL / proxy aziendale

Se vedi errori certificato SSL verso `api.github.com` (comune su **Windows** con AV/proxy aziendale, a volte anche altrove):

```bash
pip install -r requirements-optional.txt
```

Installa `truststore` opzionale (usa il trust store del SO su Windows).

## Ordine risoluzione token

La CLI legge il token automaticamente:

1. `GITHUB_TOKEN` nell'ambiente del processo (tutti i SO)
2. **Solo Windows:** variabile utente da registry (aiuta i terminali IDE)
3. `.env` nella root del repo
4. `.secrets/github_token`

L'agente deve eseguire lo script direttamente — non chiedere token o comandi all'utente se configurato.
