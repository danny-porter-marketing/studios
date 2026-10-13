# EXP-002: CTO Touch 1, proof-first vs signal-first

> Fictional experiment for demonstration. Data: `experiments/data/EXP-002-results.csv`.

**Status:** ready for readout
**Priority served:** P1 (fintech pipeline), P4 (outbound meeting rate)
**Owner:** Marketing
**Channel:** Email, Touch 1 of a 4-touch sequence
**Dates:** 2026-09-07 to 2026-10-09

---

## Hypothesis

If Touch 1 to CTOs **opens with a relevant proof story** instead of **opening with their buying signal**, the meeting rate will go up, because CTOs trust evidence over observations about their own company, and the signal opener may read as surveillance (use-cases.md: CTOs respond to specifics and evidence).

Counter-hypothesis: the signal opener is more personal and will win on replies.

## Design

| | Control (A) | Challenger (B) |
|---|---|---|
| The one variable | Opens with the account's signal ("You've had two senior backend roles open since June") | Opens with a proof story ("Ledgerline went from 3 to 11 engineers in 5 months and launched in 3 markets") |
| Everything else | Same audience, sender (Piotr), CTA, follow-ups, send times. Both mention the signal by the end. | Same |

- **Audience:** CTOs, Tier 1 and 2, fintech, B2B SaaS, healthtech
- **Assignment:** random 50/50 by contact
- **Primary metric:** `meeting_booked`
- **Secondary:** `replied`, `positive_reply`
- **Guardrails:** `negative_reply`, `unsubscribed`
- **Baseline:** 2.5% meeting rate (CTO Touch 1, Q2 to Q3)
- **Smallest lift worth detecting:** +3.5 points
- **Sample size:** 521 per variant from `sample_size.py`; planned 580 for buffer
- **Expected duration:** about 4 weeks at 300 per week
- **Stop rule:** read out when both variants pass 580

## Variants

Both passed the four-pillar audit (A 93, B 92).

### A (control, signal-first)
> Subject: backend hiring
>
> You've had two senior backend roles open since June. That usually means the roadmap is waiting on them. We put senior engineers into teams like yours, working in your repo, and the median time to first merged PR is 9 working days. Worth comparing notes on how the first two weeks work? Piotr

### B (challenger, proof-first)
> Subject: 3 to 11 engineers
>
> Ledgerline went from 3 backend engineers to 11 in five months and launched card issuing in three markets. Their platform lead kept the architecture; we added the capacity. I noticed you've had two senior backend roles open since June, so it might be relevant. Worth comparing notes on how the first two weeks work? Piotr

## Result

*Not read out yet. Run:*

```
python .claude/skills/experiment-readout/scripts/readout.py experiments/data/EXP-002-results.csv \
  --primary meeting_booked --secondary replied positive_reply \
  --guardrails negative_reply unsubscribed --segment segment --planned-n 580
```

## Decision

## Learning

## Rule change
