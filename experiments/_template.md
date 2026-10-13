# EXP-NNN: [Short name]

**Status:** designed
**Priority served:** [P1 to P4 from priorities.md]
**Owner:** [name]
**Channel:** [email / LinkedIn / paid social / landing page]
**Dates:** [launch] to [planned end]

---

## Hypothesis

If we [change one thing] for [audience], then [primary metric] will [go up / down] because [reason, ideally from use-cases.md or a past experiment].

## Design

| | Control (A) | Challenger (B) |
|---|---|---|
| The one variable | | |
| Everything else | Identical: same audience, timing, sender, sequence length | |

- **Audience:** [persona, segment, tier]
- **Assignment:** random, 50/50, by contact
- **Primary metric:** [e.g. meeting_booked per contact sent]
- **Secondary metrics:** [e.g. replied, positive_reply]
- **Guardrails:** negative_reply, unsubscribed
- **Baseline:** [current rate, source]
- **Smallest lift worth detecting:** [e.g. +3.5 points]
- **Sample size:** [n per variant, from sample_size.py] (planned [n with buffer])
- **Expected duration:** [weeks at current volume]
- **Stop rule:** read out when both variants reach planned n. No peeking decisions.

## Variants

Both pass the four-pillar audit. Scores: A [x]/100, B [x]/100.

### A
[copy]

### B
[copy]

## Result

[Paste the readout table and checks from readout.py]

## Decision

[Ship B / keep A / follow-up test] because [reason in one or two sentences].

## Learning

[One sentence that would change how we write or target in future. Which rule file it updates, if any.]

## Rule change

[Link to the pull request, or "none".]
