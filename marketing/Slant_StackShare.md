# Slant & StackShare

**URLs:** https://www.slant.co/ | https://stackshare.io/
**Type:** Tech stack and tool comparison platforms.

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
**Cons:**
*   Requires a GitHub repository to function (does not support GitLab/Bitbucket natively yet).
