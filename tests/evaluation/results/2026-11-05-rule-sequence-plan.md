# A plan: probe the sequence of the rules

## Headline

Rules 0.8.2 move two pieces of the rules to the point of use, and a script-only run tests both for about 4 USD.

1. The precedence line of the organization pilot moves to the end of the rules, as Section 8 item 4. In Section 0, it lifted A3 structure from 8 to 12 of 18, under the mark of 14.
2. The self-test gains one sentence: check the lines one at a time, in this order, each against the response. Checklists lifted self-review by 4 to 8 points in published evals.
3. The run needs no judge, so it costs about 4.10 USD, and the pass marks are set before it.

## Background

Three wording probes did not move the domain judgments, and each added rule lowers compliance with all the rules (2026-11-03-rule-changes-research.md). So this probe changes where two rules sit, not what they ask. The position of a rule is the one lever of the research note that no probe has tested on its own.

The variant is `2026-11-05-rule-sequence-plan/rules.md`, in this folder only. Against rules 0.8 it changes three lines: the version line, the self-test lead, and the new Section 8 item 4. The item keeps the words of the organization pilot (2026-11-03-organization-line), so the arms differ only in position.

## Design

Send A1, A2, A3, X1, X2, H2, and T2 to the six main executors, three samples each, with no judge:

```sh
doppler run -- python3 bin/run-evaluation.py --no-judge \
  --prompts A1,A2,A3,X1,X2,H2,T2 --samples 3 \
  --rules tests/evaluation/results/2026-11-05-rule-sequence-plan/rules.md \
  --run-id 2026-11-05-rule-sequence
```

Then score with `bin/script-checks.py`. The run folder of the plan already exists, so the run takes its own id.

## Metrics and pass marks

1. **Organization (A3).** Structure passes in 14 or more of 18 answers. The arms to beat: 8 of 18 with no line (2026-11-01-affective-baseline), 12 of 18 with the line in Section 0 (2026-11-03-organization-line).
2. **Evaluate.** The self-test lines that the script checks, except the word counts, are right in 76 or more of 90 answers. The reason-form arm sits at 78% (2026-11-03-reason-form).
3. **Guard: length.** Answers with no long sentence on X1, X2, H2, and T2 stay at 29 or more of 72, the reason-form rate.
4. **Guard: labels.** Labels with a reason stay at 55 or more of 72. The reason-form arm had 60.

The probe passes only when both metrics pass and both guards hold. A pass releases the two changes; the release picks its own version number. A fail leaves the rules at 0.8, and the write-up names the failed metric.

## Cost and stop rule

`bin/run-evaluation.py --plan` estimates 4.10 USD for 126 units with no judge. No second stage exists, so the stop rule is the run itself: one run, then the write-up. The run waits for a funded budget.
