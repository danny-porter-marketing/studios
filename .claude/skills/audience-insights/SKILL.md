---
name: audience-insights
description: Turn qualitative audience data (email replies, call notes, objections, survey answers, LinkedIn comments) into counted themes, update use-cases.md, and propose experiments. Use when asked what the audience is saying, to analyse replies or call notes, find objections, or get audience insights.
---

# Audience insights

Numbers say what happened. This says why.

## 1. Collect
Accept a CSV, a paste or an export. Save it to `experiments/data/insights-YYYY-MM-DD.csv` (or `.txt`). Strip personal data that isn't needed: keep role, segment, company size and the text. Drop email addresses and phone numbers.

## 2. Code the themes
1. Read everything once. Propose a theme list (5 to 10 themes) with a one-line definition each.
2. Assign each item to one or more themes, in a new column, in the saved file.
3. **Count with code**, overall and by persona and segment. Never estimate counts.
4. For each theme keep 2 short verbatim examples, anonymised.

## 3. Compare with what we believe
For each theme, check MESSAGING.md (objections), the persona files and `use-cases.md`:
- **Known and handled:** covered already
- **Known, handling is wrong:** what people say contradicts our answer
- **New:** not in the repo

## 4. Update the repo
- Add new objections and observations to `use-cases.md` in its formats. Mark single mentions "(one mention)".
- For each theme that suggests a testable change, write a hypothesis and add it to `experiments/backlog.md`, scored against `priorities.md` in code.
- Don't edit persona or messaging rules directly. Rule changes come from experiments (or a person's explicit decision).

## Report
Theme table (theme, count, share, top persona or segment), the 3 most important insights with a quote each, what changed in `use-cases.md`, and the hypotheses added to the backlog.
