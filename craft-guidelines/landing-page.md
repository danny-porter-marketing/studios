# Craft Guide: Landing Page

**Layer 6 · Load when the asset is a campaign page, service page or event page**
**After the copy passes audit:** run `tools/html-landing-page/TOOL.md`

---

## What this asset is

One page, one reader, one action. A landing page exists to turn a specific visitor (from an ad, an email, an event) into a scoping call. It is not the homepage and it does not describe everything Corvane does.

---

## The shape

```
SECTION 1   Hero              Headline, subheadline, one CTA
SECTION 2   Problem           The reader's situation, in their words
SECTION 3   What changes      What Corvane does differently (2 to 3 points)
SECTION 4   How it works      3 or 4 steps with a timeline
SECTION 5   Proof             Up to 3 approved proof points or one case study
SECTION 6   Objections        The 2 questions this reader will ask, answered
SECTION 7   Final CTA         Restate the action
```

---

## Section rules

### 1. Hero
- **Headline:** under 10 words. States the outcome or names the problem. Sentence case.
- **Subheadline:** one or two sentences. Who it's for and what happens.
- **CTA:** says what happens: "Book a 30-minute scoping call".

> Good: "Your roadmap is ahead of your hiring. Close the gap in three weeks."
> Bad: ~~"World-class engineering talent for innovative companies."~~

### 2. Problem
Three to five short sentences describing the reader's situation so precisely they feel seen. Use the persona file's fears. No Corvane mention yet.

### 3. What changes
Two or three points, each a bold short claim plus one sentence of explanation. Map to the core messages in MESSAGING.md.

### 4. How it works
Numbered steps with time markers. Borrow from the matching service file.

### 5. Proof
Approved proof points only. If the campaign targets a vertical, use that vertical's case study.

### 6. Objections
Pick the two most likely objections for this persona from MESSAGING.md or use-cases.md. Question in the reader's words, answer in 2 to 3 sentences.

### 7. Final CTA
One headline, one sentence, the same CTA as the hero.

---

## Length

400 to 700 words in total. If it's longer, something isn't earning its place.

## Checklist

- [ ] One reader, one CTA, repeated at top and bottom
- [ ] Problem section has zero mention of Corvane
- [ ] Every number is in MESSAGING.md
- [ ] Objections are real ones for this persona
- [ ] HTML generated and saved to `campaigns/<campaign-name>/index.html`
