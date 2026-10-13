---
name: experiment-readout
description: Read out a finished A/B test with statistics run in code, check for traps, decide ship, keep or follow up, and turn the learning into a rule change via pull request. Use when asked to read out, analyse or evaluate an experiment or A/B test, or when results come in for an EXP file.
---

# Experiment readout

**Ground rule:** the script does the statistics. You interpret. Never estimate a p-value, probability or lift yourself.

## 1. Load
The `experiments/EXP-*.md` file and its results CSV in `experiments/data/`. If results arrive as a paste or export, save them to `experiments/data/EXP-NNN-results.csv` first, one row per contact, with a variant column and 0/1 outcome columns.

## 2. Run the script
```
python <skill>/scripts/readout.py experiments/data/EXP-NNN-results.csv \
  --primary <metric> --secondary <metrics> --guardrails negative_reply unsubscribed \
  --segment segment --planned-n <n from the EXP file> --control A
```
Use the metrics and planned n written in the EXP file. Don't change the primary metric after seeing the data; that's how false wins happen.

## 3. Interpret, in this order
1. **Validity:** sample ratio OK? Planned n reached? If either fails, stop. The verdict is "fix" or "keep running", whatever the numbers say.
2. **Guardrails:** any significantly worse? If so, don't ship.
3. **Primary metric:** what's the probability the challenger is better, and how wide is the interval? Ship threshold is 95% (set in `experiments/README.md`).
4. **Secondary metrics:** do they explain the primary result? Watch for divergence: more replies but fewer meetings means the variant attracts the wrong replies.
5. **Segments:** does one segment drive most of the gain, or does any segment move the other way? If so, the learning applies to that segment only, and the right next step is often a segment-specific follow-up test.
6. **Small numbers:** if a variant has fewer than 10 primary conversions, say the direction is the finding and the size is directional.

## 4. Decide
One of:
- **Ship challenger:** meets the threshold, valid, no guardrail breach
- **Keep control:** challenger worse, or no clear difference
- **Follow-up:** promising in one segment, or a clear direction without enough evidence. Write the follow-up hypothesis and add it to `experiments/backlog.md`, scored in code.

## 5. Write it up
Fill the Result (paste the script's tables), Decision, Learning and status in the EXP file. The learning is one sentence that would change how Corvane writes or targets. Every test has a learning, including tests with no winner.

## 6. Turn learnings into rules (only when shipping)
1. Create a branch `learning/EXP-NNN-short-name`.
2. Edit the rule file the learning applies to: a persona file, MESSAGING.md, a craft guide or `abm/account-entry-plays.md`. Add or change one line, written as a rule, citing the experiment with its key numbers. Example: "**Proven rule (EXP-001):** lead with roadmap delivery..."
3. Add the learning to `priorities.md` under "What we already know".
4. Commit, push and open a pull request titled `learning: EXP-NNN <one-line learning>`. The body includes the readout table and the decision.
5. Never merge it yourself. A person reviews and merges.

If the result is segment-specific, scope the rule to that segment ("for fintech CTOs..."). Never generalise beyond what the data shows.

## Report
Verdict first, then the three numbers that matter (primary lift, probability, sample), the trap you checked or found, the learning, and the pull request link or follow-up test.
