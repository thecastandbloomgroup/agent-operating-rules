# Every model has a psychomotor score: results of 20 trials per level

## Headline

All six models now have 20 trials at each of the seven psychomotor levels, and only Sonnet 5.5 reaches 80% on every level.

1. The scores are Sonnet 1.00, Kimi K3 0.96, Grok 4.7 0.91, GLM 5.3 Flash 0.89, GPT-6.1 Sol 0.88, and Gemini 3.8 Flash 0.70.
2. Each model below 1.00 fails on one or two levels. For example, GPT-6.1 Sol passed Complex overt response in 3 of 20, and Grok passed Set in 13 of 20.
3. Gemini hit the step cap in 37 of its 140 units, and it passed P5 and P7 in 20 of 20. So its score measures the loop more than its skill with the tools [inference].
4. The four runs cost 22.28 USD, under the cap of 25 USD.

## Background

The [plan](2026-11-06-psychomotor-20-plan.md) fixed three marks before any call, and the user chose to fund it. The account ran out of credits midway, and 326 units failed with HTTP 402 or 401. After the user added credits, `bin/run-psychomotor.py --rerun-failed` ran only those units again, in place.

## Relevance

The psychomotor ladder now ranks all six models one by one. So a reader can pick a model for tool work by its weak level, not by a pooled rate.

## Information

This section gives the marks, the scores, the failures by model, and the limits.

### The marks

| Mark                                         | Result                        | Pass |
| -------------------------------------------- | ----------------------------- | ---- |
| Trials: 20 or more per level for each model  | 20 per level for all six      | yes  |
| Score: a psychomotor score for each model    | six scores                    | yes  |
| Cost under 25 USD                            | 22.28 USD                     | yes  |

[1]

After the rerun, no unit failed on the API or the network.
[1]

### The scores

| Level                  | Sonnet | Kimi | Grok | GLM | GPT | Gemini |
| ---------------------- | ------ | ---- | ---- | --- | --- | ------ |
| Perception             | 20     | 20   | 19   | 20  | 20  | 11     |
| Set                    | 20     | 20   | 13   | 20  | 20  | 13     |
| Guided response        | 20     | 20   | 20   | 20  | 20  | 13     |
| Mechanism              | 20     | 20   | 20   | 20  | 20  | 12     |
| Complex overt response | 20     | 17   | 18   | 12  | 3   | 20     |
| Adaptation             | 20     | 20   | 20   | 20  | 20  | 9      |
| Origination            | 18     | 17   | 17   | 13  | 20  | 20     |
| Score                  | 1.00   | 0.96 | 0.91 | 0.89 | 0.88 | 0.70  |

Each cell counts passes of 20 units. Only Sonnet's levels are cumulative, so its score is (L + p) / N with L = 7. Each other score is the mean of the seven rates.
[1]

### The failures by model

- **GPT-6.1 Sol skips the last check.** All 17 of its P5 failures ran no check after the last write. It passed every other level in 20 of 20.
  [1]
- **Grok writes before it looks.** All 7 of its Set failures wrote plan.md to another path. Three P7 procedures kept a banned word or a long sentence.
  [1]
- **Kimi fails late and small.** Its 3 P5 failures skipped the last check, and 3 P7 procedures failed on their form.
  [1]
- **Gemini loops on the simple prompts.** It hit the cap on P1 (7 units), P2 (4), P3 (7), P4 (8), and P6 (11). Outside the loop, it failed 5 units, and it passed P5 and P7 in 20 of 20.
  [1]

The [sandbox note results](2026-11-06-sandbox-note-results.md) found that a note that forbids other files ends the loop. That note also names a fail of P2 and P5, so the choice of a default waits on the user.

### Limits

- **One day, one rules version.** All trials ran on 2026-11-06 and 2026-11-07 with rules 0.9.
- **20 trials is a floor.** A 95% Wilson interval on 20 of 20 runs from 84% to 100%, so a mastery call at 20 trials can flip on a rerun.

## End

I recommend that we:

1. Decide the harness default for the Gemini loop, from the three options of the [answer note results](2026-11-06-answer-note-results.md).
   Increment: one answer from the user, then one change. Blocker removed: a score of 0.70 that measures the loop.
   Test (evaluative): the next psychomotor write-up states the option and the units at the cap of each model.
   Domain: Complicated. Reason: analysis, because each option has a known effect on what the ladder measures.
2. Probe the named second turn for GPT-6.1 Sol on P5, the repair that fixed 5 of 5 units before.
   Increment: 17 named turns and 17 plain retries, about 3 USD. Blocker removed: GPT's one weak level.
   Test (stochastic): the named turn repairs 14 or more of 17, and beats the retry by 5 or more.
   Domain: Complex. Reason: induction from 5 units, and GPT could fail in another way at 17.
3. Show the six scores on the evaluations page, with the cap count of each model.
   Increment: one table. Blocker removed: a page that ranks only two models.
   Test (evaluative): the table gives each model's score, its weakest level, and its units at the cap.
   Domain: Clear. Reason: deduction, because this file gives the numbers.

## Follow-up

References:

[1] `2026-11-06-psy20-gemini/`, `-gpt/`, `-grok/`, and `-kimi/`, with `2026-11-06-psychomotor-p1-p7/`, `2026-11-06-limits-sonnet/`, and `2026-11-06-limits-glm/`: tool-checks.csv, calls.csv, run.log, and run-refused.log, run 2026-11-06 and 2026-11-07. [P]
