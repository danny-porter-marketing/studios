# ICP Scoring Model

Every target account is scored on three dimensions: **Fit**, **Intent** and **Access**. The score decides the tier (`abm/account-tiers.md`) and how much effort the account gets.

Scores are calculated in code or a spreadsheet, never by eye.

---

## Dimension 1: Fit (40 points)

How closely the account matches the companies Corvane wins and keeps.

```
Criterion                    Points   Scoring
------------------------------------------------------------------------------
Company size                 10       150 to 1,000: 10 | 50 to 149: 7 | 1,000+: 6 | under 50: 2
Industry                     10       Fintech, B2B SaaS, healthtech: 10 | other software: 5 | non-software: 0
Funding stage                10       Series A to C: 10 | enterprise product team: 8 | seed: 3 | bootstrapped: 4
Stack match                   5       2+ of our core stacks: 5 | 1: 3 | none: 0
Location and overlap          5       UK, EU, Nordics: 5 | US East: 3 | elsewhere: 1
```

Core stacks: JVM (Kotlin, Java), TypeScript and Node, Python, Ruby on Rails, React and React Native, PostgreSQL, AWS, Kubernetes.

## Dimension 2: Intent (40 points)

Evidence they need engineering capacity now. See `scoring/intent-signals.md` for definitions.

```
Signal                                       Points   Scoring
------------------------------------------------------------------------------
Open senior engineering roles                12       5+ roles or any open 90+ days: 12 | 2 to 4: 8 | 1: 4 | 0: 0
Funding raised                               10       Last 6 months: 10 | 6 to 12 months: 5 | older: 0
New engineering leader                        8       New CTO or VP Eng in last 6 months: 8 | 6 to 12 months: 4
Launch, deadline or migration announced       6       Public, dated: 6 | mentioned: 3
Engagement with Corvane                       4       Scoping call request: 4 | pricing or case study page visit: 2
```

## Dimension 3: Access (20 points)

How likely outreach is to reach the right person.

```
Criterion                                    Points   Scoring
------------------------------------------------------------------------------
Decision maker identified                     8       Named CTO or VP Eng: 8 | eng manager only: 4 | none: 0
Warm path                                     6       Mutual connection, past client or partner intro: 6 | event contact: 3 | cold: 0
Active on LinkedIn                            3       Posts monthly: 3 | profile only: 1
Prior contact                                 3       Replied before: 3 | opened: 1 | none: 0
```

---

## Thresholds

```
Score     Tier       Action
------------------------------------------------------------------------
75+       Tier 1     1:1 play. Account file, named contacts, custom assets.
55 to 74  Tier 2     1:few play. Industry-level personalisation, sequence per contact.
35 to 54  Tier 3     1:many. Programmatic ads, newsletter, event invites.
Under 35  Watch      No outreach. Re-score when a new signal appears.
```

## Cadence

- New intent signal: re-score that account immediately.
- Tier 1 and 2: reviewed weekly in pipeline review.
- Everything else: re-scored monthly.

## Review the model

Every quarter, compare the scores of accounts that became opportunities against those that didn't. If a criterion doesn't separate them, reweight it. Use the `sheets-dashboard` skill for the analysis.
