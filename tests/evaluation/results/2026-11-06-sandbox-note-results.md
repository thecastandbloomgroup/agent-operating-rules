# A note on the use of the sandbox ends the Gemini loop: results of one probe

## Headline

The probe passed every mark. With the note, Gemini passed 24 of 24 units on P1 to P3, against 11 of 24 in the control.

1. No Gemini unit hit the step cap with the note, against 8 of 24 in the control. No unit wrote a scratch file, against 15 of 24.
2. P1 rose from 2 to 8 of 8, and P2 from 1 to 8 of 8. P3 held at 8 of 8 in both arms.
3. Sonnet passed 12 of 12 with the note, so the guard held.
4. The three arms cost 1.70 USD, under the mark of 3 USD.

## Background

The [plan](2026-11-06-sandbox-note-plan.md) fixed five marks before any call. `bin/run-psychomotor.py --sandbox-note` adds one line after the prompt: "The sandbox holds the task files only. Do not write any other file. Give your answer in your reply, not in a file." Gemini ran P1 to P3 with 8 samples in each arm, at the same time. Sonnet ran the same prompts with the note, as the guard.

## Relevance

The loop came from where the model put its answer, not from a lack of skill with the tools. However, the note as written also names a fail condition of two prompts, so it cannot become the default as it is [inference].

## Information

This section gives the marks, the effect per prompt, and why the note cannot be the default.

### The marks

| Mark                                   | Result                     | Pass |
| -------------------------------------- | -------------------------- | ---- |
| Baseline: control 4 or more at the cap | 8 of 24                    | yes  |
| Cap: probe 2 or fewer                  | 0 of 24                    | yes  |
| Passes: probe at least the control     | 24 against 11 of 24        | yes  |
| Guard: Sonnet 11 or more of 12         | 12 of 12                   | yes  |
| Cost under 3 USD                       | 0.60, 0.76, and 0.34 USD   | yes  |

[1]

The chance of 24 of 24 against 11 of 24 with no real effect is under 0.01%, by a one-sided Fisher exact test.
[1]

### The effect per prompt

| Prompt         | With the note | Control |
| -------------- | ------------- | ------- |
| P1, Perception | 8 of 8        | 2 of 8  |
| P2, Set        | 8 of 8        | 1 of 8  |
| P3, Guided response | 8 of 8   | 8 of 8  |

[1]

In the control, 8 units hit the cap and 5 more failed P1 or P2 for a write. On P3, scratch files do not fail the unit, so P3 passed in both arms.
[1]

### Why the note cannot be the default as it is

The sentence "Do not write any other file" names a fail of two prompts. P2 fails a plan.md in another folder, and P5 fails a scratch file. So the note gives away part of what P2 and P5 test, and it would lift those levels for every model [inference]. The sentence "Give your answer in your reply, not in a file" names no fail of any prompt. It targets the cause that the transcripts show.

### Limits

- **One model and three prompts.** The probe tested Gemini on P1 to P3 only.
- **One day.** The loop comes and goes by run, so one more same-day pair would confirm the effect.

## End

I recommend that we:

1. Probe the narrow note alone, "Give your answer in your reply, not in a file", with the same design.
   Increment: change the note text, then 60 units, about 1.7 USD. Blocker removed: a note that gives away part of P2 and P5.
   Test (stochastic): Gemini has 2 or fewer of 24 units at the cap, against 4 or more in the same-day control. Sonnet passes 11 or more of 12.
   Domain: Complex. Reason: induction from one probe, and the narrow note could miss the cause if the scratch files come from the check, not the answer.
2. If the narrow note passes, make it the default of `bin/run-psychomotor.py`, and mark later runs as a new series.
   Increment: one default and one line in each run.json. Blocker removed: a harness that costs one model three levels.
   Test (deterministic, Gherkin):
   Given `bin/run-psychomotor.py` with no flag
   When it builds the first user turn
   Then the turn ends with the narrow note.
   Domain: Clear. Reason: deduction, because the unit test checks it.
   Step 2 MUST NOT start until the test in Step 1 passes.
3. Keep `--sandbox-note` with its present text as an option, so these results can run again.
   Increment: none. Blocker removed: none new.
   Test (deterministic, Gherkin):
   Given `bin/run-psychomotor.py --sandbox-note`
   When it builds the first user turn
   Then the turn ends with the full note of this probe.
   Domain: Clear. Reason: deduction, because the unit test checks it.

## Follow-up

References:

[1] `2026-11-06-sandbox-note-probe/`, `2026-11-06-sandbox-note-control/`, and `2026-11-06-sandbox-note-guard/`: tool-checks.csv, calls.csv, and the transcripts, run 2026-11-06. [P]
