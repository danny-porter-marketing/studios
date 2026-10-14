# Next 5 content pieces, top 3 keyword plan, GA4 fixes

Builds on `seo-plan.md` in this folder (same Semrush and GA4 exports, same cleaning). New cuts in this file come from pandas on `keywords_scored.csv` and `ga4_clean.csv`. Extra clicks are monthly at position 3 using the script's click-through curve: estimates for ranking the work, not forecasts.

---

## 1. Next 5 content pieces

One piece per keyword cluster, ranked by fit with Q4 priorities first, then opportunity. Every piece links to the service or industry page that converts.

| # | Piece (working title) | Target keywords | Volume / mo | Avg KD | Extra clicks / mo | Reader | Links to | Priority |
|---|---|---|---|---|---|---|---|---|
| 1 | How to evaluate an LLM feature before you ship it | llm evaluation metrics, llm evaluation framework, how to evaluate llm features | 2,800 | 23 | 308 | CTO | /services/ai-integration | P3 |
| 2 | The contractor onboarding checklist | developer onboarding checklist, how to onboard contractors, contractor onboarding checklist | 2,890 | 18 | 318 | Engineering Manager | /services/team-extension | P2 |
| 3 | How to choose a software house: the questions to ask | how to choose a software house, questions to ask a software development company | 1,070 | 20 | 118 | CTO, VP Engineering | / and /services/team-extension | P1, P2 |
| 4 | Nearshore vs offshore: what changes for your engineering team | nearshore vs offshore | 1,000 | 31 | 107 | CTO | /services/team-extension (anchor: nearshore software development) | P2 |
| 5 | How to scale an engineering team fast when hiring can't keep up | how to scale engineering team fast, cost of hiring senior developer europe | 870 | 21 | 96 | VP Engineering, CEO | /services/team-extension | P2 |

**Why this order**
- **1 first:** the only content gap tied to a Q4 priority (P3, prove AI demand). Corvane has approved proof for it (Mendwell Health: AI triage feature shipped in 10 weeks with an evaluation suite of 1,200 test cases). Reader is the CTO, not the Head of Product: EXP-001 found Heads of Product respond to roadmap delivery, not AI.
- **2:** the biggest gap by volume, and it sells the second supporting bullet (a written onboarding playbook, median 9 working days to first merged pull request). Build it as a new page and link to it from `/blog/onboarding-docs-that-get-read`. That post gets 3,517 sessions at 0.3%, so the checklist needs a downloadable version as its call to action.
- **3:** buyer-stage questions. Give it a fintech section (security, EU data residency, audit trails, the Ledgerline proof point) so it also serves P1.
- **4:** "nearshore vs offshore" ranks 24 today on the team extension blog post, which already tries to cover too much (see action 3 below). A dedicated page takes it off that post and passes link strength to the `nearshore software development poland` quick win (position 11).
- **5:** answers narrative step 1 ("the roadmap is ahead of hiring"). Write it without salary or cost numbers: none are approved, and Corvane doesn't frame value as rates.

**Parked:** postgresql, kubernetes, react native consulting (no priority), fhir integration and healthtech (no Q4 priority). **Data gap:** the export has no fintech informational keywords beyond the industry page term. P1 carries 40% of the weight, so pull a fintech keyword list (ledger, reconciliation, card issuing, payments engineering) from Semrush before Q1 planning.

Each piece is written with the blog-article craft guide (1,000 to 1,800 words, main phrase in the title, first paragraph and one H2, Corvane mentioned twice at most) and passes the four-pillar audit before publishing.

---

## 2. Top 3 keywords into the top 3

The top 3 quick wins by opportunity score:

| Keyword | Now | Volume | KD | Clicks / mo now | At position 3 | Extra | Page that should own it |
|---|---|---|---|---|---|---|---|
| dedicated development team | 9 | 2,400 | 55 | 60 | 264 | 204 | /services/team-extension |
| fintech software development company | 17 | 1,300 | 46 | 13 | 143 | 130 | /industries/fintech |
| team extension | 12 | 1,900 | 39 | 19 | 209 | 190 | /services/team-extension (today: the blog post) |

**Be realistic.** Getting all three from page 1 or 2 into the top 3 in one quarter is a stretch, especially `dedicated development team` at KD 55 and `fintech software development company` from position 17. Set checkpoints: top 10 by week 4, top 5 by week 8, top 3 by week 12. Track positions weekly in Search Console.

### Keyword A: team extension (12 to 3)
This is the fastest win because it's mostly a cannibalisation fix, not new authority.
1. **Week 1: pick the owner.** `/services/team-extension` owns "team extension", "team extension company" and "team extension services". Put "Team extension" at the start of its title tag and in the H1. Add a short "What team extension is" section: three sentences, no more.
2. **Week 1: re-target the blog post.** Change its title and H1 to the comparison question ("Team extension vs staff augmentation vs outsourcing"). Keep the URL: it holds position 2 for "team extension vs staff augmentation". Remove "team extension" from its title as a head term.
3. **Week 1: internal links.** From the blog post's first 200 words, link to the service page with the anchor text "team extension". Do the same from the homepage and from content pieces 2, 4 and 5 when they go live.
4. **Week 2: check.** If Google keeps showing the blog post for "team extension" after 3 to 4 weeks, make the service page's intro answer the definition more directly and add an FAQ section.

### Keyword B: dedicated development team (9 to 3)
The same page as keyword A, so do it in the same edit.
1. **Week 1: on-page.** Add an H2 that answers the query: what a dedicated team from Corvane looks like (senior only, in your repo and rituals, weekly shipped-work report, 30-day notice per engineer). Use "dedicated development team" in that H2 and once in the copy.
2. **Week 1: proof on the page.** Approved proof only: 82% of clients extend after the first 6 months, average engagement 2.5 years, median 9 working days to first merged pull request.
3. **Weeks 2 to 6: authority.** KD 55 needs links from outside the site. The Clutch profile already sends 930 sessions. Check that its website link points to `/services/team-extension`, not only the homepage. Add the service page link to partner and directory profiles you already control.
4. **Weeks 4 to 12: supporting content.** Content pieces 4 and 5 link in with varied anchors ("dedicated team", "senior engineers in your team").

### Keyword C: fintech software development company (17 to 3)
The hardest of the three: it starts on page 2. This page also converts best for P1 (3.6% organic).
1. **Week 2: on-page.** Title and H1 lead with "Fintech software development". Rebuild the page around the fintech guide: external deadlines, security and compliance first, ledger and reconciliation experience, JVM, Kafka and PostgreSQL stacks. State that the client owns compliance and Corvane engineers work within it.
2. **Week 2: proof.** Ledgerline (3 engineers to 11 in 5 months, card issuing launched in 3 markets), ISO 27001, GDPR data processing agreement, all engineers employed directly.
3. **Week 2: internal links.** Today almost nothing links in. Add links from the homepage, from `/services/team-extension` (a "fintech teams" line), and from the existing Kotlin pages that rank for `hire kotlin developers` and `kotlin development company` (Kotlin is a core fintech stack).
4. **Weeks 3 to 12: authority.** Publish the Ledgerline case study as its own page linking to `/industries/fintech`. Put the page in the Q4 fintech campaign (`campaigns/2026-q4-fintech-ctos/`) so LinkedIn and email send people to it. Those visits don't move rankings directly, but links and mentions follow from them.

### How we'll know
- Positions weekly in Search Console for the three terms. Clicks and key events on the two owning pages, compared with the 13-week baseline in `ga4_report.md`.
- Run it as a before-and-after test with `experiment-design`, using unchanged pages as the control. SEO tests are slower and noisier than email tests, so read it out at week 12, not before.

---

## 3. GA4: what's working, what isn't, and the fixes

Period 6 July to 28 September 2026, spam and duplicates removed, 24 August week left out of trends.

### Working
| What | Evidence |
|---|---|
| Organic search is the main source and it's growing | 15,654 sessions, 193 key events (more than all other channels combined). Up 31% from the first 4 weeks to the last 4 |
| Service pages convert | /services/team-extension converts in every channel: 5.9% organic, 7.2% paid, 7.6% direct, 4.6% LinkedIn. AI integration and fintech: 2.2% to 3.6% in organic, paid and direct |
| Content holds attention | Blog posts are at about 60% engagement, the same as the service pages |
| Email brings engaged visitors | Highest engagement of any channel (68.9%) |

### Not working, with fixes
| Problem | Evidence | Fix | Priority |
|---|---|---|---|
| **Paid search lands on the homepage** | 74% of paid sessions (1,721) land on `/` at 1.2%. The 306 paid sessions to /services/team-extension convert at 7.2% | Point ad groups at the matching service or industry page: team extension terms to /services/team-extension, fintech terms to /industries/fintech, AI terms to /services/ai-integration. Test it with `experiment-design` before moving the whole budget | P2 |
| **Blog posts don't pass visitors on** | 9,015 blog sessions, 32 key events (0.4%). Email visitors to the blog: 449 sessions, 0 key events | Add in-body links and one end-of-post call to action to the matching service page. Build a downloadable checklist for the onboarding post | P1, P2 |
| **Team extension terms are split across two URLs** | Commercial terms rank with the blog post (0.3%), not the service page (5.9%) | Section 2, keyword A | P2 |
| **Fintech page gets little traffic** | 951 sessions in 13 weeks across all channels, despite being the P1 page | Section 2, keyword C, plus fintech campaign traffic | P1 |
| **Tracking break, week of 24 August** | 472 sessions vs a median week of 2,267, every channel at once, spam unaffected | Check the GTM version history for that week. Add a GA4 custom alert for a drop of more than 50% week on week | All |
| **`(not set)` landing pages** | 427 sessions, 0 engaged | Check consent mode and that the config tag fires before events | All |
| **Spam referral** | free-seo-traffic.xyz: 6,476 sessions, 18.6% of raw traffic | Add a referral exclusion and filter it out of reports | All |
| **Key events aren't pipeline** | GA4 counts form fills | Join key events to SQLs in the CRM (`revops/attribution-model.md`) before moving budget between channels | P2 |
| **Careers traffic mixed into marketing views** | 3,010 sessions, 0 key events | Exclude /careers from marketing dashboards | n/a |

---

## Order of work

1. **Week 1:** fix tracking (tag break, `(not set)`, spam) so the baseline is clean.
2. **Week 1:** one edit to /services/team-extension plus re-targeting the blog post (keywords A and B), with blog-to-service internal links.
3. **Week 1:** set up the paid landing page test.
4. **Week 2:** rebuild /industries/fintech (keyword C).
5. **Weeks 2 to 10:** publish content pieces 1 to 5, one every two weeks.
