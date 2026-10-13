# Lead Scoring Model

Contact-level score that sits on top of the account's ICP score. The ICP score says "is this account right". The lead score says "is this person ready".

---

## Profile points (max 40)

```
Attribute                                      Points
-------------------------------------------------------
Title: CTO, VP or Head of Engineering          20
Title: Head of Product, CEO (under 150)        15
Title: Engineering Manager, Tech Lead          10
Title: Engineer, other                          2
Account Tier 1                                 20
Account Tier 2                                 12
Account Tier 3                                  4
```

## Behaviour points (max 60, decay applies)

```
Action                                         Points   Decay
--------------------------------------------------------------
Scoping call request                           60       none (fast track)
Positive reply to outreach                     30       halves after 30 days
Event conversation logged                      25       halves after 30 days
Case study or one-pager download               10       halves after 30 days
Pricing or "how it works" page, 2+ visits      10       halves after 14 days
Webinar attended                               10       halves after 30 days
Newsletter click                                3       halves after 14 days
Blog visit                                      1       halves after 7 days
Unsubscribe                                   -20       none
```

Behaviour points cap at 60. Total score is profile plus behaviour, capped at 100.

## Thresholds

```
60+     MQL candidate (also needs fit and role; see funnel/mql-definition.md)
40-59   Warm: nurture, watch for the next signal
<40     Cold
```

## Why decay

A download from three months ago says little about today. Decay keeps scores honest and stops old activity creating MQLs sales will reject.

## Review

Quarterly, alongside the MQL review. Check which actions actually preceded SQLs and reweight. A point value that doesn't predict anything should go down.
