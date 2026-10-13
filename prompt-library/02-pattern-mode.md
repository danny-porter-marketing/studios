# Pattern Mode

**About 15 minutes · One structured asset**

---

## When to use

Any asset with a craft guide: landing page, outbound sequence, LinkedIn post, case study, one-pager, blog article, event playbook, LinkedIn ad.

## What to load

Everything in Quick Mode, plus:
- The voice file paired to the reader (see the persona file)
- The craft guide for the asset type
- The industry file if the brief names a vertical
- The service file if the brief is about a service
- The account file in `accounts/` if one exists

## Steps

1. Check the brief. Ask once for anything missing.
2. Say in one line which files you loaded. This lets the operator spot a wrong persona or voice early.
3. Draft following the craft guide's shape exactly.
4. Run the four-pillar audit. Revise until 90 or above.
5. Send to the router agent for review. List any flags under the output.
6. Run the tool if the craft guide says so (landing pages: HTML).
7. Save the final asset to `campaigns/<campaign-name>/` if a campaign is named.

## Output format

```
Loaded: CLAUDE · BRAND · MESSAGING · use-cases · persona/cto · voice/engineer-to-engineer · craft/outbound-sequence · industry/fintech

[The asset]

Brand 24 · Messaging 24 · Persona 23 · Craft 24 = 95
Weakest: persona. [One sentence.]
Reviewer flags: [list, or "none"]
Saved: campaigns/<name>/<file>.md
```
