# Weekly Update

**Every Friday · Keeps use-cases.md current**

---

## What it does

Reads the past week of the #corvane-studios Slack channel (via the Slack connector), pulls out anything worth keeping, and adds it to `use-cases.md`. The knowledge base gets better every week without anyone writing it up by hand.

## Prompt

```
Run the weekly update.

1. Read messages from the last 7 days in #corvane-studios.
2. Extract:
   - Use cases from scoping calls
   - Objections and what worked
   - What's working (or not) in outbound
   - Campaign ideas and market observations
3. For each, check use-cases.md. If it's new, add it in the section's format. If it refines an existing entry, update that entry. Never delete entries.
4. Skip anything that names a prospect who hasn't agreed to be referenced, unless it's marked internal.
5. Show me the diff before saving, with one line per change saying why it's worth keeping.
```

## If Slack isn't connected

Paste the week's notes into the session and say "run the weekly update on these notes".

## Rules

- Facts only. Don't turn one comment into a trend.
- Write entries in plain language, in the brand voice.
- Mark anything uncertain with "(one mention)".
