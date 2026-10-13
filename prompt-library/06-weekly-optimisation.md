# Weekly Optimisation Run

**Every Monday, 08:00 · Runs as a scheduled Claude Code routine, or paste it manually**

The heartbeat of the system. One run checks performance against priorities, reads out finished tests, spots waste and proposes what to test next.

---

## Prompt

```
Run the weekly optimisation.

1. Performance: pull last week's leads, stages and spend (CRM and ad exports in
   data/weekly/ or via connectors). Run the sheets-dashboard skill. Compare each
   priority in priorities.md with its target and say which are on track, at risk
   or off track, with the number.

2. Waste: list any campaign or variant with spend over EUR 1,000 and zero SQLs in
   the last 30 days. Recommend pause, fix or keep, one line each.

3. Experiments: for each EXP file with status "running", check whether both
   variants have reached planned n. If yes, run the experiment-readout skill.
   If not, report progress and the expected readout date. Never read out early.

4. Insights: if new replies or call notes landed in data/insights/, run the
   audience-insights skill.

5. Next tests: re-score experiments/backlog.md against priorities.md in code.
   Propose the top 2 to design this week, with the priority each serves.

6. Summary: post to #corvane-studios in Slack (or reply here if Slack isn't
   connected) in this format:

   Week of [date]
   Priorities: P1 [on track / at risk / off] (x of y), P2 ..., P3 ..., P4 ...
   Waste: [campaigns flagged, or none]
   Readouts: [EXP-NNN verdict, one line each, or none]
   Learnings merged: [PRs, or none]
   Proposed this week: [EXP ideas]
   Needs a decision: [anything only a person can decide]
```

## Rules

- Statistics and totals come from scripts, never from reading the numbers and estimating.
- Rule changes only happen via the readout skill's pull requests, reviewed by a person.
- If data is missing, say what's missing. Don't fill gaps with assumptions.

## Scheduling it

In Claude Code, set this up as a **routine** on the `studios` repo with a weekly schedule. Each run starts a fresh cloud session in the same environment, so it has the same Google credential and network access as a normal session.
