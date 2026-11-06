# A plan: show the judges the user's marks as examples

## Headline

A judge that sees the user's own marks on other rows targets the miss of both judges on domain fit.

1. Both judges matched the user on domain fit below chance: kappa -0.20 and -0.40 over 24 rows.
2. An instruction built from a summary of the user's notes left both judges at -0.20. So a summary does not carry the user's judgment.
3. This probe shows each judge the other 23 rows with the user's answers and notes, and asks it to judge the row left out. Each row is held out once, so no row judges itself.

## Background

The [themes results](2026-11-05-judge-themes-results.md) found that the themes instruction made the judges agree with each other in 22 of 24 rows. However, it did not move them toward the user. Examples carry cases that a summary loses, so this probe tests examples in place of rules.

## Design

1. `bin/judge-loo.py` reads `sheet.csv` and `items.json` of the marking folder. For each row, it adds the other 23 rows, with the user's answers and notes, to the built-in judge instruction. The input of each call stays the same as in `bin/judge-actions.py`.
2. Arm one: the first judge, of another provider than the executor of each row.
3. Arm two: the second judge, Gemini 4 Argon at high effort.
4. Compute the agreement and kappa with the user on the label question for each arm.

Step 4 MUST NOT start until the unit tests of step 1 pass.

## Metrics and pass marks

1. **First judge.** The kappa on the label question is 0.40 or more. Baseline: -0.20.
2. **Second judge.** The kappa on the label question is 0.40 or more. Baseline: -0.40.
3. **Cost.** Both arms cost under 4 USD.

The probe passes when either judge meets its mark. The earlier control runs of the [themes results](2026-11-05-judge-themes-results.md) set the noise: the old instruction scored -0.32 on a rerun.

## Cost and stop rule

48 judge calls of about 4,500 words of input each cost about 3 USD. One run, then the write-up. A pass does not change `bin/judge-actions.py` until a second marked sheet confirms it, because the examples come from one marker.
