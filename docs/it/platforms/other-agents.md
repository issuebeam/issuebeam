# Altri agenti

Copia **`AGENTS.md`** nel formato richiesto dal tuo tool.

## Riferimento piattaforme

| Piattaforma | File istruzioni | Setup |
|-------------|-----------------|-------|
| **Windsurf** | `.windsurfrules` | `copy AGENTS.md .windsurfrules` |
| **Cline** | `.clinerules` o istruzioni custom | Incolla `AGENTS.md` nelle impostazioni Cline |
| **Continue.dev** | `.continue/rules` o config YAML | Referenzia `AGENTS.md` nella config |
| **Gemini CLI** | `GEMINI.md` | `copy AGENTS.md GEMINI.md` |
| **OpenAI Codex CLI** | `AGENTS.md` | Incluso da adopt — avvia dalla root |
| **Aider** | `CONVENTIONS.md` o `/read AGENTS.md` | Carica all'avvio sessione |
| **Custom / CI** | `AGENTS.md` nel system prompt | Concedi tool shell limitato al repo |

## Uso manuale (senza AI)

Nessun agente richiesto:

```cmd
python scripts/github_issue.py create "Bug: redirect login" --labels bug
python scripts/github_issue.py list
```

Molti team adottano issuebeam per **CLI + label + template** e aggiungono le regole agente per IDE in un secondo momento.

## Agenti custom e CI

Qualsiasi automazione con Python può usare issuebeam senza LLM:

```cmd
python scripts/github_issue.py create "CI: test flaky su main" --labels bug,area-infra
```

Per agenti LLM custom:

- Metti `AGENTS.md` nel system prompt o contesto RAG
- Concedi un tool shell limitato al repo
- Non passare il token al modello — solo variabili d'ambiente
