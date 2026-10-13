# Payhawk

> Real company, researched from public sources on 2026-10-13. Unlike the fictional Corvane material in this repo, these facts are about a real business: keep them sourced and keep them current.

**Tier:** 2   **ICP score:** 58 (Fit 40/40 · Intent 10/40 · Access 8/20)
**Entry play:** Play 4, The deadline play (Nordic and Polish market launches). Play 1 as backup if open-role age is verified.
**Owner:** Sales team   **Last updated:** 2026-10-13

## Snapshot
- What they do: Spend management platform. Corporate cards, expenses, payables and accounts in one product, now rebuilt around AI agents (Financial Controller Agent, agentic playbooks, an MCP server for querying spend from an AI assistant). [S5, S8, S9]
- Industry: Fintech (spend management, card issuing, EU e-money licence). [S11, S12]
- Employees: about 470 to 500, third-party estimates only. Revelio: ~485 (Mar 2026). LeadIQ: ~472 (Aug 2026). Latka: 501. [S13, S14, S15]
- Funding: Series B, last closed March 2022 ($100m extension, total Series B $215m, $1bn valuation; QED, Earlybird, Greenoaks among investors). Bloomberg reported early talks in January 2026 to raise $100m+ at ~$2bn. No close found. [S1, S2, S3]
- Revenue: passed $100m ARR, announced 2026-07-08. Company target: $1bn ARR by 2030. [S4, S11]
- HQ and engineering locations: Engineering is in Sofia (all live engineering postings are Sofia; a recruiting page says the product and engineering team is entirely in Bulgaria). Other offices include London, Berlin, Barcelona, Paris, Amsterdam, Vilnius, and from 2026-09-30 Stockholm and Warsaw. Warsaw is a sales office (4-person team planned). [S6, S10, S11, S16]
- Stack: TypeScript and Node.js, React and React Native, PostgreSQL, Kafka, Kubernetes and Docker on Google Cloud. Postings say engineers should be "technology agnostic" and mention LLM-based features. [S6, S7]
- Engineering org: ~70+ full-stack engineers in a 2024 interview. Engineering Leadership Team of CTO, Chief of Staff and Engineering Directors, each Director owning a product domain. [S17]

## Signals
| Signal | Detail | Date | Source |
|---|---|---|---|
| Market expansion, dated | Stockholm opened as Nordic hub. SEK accounts, SEK cards and Swedish IBANs to launch in Q4 2026. | 2026-09-30 | S10, S11 |
| Market expansion | Warsaw opened, Poland made its own region. Planned: PLN accounts and cards, Polish IBANs, KSeF e-invoicing integration, local accounting software links. No date given. | 2026-09-30 | S11, S12 |
| Milestone | $100m ARR. ARR per FTE up 75% to ~$238k. Sales team ~10% smaller. Credits a 24-month "AI-native rebuild". | 2026-07-08 | S4 |
| Product launches | Financial Controller Agent (Jul). Summer '26 edition (Jun). Fall '26 edition: agentic playbooks, Teams integration, Payhawk MCP (Sep 15). | 2026-06 to 2026-09 | S5, S8, S9 |
| Funding talks | Bloomberg: early talks to raise $100m+ at ~$2bn. Not confirmed closed. | 2026-01-07 | S2, S3 |
| Open engineering roles | 4 engineering roles on Greenhouse, all Sofia: Senior Software Engineer, Software Engineer, Security Engineer, Junior Security Engineer. Only 1 is senior. No posting dates visible. Low requisition ID on the senior role (4000039101) suggests an evergreen posting. | 2026-10 (snapshot) | S6, S18 |
| Hiring slowdown (soft negative) | Revelio estimate: 14 new roles a month in 2026, down from 26 in 2025. 51 postings in 2026, down 25.6%. Engineering headcount up slightly. | 2026 | S13 |
| New engineering leader | None found. Co-founder Boyko Karadzhov is still CTO. | n/a | S17, S19 |
| Layoffs | None found in press. The company describes itself as "leaner" and reports a ~10% smaller sales team, which reads as attrition or reallocation, not an announced cut. | n/a | S4, S13 |

## Why now
Payhawk committed publicly on 2026-09-30 to launch SEK accounts and cards in Q4 and to build PLN accounts, Polish IBANs and KSeF integration with no date. Two new-currency launches in one quarter land on a Sofia-only engineering team whose public story is doing more with fewer people.

**Caution:** the dated item (Q4 SEK) is probably already built by mid-October, and their own narrative argues against adding people. This is a Tier 2 account, not a Tier 1 chase.

## Buying group
| Name | Title | Role in deal | LinkedIn | Last touch | Status |
|---|---|---|---|---|---|
| Boyko Karadzhov | Co-founder and CTO | Decision maker, first thread | not checked | none | Not contacted |
| Elena Kiranova | Director of Engineering, Spend Management | Evaluator, domain owner (cards and accounts likely here, unverified) | not checked | none | Not contacted |
| Diyan Bogdanov | Director of Engineering, Expense Automation | Evaluator, second domain thread | not checked | none | Not contacted |
| Hristo Borisov | Co-founder and CEO | Economic sponsor, not first contact (company is well over 150 people) | not checked | none | Not contacted |
| Head of Product | not found | Pain thread for the deadline play | n/a | n/a | Identify |
| Procurement or vendor manager | not found | Late stage | n/a | n/a | Identify |

Sources: Karadzhov [S17, S19, S20]; Kiranova [S16]; Bogdanov [S21]; Borisov [S22]. Director titles come from company pages that may be dated: confirm before writing.

## Angle
- Problem we think they have: two new-currency launches (SEK now, PLN next, plus KSeF) competing for the same Sofia team that owns the AI roadmap. Localisation work (new rails, IBANs, e-invoicing, accounting integrations) is the kind of work that slips behind headline AI features.
- Service that fits: Team Extension, 2 to 3 senior TypeScript and Node engineers embedded in the domain team that owns market launches. Product Delivery if they want a squad to own the Polish launch end to end.
- Proof to use: Ledgerline (3 to 11 engineers in 5 months, card issuing in 3 markets). It's the closest approved match: card issuing across markets.
- Hook from their own words: Karadzhov's interview on being "a good host for other engineers" and keeping codebases open for collaborators [S17]. That's the Team Extension model in his language.
- Objections we expect:
  - "We're AI-native and getting leaner. We don't add people." Answer: frame it as capacity for the launch dates, not headcount. Weekly shipped-work reports, not hours.
  - "Sofia engineers cost us less." Answer: don't argue rate. Use time to first merged PR (see use-cases.md objection on day rate).
  - "We only want EU engineers on customer data." Answer: all Corvane engineers are EU-based, working on client hardware under client security policy.

## Activity log
- 2026-10-13: Account file created from public sources. Scored 58, Tier 2, Play 4.

## To verify
- Whether the Senior Software Engineer role (req 4000039101) has been open 90+ days. If yes, Intent rises by 8 and the score to 66 (still Tier 2).
- Current open engineering roles and posting dates. The Greenhouse board could not be opened from this environment (network policy); counts come from search snapshots.
- Whether the January 2026 round closed. If it closed after mid-April 2026, add 10 (last 6 months) or 5 (6 to 12 months).
- Headcount. Only third-party estimates (472 to 501) exist; the company hasn't published one.
- Whether Elena Kiranova and Diyan Bogdanov still hold their titles, and which domain owns the SEK and PLN launches.
- Name of the head of product. Not found.
- Whether the "~10% smaller sales team" came from layoffs or attrition. No layoff report found.
- Karadzhov's LinkedIn activity (scored 0 until checked).
- Any warm path: past Corvane clients or engineers with Payhawk connections.
- The "product and engineering team is entirely in Bulgaria" claim comes from a recruiting page of unknown date.

## Sources
Primary pages (globenewswire.com, payhawk.com, greenhouse.io, bloomberg.com) were blocked by this environment's network policy, so facts were read through search results that cite them. Re-open the primary pages before quoting anything in outreach.

- S1: TechCrunch, Payhawk becomes a unicorn as it extends its Series B (2022-02-28): https://techcrunch.com/2022/02/28/payhawk-becomes-a-unicorn-as-it-extends-its-series-b/
- S2: Bloomberg, Fintech Payhawk Seeks $2 Billion Valuation (2026-01-07): https://www.bloomberg.com/news/articles/2026-01-07/fintech-payhawk-seeks-2-billion-valuation-in-new-funding-round
- S3: PYMNTS on the 2026 talks: https://www.pymnts.com/news/investment-tracker/2026/payhawks-valuation-could-soar-to-2-billion-with-new-funding/ and PitchBook profile: https://pitchbook.com/profiles/company/277307-56
- S4: Payhawk press release, $100M ARR (2026-07-08): https://www.globenewswire.com/news-release/2026/07/08/3323836/0/en/payhawk-surpasses-100m-arr-and-grows-faster-and-leaner-in-europe-driven-by-ai-native-rebuild.html and https://payhawk.com/blog/news-payhawk-passes-100m-arr
- S5: Financial Controller Agent release (2026-07-21): https://www.manilatimes.net/2026/07/21/tmt-newswire/globenewswire/payhawk-releases-financial-controller-agent-capability-that-gathers-vendor-invoices-12-times-faster-than-humans/2388122/amp
- S6: Senior Software Engineer, Sofia: https://payhawk.com/careers/4000039101/senior-software-engineer
- S7: Software Engineer, Sofia: https://payhawk.com/careers/4000749101/software-engineer and jobs.bg company profile: https://www.jobs.bg/en/company/297917
- S8: Fall '26 edition: https://payhawk.com/en-us/editions/fall-2026
- S9: Agentic playbooks coverage: https://ffnews.com/news/payhawk-transforms-how-finance-teams-work-with-new-agentic-playbooks-608ec3dd
- S10: Stockholm Nordic hub release (2026-09-30): https://www.globenewswire.com/news-release/2026/09/30/3371547/0/en/payhawk-makes-stockholm-its-nordic-hub-in-european-expansion.html
- S11: Poland expansion release (2026-09-30): https://www.globenewswire.com/news-release/2026/09/30/3371550/0/en/payhawk-expands-in-poland-to-support-growing-businesses-with-ai-native-spend-management.html and Finextra: https://www.finextra.com/pressarticle/111087/payhawk-opens-new-offices-in-stockholm-and-warsaw
- S12: Warsaw Business Journal, Payhawk opens office in Warsaw: https://wbj.pl/bulgarias-payhawk-opens-office-in-warsaw/post/151386
- S13: Revelio Labs headcount and hiring estimates: https://www.reveliolabs.com/companies/payhawk/employees
- S14: LeadIQ employee directory: https://leadiq.com/c/payhawk/5ca77cae2000000c0148589f/employee-directory
- S15: Latka: https://getlatka.com/companies/payhawk-payhawkcom
- S16: Payhawk careers page (features Elena Kiranova): https://payhawk.com/careers
- S17: tsh.io interview with Boyko Karadzhov (2024-05-16): https://tsh.io/blog/business-it-alignment
- S18: Payhawk Greenhouse board: https://job-boards.greenhouse.io/payhawkio
- S19: Endeavor Bulgaria profile, Boyko Karadzhov: https://bulgaria.endeavor.org/boyko-karadzhov/
- S20: Payhawk team page: https://payhawk.com/team
- S21: Payhawk blog author page, Diyan Bogdanov: https://payhawk.com/blog/authors/diyan-bogdanov
- S22: Payhawk blog author page, Hristo Borisov: https://payhawk.com/en-us/blog/authors/hristo-borisov
