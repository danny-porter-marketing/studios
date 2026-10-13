# SEO action plan: Semrush keywords + GA4 landing pages

Sources: `raw/semrush_keywords.csv` (48 rows) and `raw/ga4_landing_pages.csv` (GA4, 6 July to 28 September 2026). Reports: `keywords_report.md`, `ga4_report.md`. Every number below comes from `seo_analysis.py` or a pandas check on its output CSVs.

## Data problems found and handled

**Keywords**
- 3 duplicate keywords: 2 exact (`software house poland`, `how to evaluate llm features`) and 1 case variant (`Team Extension Services`). The lowercase copy had no difficulty score, so de-duplication kept the row that had one (34). Cleaned file: `clean/semrush_keywords.csv`.
- 7 search volumes stored as text with commas, converted to numbers.
- 10 keywords excluded. Brand (4): `corvane`, `corvane reviews`, `corvane careers`, `corvane software house`. These are defended, not targeted. Wrong audience (6): job seekers (`jobs`) and wrong buyers (`cheap`, `freelance`, `wordpress`). The six wrong-audience terms add up to 21,800 searches a month that a CTO or VP Engineering would never make.

**GA4**
- Spam referral `free-seo-traffic.xyz` removed: 6,476 sessions, 18.6% of the raw total.
- 2 exact duplicate rows removed. 427 `(not set)` sessions with zero engagement, kept in totals and left out of page tables.
- Week of 24 August is a probable tracking break (472 sessions against a median week of 2,267, while the spam kept arriving as normal). Excluded from trends. Confirm with whoever owns GTM.

## The story where both datasets agree

Your biggest keyword cluster ranks on the page that doesn't convert.

| Organic landing page | Organic sessions | Key event rate |
|---|---|---|
| /services/team-extension | 1,127 | 5.9% |
| /industries/fintech | 504 | 3.6% |
| /services/ai-integration | 610 | 3.1% |
| / | 6,017 | 1.2% |
| /blog/team-extension-vs-outsourcing | 3,374 | 0.3% |
| /blog/onboarding-docs-that-get-read | 2,167 | 0.3% |

The team extension cluster is split between two URLs (cannibalisation). The commercial head term `team extension` (1,900 searches, position 12) and `team extension company` (590, position 16) rank with the **blog post**. The service page ranks for the other commercial terms. The blog post converts organic visitors at 0.3%. The service page converts them at 5.9%.

## Top 5 actions

Extra clicks are monthly, at position 3, from the script's click-through curve. Extra key events are those clicks multiplied by the organic key event rate of the page that should own the term. Both are rough estimates for ranking the work, not forecasts.

| # | Keyword or cluster | Target page | Action | Extra clicks / mo | Extra key events / mo | Priority |
|---|---|---|---|---|---|---|
| 1 | **Team extension cluster:** `team extension`, `team extension company` | `/services/team-extension` | **Merge intent.** Make the service page own commercial terms (title, H1, copy). Re-target the blog post at the informational terms it should own (`what is team extension`, `staff augmentation vs outsourcing`, `team extension vs staff augmentation`). Link from the blog to the service page with "team extension" as the anchor text. | 249 | 14.8 on the service page vs 0.7 if the blog keeps them | P2 |
| 2 | `dedicated development team` (pos 9, 2,400) and `team extension services` (pos 8) | `/services/team-extension` | **Optimise** the same page in the same pass: add a section that answers the dedicated-team query directly. | 274 | 16.3 | P2 |
| 3 | `fintech software development company` (pos 17, 1,300) | `/industries/fintech` | **Optimise.** Strongest P1 page in GA4 (3.6%), still on page 2. Needs fintech proof from MESSAGING.md and links from the homepage and the blog post. | 130 | 4.6 | P1 (40%) |
| 4 | AI and LLM: `llm integration services` (pos 13) plus content gaps `llm evaluation metrics` (1,600), `llm evaluation framework` (880) | `/services/ai-integration` + **new** guide | **Optimise** the service page; **create** one evaluation guide (craft: blog-article) that links to it. | 48 (page) + 273 (guide) | 1.5 (page) | P3 |
| 5 | Tracking | Site-wide | **Fix** the 24 August break and `(not set)` sessions, add the spam exclusion, then join key events to SQLs (`revops/attribution-model.md`) | n/a | n/a | All |

## Content gaps (new pages, one per cluster)

| Cluster | Gap volume | Fit with Q4 priorities | Decision |
|---|---|---|---|
| AI and LLM | 2,800 | P3 | Create now (action 4) |
| Onboarding (`developer onboarding checklist`, `how to onboard contractors`, `contractor onboarding checklist`) | 2,890 | Weak. Informational, low CPC, and the existing onboarding post converts at 0.3% | Later. Add the checklist to the existing post rather than a new page |
| Software house buyer guides (`how to choose a software house`, `questions to ask a software development company`) | 1,070 | Buyer-stage, links to service pages | Next quarter |
| Healthtech (`fhir integration services`), stack services | 490 | No Q4 priority | Park |

## Defend and long shots

- **Defend:** `software house krakow` (position 3) and `team extension vs staff augmentation` (position 2). Keep both pages fresh during the action 1 changes and don't change the blog post's URL.
- **Long shots, not chased:** `it outsourcing`, `software outsourcing`, `software development company` (55,100 combined volume, difficulty 74 to 81). They are also off-brand: Corvane is the alternative to outsourcing, so it doesn't target the word.

## Assumptions

- Click-through curve is an industry average; Search Console would be better. Search volume and difficulty are Semrush estimates.
- Opportunity uses CPC as a stand-in for commercial value. Key events are GA4 form submissions, not SQLs.
- The key event estimates apply the page's current 13-week organic rate to new clicks. New visitors from commercial terms may convert better than the page average, and visitors from broader terms may convert worse.
- Testing: actions 1 to 3 can run as a before-and-after test with a control group of pages via `experiment-design`. SEO tests are slower and noisier than email tests: expect weeks, not days, before rankings settle.
