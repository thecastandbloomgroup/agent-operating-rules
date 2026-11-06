# A plan: a note on the use of the sandbox, for the Gemini loop at the step cap

## Headline

One line after the prompt, which says that the sandbox holds the task files only, targets the Gemini loop at the step cap.

1. Gemini hit the cap in 8 of 24, 1 of 8, and 7 of 28 units of three runs. Each time it wrote drafts of its answer to scratch files and checked them.
2. A check of text that writes no file cost Sonnet 4 passes on P5, so a change of the tools is ruled out.
3. A note changes only the first user turn, and the tools and the grader stay the same.

## Background

The [P1 to P7 results](2026-11-06-psychomotor-p1-p7-results.md) found the loop on P1, P2, and P3. A new tool changes which checks the models run, per the [check text results](2026-11-06-check-text-results.md). `bin/run-psychomotor.py --sandbox-note` adds this line after the prompt: "The sandbox holds the task files only. Do not write any other file. Give your answer in your reply, not in a file."

## Design

1. Probe arm: Gemini 3.8 Flash on P1, P2, and P3, 8 samples, with `--sandbox-note`: 24 units.
2. Control arm: the same 24 units with no note, run at the same time.
3. Guard arm: Sonnet 5.5 on P1, P2, and P3, 4 samples, with `--sandbox-note`: 12 units.
4. Grade each arm with `bin/check-psychomotor.py`.

## Metrics and pass marks

1. **Baseline.** The control has 4 or more of 24 Gemini units at the cap. Otherwise the loop did not occur that day, and mark 2 does not count.
2. **Cap.** The probe has 2 or fewer of 24 Gemini units at the cap.
3. **Passes.** Gemini passes in the probe are at least its passes in the control.
4. **Guard.** Sonnet passes 11 or more of 12 with the note.
5. **Cost.** All three arms cost under 3 USD.

The probe passes when marks 1 to 4 pass.

## Cost and stop rule

60 units at about 0.035 USD each, from the Gemini cost of 2026-11-05, cost about 2.1 USD. One round, then the write-up. A pass makes the note a default only in a later change, because it changes every ladder run.
