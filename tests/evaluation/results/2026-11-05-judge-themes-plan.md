# A plan: teach the judges the user's view of domain fit

## Headline

A judge instruction that carries the four themes of the user's notes targets the miss of both judges on domain fit.

1. Both judges matched the user on domain fit below chance: kappa -0.20 and -0.40 over 24 rows.
2. The present instruction asks whether the label fits the expected answer of the test. The user's question asked whether the label fits the work of the action.
3. The probe judges the same 24 rows again with the new instruction. A run with the old instruction is the control, and the whole probe costs under 2 USD.

## Background

The [judge trust results](2026-11-05-judge-trust-results.md) found that the two judges agree with each other in 19 of 24 rows. However, the user gave the same answer in only 7 of those. The user's notes form four themes. The largest is that a step that needs expertise or facilitation is Complicated. The themes come from these same 24 rows, so a pass here is in-sample. A held-out sheet must confirm it.

## Design

1. Let `bin/judge-actions.py` take `--instructions FILE`, which replaces its built-in instruction. The input of each call stays the same.
2. Write the themes instruction in `2026-11-05-judge-themes/instructions.txt`. It asks whether the label fits the work of this action, with the expected answer of the test as context. It adds the four themes as tests of fit.
3. Write one actions CSV per run folder from the sheet, so each arm judges the same 24 rows.
4. Arm one, themes: both judges with the new instruction. The first judge keeps its rule of another provider than the executor, and the second judge is Gemini 4 Argon at high effort.
5. Arm two, control: the first judge with the old instruction. Its spread from the first run shows how far a judge moves with no change.
6. Compute the agreement and kappa with the user for each arm and each question.

Step 6 MUST NOT start until the unit tests of step 1 pass.

## Metrics and pass marks

1. **First judge.** Under the themes instruction, the kappa on the label question is 0.40 or more. Baseline: -0.20.
2. **Second judge.** Under the themes instruction, the kappa on the label question is 0.40 or more. Baseline: -0.40.
3. **Control.** The control's kappa on the label question stays under 0.20. If the control also reaches 0.40, the rise is noise, and marks 1 and 2 do not count.
4. **Cost.** All three arms cost under 2 USD.

The reason question is reported but has no mark, because the user said yes in 23 of 24 rows.

## Cost and stop rule

72 judge calls at about 0.02 USD each cost about 1.4 USD. One run, then the write-up. A pass moves the instruction into `bin/judge-actions.py` only after a held-out sheet confirms it.
