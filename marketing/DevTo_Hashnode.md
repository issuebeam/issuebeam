# Dev.to & Hashnode

**URLs:** https://dev.to/ | https://hashnode.com/
**Type:** Blogging platforms for developers. Best for tutorials and "How-I-built-this" articles.

## Article Idea: "Stop losing your bugs in AI chats: How to connect Cursor/Claude to GitHub Issues"

**Tags:** `#productivity` `#opensource` `#ai` `#python`

**Article Outline / Content:**

### The Problem with "Vibe Coding"
If you use AI tools like Cursor, Windsurf, or Claude Code, you know the feeling: you are flying through a refactor, the AI is doing great, but suddenly you notice a separate bug. You mention it in the chat, the AI acknowledges it, but you move on. 

Two days later... *what was that bug again?* It's buried in a chat history. 

### The Solution
AI agents are great at writing code, but they are isolated from our project management tools. I wanted my AI to just open a GitHub issue for me, just like a real pair programmer would.

That's why I created **[issuebeam](https://github.com/issuebeam/issuebeam)**.

### What is issuebeam?
It's an open-source (MIT) bridge between your AI agent and your official GitHub repository. It consists of:
1. A zero-dependency Python CLI that can list, create, and manage issues.
2. Optimized prompt instructions (`AGENTS.md`, `.cursor/rules`) that teach the AI how to use the CLI.

### Why not just use the `gh` CLI?
I wanted this to work everywhere—Windows, Mac, Linux—without forcing developers to install binaries or deal with OS-specific shell scripts. Python is ubiquitous, and by restricting issuebeam to the standard library (`urllib`), any AI agent can execute it effortlessly.

### How to use it in your project
*(Insert code blocks showing the quick start)*
1. Get a GitHub Token
2. Run the `adopt.py` script in your repo.
3. Tell your AI: "Track this bug"

### Conclusion
If you are building software with AI, you need AI-native tooling. issuebeam is completely free and open source. Check out the repository [here](https://github.com/issuebeam/issuebeam) and let me know your thoughts in the comments!
