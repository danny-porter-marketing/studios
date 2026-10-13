# Campaign plan: Fintech CTOs, Q4 2026

> Worked example from the `campaign-plan` skill. Corvane and all accounts are fictional.

**Priority:** P1, more fintech pipeline in UK, DACH, Nordics (weight 40%)
**Goal:** 20 SQLs from fintech accounts, 5 October to 27 December 2026 (12 weeks)
**Owner:** Marketing, with Piotr (CTO) as sender and speaker

---

## Core message

"Your launch date is fixed and your backend roles are open. Senior engineers in your codebase from week two."
From MESSAGING.md (one-liner and message 2), adapted to fintech's external deadlines (`industries/fintech.md`).

**Proof:** Ledgerline (3 to 11 engineers in 5 months, card issuing in 3 markets); median 9 working days to first merged PR; 82% of clients extend after 6 months.

---

## Audience by tier

| Tier | Accounts | Contacts | Personalisation | Channels |
|---|---|---|---|---|
| 1 | 15 | 45 (3 per account: CTO, VP Eng, Head of Product) | 1:1, account signal and role in deal | Outbound from Piotr, multi-threaded; dinner invite |
| 2 | 60 | 120 (2 per account) | Industry and persona | Outbound sequence; LinkedIn ads to account list |
| 3 | All other fintech in ICP | about 1,515 contacts over the quarter | Persona | Outbound (EXP-003 runs here), LinkedIn document ads, Piotr's posts, newsletter |

---

## Assets

| Asset | Channel | Persona | Made by | Due |
|---|---|---|---|---|
| **Campaign pack: "Launch date fixed, roles open"** | All | CTO | `campaign-pack` | Week 1 |
| (in pack) Outbound sequence template, fintech | Email + LinkedIn | CTO | `outbound-sequence` | Week 1 |
| (in pack) Landing page, fintech CTOs | Web | CTO | `landing-page` | Week 1 |
| (in pack) LinkedIn ad set, 3 variants | Paid social | CTO, VP Eng | craft: linkedin-ad | Week 1 |
| (in pack) Piotr LinkedIn post | Organic | CTO | `linkedin-post` | Week 1 |
| (in pack) One-pager, fintech Team Extension | Sales | CTO, procurement | craft: one-pager | Week 1 |
| Tier 1 account files (15) | Research | n/a | `account-research` (batch) | Weeks 1 to 2 |
| Tier 1 custom sequences (45 contacts) | Email + LinkedIn | CTO, VP Eng, HoP | `outbound-sequence` (batch) | Weeks 2 to 3 |
| Export to Instantly and HeyReach, paused | Tools | n/a | `outbound-export` | Weeks 2 to 3 |
| Ledgerline full case study | Web, sales | CTO | `case-study` | Week 3 |
| Fintech engineering dinner playbook | Event | CTO | craft: event-playbook | Week 4 |
| Piotr posts, weekly (8 more) | Organic | CTO, VP Eng | `linkedin-post` | Weekly |

---

## Embedded experiments

| Test | Runs on | Sample needed | Fits? |
|---|---|---|---|
| EXP-003: proof-first vs signal-first Touch 1, fintech CTOs | Tier 3 outbound | 970 (485 per variant) | Yes: about 1,515 Tier 3 contacts available |
| EXP-004: checklist document ad vs case study ad (VP Eng) | Tier 2 and 3 paid | Sized at design | Check at week 1 |

EXP-003 matters for the forecast: if proof-first lifts the fintech meeting rate the way EXP-002 suggested, it closes the gap in the pessimistic case.

---

## Capacity check and forecast

Calculated in code. Assumptions marked (A) aren't from Corvane data yet.

```
Fintech contacts available: 140 per week x 12 weeks = 1,680
  Tier 1: 45   Tier 2: 120   Tier 3: 1,515   EXP-003 needs 970: fits

Meeting rate 2.5% (priorities.md baseline) -> 42 meetings
Plus events 2 SQLs (A), partner referrals 3 SQLs (A)

Meeting-to-SQL (A)   Outbound SQLs   Total SQLs   vs target 20
30% (pessimistic)    12.6            17.6         miss by 2.4
40% (base)           16.8            21.8         hit
50% (optimistic)     21.0            26.0         hit
```

**The pessimistic case misses.** Levers, in order:
1. EXP-003: a proof-first win in fintech raises the meeting rate on the biggest block of volume.
2. Partners: ask the 3 happiest fintech clients for one intro each (week 2).
3. If at week 6 the run-rate projects below 18 SQLs, move 20% of the Tier 3 paid budget to Tier 2 account-list ads.

---

## Calendar

| Week | Starts | Launch and send | Content | Experiments and reviews |
|---|---|---|---|---|
| 1 (5 Oct) | Campaign pack built and audited | Landing page live | Piotr post 1 | EXP-003 designed; EXP-004 sized |
| 2 | Tier 1 research (batch) | Tier 2 sequences start | Piotr post 2 | EXP-003 launched (paused, then approved) |
| 3 | Tier 1 sequences written and exported | Tier 1 outbound starts; ads live | Ledgerline case study; post 3 | Weekly optimisation run |
| 4 | Dinner invites | | Post 4 | |
| 5 | | | Post 5 | |
| 6 | | | Post 6 | **Mid-campaign review:** run-rate vs 20 SQLs, apply lever 3 if needed |
| 7 | Dinner (Warsaw fintech meetup week) | Follow-ups within 48 hours | Post 7 | |
| 8 | | | Post 8 | |
| 9 | | | Post 9 | **EXP-003 readout** (planned n reached at about week 9) |
| 10 | Roll out EXP-003 winner to all fintech outbound | | | Rule change PR if shipped |
| 11 to 12 | | Final pushes to Tier 1 | | **Campaign readout:** SQLs vs target, learnings to use-cases.md |

---

## Risks

1. Meeting-to-SQL rate is an assumption. Measure it from week 3 and re-run the forecast.
2. Tier 1 needs Piotr's time (about 2 hours a week for replies and calls). Confirm before launch.
3. A layoff or hiring freeze at a target account pauses its outreach (`scoring/intent-signals.md`).

## Needs a decision

- Approve the dinner budget (week 4 invites).
- Confirm Piotr's availability for Tier 1.
