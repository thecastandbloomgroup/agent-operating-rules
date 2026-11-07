# The named second turn repairs 26 of 27 P5 failures: results of one probe

## Headline

The probe passed every mark: a turn that names the missing check repaired 26 of 27 units, against 8 of 27 for a plain retry.

1. The named turn beat the retry by 18 units, over the mark of 8.
2. GPT-6.1 Sol was repaired in 17 of 17 units with the named turn, and in 0 of 17 with the retry.
3. Under the retry, GPT-6.1 Sol checked its work by reading the files back, and it never called check_file.
4. The two arms cost 2.08 USD, under the mark of 3 USD.

## Background

The [plan](2026-11-07-p5-repair-plan.md) fixed four marks before any call. Each of the 27 units is a P5 failure with no check after the last write. The script `bin/repair-psychomotor.py` started each unit from the end state of its sandbox. The named turn said that no check_file call ran after the last write. The retry asked only for a check.

## Relevance

The weakest level of the pool has a repair that holds at five times the size of its first test. So a harness that names the missing check after a P5 failure lifts that level for every model tested [inference].

## Information

This section gives the marks and the repairs per model.

### The marks

| Mark                                         | Result              | Pass |
| -------------------------------------------- | ------------------- | ---- |
| Repair: the named turn 22 or more of 27      | 26 of 27            | yes  |
| Lift: 8 or more above the retry              | 26 against 8        | yes  |
| Per model: GPT-6.1 Sol 14 or more of 17      | 17 of 17            | yes  |
| Cost under 3 USD                             | 1.04 and 1.04 USD   | yes  |

[1]

### The repairs per model

| Model         | Units | Named turn | Retry |
| ------------- | ----- | ---------- | ----- |
| GPT-6.1 Sol   | 17    | 17         | 0     |
| GLM 5.3 Flash | 7     | 7          | 6     |
| Kimi K3       | 3     | 2          | 2     |

[1]

- **The retry works for GLM but not for GPT.** GLM ran check_file under both turns. GPT-6.1 Sol answered the retry with 28 read_file calls and 13 list_files calls over 13 units, and no check_file call.
  [1]
- **Each failure left is the same failure.** All 19 retry failures and the one named failure still ran no check after the last write.
  [1]

So the word that does the work is the name of the tool, as in the probe of 2026-11-05 [inference].

### Limits

- **A second turn is not a first turn.** The repair lifts P5 after a failure is found. The first-turn rate of P5 stays at 90 of 120.
- **The script finds the failure.** The named turn needs the grader to name the missing check first. A harness without a grader cannot send it.

## End

I recommend that we:

1. Report P5 with two rates on the evaluations page: the first turn and the first turn with the named repair.
   Increment: one sentence and one link. Blocker removed: a page that gives only the first-turn rate of the weakest level.
   Test (evaluative): the page gives 90 of 120 for the first turn, and the repair of 26 of 27 failures.
   Domain: Clear. Reason: deduction, because this file gives the numbers.
2. Name the tool in each second turn that `bin/second-turn.py` sends after a failed check of form.
   Increment: one review of the second-turn messages, with no paid call. Blocker removed: retries that let a model check by reading.
   Test (evaluative): each message of a check failure names the tool or the part that failed.
   Domain: Complicated. Reason: analysis, because each message can be read against these results.
3. Keep the first-turn rate as the score of the ladder, because a repair needs a grader that most harnesses lack.
   Increment: none. Blocker removed: none new.
   Test (deterministic, Gherkin):
   Given `bin/ladder-scores.py` on the 20-trial runs
   When it scores P5
   Then it counts the first turn only.
   Domain: Clear. Reason: deduction, because the repair runs sit in their own folders.

## Follow-up

References:

[1] The eight `2026-11-07-p5-repair-*` run folders: tool-checks.csv, calls.csv, and the transcripts, run 2026-11-07. [P]
