# Reporting Framework

What gets reported, to whom, how often, and how it's built. Reports drive decisions. A number nobody acts on gets removed.

---

## Weekly: marketing and sales pipeline review (30 minutes)

```
Metric                                    Why
------------------------------------------------------------------------------
New SQLs this week, by channel and play   Is the engine producing real conversations
Tier 1 accounts: engaged / not engaged    Is ABM effort landing
MQL acceptance rate                       Is marketing sending the right people
Campaigns with spend and 0 SQLs in 30d    What to fix or stop this week
Pipeline created (EUR)                    The number leadership cares about
```

## Monthly: leadership report (one page)

```
Metric                                         Compared to
-------------------------------------------------------------
Pipeline created, by channel                   Last month, same month last year, target
Closed won, by original channel                Rolling 6 months
Cost per SQL, by channel                       Rolling 3 months
Win rate from SQL, by channel and play         Rolling 6 months (state deal count)
Self-reported source breakdown                 Rolling 3 months
```

Plus three lines: what worked, what didn't, what we're changing.

## Quarterly: model review

- ICP scoring weights vs actual conversion
- MQL definition vs actual SQL conversion
- Lead scoring points vs actual SQL conversion
- Attribution: do the three views agree?

## How reports are built

1. Export from the CRM and ad platforms (or pull via connectors).
2. Paste or save the data into Claude Code and run the `sheets-dashboard` skill.
3. The skill profiles and cleans the data, calculates every metric with code and formulas (never mental arithmetic), and builds a Google Sheets dashboard where every number is traceable to its formula.
4. Findings, caveats and next steps are written in the Notes tab.

## Automation (target state)

A scheduled weekly job that:
1. Pulls CRM and ad spend data through connectors
2. Applies the same cleaning rules as the last run
3. Rebuilds the dashboard
4. Posts to #corvane-studios in Slack: the headline numbers and any campaign that spent over EUR 1,000 with zero SQLs in 30 days

## Rules for every report

- **Pipeline over volume.** SQLs and pipeline first, leads and MQLs second.
- **Always show the sample size** behind rates.
- **Always state the caveats:** time lag, attribution limits, small numbers.
- **Every report ends with a decision or a question,** never just numbers.
