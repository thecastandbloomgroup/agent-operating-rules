# A check that writes no file does not help, and the loop it targets did not come back: results of one probe

## Headline

The probe failed. The loop at the step cap did not come back in the control, and the new tool cost Sonnet 4 passes on P5.

1. In the control arm, Gemini hit the 12-step cap in 1 of 8 units, against 7 of 8 in the run of 2026-11-05. So the baseline mark failed, and the cap mark cannot count.
2. With `check_text` on offer, P5 passed 14 of 24, against 19 of 24 in the control. Sonnet fell from 4 of 4 to 0 of 4 on P5, so the mark of no harm failed.
3. P3 passed 23 of 24 in both arms. No Gemini unit wrote a scratch file in the probe arm, against 1 in the control.
4. The two arms cost 3.73 USD, under the mark of 5 USD.

## Background

The [plan](2026-11-06-check-text-plan.md) fixed four marks before any call. It traced 7 Gemini failures at the cap to drafts of the answer that the model wrote to scratch files to check them. The probe arm offered `check_text`, a check of a text that writes no file. The control arm ran the same 48 units with the four file tools, at the same time, with rules 0.9.

## Relevance

The default tools stay as they are. The Gemini loop is now a rare event, not a gap that the harness must fix [inference].

## Information

This section gives the marks, the cause of the new failures, and the limits.

### The marks

| Mark                                              | Probe          | Control       | Pass |
| ------------------------------------------------- | -------------- | ------------- | ---- |
| Gemini at the cap: probe 2 or fewer of 8          | 1 of 8         | 1 of 8        | does not count |
| Baseline: control 5 or more of 8                  |                | 1 of 8        | no   |
| Gemini scratch files: probe 1 or fewer of 8       | 0 of 8         | 1 of 8        | yes  |
| No harm: each provider within 1 pass of control   | Sonnet 4 of 8  | Sonnet 8 of 8 | no   |
| Cost under 5 USD                                  | 2.00 USD       | 1.73 USD      | yes  |

[1]

### The cause of the new failures

- **Sonnet checked one file, not two.** On P5, the grader needs a `check_file` of both files after the last write. In all 4 probe units, Sonnet checked only notes/decisions.md, and it never called `check_text`. In the control, it checked both files in all 4 units.
  [1]
- **GPT-6.1 Sol checked text, not files.** In all 4 probe units of P5, its last check was a `check_text` call, so no `check_file` followed its last write. In the control, it ran no final check in 3 of 4 units, so P5 failed for it in both arms.
  [1]
- **Gemini used the tool most.** It sent 20 `check_text` calls over its 8 units. It passed 7 of 8 in each arm.
  [1]

So an extra check tool changes which checks the models run, and the change costs passes [inference]. The run of 2026-11-05 used rules 0.8.1. Rules 0.9 changed only the coded labels, so the drop in the loop is likely chance across days, not the rules [inference].

### Limits

- **Four samples per provider and prompt.** Sonnet's fall from 4 of 4 to 0 of 4 on P5 has a Fisher exact p of 0.03. That is one comparison of six, so a rerun has to confirm it.
- **One control.** One control arm cannot say how often the Gemini loop occurs. The two runs give 8 of 16 units at the cap.

## End

I recommend that we:

1. Keep the four file tools as the default, and keep `--check-text` only as an option that its results file documents.
   Increment: none beyond this merge request. Blocker removed: a tool change that costs passes.
   Test (deterministic, Gherkin):
   Given `bin/run-psychomotor.py` with no `--check-text`
   When it builds the tools of a call
   Then it sends the four file tools only.
   Domain: Clear. Reason: deduction, because the unit test checks it.
2. Count Gemini units at the cap in each later psychomotor run, and probe again only if the rate stays above 25%.
   Increment: one line in the write-up of each run. Blocker removed: a fix for a loop that may be rare.
   Test (stochastic): over the next 24 Gemini units, the share at the cap is reported against the 8 of 16 of these two runs.
   Domain: Complex. Reason: induction from two runs, and a change of model version could break the pattern.
3. Rerun P5 for Sonnet with and without `--check-text`, only if a later change makes the tool a default.
   Increment: 16 units, about 0.2 USD. Blocker removed: one comparison at 4 samples.
   Test (stochastic): Sonnet passes P5 in at least 7 of 8 units with the tool, against the control.
   Domain: Complex. Reason: induction from 4 samples, and a model update could break the pattern.

## Follow-up

References:

[1] `2026-11-06-check-text-probe/` and `2026-11-06-check-text-control/`: tool-checks.csv, calls.csv, and the transcripts, run 2026-11-06. [P]
