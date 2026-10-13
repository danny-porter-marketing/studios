# Funnel Stages

One shared definition of every stage, used by marketing, sales and the CRM. If a stage isn't defined here, it doesn't exist in reporting.

---

```
Stage              Definition                                          Owner       Exit criteria
--------------------------------------------------------------------------------------------------------------
Target account     In ICP, scored, tiered. No engagement yet.          Marketing   Any engagement
Engaged            Someone at the account engaged: reply, event        Marketing   Meets MQL definition
                   conversation, content download, site visit by a
                   known contact
MQL                Meets funnel/mql-definition.md                      Marketing   Sales accepts within 2
                                                                                   working days, or rejects
                                                                                   with a reason
SAL                Sales accepted. Sales has agreed to work it.         Sales       Scoping call booked
SQL                Scoping call held. Real need, timeline under 6      Sales       Proposal requested
                   months, budget owner identified.
Opportunity        Proposal requested or in progress. Value and        Sales       Signed or lost
                   close date set in the CRM.
Closed won         Contract signed.                                    Sales       First engineer starts
Closed lost        Lost, with a reason code.                           Sales       Back to Watch for 6 months
Active client      Engineers working.                                  Delivery    Extension or end
```

---

## Rules

- **Every stage change has a date** in the CRM. Conversion time is calculated from those dates.
- **Lost always has a reason code:** price, timing, chose to hire, chose competitor, no decision, bad fit. "Other" needs a note.
- **Accounts and contacts both carry stage.** A contact can be MQL while the account is still Engaged. The account stage is the highest of its contacts.
- **Recycling:** Closed lost goes to Watch for 6 months, then is re-scored.

## Typical timings (for planning, not targets)

Track these in the reporting dashboard (`revops/reporting-framework.md`) rather than assuming them. Review quarterly.

- MQL to SQL: measured median in days
- SQL to Closed won: measured median in days
- Win rate from SQL: measured per channel and per play
