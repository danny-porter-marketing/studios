---
name: sheets-dashboard
description: Turn pasted marketing data or stats into a cleaned, formula-driven Google Sheets dashboard. Use when the operator pastes data, a CSV or a table and asks to analyse it, chart it, build a dashboard, or "put it in Sheets".
---

# Sheets dashboard

Pasted data in, Google Sheet out. Every number in the sheet is a live formula, so anyone can click a cell and see how it was built.

**Ground rule: never do arithmetic in your head.** All counting, summing and ratios happen in Python or in sheet formulas. You decide what to calculate; code calculates it.

Scripts live in `scripts/` next to this file:
- `build_dashboard.py`: cleaned CSV + JSON spec → styled .xlsx (Dashboard, Summary, Clean data, Raw data, Notes tabs)
- `upload_to_sheets.py`: .xlsx → native Google Sheet via the Drive API (one-time setup in the script header)
- `examples/practice_spec.json`: full worked example

Work in a new folder per run: `analysis/YYYY-MM-DD-<short-name>/`.

## 1. Capture

Save the pasted data **exactly as given** to `raw.csv` (or `raw.txt` if it isn't tabular yet). Don't fix anything at this stage. The raw tab is the audit trail.

If several tables were pasted (e.g. leads and spend), save each one separately.

## 2. Ask one question

Ask what decision the data needs to support, unless it's already clear. If there's no answer, pick one and state it: "I'll look at which channels produce pipeline, not just leads."

## 3. Profile before cleaning

Write and run a short pandas script that prints:
- row count and exact duplicates
- for each column: type, blanks, unique count, and the top values for text columns
- mixed date formats, numbers stored as text (currency symbols, commas, %), inconsistent spellings or casing of the same value
- anything that looks like a total row or a subtotal mixed in with the data

Tell the operator what you found in a short list **before** cleaning. This is the step that catches traps.

## 4. Clean

Write `clean.py`, which reads `raw.csv` and writes `clean.csv`. Rules:
- Every fix is explicit in code (a mapping dict, a parse rule), never edited by hand.
- Keep IDs. Drop exact duplicates only, and log how many.
- Blanks in grouping columns become `"Unknown"`, not dropped.
- Turn status or stage fields into **1/0 flag columns** (`is_mql`, `is_sql`, `is_won`). Then every metric in the sheet is a simple SUMIFS.
- Add value columns that only count when the flag is true (e.g. `won_value_eur`).
- Put lookup data (spend, targets) in its own CSV with a clean key column that matches the main data exactly.

Print a before/after row count and check the mappings left no unmapped values.

## 5. Check the numbers independently

Before building the sheet, compute the headline numbers (totals and the main breakdown) in pandas. These are the numbers you'll check the sheet against later.

## 6. Write the spec

Write `spec.json` (copy the structure from `examples/practice_spec.json`):
- **kpis**: 4 to 8 headline tiles. Pipeline metrics before volume metrics.
- **breakdowns**: one per useful grouping (channel, campaign, content, persona, region). Each breakdown gets volume, the outcome that matters, a rate, and a cost metric if spend exists. Use `highlight` on rates and costs. Use `exclude` to drop placeholder groups like `(none)`.
- **chart**: one per breakdown, on the metric that tells the story (usually a rate or cost, not volume).
- **notes**:
  - `findings`: 3 to 5 one-line conclusions with the number in them
  - `cleaning`: what was fixed and how many rows it touched
  - `caveats`: sample size, attribution limits, time lag, anything the data can't show
  - `next_steps`: 2 to 3 concrete actions

Use the plain, direct voice from the Voice layer. No em dashes.

## 7. Build and verify

```bash
python <skill>/scripts/build_dashboard.py spec.json dashboard.xlsx
```

Then recalculate and compare against step 5:
```bash
soffice --headless --convert-to xlsx --outdir /tmp/recalc dashboard.xlsx
```
Read the recalculated values with openpyxl (`data_only=True`) and confirm the KPIs and totals match the pandas numbers. Check there are no `#REF!`, `#DIV/0!` or `#NAME?` errors. If LibreOffice isn't installed, skip the recalculation and check the formulas once the sheet is in Google Sheets.

## 8. Send to Google Sheets

Use the first option that works:

1. **Direct upload (preferred):** `python <skill>/scripts/upload_to_sheets.py dashboard.xlsx "<title>"`. It prints the sheet URL.
2. **Drive connector:** for small files only (roughly under 30 KB / a few hundred rows), base64 the .xlsx and call the Google Drive `create_file` tool with `contentMimeType` set to the xlsx mime type. Drive converts it to a native Sheet. Larger files are slow and costly this way because the whole file passes through the conversation.
3. **Fallback:** give the operator the .xlsx path to drag into Google Drive. It opens as a Sheet.

After upload, read the sheet back (Drive `read_file_content`) and spot-check two numbers against step 5.

## 9. Report back

Reply with:
- the sheet link
- the 3 findings that matter most, each with its number
- the biggest caveat
- one automation that would make this run on a schedule (e.g. weekly pull from HubSpot, rebuild the dashboard, post a Slack alert for any campaign with spend and zero SQLs in 30 days)
