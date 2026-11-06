# The narrow note does not end the Gemini loop: results of one probe

## Headline

The probe failed. With only the note on where the answer goes, Gemini stayed at the step cap in 12 of 24 units.

1. The same-day control had 7 of 24 units at the cap, so the baseline held, and the cap mark failed.
2. Gemini passed 9 of 24 with the narrow note, against 10 of 24 in the control, so the passes mark failed too.
3. So the full note of the earlier probe worked through its other sentences, which forbid any other file [inference].
4. The four arms cost 2.87 USD, under the mark of 4 USD.

## Background

The [plan](2026-11-06-answer-note-plan.md) fixed six marks before any call. The [sandbox note results](2026-11-06-sandbox-note-results.md) found that a three-sentence note ended the loop. However, one sentence of it names a fail of P2 and P5. This probe kept only the sentence that names no fail.

## Relevance

No note that leaves the tests untouched has ended the loop yet. So a default for the harness now needs a choice between a clean test and a fair one for Gemini [judgment].

## Information

This section gives the marks, the P5 arm, and the choice that is left.

### The marks

| Mark                                   | Result                  | Pass |
| -------------------------------------- | ----------------------- | ---- |
| Baseline: control 4 or more at the cap | 7 of 24                 | yes  |
| Cap: probe 2 or fewer                  | 12 of 24                | no   |
| Passes: probe at least the control     | 9 against 10 of 24      | no   |
| Guard: Sonnet 11 or more of 12         | 12 of 12                | yes  |
| No give-away on P5: no rise of 2 or more | the largest rise is 1, for GPT-6.1 Sol | yes |
| Cost under 4 USD                       | 2.87 USD                | yes  |

[1]

Scratch files stayed: 18 of 24 probe units and 16 of 24 control units wrote a file other than the task files.
[1]

### The P5 arm

P5 passed 17 of 24 with the narrow note, against 18 of 24 in the P1 to P7 run of the same day. Sonnet passed 1 of 4, against 4 of 4, and each of its 3 failures checked one file, not both, after the last write. Sonnet passed P5 in 4 of 4 in each of three runs with no change to the prompt or the tools. It fell to 0 of 4 with `check_text` and to 1 of 4 with this note. So a change to the first turn or the tools costs Sonnet the second check on P5 [inference].
[1]

### The choice that is left

The full note ends the loop, but its sentence "Do not write any other file" names a fail of P2 and P5. Three options remain:

1. Use the full note as the default, and accept that P2 and P5 then test less.
2. Keep the tests clean, and report Gemini's low levels as a loop of the harness, not a lack of skill.
3. Change P2 and P5 so that they no longer fail on a file that the note forbids. For example, grade P2 on a look before the first write only.

This choice changes what the ladder measures, so it waits on the user [judgment].

## End

I recommend that we:

1. Decide which of the three options sets the default of the harness.
   Increment: one answer from the user, then one change to `bin/run-psychomotor.py` or the tests. Blocker removed: a harness that costs one model up to three levels.
   Test (evaluative): the answer names the option, and the write-up of the next full run states it.
   Domain: Complicated. Reason: analysis, because each option has a known effect on what the ladder measures.
2. Until then, report Gemini's psychomotor rates with its count of units at the cap.
   Increment: one column in the write-up of each run. Blocker removed: low rates read as low skill.
   Test (evaluative): each later psychomotor write-up gives the cap count of each provider.
   Domain: Clear. Reason: deduction, because the grader notes give the count.
3. Rerun Sonnet on P5 with 8 samples with the narrow note and 8 without, at the same time.
   Increment: 16 units, about 0.4 USD. Blocker removed: a harm to Sonnet that rests on two runs of 4 units.
   Test (stochastic): the harm counts as real when Sonnet passes 7 or more of 8 without the note, and 4 or fewer of 8 with it.
   Domain: Complex. Reason: induction from runs, and the day could break the pattern.

## Addendum: the Sonnet rerun of P5

Step 3 ran at once, with its test fixed in this file before the run. With the narrow note, Sonnet passed P5 in 2 of 8 units, and each failure checked one file, not both. Without the note, it passed 8 of 8. So the harm counts as real, with a one-sided Fisher exact p of 0.004. The two arms cost 0.53 USD.
[2]

The full sandbox note of the earlier probe ran its Sonnet guard on P1 to P3 only. So its effect on Sonnet's P5 is not measured, and option 1 needs that test first [inference].

## Follow-up

References:

[1] `2026-11-06-answer-note-probe/`, `-control/`, `-guard/`, and `-p5/`: tool-checks.csv, calls.csv, and the transcripts, run 2026-11-06. [P]

[2] `2026-11-06-sonnet-p5-note/` and `2026-11-06-sonnet-p5-plain/`: tool-checks.csv and calls.csv, run 2026-11-06. [P]
