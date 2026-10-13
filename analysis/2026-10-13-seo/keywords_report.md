# Keyword analysis

## Cleaning

- Rows in: 45
- Duplicates removed (case-insensitive): 0
- Volume stored as text with commas, converted: 6
- Missing difficulty: 1 (treated as 50, flagged)
- Excluded: 10 ({'brand': 4, 'off-target audience': 6})

## Buckets

| bucket | keywords | volume | opportunity |
|---|---|---|---|
| Quick win | 13 | 13,170 | 11,756 |
| Content gap | 12 | 8,120 | 4,071 |
| Defend | 2 | 850 | 1,034 |
| Later | 5 | 2,580 | 2,318 |
| Long shot | 3 | 55,100 | 0 |

Long shots (difficulty 70+) score zero: it outsourcing, software development company, software outsourcing. Combined volume 55,100, but not realistic to win soon.

## Top quick wins

| keyword | intent | position | volume | difficulty | cpc | extra_clicks | opportunity | url |
|---|---|---|---|---|---|---|---|---|
| dedicated development team | commercial | 9 | 2,400 | 55 | €19.80 | 204.0 | 1,818 | /services/team-extension |
| fintech software development company | commercial | 17 | 1,300 | 46 | €24.10 | 130.0 | 1,692 | /industries/fintech |
| team extension | commercial | 12 | 1,900 | 39 | €14.30 | 190.0 | 1,657 | /blog/team-extension-vs-outsourcing |
| software house poland | commercial | 14 | 1,600 | 48 | €15.90 | 160.0 | 1,323 | / |
| nearshore software development poland | commercial | 11 | 720 | 41 | €22.40 | 72.0 | 952 | /services/team-extension |
| team extension services | commercial | 8 | 880 | 34 | €18.50 | 70.4 | 860 | /services/team-extension |
| llm integration services | commercial | 13 | 480 | 31 | €21.70 | 48.0 | 719 | /services/ai-integration |
| team extension company | commercial | 16 | 590 | 37 | €17.90 | 59.0 | 665 | /blog/team-extension-vs-outsourcing |
| hire kotlin developers | transactional | 19 | 720 | 47 | €15.10 | 72.0 | 576 | /services/team-extension |
| kotlin development company | commercial | 12 | 390 | 27 | €16.20 | 39.0 | 461 | /services/team-extension |

## Top content gaps

| keyword | intent | position | volume | difficulty | cpc | extra_clicks | opportunity | url |
|---|---|---|---|---|---|---|---|---|
| llm evaluation metrics | informational | - | 1,600 | 29 | €6.30 | 176.0 | 787 |  |
| llm evaluation framework | informational | - | 880 | 24 | €7.90 | 96.8 | 581 |  |
| postgresql consulting | commercial | - | 320 | 35 | €17.50 | 35.2 | 400 |  |
| developer onboarding checklist | informational | - | 1,300 | 21 | €3.40 | 143.0 | 384 |  |
| fhir integration services | commercial | - | 170 | 25 | €26.40 | 18.7 | 370 |  |
| how to choose a software house | informational | - | 590 | 22 | €6.70 | 64.9 | 339 |  |
| how to onboard contractors | informational | - | 1,000 | 18 | €3.10 | 110.0 | 280 |  |
| questions to ask a software development company | informational | - | 480 | 17 | €5.90 | 52.8 | 259 |  |
| cost of hiring senior developer europe | informational | - | 390 | 23 | €5.60 | 42.9 | 185 |  |
| how to scale engineering team fast | informational | - | 480 | 19 | €4.10 | 52.8 | 175 |  |

## Clusters

| cluster | keywords | volume | extra_clicks | opportunity | avg_kd |
|---|---|---|---|---|---|
| team extension | 12 | 11,050 | 1,035.0 | 8,609 | 35 |
| software house | 5 | 25,460 | 2,820.0 | 2,752 | 38 |
| ai and llm | 5 | 3,490 | 378.5 | 2,547 | 26 |
| fintech | 1 | 1,300 | 130.0 | 1,692 | 46 |
| healthtech | 2 | 890 | 97.9 | 1,315 | 34 |
| stack services | 3 | 970 | 106.7 | 1,084 | 39 |
| onboarding | 3 | 2,890 | 317.9 | 820 | 18 |
| scaling engineering | 2 | 870 | 95.7 | 360 | 21 |
| outsourcing head terms | 2 | 32,900 | 3,619.0 | 0 | 78 |

## Possible cannibalisation (more than one URL ranking in a cluster)

- **team extension**: `/blog/team-extension-vs-outsourcing` (5 keywords); `/services/team-extension` (6 keywords)

## Assumptions

- Clicks use an average position click-through curve; real CTR depends on SERP features. Search Console data beats this.
- Opportunity uses CPC as a proxy for commercial value. It ranks keywords; it isn't a revenue forecast.
- Search volume is a tool estimate, not measured traffic.