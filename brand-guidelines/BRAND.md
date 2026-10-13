# BRAND.md: Corvane Brand Guidelines

**Layer 1 · Always loaded · Applies to every artifact**

Read this straight after CLAUDE.md. Every output must pass the brand fidelity pillar. This file defines what that means.

---

## What Corvane sounds like

Corvane sounds like a senior engineer who has sat on the client side of a bad outsourcing deal and decided to build the opposite. Plain. Technical when it helps. Honest about what is hard. Never selling.

The test for every asset: would a CTO who has been burned by a vendor before read this and think "these people have done the job", or would they clock it as agency copy? Write for the first reaction.

**Four words:**

```
Plain        Say it the way you'd say it in a stand-up.
Specific     Name the stack, the timeline, the number. Vague is a red flag to engineers.
Honest       Say what's hard. Say what we won't do. Buyers trust the vendor who admits limits.
Calm         No urgency theatre. No hype. Senior people don't shout.
```

---

## Tone dial

The register moves. The character doesn't.

```
More formal  <--------------------------------------------->  More conversational
Procurement doc    CTO email    Case study    LinkedIn post    Piotr's post
```

What never changes: no em dashes, no banned words, no filler openers, no hype, no AI patterns.

---

## The voice in practice

### What Corvane copy sounds like

Short sentences. One idea at a time. Verbs do the work.

Engineers smell vagueness. "We onboard fast" is noise. "Your new engineers open their first pull request in week two" is a claim they can test.

The reader's problem comes first. The service is the answer to that problem, not the subject of the sentence.

**Wrong:**
> ~~Corvane is an innovative, world-class software development partner that leverages cutting-edge talent to empower your digital transformation journey.~~

**Right:**
> Your roadmap is three engineers ahead of your hiring plan. Corvane's engineers join your team, work in your repo, and ship from week two.

### What Corvane copy never sounds like

**Significance inflation**
> ~~"A new era of software delivery."~~

**Vendor flattery**
> ~~"We were so impressed by what you're building at [Company]."~~

**Hedging into nothing**
> ~~"We may potentially be able to help in some cases."~~

**Headcount talk**
> ~~"Access a pool of 500+ developers."~~ Buyers don't want a pool. They want work shipped.

**Rate talk up front**
> ~~"Save 40% versus local hires."~~ Price comes up when the buyer raises it. Leading with cheap attracts the wrong buyer and invites the wrong comparison.

---

## AI writing patterns to strip

Run every draft against this list. Each one fails Pillar 1.

- Filler openers: "In today's fast-moving market", "I hope this finds you well", "I wanted to reach out"
- Negative parallelism: "It's not just X, it's Y"
- Rule of three padding where one word would do
- "-ing" tails: "...ensuring quality", "...driving results", "...fostering collaboration"
- Copula dodging: "serves as", "stands as", "functions as". Use "is".
- Vague attribution: "experts say", "studies show"
- Signposting: "Here's the thing", "Let's dive in"
- Excited filler: "Thrilled to announce"
- Emoji
- Em dashes

---

## Formatting rules

- Sentence case for headlines and buttons. Not Title Case.
- Numbers as digits: 2 weeks, 90 engineers, 14 days.
- British English spelling (organise, optimise) in all European-facing copy. US spelling only when the brief says the reader is US-based.
- Oxford comma: no.
- Name technologies correctly: TypeScript, PostgreSQL, Kubernetes, React Native, Ruby on Rails.
- Buttons say what happens: "Book a 30-minute scoping call", not "Learn more" or "Submit".

---

## Visual identity

Used by `tools/html-landing-page/template.html` and any designed asset.

```
Colour          Hex        Use
----------------------------------------------------------
Pine            #12352B    Primary. Headlines, buttons, footer.
Paper           #F6F4EF    Background.
Ink             #1C1F1E    Body text.
Amber           #E8A33D    Accent. One element per screen, never body text.
Fog             #D9DED9    Rules, borders, table lines.
```

```
Type            Font                 Use
----------------------------------------------------------
Headlines       Inter, 600           Sentence case, tight tracking.
Body            Inter, 400           16 to 18px, generous line height.
Code / data     IBM Plex Mono, 400   Stack names, metrics, labels.
```

**Imagery:** real screens, real code, real whiteboards. No stock photos of people pointing at laptops. No glowing brains or robot hands for AI topics.

---

## Words Corvane uses

```
Use                          Instead of
----------------------------------------------------------
engineers                    resources, developers (as a pool), talent
join your team               provide staff
ship                         deliver value
your codebase                the project
delivery partner             outsourcing vendor
scoping call                 discovery call, demo
shipped-work report          timesheet
senior                       experienced, top-tier, A-player
```
