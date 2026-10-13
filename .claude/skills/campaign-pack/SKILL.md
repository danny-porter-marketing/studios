---
name: campaign-pack
description: Turn one campaign brief into a consistent set of assets for every channel (outbound sequence, LinkedIn post, LinkedIn ad set, landing page, one-pager, optional blog), all built from one message house and each audited. Use when asked for a campaign pack, assets for all channels, a multi-channel campaign, or to scale one message across channels.
---

# Campaign pack

One brief, every channel, one story. Each asset follows its own craft guide, but they all say the same thing in the way that channel needs.

## 1. Brief
Need: campaign name, priority served (`priorities.md`), reader persona, industry, service, the core answer, the reader's question, the CTA, and which channels. If a `campaigns/<name>/plan.md` exists, take these from it. Ask once for anything missing.

Default channels: outbound sequence, LinkedIn post, LinkedIn ad set (3 variants), landing page with HTML, one-pager. Blog article only if asked.

## 2. Load once
`CLAUDE.md`, `BRAND.md`, `MESSAGING.md`, `use-cases.md`, the persona and its paired voice, the industry and service files, and any **Proven rule (EXP-NNN)** lines that apply. Then load each craft guide as you reach that asset.

## 3. Build the message house first
Before writing any asset, write and show `campaigns/<name>/message-house.md`:

```
Core message      One sentence. Every asset must carry it.
Problem           The reader's situation, in their words (from the persona file)
Pillar 1          Claim + approved proof
Pillar 2          Claim + approved proof
Pillar 3          Claim + approved proof
Objection         The most likely one, and the answer (MESSAGING.md or use-cases.md)
CTA               One action, the same everywhere
Words to use      From the persona's language list
Never say         Anything the brief, persona or messaging rules exclude
```

This is the single source for the pack. If the operator changes it, every asset is regenerated from it.

## 4. Write each asset from the message house
In this order, each with its own craft guide and skill:

| Asset | Craft guide | Skill | Voice |
|---|---|---|---|
| Landing page + HTML | landing-page | `landing-page` | engineer-to-engineer or founder-direct per persona |
| Outbound sequence template | outbound-sequence | `outbound-sequence` | sender's voice |
| LinkedIn ad set, 3 variants | linkedin-ad | (craft guide) | brand voice |
| LinkedIn post | linkedin-post | `linkedin-post` | piotr-linkedin or marta-linkedin |
| One-pager | one-pager | (craft guide) | persona's paired voice |
| Blog article (optional) | blog-article | (craft guide) | brand voice |

The outbound template uses placeholders for account-level personalisation: `{{signal}}`, `{{company}}`, `{{first_name}}`. The `outbound-sequence` skill fills them per account later (batch).

## 5. Audit each asset
Four-pillar audit per asset. Revise anything under 90.

## 6. Consistency check across the pack
Check, and show as a table:
- Every asset carries the core message (quote where)
- The CTA is identical everywhere
- Every number appears in MESSAGING.md approved proof points
- No asset contradicts another (different claims, different offers)
- Each asset fits its channel's limits (subject length, ad characters, post length), counted with code

Then hand the whole pack to the router agent for review.

## 7. Save
```
campaigns/<name>/
  message-house.md
  landing-page.md + index.html
  outbound-template.md
  linkedin-ads.md
  linkedin-post-<author>.md
  one-pager.md
  blog-article.md (if asked)
  pack-summary.md      scores, consistency table, reviewer flags
```

## 8. Next steps to offer
- Personalise the outbound per account: `outbound-sequence` in batch over the campaign's account list
- Push to sending tools: `outbound-export` (paused campaigns)
- Turn one asset into an experiment: `experiment-design` (for example two ad hooks or two landing page heroes)

## Report
The message house, a table of assets (file, score, weakest pillar), the consistency check, reviewer flags, and the file paths.
