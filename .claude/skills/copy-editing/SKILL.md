---
name: copy-editing
description: Strip AI writing patterns from any copy and rewrite it in the Corvane voice, in two passes. Use when asked to edit, humanise, tighten, clean up, or check copy, or when copy "sounds like AI".
---

# Copy editing

Two passes. The first removes patterns; the second fixes what still reads as machine-written.

## Load
`brand-guidelines/BRAND.md` (especially "AI writing patterns to strip" and the banned list in `CLAUDE.md`). If the copy has a known reader, load that persona and voice too.

## Pass 1: strip
Remove or rewrite every instance of:
- Banned words and em dashes
- Filler openers and signposting
- Negative parallelism ("It's not X, it's Y")
- Rule-of-three padding
- "-ing" tails ("...ensuring quality")
- Copula dodging ("serves as" becomes "is")
- Significance inflation and promotional adjectives
- Vague attribution
- Emoji and exclamation marks

## Audit
List the 2 to 4 things that still read as machine-generated after pass 1. Be specific: quote the phrase.

## Pass 2: fix
Rewrite those parts. Keep at least one rough edge; real writing isn't perfectly smooth. Keep the author's meaning and any facts exactly.

## Output

```
Draft (pass 1)
[text]

Still reads as AI
1. ...
2. ...

Final (pass 2)
[text]

What changed
[2 to 3 sentences]
```

If the copy has a reader and asset type, also give the four-pillar score for the final version.
