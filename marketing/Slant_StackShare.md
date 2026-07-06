# Slant & StackShare

**URLs:** https://www.slant.co/ | https://stackshare.io/
**Type:** Tech stack and tool comparison platforms.

## Status
- [x] **StackShare — Pubblicato.** Live come "Issuebeam — GitHub Issues for AI Agents" nella categoria "Code Collaboration". Descrizione e tag inseriti. Pros/Cons lasciati vuoti deliberatamente — richiederebbe creare 10 "stacks" prima di poter contribuire, non ne vale la pena per un dettaglio minore.
- [ ] **Slant — Deprioritizzato per ora.** UI poco chiara (question-based, non un semplice form) e il sito blocca l'accesso automatico per verificarne i dettagli. Basso traffico/priorità rispetto ad altre directory già fatte. Da riprendere solo se avanza tempo — vedi sezione sotto per i passaggi generali (cerca una domanda pertinente o creane una con "Ask Question", poi "I Recommend" per aggiungere issuebeam come opzione).

## Setup Information

*   **Tool Name:** issuebeam
*   **Website:** https://issuebeam.github.io
*   **Description:** A lightweight, cross-platform Python tool that connects AI coding agents (Cursor, Claude Code, Copilot) directly to GitHub Issues.
*   **Category/Tags:** Issue Tracking, Productivity, Developer Tools, AI Assistants.

## StackShare "Why we use it" Post
**Title:** Bridging the gap between AI coding and GitHub
**Content:** We adopted issuebeam into our stack because we were constantly losing track of bugs and technical debt within our AI chat interfaces (like Cursor and Windsurf). issuebeam allows our AI agents to natively interact with GitHub Issues without requiring complex dependencies or `gh` CLI installations across different operating systems. It runs purely on standard-library Python, making it perfectly suited for autonomous agents.

## Slant Recommendations
*If creating a question like "What are the best tools for AI-assisted coding?" or "How to track issues when using Cursor/Claude?":*

**Recommendation Name:** issuebeam
**Pros:**
*   Zero dependencies (only standard Python `urllib`).
*   Cross-platform (Windows, Mac, Linux) out of the box.
*   Comes with pre-written agent instructions (`.cursor/rules/`, `AGENTS.md`).
*   Open Source (MIT).
*   No MCP client/server setup required, unlike GitHub's official MCP Server — just a script the agent runs directly.
**Cons:**
*   Requires a GitHub repository to function (does not support GitLab/Bitbucket natively yet).
*   Narrower scope than GitHub's MCP Server (issues only, not the full GitHub API surface).
