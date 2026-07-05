# Indie Hackers

**URL:** https://www.indiehackers.com/
**Type:** Community for bootstrapped founders and makers.

## Post Idea: "I got tired of losing bugs in Cursor chats, so I built a zero-dependency CLI to link AI to GitHub Issues"

**Group:** Developer Tools / Open Source

**Body:**
Hey IH,

Like many of you, I've been shipping faster recently by using AI coding assistants (specifically Cursor and Claude). It’s amazing for "vibe coding", but I noticed a major workflow friction: 

When I’m in the middle of a refactor and the AI spots a bug (or I think of a new feature), I don't want to break my flow to go to GitHub, open an issue, write a description, etc. But if I just mention it in the AI chat, it inevitably gets lost when the context window clears.

I built **[issuebeam](https://github.com/issuebeam/issuebeam)** to fix this. It’s a completely free, open-source tool that allows your AI agent to natively manage your official GitHub Issues. 

Instead of dealing with OS-specific shell scripts or requiring developers to install the `gh` CLI, I wrote it entirely in standard-library Python (`urllib`). This means the AI can just run `python scripts/github_issue.py create "Title"` and it works out of the box on Windows, macOS, and Linux.

It includes an `adopt.py` script that instantly copies the setup into any repo, plus the markdown instructions you need to feed your agent (`AGENTS.md` / `.cursor/rules`).

Would love to hear if any other makers here are facing similar issues bridging the gap between AI chat and traditional project management tools!

Repo: https://github.com/issuebeam/issuebeam
Docs: https://issuebeam.github.io/docs/
