# Attribution Model

How Corvane decides which marketing activity gets credit for pipeline. No model is perfectly right in a B2B sale with 3 to 6 people and a 2 to 4 month cycle. The goal is to make decisions that are directionally right and consistent over time.

---

## Three views, used together

### 1. Self-reported attribution (the most honest)
Every scoping call form and every first sales call asks: **"How did you hear about Corvane?"** (free text). Coded weekly into channels.

Catches what tracking misses: podcasts, word of mouth, a LinkedIn post someone saw on their phone, a recommendation in a private Slack.

### 2. Touch-based attribution (the most measurable)
**W-shaped model** on opportunities:

```
Touch                                   Credit
-----------------------------------------------
First touch (first known engagement)    30%
MQL-creating touch                      30%
Opportunity-creating touch              30%
All other touches, split evenly         10%
```

Calculated at **account level**, not contact level, because the buying group is several people. Every touch from every contact at the account counts.

### 3. Incrementality tests (the most reliable, used sparingly)
For big decisions (scale a channel, cut a channel) run a holdout test:
- Split comparable target accounts into two groups
- Run the activity for one group only for 6 to 8 weeks
- Compare engagement, meetings and pipeline per account between the groups

## How to decide

- **When the three views agree:** act with confidence.
- **When self-reported says a channel matters and tracking doesn't see it:** trust self-reported for the direction, keep spending, and look for better tracking.
- **When tracking credits a channel but no one ever mentions it:** be sceptical. Check with an incrementality test before scaling.

## What we report

- Pipeline and closed won by channel, using the W-shaped model
- Self-reported source breakdown
- Cost per SQL and cost per opportunity by channel and campaign
- Never MQL volume alone. It rewards channels that produce volume that doesn't convert.

## Known limits

- Small numbers: with a few deals a quarter per channel, results move a lot. Report rolling 6-month figures and say how many deals sit behind each number.
- Dark social and word of mouth will always be under-tracked.
- Time lag: leads from the last 60 days haven't had time to close. Exclude or flag them in win-rate figures.
