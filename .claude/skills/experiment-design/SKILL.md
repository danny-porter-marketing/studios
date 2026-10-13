---
name: experiment-design
description: Design a marketing A/B test tied to a business priority, with a hypothesis, one variable, pipeline metric, guardrails, sample size calculated in code, and audited variants. Use when asked to design a test, run an experiment, A/B test something, decide what to test next, or optimise a campaign.
---

# Experiment design

## 1. Load
- `priorities.md`: the quarter's priorities, weights and constraints (volume per week)
- `experiments/backlog.md` and every `experiments/EXP-*.md`: what's queued and what's already been learned
- `use-cases.md`: objections and observations that suggest hypotheses
- `experiments/_template.md`

## 2. Pick the test
If the operator names a test, use it. Otherwise:
1. Take the top of `backlog.md`. If priorities changed since it was scored, re-score with code first (weight x impact x confidence / effort) and show the new ranking.
2. Check no finished experiment already answers it.
3. Say which priority it serves and why it's worth the volume.

## 3. Write the hypothesis
"If we [change one thing] for [audience], [primary metric] will [move] because [evidence]." The "because" must cite something: use-cases.md, a past experiment, or call data. No evidence means a weak test; say so.

## 4. Lock the design
- **One variable.** Name it. List what stays identical.
- **Primary metric:** a pipeline metric (meeting_booked, positive_reply, SQL). Never opens or clicks.
- **Secondary metrics:** to explain the result (replied, positive_reply).
- **Guardrails:** negative_reply and unsubscribed, always.
- **Baseline:** from past data. If none exists, say so and use a conservative estimate.

## 5. Size it in code
```
python <skill>/scripts/sample_size.py --baseline <rate> --mde <points> --weekly-volume <n>
```
Use the weekly volume from `priorities.md`. If it needs more than 8 weeks, don't run it as designed. Offer one of: a bigger difference between variants, a higher-volume metric, or pooling segments. Plan about 10% above the calculated n as a buffer.

## 6. Write the variants
Use the normal layer stack (persona, voice, craft guide) and the matching skill (`outbound-sequence`, `linkedin-post`, `landing-page`). **Both variants must pass the four-pillar audit**, and they must be identical except for the one variable. Show a line-by-line diff so the operator can see only the variable changes.

## 7. Save
Copy `_template.md` to `experiments/EXP-NNN-short-name.md` (next free number), fill every section up to Variants, set status `designed`, and remove it from the backlog. Add the CRM campaign name per `revops/crm-conventions.md`, with the variant as a suffix (`..._A`, `..._B`).

## 8. Launch handoff
Variants go into the sending tool as a **paused** campaign with a random 50/50 split. A person reviews and launches. Never launch automatically.

## Report
Hypothesis, design table, sample size and duration, both variants with scores, and the file path.
