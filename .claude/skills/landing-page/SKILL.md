---
name: landing-page
description: Write a Corvane landing page through the full layer stack, audit it, and build the branded HTML file. Use when asked for a landing page, campaign page, service page or event page.
---

# Landing page

## 1. Brief
Check for: asset type, reader, source, answer, question, plus CTA and campaign name. If anything is missing, ask once in a single message. Use the template in `prompt-library/00-brief-templates.md` as the checklist.

## 2. Load
- `CLAUDE.md`, `brand-guidelines/BRAND.md`, `messaging-guidelines/MESSAGING.md`, `use-cases.md`
- `messaging-guidelines/personas/<reader>.md`
- The voice named in that persona file
- `messaging-guidelines/services/<service>.md` and `messaging-guidelines/industries/<industry>.md` if named
- `craft-guidelines/landing-page.md`
- In Pro Mode, all three `lineage/` files

State the files loaded in one line.

## 3. Draft
Follow the seven sections in the craft guide in order. Problem section has no Corvane mention. Proof uses approved points only. Objections come from MESSAGING.md or use-cases.md for this persona.

## 4. Audit
Score the four pillars. Revise until 90 or more. Then ask the router agent (`.claude/agents/router.md`) to run the reviewers. List flags under the copy.

## 5. Build
Follow `tools/html-landing-page/TOOL.md`. Save to `campaigns/<campaign-name>/index.html` and the copy to `campaigns/<campaign-name>/landing-page.md`.

## 6. Report
Copy, score, flags, file paths. One line on what to test first (usually the headline).
