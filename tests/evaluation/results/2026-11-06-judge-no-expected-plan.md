# A plan: judge the work of the action, with no expected answer

## Headline

A judge that does not see the expected answer of the test targets the likely cause of its miss on domain fit.

1. In the leave-one-out probe, both judges reached a label kappa of -0.01 with the user, under the mark of 0.40.
2. The judge notes quote the expected answer of evaluation-tests.md, for example "the stabiliser the test expects". The user judged the work of the action with no expected answer in view.
3. This probe repeats the leave-one-out probe with one change. The judge input has no expected answer, and item 1 asks whether the label fits the work.

## Background

The [leave-one-out results](2026-11-05-judge-loo-results.md) found that the user's own marks lift both judges only to chance. Two instruction changes have now failed, so this probe changes the input of each call in place of the instruction.

## Design

1. Add `--no-expected` to `bin/judge-loo.py`. It removes the expected answer from the input of each call. It replaces item 1 of the built-in instruction with the five domain definitions of the marking page. Items 2 and 3 stay the same.
2. Arm one: the first judge, of another provider than the executor of each row.
3. Arm two: the second judge, Gemini 4 Argon at high effort.
4. Compute the agreement and kappa with the user on the label question for each arm.

Step 4 MUST NOT start until the unit tests of step 1 pass.

## Metrics and pass marks

1. **First judge.** The kappa on the label question is 0.40 or more. Baseline: -0.01, from the leave-one-out probe.
2. **Second judge.** The kappa on the label question is 0.40 or more. Baseline: -0.01.
3. **Cost.** Both arms cost under 3 USD.

The probe passes when either judge meets its mark. The leave-one-out probe is the control, because only the expected answer and item 1 change.

## Cost and stop rule

48 judge calls cost about 2.2 USD, as in the leave-one-out probe. One run, then the write-up. A pass does not change `bin/judge-actions.py` until a second marked sheet confirms it. The domain rates of past runs depend on the expected answer, so a pass also needs a decision on what those rates measure.
