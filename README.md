# Corvane Studios

**An in-house creative agency and marketing operations system, in a GitHub repo, run by Claude Code.**

> **This is a demonstration build.** Corvane is a fictional software house. Every name, number, client and quote in this repo is invented. The architecture is a system I designed and ran in-house at a previous company, rebuilt here with a fictional brand so it can be shown openly.
> Built by Danny Porter.

---

## What it is

A repo that holds everything an AI agent needs to produce on-brand marketing and run marketing analysis without being re-briefed: positioning, voice, buyer personas, asset templates, review rules, go-to-market playbooks and reusable workflows.

Open Claude Code in this repo, paste a brief, and you get an asset that has already been checked against the brand, the messaging, the reader and the format. Paste a CSV and you get a cleaned, formula-driven Google Sheets dashboard.

**Not a tool or a SaaS seat. A repo.** Edit a markdown file on GitHub and the next session uses the change. Every change to the brand is version-controlled, reviewable and reversible, the same way engineers treat code.

---

## Why it exists

Marketing context usually lives in a few people's heads, a brand PDF nobody opens and a positioning deck from last year. Every AI-assisted asset starts from zero, so output drifts, and the team spends its time re-explaining instead of shipping.

This system fixes that by putting the context where the agent can read it, and by making the agent check its own work before a human sees it.

What it changed when it ran in production:
- More campaigns launched per week from the same headcount
- Hyper-personalised campaigns at scale that weren't feasible to write by hand

---

## How it works

Every asset composes through the same eight layers. Higher layers win on conflict.

```
LAYER 0 · Brief       What are we making, for whom, and why
LAYER 1 · Brand       How Corvane looks and sounds           always loaded
LAYER 2 · Messaging   What Corvane says                      always loaded
LAYER 3 · Persona     Who is reading
LAYER 4 · Voice       Who is writing to them
LAYER 5 · Lineage     Which creative director (Pro Mode only)
LAYER 6 · Craft       What shape the asset takes
LAYER 7 · Skills      Reusable workflows that load on match
LAYER 8 · Agents      Read-only reviewers that audit before ship
```

**Brand beats messaging. Messaging beats persona. Persona beats voice. Voice beats craft. Craft beats the brief.**

Every draft is scored by a four-pillar audit (brand, messaging, persona, craft, 25 points each). Under 75, the draft is never shown. Then a router agent sends it to specialist reviewers who flag issues without rewriting, so a human makes the final call.

### Three modes

```
Quick Mode     ~5 min    One short asset (subject line, headline, reply)
Pattern Mode   ~15 min   A structured asset (sequence, landing page, case study)
Pro Mode       30+ min   Three versions from three creative directors, scored, operator picks
```

---

## What's in the repo

```
CLAUDE.md                    The system contract. The agent reads it first.
use-cases.md                 Living knowledge base: objections, wins, what's working.
brand-guidelines/            Voice, banned words, visual identity.
messaging-guidelines/        Positioning, proof points, 6 personas, 6 voices,
                             3 industries, 3 services.
lineage/                     Three creative director perspectives for Pro Mode.
craft-guidelines/            8 asset types, each with its own structure.
prompt-library/              Copy-paste brief templates for every mode.
.claude/skills/              7 reusable workflows (see below).
.claude/agents/              5 review agents: router plus 4 auditors.
abm/  accounts/              Account-based marketing: ICP scoring, tiers, entry plays.
funnel/  scoring/            Funnel stages, MQL definition, lead scoring, intent signals.
revops/                      Attribution model, CRM conventions, reporting framework.
campaigns/                   Channel strategy and a worked example campaign.
tools/                       Turns approved copy into an HTML landing page.
```

### Skills

```
landing-page        Full layer stack for a landing page, plus HTML output
outbound-sequence   Account-personalised email sequences
linkedin-post       Posts in the CEO's or CTO's voice
case-study          Client stories built from approved proof only
copy-editing        Strips AI writing patterns, rewrites in the brand voice
account-research    Builds an account file from public buying signals
sheets-dashboard    Pasted data in, cleaned Google Sheets dashboard out,
                    every number a live formula
```

---

## Try it

1. Open this repo in Claude Code (claude.ai/code or the terminal).
2. Copy a template from `prompt-library/00-brief-templates.md`, fill it in, paste it.
3. Or paste a CSV and say "build me a dashboard from this".

A worked example campaign lives in `campaigns/2026-10-scaleup-ctos/`: the brief, the outputs, the audit scores and the landing page.

---

## Design choices

- **Markdown, not a database.** Anyone can edit the brand on GitHub. No app to maintain.
- **The agent checks itself before a human does.** Reviews start from a draft that already passes, so feedback is about judgement, not typos and banned words.
- **Reviewers flag, they don't rewrite.** Keeps a human accountable for what ships.
- **No numbers from the model's head.** Proof points come from an approved list. Analysis runs in code and spreadsheet formulas, never mental arithmetic.
- **Version control for brand.** Every change has an author, a reason and a rollback.
