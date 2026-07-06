# AlternativeTo Listing

**URL:** https://alternativeto.net/
**Type:** Software discovery platform. Great for SEO.

## Status
- [ ] **Blocked.** New app submissions require an account age of at least 7 days. Can retry after **July 13, 2026, 4:04 PM (Stockholm time)**.
- [x] All setup info / descriptions below are ready to paste once unblocked

## Setup Information

*   **Application Name:** issuebeam
*   **Tags/Keywords:** GitHub Issues, Issue Tracking, AI Agent, Vibe Coding, Cursor, Copilot, Python CLI, Productivity
*   **License:** Open Source (MIT)
*   **Platforms:** Windows, macOS, Linux
*   **Official Website:** https://issuebeam.github.io
*   **GitHub Repository:** https://github.com/issuebeam/issuebeam

## Short Description (Pitch - max 150 chars)
Connect AI coding agents (Cursor, Copilot, Claude) directly to GitHub Issues via a Python CLI. Never lose track of bugs while vibe coding.

## Full Description
**issuebeam** is a lightweight, open-source tool designed for developers who embrace "vibe coding" with AI agents like Cursor, Claude Code, GitHub Copilot, Windsurf, or the Gemini CLI. 

When you are iterating fast with an AI, bug reports and planned tasks often get buried in the chat history. **issuebeam** solves this by wiring your AI agent directly to your official GitHub Issues. 

Instead of asking you to open a browser or copy-paste `gh` CLI commands, the agent uses issuebeam's Python CLI to seamlessly list, create, comment on, and close GitHub Issues right from the terminal. 

**Key Features:**
*   **Universal Compatibility:** Works on Windows, macOS, and Linux without requiring `gh` CLI or complex PowerShell scripts.
*   **Multi-Agent Ready:** Comes with ready-to-use agent instructions (`AGENTS.md`, `.cursor/rules`, etc.) for all major AI coding assistants.
*   **Zero Dependencies:** Uses standard Python libraries (`urllib`).
*   **Easily Adoptable:** Includes an `adopt.py` script to instantly copy the tracking skeleton into any existing repository.

Stop losing track of your ideas and bugs in AI chats. Let your AI manage your GitHub Issues for you.

**How it compares to GitHub's official MCP Server:** GitHub's MCP server covers similar ground but requires an MCP-compatible client and server setup. issuebeam trades that breadth for simplicity: it's a single dependency-free Python script any agent can run directly, no MCP configuration needed.

## Alternatives you are replacing/competing with (for the "Alternative to" section)
*   GitHub CLI (`gh` issue)
*   GitHub MCP Server (official, broader scope, requires MCP setup)
*   Linear (partially, for issue tracking context)
*   Jira (partially)
