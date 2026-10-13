# SEO action plan: GA4 landing pages, 6 July to 28 September 2026

Source: `raw/ga4_landing_pages.csv` (GA4 landing page export, 13 weeks). Full tables in `ga4_report.md`, `by_channel.csv`, `by_page.csv`, `ga4_clean.csv`. Every number below comes from `seo_analysis.py ga4` or a pandas check run on `ga4_clean.csv`.

**Scope limit:** this is GA4 data only. There is no keyword export, so there are no quick wins, content gaps, cannibalisation checks or extra-click estimates yet. Run `seo_analysis.py keywords` on a Semrush or Search Console export (brand: `corvane`) to fill those in.

## Data problems found and handled

| Problem | Size | What we did |
|---|---|---|
| Spam referral `free-seo-traffic.xyz` | 6,476 sessions, 23 engaged, 0 key events | Removed. It was 18.6% of raw sessions and would have hidden the real trend. Add a GA4 referral exclusion. |
| Exact duplicate rows | 2 | Removed |
| `(not set)` landing page | 427 sessions, 0 engaged | Kept in totals, excluded from page tables. Zero engagement points to sessions with no page_view (consent mode or a tag firing order issue). |
| Probable tracking break, week of 24 August | 472 sessions vs a median week of 2,267; 2 key events | Excluded from trends. Every channel fell together while the spam referral (which does not depend on the site tag) kept arriving at its normal level. That is a tag problem, not a demand problem. Confirm with whoever owns GTM. |

## The channel and page story

- **Organic search is the engine.** 15,654 sessions, 193 key events: more than every other channel combined. Organic sessions grew 31% (first four weeks vs last four, break week excluded).
- **Paid search converts best per session** (2.1% vs 1.0% to 1.3% elsewhere). That is GA4 key events, not SQLs. Join to the CRM before using it for P2 (cost per SQL).
- **Service and industry pages convert; blog posts don't hand visitors on.** Excluding careers and `(not set)`:

| Page | Share of sessions | Share of key events | Key event rate |
|---|---|---|---|
| / | 46.6% | 38.8% | 1.3% |
| /blog/team-extension-vs-outsourcing | 22.1% | 5.6% | 0.4% |
| /blog/onboarding-docs-that-get-read | 14.1% | 2.9% | 0.3% |
| /services/team-extension | 8.6% | 35.8% | 6.3% |
| /services/ai-integration | 4.7% | 9.4% | 3.0% |
| /industries/fintech | 3.8% | 7.5% | 2.9% |

The two blog posts bring 36.3% of marketing sessions and 8.6% of key events. Engagement on them is the same as everywhere else (about 60%), so people read them. They just don't go anywhere next.

- **`/careers`** (3,010 sessions, 0 key events) is job-seeker traffic. Excluded from marketing judgement.
- **A conversion dip from 17 August to 7 September** (0.89% to 1.09% a week, against 1.3% to 1.7% before and after) sits around the tracking break. Check whether the form event was affected too before reading anything into it.

## Top 5 actions

| # | Target page | Action | Why | Priority served |
|---|---|---|---|---|
| 1 | Both blog posts | **Fix conversion:** add in-body and end-of-post links and a CTA to `/services/team-extension` (and `/industries/fintech` from the outsourcing post) | 9,015 sessions in 13 weeks at 0.3% to 0.4%. Biggest gap between traffic and conversion on the site. No new traffic needed. | P1, P2 (more organic conversions lowers blended cost per SQL) |
| 2 | Site-wide (GTM / GA4) | **Fix tracking:** confirm the 24 August break, fix `(not set)` sessions, add the spam referral exclusion | Every later readout depends on clean data. Cheap and fast. | All |
| 3 | `/industries/fintech` | **Optimise and grow:** strongest P1 page, 3.6% organic key event rate, but only 504 organic sessions | Needs keyword data to pick targets: run the keywords mode with the fintech cluster | P1 (40% weight) |
| 4 | `/services/ai-integration` | **Optimise:** 610 organic sessions at 3.1%. Link to it from the homepage and the onboarding blog post | Small page, solid conversion, direct line to P3 | P3 |
| 5 | Key events by channel | **Join to CRM:** match GA4 key events to SQLs per `revops/attribution-model.md` | Paid search looks best on key events. P2 is judged on SQLs, not form fills. | P2 |

Action 1 can run as a before-and-after test with `experiment-design` (blog posts with new links vs a control period). Expect it to be slower and noisier than an email test: about 700 blog sessions a week means weeks, not days, to read out.

## Assumptions

- Key events are GA4 form submissions, not pipeline.
- GA4 attributes sessions by its own last-click-style rules and may sample.
- Spam threshold: 100+ sessions at under 5% engagement. Tracking-break threshold: week total under 50% of the median.
- The 24 August week is excluded from trends but kept in totals.
