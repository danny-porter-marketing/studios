# CRM Conventions

Rules for how data goes into the CRM (HubSpot or Salesforce). Bad inputs make every report wrong, so these are not optional.

---

## Naming

```
Object         Format                                    Example
-----------------------------------------------------------------------------------------
Campaign       YYYY-MM_channel_audience_offer            2026-10_email_scaleup-cto_scoping
Deal           Account - Service - Start month           Halvard Pay - Team Extension - 2027-01
UTM campaign   same as campaign name                     2026-10_linkedin_vpeng_checklist
UTM source     platform, lower case                      linkedin, google, newsletter, event
UTM medium     paid, organic, email, referral, event     paid
```

## Required fields

**Account:** industry, employees, funding stage, ICP score, tier, entry play, owner.
**Contact:** title, persona (one of the six), lead score, lifecycle stage, source (original), self-reported source.
**Deal:** service, value, expected close date, stage, primary campaign, lost reason (if lost).

A record missing required fields can't move to the next stage. This is enforced by required properties in the CRM.

## Picklists, not free text

Persona, industry, service, funding stage, tier, lost reason and channel are picklists. Free text in those fields breaks reports. Example: "LinkedIn", "linkedin ads" and "LI" are three different channels to a report, one channel to a human.

## Stage dates

Every lifecycle and deal stage change stamps a date property automatically. Conversion times come from these, never from memory.

## Hygiene

- **Weekly:** merge duplicates, check MQLs missing a persona or tier.
- **Monthly:** check campaign names against the format, fix UTMs.
- **Quarterly:** archive contacts with no activity in 18 months, review picklist values.

## Ownership

Marketing owns campaigns, lead scoring and lifecycle stages up to MQL. Sales owns everything from SAL. RevOps (or marketing, until there is a RevOps person) owns the field definitions and this file.
