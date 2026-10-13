---
name: account-research
description: Research a target account from public sources, score it against the ICP, identify buying signals and contacts, and save an account file. Use when asked to research a company, build an account file, qualify a prospect, or find a reason to reach out.
---

# Account research

## 1. Search
Use web search for the company. Look for, in this order:
1. **Buying signals** (see `scoring/intent-signals.md`): funding in the last 6 months, open engineering roles (count and how long open), a new CTO or VP Engineering, product launches or market expansion, regulatory deadlines, public mentions of a migration or AI initiative.
2. **Fit data:** employees, industry, funding stage, HQ and engineering locations, tech stack (job ads are the best source).
3. **People:** CTO, VP Engineering, Head of Product, relevant engineering managers. Names and titles from the company site or press only.

Record the source URL for every fact. Don't guess what you can't find; write "not found".

## 2. Score
Apply `abm/icp-scoring.md`. Show the score per dimension. Never compute the total in your head: write the scores into a small table and add them with code, or show the sum explicitly line by line.

## 3. Tier and play
Assign a tier using `abm/account-tiers.md` and pick the matching entry play from `abm/account-entry-plays.md`.

## 4. Save
Write `accounts/<company-slug>.md` using `abm/account-research-template.md`. Include sources.

## 5. Report
Score, tier, the strongest signal, the recommended play and first contact, and what's missing. Offer to run the `outbound-sequence` skill next.

## Rules
- Public, professional information only. Nothing about people's private lives.
- Every fact has a source. Unsourced facts go in a "To verify" list.
