# Skills (Layer 7)

Reusable workflows Claude Code loads when a request matches. Each skill is a folder with a `SKILL.md` (the instructions) and any scripts it needs.

| Skill | What it does |
|---|---|
| landing-page | Full layer stack for a landing page, audit, then branded HTML |
| outbound-sequence | Signal-based, account-personalised 4-touch sequences |
| linkedin-post | Posts and carousels in Marta's or Piotr's voice |
| case-study | Client stories from approved proof only, with a fact table |
| copy-editing | Two-pass edit that strips AI patterns and rewrites in the brand voice |
| account-research | Public-signal research, ICP score, tier, entry play, saved account file |
| sheets-dashboard | Pasted data in, cleaned Google Sheets dashboard and HTML report out, every number a live formula |
| experiment-design | Priority in, sized A/B test with audited, one-variable variants out |
| experiment-readout | Results in, statistics in code, verdict, and a rule-change pull request out |
| audience-insights | Replies and call notes in, counted themes, use-cases.md updates and new hypotheses out |

To add a skill: create `.claude/skills/<name>/SKILL.md` with `name` and `description` in the frontmatter. The description decides when it loads, so say what it does and when to use it.
