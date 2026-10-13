# Craft Guide: Outbound Sequence

**Layer 6 · Load when the asset is a cold email sequence, a LinkedIn message sequence, or a multi-channel outbound play**

---

## What this asset is

A short sequence of messages to one person at one account, built on a specific reason to write now. Each message must stand alone (most people only read one) and each adds something new.

The reason to write is everything. No signal, no sequence. See `scoring/intent-signals.md` and `abm/account-entry-plays.md`.

---

## The shape

```
Touch 1   Day 0    Email       The signal + the problem it implies + one question
Touch 2   Day 3    LinkedIn    Connection request, no pitch (under 200 characters)
Touch 3   Day 5    Email       A different angle: proof or a useful insight
Touch 4   Day 10   Email       The honest breakup: offer value, close the loop
```

Four touches maximum. More than that is noise.

---

## Touch rules

### Touch 1: the signal email
- **Subject line:** 2 to 5 words, lower case, sounds internal. "platform hiring", "q1 card launch".
- **Line 1:** the signal, stated as a fact about them. "You've had two senior backend roles open since June."
- **Lines 2 to 3:** what that usually means, and what Corvane does about it, in one or two sentences.
- **Line 4:** one low-friction question.
- Under 120 words. No links, no attachments.

### Touch 2: LinkedIn connection
A plain note referring to the same topic. No pitch, no link.

### Touch 3: the second angle
One of: a relevant approved case study in two sentences, or a genuinely useful observation (how to structure contractor onboarding, for example). Ends with a softer question.

### Touch 4: the breakup
Short, honest, no guilt. Offer something useful (the onboarding checklist, a short call with an engineer) and say this is the last note.

> "I'll stop here. If the platform roles fill up, great. If they don't and Q1 gets tight, the offer of a 30-minute call with one of our engineers stands. Piotr"

---

## Personalisation rules

- Every Touch 1 references at least one real, verifiable fact about the account from `accounts/<account>.md` or the brief.
- Never fake familiarity ("Loved your recent post!") unless the operator confirms it's true.
- Never personalise with anything private or creepy (personal life, family, location).

## Checklist

- [ ] There's a real signal and Touch 1 opens with it
- [ ] Each touch works alone
- [ ] Under 120 words per email
- [ ] One question per message
- [ ] Voice matches the sender (Piotr: engineer-to-engineer, Marta: founder-direct)
