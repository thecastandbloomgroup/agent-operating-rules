# A plan: give the psychomotor tools a check that writes no file

## Headline

A check of a draft answer that writes no file targets the cause of each Gemini failure at the step cap on P3 and P5.

1. In the last full run, Gemini hit the 12-step cap in 3 of 4 units of P3 and 4 of 4 units of P5. No other provider hit the cap on these prompts.
2. Each of those 7 transcripts does the task in 4 to 6 steps. Then the model writes a draft of its answer to a scratch file, such as `draft.md`. It runs `check_file` on the draft until the cap.
3. The rules tell the model to check its answer before it sends it. The sandbox can check only files, so the rules and the tools pull against each other.

## Background

The [full psychomotor results](2026-11-05-psychomotor-full-results.md) name the step cap as one cause of the P5 failures. The transcripts of `2026-11-05-psychomotor-full-b/` show the loop. So the loop is a gap of the harness, not a skill that the ladder means to measure [inference].

## Design

1. Add a `check_text` tool to `bin/tool-sandbox.py`. It runs the checks of `check_file` on a text in the call. It writes nothing in the sandbox. `bin/run-psychomotor.py` offers it only with `--check-text`, so the default tools stay the same as in past runs.
2. Probe arm: P3 and P5, 4 samples, all six providers, with `--check-text`.
3. Control arm: the same units with no `--check-text`, run at the same time with the same rules.
4. Grade both arms with `bin/check-psychomotor.py`. The grader does not change, so a pass still needs a `check_file` of the task file after the last write.

Step 2 MUST NOT start until the unit tests of step 1 pass.

## Metrics and pass marks

1. **Cap.** Gemini units at the step cap: 2 or fewer of 8 in the probe arm. The control arm sets the baseline, and it must keep 5 or more of 8 for the mark to count.
2. **Scratch files.** Gemini units that write a file other than the task files: 1 or fewer of 8 in the probe arm.
3. **No harm.** For each other provider, the passes on P3 and P5 in the probe arm are at least the passes of the control arm, less 1.
4. **Cost.** Both arms cost under 5 USD.

The probe passes when marks 1, 2, and 3 pass.

## Cost and stop rule

96 units at about 0.03 USD each, from the last full run, cost about 3 USD. One round, then the write-up. A pass makes `--check-text` the default only in a later change, because it changes the tools of every ladder run.
