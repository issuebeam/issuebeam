# GitHub Copilot

Copilot usa le **istruzioni workspace**:

```
.github/copilot-instructions.md
AGENTS.md
```

## Setup

1. [Adotta](../getting-started/adopt.md) issuebeam — entrambi i file sono inclusi.
2. Abilita Copilot Chat con capacità **agent / edit** e terminale in VS Code.
3. Configura [token](../getting-started/token.md) e [slug repository](../getting-started/repository.md).

## Visual Studio

Stesso schema `copilot-instructions.md` quando il contesto workspace Copilot è attivo. La cartella soluzione deve essere la root del repo dove c'è `scripts/`.

## Verifica

In Copilot Chat: *"Track this bug on GitHub using our issuebeam CLI"*.

## Troubleshooting

| Problema | Soluzione |
|----------|-----------|
| Funziona in Cursor, non in Copilot | Controlla che esista `.github/copilot-instructions.md` |
| L'agente non esegue comandi | Abilita permessi terminale nelle impostazioni Copilot |
| Repo sbagliato | Apri la soluzione alla root del repository |
