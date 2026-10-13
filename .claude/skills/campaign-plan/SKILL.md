---
name: campaign-plan
description: Turn a business priority into a campaign plan with audience, channels, asset list, personalisation level per tier, embedded experiments, a week-by-week calendar, and a capacity check and pipeline forecast calculated in code. Use when asked to plan a campaign, plan the quarter, build a content calendar, or decide what to run for a goal.
---

# Campaign plan

A plan answers: what are we trying to move, who do we need to reach, through which channels, with what, when, and will it be enough?

## 1. Load
- `priorities.md`: the priority, its target, weight and constraints (weekly volume, budget)
- `campaigns/channel-strategy.md`: which channels serve which audience
- `abm/account-tiers.md` and `abm/icp-scoring.md`: how many accounts per tier, what each tier gets
- `experiments/backlog.md` and finished `experiments/EXP-*.md`: what to test and what's already proven
- `use-cases.md`: current objections and what's working
- `campaigns/calendar.md`: what's already scheduled, to avoid clashes

## 2. Define the campaign
One priority per campaign. Write:
- **Goal:** the priority's metric and target, for example 20 fintech SQLs this quarter
- **Audience:** personas, industries, tiers, and the number of accounts per tier
- **Core message:** one sentence from MESSAGING.md, adapted to this audience
- **Proof:** which approved proof points and case studies apply

## 3. Choose channels and personalisation by tier

| Tier | Personalisation | Channels | Assets |
|---|---|---|---|
| 1 | Account and individual (1:1) | Outbound from Piotr or Marta, multi-threaded | Account file, custom sequence per contact, optional account landing page |
| 2 | Industry and persona (1:few) | Outbound sequence per contact, LinkedIn ads to the account list | Industry sequence template, ad set, industry landing page |
| 3 | Persona (1:many) | Paid social, newsletter, organic LinkedIn, events | Ads, posts, guide or checklist |

Adjust to what `channel-strategy.md` says works for this audience.

## 4. Build the asset list
List every asset with: channel, persona, craft guide, skill that makes it, owner and due week. Mark which assets are produced as a **campaign pack** (one brief, all channels; see the `campaign-pack` skill).

## 5. Embed experiments
Pick 1 or 2 backlog tests that serve this priority and run inside the campaign's volume. Use their sample sizes from the EXP files or `sample_size.py`. Check they fit the volume.

## 6. Capacity check and forecast, in code
Write and run a short script that calculates:
- Contacts or impressions available over the campaign (weekly volume x weeks)
- How they split across tiers and experiments, and whether the experiments fit
- Forecast: contacts x meeting rate x meeting-to-SQL rate, plus other sources (events, partners)
- The forecast against the target at 3 assumptions (pessimistic, base, optimistic)

Label every assumption that isn't from real data. If the pessimistic case misses the target, say so and name the lever that closes the gap (an experiment, more volume, a different channel). A plan that only works in the optimistic case isn't a plan.

## 7. Calendar
Week-by-week table: what launches, what's sent, what posts, when experiments start and read out, review points. Add the campaign's rows to `campaigns/calendar.md`.

## 8. Save
`campaigns/<YYYY-qN-short-name>/plan.md`. Include the script's output.

## Report
Goal and forecast (with the pessimistic case), audience by tier, channel and asset summary, embedded experiments, the 3 biggest risks, and what needs a person's decision.
