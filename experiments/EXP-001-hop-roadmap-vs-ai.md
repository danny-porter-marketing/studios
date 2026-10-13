# EXP-001: Head of Product opener, roadmap-led vs AI-led

> Fictional experiment for demonstration. Data: `experiments/data/EXP-001-results.csv`.

**Status:** shipped
**Priority served:** P4 (outbound meeting rate), P3 (AI Integration demand)
**Owner:** Marketing
**Channel:** Email, Touch 1 of a 4-touch sequence
**Dates:** 2026-08-03 to 2026-09-04

---

## Hypothesis

If we open Touch 1 to Heads of Product with **roadmap delivery** instead of **AI Integration**, the meeting rate will go up, because Heads of Product who replied to AI-led emails asked about the roadmap problem, not the AI (use-cases.md, August).

## Design

| | Control (A) | Challenger (B) |
|---|---|---|
| The one variable | Opens with AI Integration ("Your board wants an AI feature on the roadmap") | Opens with roadmap delivery ("Two of your Q3 roadmap items are still waiting on engineering") |
| Everything else | Same audience, sender (Marta), send times, follow-up touches, CTA | Same |

- **Audience:** Heads of Product, Tier 1 and 2 accounts, fintech, B2B SaaS, healthtech
- **Assignment:** random 50/50 by contact
- **Primary metric:** `meeting_booked`
- **Secondary:** `replied`, `positive_reply`
- **Guardrails:** `negative_reply`, `unsubscribed`
- **Baseline:** 2.0% meeting rate (previous Head of Product sends)
- **Smallest lift worth detecting:** +4.5 points (we only change our approach for a large effect)
- **Sample size:** 315 per variant from `sample_size.py`; planned 400 for buffer
- **Expected duration:** about 4 weeks at 200 per week
- **Stop rule:** read out when both variants pass 400

## Variants

Both passed the four-pillar audit (A 92, B 94).

### A (control)
> Subject: ai on the roadmap
>
> Your board wants an AI feature on next year's roadmap, and nobody on the team has shipped one yet. We add LLM features to existing products, starting with an evaluation suite so you know it works before customers do. Worth 20 minutes? Marta

### B (challenger)
> Subject: q3 roadmap
>
> Two of your Q3 roadmap items are still waiting on engineering capacity. We put senior engineers into product teams like yours, and they ship from week two. Worth 20 minutes to see if it fits? Marta

## Result

Readout from `readout.py`, 2026-09-05:

| Metric | Role | Control | Challenger | Lift | 95% interval | p-value | P(challenger better) |
|---|---|---|---|---|---|---|---|
| meeting_booked | primary | 1.7% (7) | 4.7% (19) | +3.0 pts (176% rel.) | +0.6 pts to +5.4 pts | 0.015 | 99.2% |
| replied | secondary | 7.5% (31) | 8.4% (34) | +0.9 pts (12% rel.) | -2.8 pts to +4.6 pts | 0.646 | 67.8% |
| positive_reply | secondary | 2.2% (9) | 5.4% (22) | +3.2 pts (149% rel.) | +0.6 pts to +5.9 pts | 0.015 | 99.2% |
| negative_reply | guardrail | 2.4% (10) | 0.7% (3) | -1.7 pts (-69% rel.) | -3.4 pts to +0.0 pts | 0.054 | 3.0% |
| unsubscribed | guardrail | 0.5% (2) | 0.5% (2) | +0.0 pts (2% rel.) | -0.9 pts to +1.0 pts | 0.986 | 50.8% |

- Sample ratio OK (p = 0.807). Planned n reached. No guardrail breached.
- Small numbers: control had 7 meetings. Treat the size of the lift as directional; the direction is clear.
- All three segments moved the same way. Fintech accounts for 58% of the gain, below the 60% warning line.

## Decision

**Ship B.** 99% probability the roadmap-led opener books more meetings, consistent across segments, and fewer negative replies. Reply rate barely moved: the difference is in the *quality* of replies, which is exactly why reply rate is never the primary metric.

## Learning

For Heads of Product, lead with roadmap delivery. Mention AI second, if at all.

## Rule change

`messaging-guidelines/personas/head-of-product.md`, "How they buy" section: the observation becomes a **Proven rule (EXP-001)**. Pull request: [#1 learning: EXP-001 Heads of Product respond to roadmap delivery, not AI](https://github.com/danny-porter-marketing/studios/pull/1).
