# Reddit Publishing

**URL:** https://www.reddit.com
**Type:** Community. **Crucial:** Be authentic. Do not sound like an ad. Provide value first.

## Subreddits to Target
*   `r/Python` (Focus on the Python standard library aspect)
*   `r/SideProject` (Focus on the problem it solves for you)
*   `r/opensource` (Focus on the MIT license and community aspect)
*   `r/programming` (General developer audience)
*   `r/CursorAI`, `r/ClaudeAI`, `r/ChatGPT` (Focus on the AI agent workflow)

---

## Post Template 1: For AI / Cursor Subreddits (e.g., r/CursorAI)
**Title:** I built an open-source tool that lets Cursor/Claude manage your GitHub Issues directly so you stop losing track of bugs

**Body:**
Hey everyone,

Whenever I'm iterating fast with Cursor or Claude Code, I often find bugs or think of features that I don't want to fix *right now*. But if I just leave them in the chat, they get lost. 

I wanted my AI agent to just open a GitHub issue for me automatically. 

I built **issuebeam** (Open Source, MIT) to do exactly this. It’s a lightweight Python CLI that connects your AI agent to GitHub Issues. 

You just drop the skeleton into your repo (`python scripts/adopt.py`), and your AI gets a set of rules (`AGENTS.md` / `.cursor/rules`) teaching it how to use the CLI. Whenever you tell Cursor "open an issue for this bug", it runs the python script, talks to the GitHub API, and creates the issue with the right labels.

It works on Windows, Mac, and Linux, and relies only on standard Python libraries (`urllib`) so you don't need to install `gh` CLI everywhere.

Repo: https://github.com/issuebeam/issuebeam
Docs: https://issuebeam.github.io/docs/

Let me know if you find it useful for your vibe coding workflows!

---

## Post Template 2: For Python / Open Source Subreddits
**Title:** issuebeam: A zero-dependency Python tool to wire AI agents to GitHub Issues

**Body:**
Hi r/[Subreddit],

I recently open-sourced **issuebeam**, a tool written in Python that allows AI coding assistants (like Copilot, Claude Code, Cursor) to natively interact with GitHub Issues. 

The interesting part (for Python devs): I built the CLI using only the standard library (`urllib`, `argparse`, `pathlib`) so it can be executed by an AI agent on literally any OS without requiring the user to install third-party dependencies or the GitHub CLI (`gh`). 

It includes an `adopt.py` script that copies the necessary python scripts and agent markdown instructions directly into your target repository.

If you use AI for coding and hate losing track of technical debt in chat logs, check it out.

GitHub: https://github.com/issuebeam/issuebeam

Feedback and PRs are welcome!
