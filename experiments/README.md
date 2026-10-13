# Experiments

One file per test. Version-controlled, so every decision has a record: what we believed, what we changed, what happened, and what we did about it.

```
experiments/
  README.md              How the loop works (this file)
  _template.md           Copy for every new test
  backlog.md             Ranked list of tests not yet run
  EXP-001-*.md           Finished: shipped, rule updated
  EXP-002-*.md           Results in, ready for readout
  data/                  Raw results, one CSV per experiment
```

---

## The loop

```
priorities.md  ->  backlog.md  ->  EXP file (designed)  ->  launch  ->  data/EXP-xxx.csv
                                                                              |
     rule files (personas, messaging, craft)  <-  pull request  <-  readout  <-+
```

1. **Design** (`experiment-design` skill): pick the top backlog item for the current priorities, write the hypothesis, choose one variable, set the primary metric and guardrails, calculate sample size in code, write variants that all pass the four-pillar audit.
2. **Launch:** variants go into the sending tool (Instantly, HeyReach, LinkedIn Ads) as a paused campaign. A person checks and launches.
3. **Read out** (`experiment-readout` skill): when the planned sample is reached, run `readout.py`. It does the statistics and the checks. Claude interprets.
4. **Decide:** ship, keep control, or follow up with a narrower test.
5. **Learn:** if something ships, the skill opens a pull request that updates the rule it proved (a persona file, MESSAGING.md, a craft guide), citing the experiment. A person reviews and merges. Every future asset uses the learning.

## Rules

- **One variable per test.** Both variants pass the same audit. Only the thing being tested differs.
- **Pipeline metrics, not vanity metrics.** Primary metric is meetings booked or positive replies. Opens and clicks are never primary.
- **Decide the sample size and stop rule before launch.** Never call a test early because it looks good.
- **Guardrails always:** negative reply rate and unsubscribe rate. A worse guardrail blocks shipping.
- **Ship threshold:** at least 95% probability the challenger is better on the primary metric, planned sample reached, no guardrail breached.
- **Small numbers are normal in B2B.** Say so in the readout. Test big differences, not button colours.
- **Segment check before generalising.** If one segment drives the result, the learning applies to that segment only.
- **Every test ends with a learning,** including the ones with no winner.

## IDs and status

`EXP-NNN-short-name.md`. Status: `backlog`, `designed`, `running`, `ready for readout`, `shipped`, `kept control`, `follow-up`.
