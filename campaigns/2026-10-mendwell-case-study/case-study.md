# Case study: Mendwell Health (AI Integration)

> Fictional demo client. Mendwell Health and every fact below are invented to show how the system works.

**Mode:** Pattern · **Reader:** CTO · **Voice:** engineer-to-engineer · **Craft:** case-study (full)
Loaded: CLAUDE · BRAND · MESSAGING · use-cases · persona/cto · voice/engineer-to-engineer · industries/healthtech · services/ai-integration · craft-guidelines/case-study

## Fact table

| Fact | Source | Approved for public use? |
|---|---|---|
| Client name: Mendwell Health | MESSAGING.md approved list | Y |
| AI triage feature shipped in 10 weeks | MESSAGING.md proof point | Y |
| Evaluation suite of 1,200 test cases | MESSAGING.md proof point | Y |
| Patient app used by GP practices in the UK | Operator source | Y (operator) |
| Board wanted an AI triage feature that sorts incoming patient messages by urgency | Operator source | Y (operator) |
| No one on the engineering team had shipped an LLM feature | Operator source | Y (operator) |
| Clinical safety lead would not sign off without evidence it worked | Operator source | Y (operator) |
| Steps: use-case workshop, evaluation suite, prototypes compared against the suite, launch behind a feature flag with monitoring | Operator source | Y (operator) |
| Suite built from anonymised historical messages and agreed with the clinical safety lead | Operator source | Y (operator) |
| Mendwell kept the suite and tests every model or prompt change against it | Operator source | Y (operator) |
| Client quote | None supplied | Section 7 left out |

Not written because no source exists: accuracy or error rates, urgency categories, models used, Corvane team size, number of practices or patients, compliance certifications (DSPT), any clinical or patient outcome.

---

# AI triage shipped in 10 weeks, tested against 1,200 cases

## At a glance

- **Client:** Mendwell Health
- **Industry:** Healthtech. A patient app used by GP practices in the UK.
- **Service:** AI Integration
- **Duration:** 10 weeks to ship
- **Numbers:** shipped in 10 weeks · 1,200 test cases in the evaluation suite

## The situation

Mendwell Health runs a patient app used by GP practices in the UK. Mendwell's board wanted an AI triage feature that sorts incoming patient messages by urgency.

Mendwell had 2 problems.

Nobody on Mendwell's engineering team had shipped an LLM feature. Building the feature is the visible part. Proving it works is the part teams new to LLMs have not done before.

And Mendwell's clinical safety lead would not sign off without evidence that it worked. A triage feature that ranks an urgent message low is a clinical safety problem. A demo on a few hand-picked messages says nothing about the messages that arrive next week.

So the team faced a hard version of a common question: how do you ship an AI feature without it giving wrong answers to the people who rely on it?

## What we did

We ran our AI Integration service. The clinical safety lead decided what counted as evidence; our engineers built the suite and the feature to meet it.

1. **Use-case workshop.** We started with a workshop with Mendwell to pin down the use case before any build work.
2. **Evaluation suite first.** We built 1,200 test cases from anonymised historical patient messages. Mendwell's clinical safety lead agreed the suite. It became the definition of "working".
3. **Prototypes against the suite.** We built prototypes and ran each one against the same 1,200 cases. Every comparison used the same evidence, so choosing between them was a reading of results.
4. **Launch behind a feature flag.** The feature launched behind a flag, with monitoring.
5. **Handover.** Mendwell kept the evaluation suite.

## What changed

- **Shipped in 10 weeks.** Launched behind a feature flag, with monitoring.
- **Evidence before launch.** The clinical safety lead asked for evidence that it worked. Before launch, that evidence existed: results against 1,200 test cases they had agreed.
- **A test gate Mendwell owns.** Mendwell now tests every model or prompt change against the suite.

## The detail

The suite matters more than the feature.

LLM features change under you. Providers release new models. A prompt edit that fixes one complaint can break cases nobody was looking at. Without a fixed set of tests, every change is a judgement call made on whatever examples someone thought to try.

Mendwell's suite is built from their own anonymised historical messages, so it tests the kind of messages their patients send. The clinical safety lead agreed it, so a pass means something to the person who signs off. And it sits with Mendwell's team. When they try a new model or change a prompt, they run it against the same 1,200 cases and read the result.

That is what "define what working means before you build" looks like in practice. It is a test suite your own team owns and runs on every change.

## Talk to us

If your board wants an AI feature and someone on your side needs evidence before they sign off, book a 30-minute scoping call with one of our engineers.

---

## Four-pillar audit

- Brand 24/25: no banned words or em dashes, digits throughout, British spelling, no AI patterns.
- Messaging 24/25: only 10 weeks and 1,200 (MESSAGING.md) plus operator facts; no accuracy, clinical outcome or volume claims; no quote.
- Persona 22/25: CTO language (evidence, sign-off, model and prompt changes, test gate), but nothing on how the engineering team worked alongside ours, which a CTO would ask.
- Craft 22/25: all 7 applicable sections, quote left out, 564 words, 10-word headline. Step 1 is thin because the source says only "a use-case workshop".
- **Total 92/100 (summed in code). Ship.**
- Weakest pillar: Craft and Persona tie. The thin workshop step and the missing team detail both need facts the source doesn't give.

Review agents (router: brand, messaging, craft): 5 blocking flags, all fixed. Removed the illustrative numbers ("ten", "ten thousand", "three other cases") and 2 unsourced client claims ("They knew their product...", "set the bar at every step"), and cut the headline to 10 words. Also applied: workshop detail no longer borrowed from the service template, "live" changed to "launched", Oxford comma removed, vague "many CTOs" claim removed.

## For MESSAGING.md (once Mendwell approves)

No new numbers. These operator-supplied facts are now public in this case study and could be added to the approved Mendwell entry:
- Suite built from anonymised historical patient messages, agreed with the clinical safety lead
- Launched behind a feature flag with monitoring
- Mendwell tests every model or prompt change against the suite

## Facts to get for a stronger version
- What the use-case workshop decided (who uses the feature, how it is measured)
- How Mendwell's engineers and ours split the work
- A quote from the clinical safety lead or CTO, word for word
