# Altri agenti

Copia **`AGENTS.md`** nel formato richiesto dal tuo tool. La CLI è identica su **Windows, macOS e Linux**.

## Riferimento piattaforme

| Piattaforma | File istruzioni | Setup |
|-------------|-----------------|-------|
| **Windsurf** | `.windsurfrules` | `cp AGENTS.md .windsurfrules` |
| **Cline** | `.clinerules` o istruzioni custom | Incolla `AGENTS.md` nelle impostazioni Cline |
| **Continue.dev** | `.continue/rules` o config YAML | Riferisci `AGENTS.md` nella config |
| **Gemini CLI** | `GEMINI.md` | `cp AGENTS.md GEMINI.md` |
| **OpenAI Codex CLI** | `AGENTS.md` | Incluso da adopt — esegui dalla root del repo |
| **Aider** | `CONVENTIONS.md` o `/read AGENTS.md` | Carica all'avvio sessione |
| **Custom / CI** | `AGENTS.md` nel system prompt | Concedi shell tool con scope sul repo |

## Uso manuale (senza AI)

Nessun agente richiesto:

```bash
python scripts/github_issue.py create "Bug: login redirect" --labels bug
python scripts/github_issue.py list
```

Molti team adottano issuebeam per **CLI + label + template** prima, poi aggiungono regole agente per IDE.

## Agenti custom e CI

Qualsiasi automazione Python può usare issuebeam senza LLM:

```bash
python scripts/github_issue.py create "CI: flaky test on main" --labels bug,area-infra
```

Per agenti LLM custom:

- Metti `AGENTS.md` nel system prompt o contesto RAG
- Concedi uno shell tool con scope sul repo
- Non passare mai il token al modello — solo variabili d'ambiente
