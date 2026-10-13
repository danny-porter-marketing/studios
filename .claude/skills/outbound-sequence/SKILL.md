---
name: outbound-sequence
description: Write a signal-based, account-personalised outbound sequence for a named contact. Use when asked for cold emails, an outbound sequence, prospecting messages, or outreach to a specific account or list.
---

# Outbound sequence

## 1. Find the signal
A sequence needs a reason to write now. Check, in order:
1. The brief's Signal field
2. `accounts/<account>.md` (Signals section)
3. If neither exists, run the `account-research` skill first, or ask the operator.

No signal, no sequence. Say so rather than writing a generic one.

## 2. Load
- `CLAUDE.md`, `BRAND.md`, `MESSAGING.md`, `use-cases.md` (check "What's working in outbound")
- Persona file for the reader
- Sender voice: Piotr uses `engineer-to-engineer.md`, Marta uses `founder-direct.md`
- `craft-guidelines/outbound-sequence.md`
- Industry file for the account's vertical
- `abm/account-entry-plays.md` to match the signal to a play

## 3. Write
Four touches as defined in the craft guide. Touch 1 opens with the signal as a verifiable fact. Every touch stands alone. One question each. Under 120 words per email.

## 4. Audit
Four-pillar audit on the sequence as a whole, plus a check that every fact about the account is in the account file or the brief. Flag anything that isn't.

## 5. For a list of accounts
If the operator gives several accounts, write one sequence per account, each with its own signal. Never reuse Touch 1 across accounts. Save each to `campaigns/<campaign-name>/outbound/<account>.md` and produce a summary table:

```
Account | Contact | Signal | Play | Subject line | Score
```

## 6. Report
The sequence, the score, any facts that need checking, and the CRM fields to set (see `revops/crm-conventions.md`).
