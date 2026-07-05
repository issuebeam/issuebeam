# FAQ

## Cos'è Issuebeam?

Uno skeleton leggero che collega agenti AI di coding a GitHub Issues. L'agente esegue una CLI Python per creare, commentare e chiudere issue — senza `gh` CLI e senza script PowerShell.

## Funziona solo con Cursor?

**No.** Cursor è il percorso più testato, ma la stessa CLI funziona con Claude Code, GitHub Copilot, Windsurf, Cline, Gemini CLI, Codex CLI, Aider e uso manuale. Vedi [Piattaforme](../platforms/overview.md).

## Serve la gh CLI?

No. Issuebeam usa Python stdlib (`urllib`) contro l'API REST di GitHub. Ti basta Python e un PAT con Issues read/write.

## Come fa l'agente a usarlo?

File istruzioni nel repo: `AGENTS.md` (universale), `.cursor/rules/` per Cursor, `CLAUDE.md` per Claude Code, `.github/copilot-instructions.md` per Copilot. L'agente esegue `python scripts/github_issue.py` direttamente.

## Posso adottarlo in un progetto esistente?

Sì: `python scripts/adopt.py --target ../my-repo --repo myorg/my-app`

## Dove metto il token?

Preferisci `GITHUB_TOKEN` come variabile d'ambiente (Windows, macOS, Linux). Alternative: `.env` (gitignored) o `.secrets/github_token`. Su Windows la CLI può leggere anche le variabili utente dal registry se il terminale IDE non le eredita.

## Posso usarlo senza agente AI?

Sì. La CLI funziona anche per umani — molti team partono da CLI + label, poi aggiungono le regole agente.

## Come pubblico questa documentazione?

```bash
pip install -r docs/requirements.txt
python scripts/publish_docs.py
cd ../issuebeam.github.io
git push
```

Sito: [issuebeam.github.io/docs/it](https://issuebeam.github.io/docs/it/)
