# Tools

Tools turn approved copy or data into a usable file. They run after the work passes the audit, never instead of it.

```
Tool                 What it produces                      Instructions
-------------------------------------------------------------------------------------------
html-landing-page    Branded, responsive HTML landing      tools/html-landing-page/TOOL.md
                     page from approved copy
sheets-dashboard     Google Sheets dashboard from pasted   .claude/skills/sheets-dashboard/
                     data (lives as a skill, with scripts)
```

To add a tool: create a folder here with a `TOOL.md` explaining when to run it, its inputs and where it saves output. Reference it from the relevant craft guide.
