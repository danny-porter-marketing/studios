---
name: outbound-export
description: Export approved, per-account outbound sequences to Instantly (email) and HeyReach (LinkedIn) as import files with each contact's copy stored in custom variables, validated before import, always into paused campaigns. Use when asked to push, export, load or send sequences to Instantly, HeyReach or another sending tool.
---

# Outbound export

The copy is written and audited in Studios. The sending tool only handles timing and delivery. Each contact's personalised copy travels as **custom variables**, so the tool's sequence is just `{{t1_body}}`, `{{t3_body}}` and so on.

## 1. Check inputs
- Sequences: one approved file per account in `campaigns/<name>/outbound/<account>.md`, written by the `outbound-sequence` skill and passing the audit. Never export a sequence that hasn't passed.
- Contacts: `campaigns/<name>/contacts.csv` with columns `sequence, first_name, last_name, email, linkedin_url, company, title`. `sequence` is the account file name without `.md`.

If contacts come from a CRM export, map them to these columns first and save the CSV. Don't invent emails or profile URLs. Missing data stays missing and gets flagged.

## 2. Run the export
```
python <skill>/scripts/export_sequences.py \
  --sequences campaigns/<name>/outbound \
  --contacts campaigns/<name>/contacts.csv \
  --out campaigns/<name>/export
```
Add `--html-breaks` if the tool shows line breaks badly in a test send.

## 3. Read the report
`export-report.md` lists:
- **Blocking:** missing sequence, missing or invalid email, missing LinkedIn URL (HeyReach drops these silently), duplicate email, em dash or banned word, unfilled `{{placeholder}}`, LinkedIn note over 300 characters
- **Warnings:** emails over 120 words, LinkedIn notes over 200 characters

Fix every blocking item (or remove that contact) and re-run until the verdict is "Ready to import".

## 4. Load into the tools, paused
Follow `sequence-setup.md`:
- **Instantly:** import `instantly.csv` into a new campaign, map the `t{N}_subject` and `t{N}_body` columns as custom variables, and set each step's subject and body to the variables. If the Instantly MCP server is connected (`mcp.instantly.ai`, API key stored as a network secret), you can create the campaign and add leads through it. Leave the campaign **paused**.
- **HeyReach:** import `heyreach.csv`, or add leads via the API's add-leads-to-campaign endpoint with `customUserFields`. Use `{linkedin_note}` from the variable dropdown in the connection request step. Leave the campaign **paused**.

## 5. Hand over
Never activate a campaign. Tell the operator: campaign names, lead counts, and "send yourself a test, check 2 or 3 leads' variables, then launch."

Log the CRM campaign name per `revops/crm-conventions.md` so replies and meetings come back to the right campaign for the weekly optimisation run.

## Report
Lead counts per tool, blocking items fixed or removed, warnings, file paths, and what the operator must do before launching.
