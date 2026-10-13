# Brief Templates: Corvane Studios

Every asset starts with a brief. Find the template, copy it, fill every field, paste it into Claude Code. Don't skip fields. A vague brief produces a vague asset.

---

## Which template

```
What you're making                           Template
---------------------------------------------------------------------
A subject line, headline, reply, short copy   01 Quick Mode
A landing page                                02 Pattern Mode: Landing page
A cold outbound sequence                      02 Pattern Mode: Outbound
A LinkedIn post (Marta or Piotr)              02 Pattern Mode: LinkedIn post
A case study                                  02 Pattern Mode: Case study
A one-pager                                   02 Pattern Mode: One-pager
A LinkedIn ad set                             02 Pattern Mode: LinkedIn ad
A high-stakes asset needing 3 directions      03 Pro Mode
Research an account                           Skill: account-research
Analyse pasted data                           Skill: sheets-dashboard
Update use-cases.md                           04 Weekly update
```

**Persona files:** `messaging-guidelines/personas/` (cto, vp-engineering, head-of-product, ceo-founder, engineering-manager, procurement)

---

## 01 · Quick Mode

```
Quick Mode.

Asset type:  [subject line / headline / reply / one paragraph]
Reader:      [persona]
Source:      [what we know about them]
Answer:      [the one thing it must say]
Question:    [the question in their head]

Give me one output and the audit score.
```

---

## 02 · Pattern Mode: Landing page

```
Pattern Mode. Landing page.

Asset type:  Landing page for [campaign name]
Reader:      [persona]
Industry:    [fintech / b2b-saas / healthtech / none]
Service:     [team-extension / product-delivery / ai-integration]
Source:      [traffic source, what the visitor just saw, anything known about them]
Answer:      [the one thing the page must communicate]
Question:    [the question the visitor arrives with]
CTA:         [e.g. Book a 30-minute scoping call]

Write the copy, audit it, then build the HTML with the html-landing-page tool.
```

---

## 02 · Pattern Mode: Outbound

```
Pattern Mode. Outbound sequence.

Asset type:  4-touch outbound sequence
Sender:      [Piotr / Marta]
Reader:      [name, title, persona]
Account:     [company, or path to accounts/<file>.md]
Signal:      [the reason to write now: funding, hiring, new leader, launch, deadline]
Answer:      [what we want them to take away]
Question:    [the question in their head when they read it]
```

---

## 02 · Pattern Mode: LinkedIn post

```
Pattern Mode. LinkedIn post.

Author:      [Marta / Piotr]
Post type:   [observation / contrarian / story / framework / carousel]
Reader:      [who should feel this was written for them]
Source:      [the moment, idea or data behind the post]
Answer:      [the one point]
Question:    [what the reader should be thinking after]
```

---

## 02 · Pattern Mode: Case study

```
Pattern Mode. Case study.

Client:      [approved client name]
Format:      [full case study / short proof story]
Reader:      [persona]
Source:      [facts, numbers, timeline, supplied quotes]
Answer:      [the outcome to lead with]
Question:    [what a reader in a similar situation is wondering]
```

---

## 02 · Pattern Mode: One-pager

```
Pattern Mode. One-pager.

Reader:      [persona]
Service:     [service]
Industry:    [industry or none]
Source:      [context: after which call, for which account]
Answer:      [the outcome]
Question:    [what the reader needs answered to take the next step]
Contact:     [name on the page]
```

---

## 02 · Pattern Mode: LinkedIn ad

```
Pattern Mode. LinkedIn ad, 3 variants.

Reader:      [persona; one per ad set]
Offer:       [scoping call / checklist / guide / event]
Source:      [targeting and campaign context]
Answer:      [the outcome or offer]
Question:    [what makes them stop scrolling]
Landing:     [URL or campaign folder]
```

---

## 03 · Pro Mode

```
Pro Mode.

Asset type:  [asset]
Reader:      [persona]
Source:      [everything relevant]
Answer:      [the one thing]
Question:    [the question in their head]

Three versions (Editor, Provocateur, Architect). Score each with the four-pillar audit and give a verdict.
```

---

## 04 · Weekly update

```
Run prompt-library/04-weekly-update.md for this week.
```
