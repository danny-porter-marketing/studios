# GA4 analysis

## Cleaning

- Rows in: 531
- Exact duplicate rows removed: 2
- Sessions stored as text with commas, converted: 0
- Spam sources removed (100+ sessions, under 5% engaged): ['free-seo-traffic.xyz / referral'] (6,476 sessions)
- '(not set)' landing page sessions: 427 (kept in totals, excluded from page tables)
- Probable tracking breaks (week total under 50% of median): ['2026-08-24']

## By channel

| channel | sessions | engagement_rate | key_events | conversion_rate |
|---|---|---|---|---|
| Organic Search | 15,654 | 61.1% | 193 | 1.2% |
| Direct | 5,343 | 53.5% | 72 | 1.3% |
| Organic Social | 2,759 | 49.7% | 34 | 1.2% |
| Paid Search | 2,326 | 54.9% | 50 | 2.1% |
| Email | 1,290 | 68.9% | 16 | 1.2% |
| Referral | 930 | 66.0% | 9 | 1.0% |

## By landing page

| page | sessions | engagement_rate | key_events | conversion_rate |
|---|---|---|---|---|
| / | 11,591 | 59.4% | 145 | 1.3% |
| /blog/team-extension-vs-outsourcing | 5,498 | 58.8% | 21 | 0.4% |
| /blog/onboarding-docs-that-get-read | 3,517 | 60.1% | 11 | 0.3% |
| /careers | 3,010 | 60.4% | 0 | 0.0% |
| /services/team-extension | 2,141 | 59.2% | 134 | 6.3% |
| /services/ai-integration | 1,167 | 60.0% | 35 | 3.0% |
| /industries/fintech | 951 | 59.2% | 28 | 2.9% |

## Organic search by landing page

| page | sessions | engagement_rate | key_events | conversion_rate |
|---|---|---|---|---|
| / | 6,017 | 61.1% | 72 | 1.2% |
| /blog/team-extension-vs-outsourcing | 3,374 | 60.2% | 10 | 0.3% |
| /blog/onboarding-docs-that-get-read | 2,167 | 61.7% | 7 | 0.3% |
| /careers | 1,855 | 61.9% | 0 | 0.0% |
| /services/team-extension | 1,127 | 61.3% | 67 | 5.9% |
| /services/ai-integration | 610 | 61.6% | 19 | 3.1% |
| /industries/fintech | 504 | 61.3% | 18 | 3.6% |

## Organic trend (tracking-break weeks excluded)

- First 4 weeks average: 1,121 sessions a week; last 4 weeks: 1,468 (+31%)

## Assumptions and limits

- Key events are GA4 conversions (form submissions), not SQLs. Join to the CRM before judging channel value.
- GA4 attributes sessions by its own rules; compare with revops/attribution-model.md before reallocating budget.
- Weeks flagged as tracking breaks are excluded from trends, not from totals. Confirm with whoever owns the tag.