# Demo Briefs

Four ready-to-run briefs that show different parts of the system. Copy one, paste it into Claude Code, and watch which layers it loads.

---

## 1 · Case study (Pattern Mode)

**What it shows:** facts vs claims. The skill builds a fact table first, uses approved numbers only, and leaves out the quote section because no quote was supplied.

```
Pattern Mode. Case study. Use the case-study skill.

Client:      Mendwell Health
Format:      Full case study
Reader:      CTO
Industry:    healthtech
Service:     ai-integration
Source:      Mendwell Health runs a patient app used by GP practices in the UK. Their
             board wanted an AI triage feature that sorts incoming patient messages by
             urgency. Their engineering team had no one who had shipped an LLM feature,
             and their clinical safety lead would not sign off without evidence it worked.
             Corvane ran the AI Integration service: a use-case workshop, then an
             evaluation suite of 1,200 test cases built from anonymised historical
             messages and agreed with the clinical safety lead, then prototypes compared
             against the suite, then a launch behind a feature flag with monitoring.
             Shipped in 10 weeks. Mendwell kept the evaluation suite and now tests every
             model or prompt change against it. No client quote supplied.
Answer:      Define what "working" means before you build, and you can ship AI safely
             in a regulated product.
Question:    "How do I ship an AI feature without it giving my customers wrong answers?"
```

---

## 2 · LinkedIn post by Piotr (Pattern Mode)

**What it shows:** a named voice, the craft guide's hook rules, three hook options, and the check on how often Corvane is mentioned.

```
Pattern Mode. LinkedIn post. Use the linkedin-post skill.

Author:      Piotr
Post type:   Framework
Reader:      CTOs and VP Engineering being asked by their board to "add AI"
Source:      Most teams demo an LLM feature on a handful of hand-picked examples, it
             looks great, then it fails on real inputs after launch. What works is
             writing the test cases first: a few hundred real examples with the answer
             you'd accept, agreed with whoever owns the risk. Then every model, prompt
             or retrieval change gets scored against the same set. It turns "it feels
             better" into a number.
Answer:      Write the evaluation set before you write the feature.
Question:    "How do I know our AI feature actually works before customers find out it doesn't?"
```

---

## 3 · LinkedIn ad set (Pattern Mode)

**What it shows:** three variants on different angles, character limits, one persona, approved proof only.

```
Pattern Mode. LinkedIn ad, 3 variants.

Reader:      VP Engineering
Industry:    fintech and b2b-saas
Offer:       Free download: "The contractor onboarding checklist we use with every
             client" (a 6-page PDF, used as a document ad)
Source:      Targeting VP and Head of Engineering at Series A to C fintech and SaaS
             companies, 150 to 1,000 employees, UK, Nordics, DACH and Benelux.
             Retargeting excluded. Campaign: 2026-11_linkedin_vpeng_checklist.
Answer:      Most contractor engagements go wrong in the first two weeks. This
             checklist fixes the first two weeks.
Question:    "Why do new contractors take so long to become useful?"
Landing:     campaigns/2026-11-onboarding-checklist/
```

---

## 4 · Account research (skill)

**What it shows:** live web research, sourced facts, ICP scoring done in code, tier, entry play, saved account file, then a handoff into outbound.

```
Use the account-research skill on Payhawk (payhawk.com), the spend management
fintech.

Find buying signals (funding, open senior engineering roles and how long they've
been open, new engineering leaders, launches, market expansion, any layoffs),
fit data (size, stage, stack from job ads, locations) and the engineering buying
group. Source every fact and list anything you couldn't verify.

Score it with abm/icp-scoring.md, assign a tier and entry play, and save the file to
accounts/payhawk.md. Then tell me the strongest signal and who Piotr should write to
first.
```

If Payhawk turns up a negative signal such as recent layoffs, that's a good demo moment too: the system should recommend pausing outreach rather than pushing on. To try another account, swap in any European fintech or SaaS scale-up with 150 to 1,000 employees.
