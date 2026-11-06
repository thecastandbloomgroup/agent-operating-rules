# The user's own marks lift the judges to chance, not to the mark: results of one probe

## Headline

The leave-one-out probe failed both label marks, because the judges still accept the label in 4 of the 5 rows where the user said no.

1. Each judge saw the user's marks on the other 23 rows as examples. Both then matched the user on the label in 16 of 24 rows, a kappa of -0.01. The mark asked for 0.40.
2. The kappa rose from -0.20 and -0.40, so the examples moved both judges up to chance. However, chance is not agreement.
3. The two judges gave the same answer in all 24 rows, against 22 under the themes instruction. So the examples made the judges consistent, as the themes did.
4. The two arms cost 2.18 USD, under the mark of 4 USD.

## Background

The [plan](2026-11-05-judge-loo-plan.md) fixed three marks before any call. For each of the 24 marked rows, `bin/judge-loo.py` added the other 23 rows, with the user's answers and notes, to the built-in judge instruction. Then the judge marked the row left out. The first judge followed the rule of another provider than the executor, and the second judge was Gemini 4 Argon at high effort.

## Relevance

Two instruction changes have now failed to make a judge match the user on the label. So the cause is likely in the input of each call, not in the instruction [inference].

## Information

This section gives the marks, the rows that the judges still miss, and the likely cause.

### The marks

| Mark                                   | Result                  | Pass |
| -------------------------------------- | ----------------------- | ---- |
| First judge, label kappa 0.40 or more  | -0.01, from -0.20       | no   |
| Second judge, label kappa 0.40 or more | -0.01, from -0.40       | no   |
| Cost under 4 USD                       | 1.31 and 0.87, 2.18 USD | yes  |

[1]

### The rows that the judges still miss

- **The judges catch 1 of the 5 rows where the user said no.** On row 19 both judges now reject the Chaotic label. On rows 7, 16, 20, and 24 both still accept the label.
  [1]
- **The judges reject 4 rows that the user accepted.** On rows 12, 13, and 17 the label is Clear, and both judges expect Complicated. On row 3 the label is Confused, and both expect Complex.
  [1]
- **Three rows moved to the user for the first time.** On rows 9, 14, and 21 every earlier judge run rejected the label, and both judges now accept it with the user.
  [1]

### The likely cause

Each call still gives the judge the expected answer of evaluation-tests.md, and the instruction asks whether the label fits it. The notes of the judges cite that expected answer on rows 12, 17, and 24. For example, the note on row 24 calls the hold "the stabiliser the test expects". The user judged the work of the action, with no expected answer in view. So the judges answer a different question from the user [inference].
[1]

### Limits

- **One marker.** The examples and the marks come from one person, so a pass would still have needed a second sheet.
- **One run per arm.** The control of the themes probe moved by 0.12 with no change. So the rise of the first judge, 0.19, is about one and a half times that noise.
- **Few no answers.** The user said no in 5 of 24 rows, so each of those rows moves the kappa by a large step.

## End

I recommend that we:

1. Keep the built-in judge instruction, and keep `bin/judge-loo.py` as a tool for the next marked sheet.
   Increment: none beyond this merge request. Blocker removed: a second failed change to the judge.
   Test (deterministic, Gherkin):
   Given `bin/judge-actions.py` on main
   When it runs with no `--instructions`
   Then it sends the built-in instruction.
   Domain: Clear. Reason: deduction, because the unit test checks it.
2. Probe a judge input with no expected answer. The judge sees the prompt and the action, and it asks whether the label fits the work, as the user did.
   Increment: one flag on `bin/judge-loo.py` and 48 calls, about 2 USD. Blocker removed: the judge and the user answer different questions.
   Test (stochastic): the label kappa with the user reaches 0.40 or more for either judge, over 24 left-out rows.
   Domain: Complex. Reason: induction from one marker, and the judge could lose the context that the expected answer gives.
3. Report the domain rates of past runs as the judges' rates until a judge passes.
   Increment: already done on the evaluations page. Blocker removed: none new.
   Test (evaluative): each domain rate on the page names the judge that set it.
   Domain: Clear. Reason: deduction, because the page states it.

## Follow-up

References:

[1] `2026-11-05-judge-loo/loo-first.csv` and `loo-argon.csv`, judged 2026-11-05, with the user's marks in `2026-11-05-human-marking/sheet.csv`. [P]
