# Intent Signals

Signals that an account needs engineering capacity now. They drive the Intent dimension of the ICP score and decide which entry play to run.

---

## Signal library

```
Signal                    Where to find it                       Strength   Freshness window
---------------------------------------------------------------------------------------------------
Senior eng roles open     Careers page, LinkedIn jobs            High       Live; stronger if 90+ days open
Funding round             Press, Crunchbase, LinkedIn            High       6 months
New CTO or VP Eng         LinkedIn, press                        High       Weeks 4 to 26 in role
Public dated deadline     Press, regulator notices, investor     High       Until the date
                          updates, product announcements
Market expansion          Press, new country job ads             Medium     6 months
Migration mentioned       Eng blog, job ads ("help us move off   Medium     6 months
                          our monolith")
AI initiative             Press, job ads, CEO posts              Medium     3 months
Eng leader posting about  LinkedIn                               Medium     1 month
  hiring pain
Layoffs                   Press                                  Negative   Pause outreach 3 months
Hiring freeze announced   Press                                  Negative   Pause outreach 3 months
```

## First-party signals (from our own channels)

```
Signal                                  Strength
-------------------------------------------------
Scoping call request                    Very high
Reply to outreach                       High
Repeat visits to "how it works" page    Medium
Case study download                     Medium
Event conversation                      Medium
Newsletter engagement                   Low
```

## Rules

- **Combine signals.** Funding plus open roles plus a new leader is much stronger than any one of them. The ICP score handles this.
- **Use the signal in the message.** The strongest signal is the opening line of Touch 1 (see `craft-guidelines/outbound-sequence.md`).
- **Respect negative signals.** Never write to a company in the month it announced layoffs.
- **Log the source.** Every signal in an account file has a date and a link.
