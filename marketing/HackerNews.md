# Hacker News (Show HN)

**URL:** https://news.ycombinator.com/
**Type:** Developer community. Needs a very technical and humble tone. No marketing fluff.

## Submission Guidelines
*   **Title Format:** Show HN: issuebeam – Let your AI coding agent manage your GitHub Issues
*   **URL:** Point directly to the GitHub repo `https://github.com/issuebeam/issuebeam` or the docs `https://issuebeam.github.io/docs/`. GitHub repo is usually preferred by HN.

## First Comment (The "Show HN" explanation)
*HN prefers plain text, technical explanations of *why* you built it and *how* it works.*

Hi HN,

I’ve been doing a lot of "vibe coding" lately using agents like Cursor and Claude Code. One major friction point I found was losing track of bugs, technical debt, and planned tasks because they just get buried in the AI chat history. I wanted the AI to manage the issue tracker directly.

I built issuebeam to solve this. It wires any AI agent to GitHub Issues via a standard-library Python CLI. 

I explicitly avoided relying on the `gh` CLI or OS-specific shell scripts to make it perfectly cross-platform (Windows/macOS/Linux) and easy for the LLM to use. The AI just runs `python scripts/github_issue.py create "Title"` and it's done. 

It uses `urllib` to minimize dependencies and includes an `adopt.py` script so you can easily copy the tracking skeleton and agent instructions (`AGENTS.md`, `.cursor/rules/`, etc.) into any existing project. 

It’s open source (MIT). Would love to hear your feedback on the approach or if you've found other ways to bridge the gap between AI chat contexts and official issue trackers.

Thanks!
