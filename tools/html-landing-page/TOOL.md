# Tool: html-landing-page

**Turns approved landing page copy into a branded HTML file**

---

## When to run

Automatically, after landing page copy has passed the four-pillar audit. Never before. Also when the operator asks for HTML.

## Steps

1. Read `tools/html-landing-page/template.html`.
2. Replace every `{{PLACEHOLDER}}` with the approved copy:

```
{{PAGE_TITLE}}                Campaign or page name (browser tab)
{{HERO_HEADLINE}}             H1
{{HERO_SUBHEADLINE}}          Subheadline
{{HERO_CTA_TEXT}}             Primary button text
{{PROBLEM_HEADLINE}}          Problem section H2
{{PROBLEM_BODY}}              Problem copy, wrapped in <p> tags
{{CHANGES_HEADLINE}}          What changes H2
{{CHANGE_1_TITLE}} / _BODY    Point 1 (repeat for 2 and 3)
{{HOW_HEADLINE}}              How it works H2
{{STEP_1_WHEN}}               Time marker, e.g. "Day 0", "Week 2"
{{STEP_1_TITLE}} / _BODY      Step 1 (repeat for 2 to 4)
{{PROOF_HEADLINE}}            Proof H2
{{PROOF_1}} to {{PROOF_3}}    Approved proof points
{{OBJECTIONS_HEADLINE}}       Questions H2
{{OBJECTION_1_Q}} / _A        Objection 1 (repeat for 2)
{{FINAL_CTA_HEADLINE}}        Final headline
{{FINAL_CTA_BODY}}            One sentence
{{FINAL_CTA_TEXT}}            Button text, same as the hero
```

3. If a section has fewer items (for example 3 steps), delete the unused block rather than leaving a placeholder.
4. Check no `{{` remains in the file.
5. Escape `&`, `<` and `>` in copy.
6. Save to `campaigns/<campaign-name>/index.html`.
7. Tell the operator the path, and that it opens in any browser.

## Don't

- Change the template's colours, fonts or structure. Brand lives in the template.
- Add images, stock photos or icons.
- Add copy that didn't pass the audit.
