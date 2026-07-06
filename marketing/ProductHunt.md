# Product Hunt Launch

**URL:** https://www.producthunt.com/
**Type:** Launch platform. Best for spikes in traffic and getting early adopters.

## Status
- [ ] **Account restriction trovata.** Serve aspettare almeno 1 settimana dalla creazione dell'account prima di poter postare (o account potrebbe essere segnalato come "branded" invece che personale — verificare nome completo/foto/bio nel profilo). Newsletter già iscritta, non utile come scorciatoia. In attesa.
- [x] Thumbnail (1280x720px) — created, saved at both `issuebeam.github.io/assets/images/og-images/producthunt-thumbnail.png` and `marketing/video-product-hunt/screenshots/0-thumbnail-1280x720.png` (branded: logo mark + wordmark + tagline on dark background)
- [x] Screenshots (4) — extracted and cropped from the real demo recording, saved at `marketing/video-product-hunt/screenshots/`: 1-ask-ai-to-open-issue.png, 2-cli-command-permission.png, 3-issue-created-confirmation.png, 4-live-on-github.png. Cropped to remove VS Code sidebar, browser tabs, and OS taskbar.
- [x] Demo video — recorded, raw file at `marketing/video-product-hunt/2026-07-06 17-56-56.mp4` (real workflow: ask AI to open an issue on qwibo repo → CLI runs → issue live on GitHub)
- [ ] Launch not yet scheduled

## Pre-Launch Checklist
- Create a maker account.
- Prepare a 1280x720px thumbnail (maybe a GIF showing Cursor/Claude creating an issue).
- Prepare 3-5 screenshots showing the workflow.
- Prepare a 1-minute demo video (optional but highly recommended).

## Setup Information

*   **Name:** issuebeam
*   **Tagline (60 chars):** Connect AI agents directly to GitHub Issues
*   **Topics:** Developer Tools, Artificial Intelligence, Productivity, GitHub, Open Source

## First Comment (Maker's Comment)
Hey Product Hunt! 👋 I'm Antonio, the creator of issuebeam.

If you're like me and use AI agents like Cursor, Claude Code, or Copilot for "vibe coding", you've probably noticed a problem: bugs, tasks, and ideas often get lost in the long AI chat history. 

I built **issuebeam** to fix this. It’s an open-source tool that wires any AI agent directly to your official GitHub Issues. 

Using a lightweight Python CLI (no `gh` CLI dependencies), your AI can now autonomously check existing issues, create new ones, comment, and close them without breaking your flow. 

**Why issuebeam?**
✨ Multi-platform (Windows, Mac, Linux)
🤖 Works with Cursor, Windsurf, Claude Code, Copilot, etc.
🚀 Zero heavy dependencies, easily adoptable into any repo (`python scripts/adopt.py`)

It's completely free and open-source (MIT). I'd love for you to try it with your favorite AI agent and let me know what you think! Happy to answer any questions! 

## Description (for the product page)
issuebeam links your AI coding agents directly to your official GitHub issue tracker. Instead of losing track of bugs and tasks in endless chat logs, issuebeam allows Cursor, Claude Code, Copilot, and other agents to list, create, and manage GitHub issues autonomously using a simple Python CLI. Fast, multi-platform, and fully open-source.

## Anticipated Q&A: "How is this different from GitHub's official MCP Server?"
GitHub's MCP Server covers similar (and broader) ground, but needs an MCP-compatible client and server setup. issuebeam is for when you don't want that overhead — it's a single dependency-free Python script your agent runs directly, no MCP configuration required. Different tradeoff (narrower scope, near-zero setup), not a replacement.
