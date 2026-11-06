# With no expected answer, the judges move toward the user, but not to the mark: results of one probe

## Headline

The probe failed both label marks, but it is the first change that lifts either judge above chance agreement with the user.

1. With no expected answer in the input, the first judge matched the user on the label in 18 of 24 rows, a kappa of 0.24. The second judge matched in 17, a kappa of 0.18. The mark asked for 0.40.
2. The baseline was -0.01 for both, so the first judge rose by 0.25 and the second by 0.19. The noise of one rerun was 0.12, so each rise is less than twice the noise.
3. The two judges now agree with each other in 21 of 24 rows, against 24 in the leave-one-out probe. So they no longer answer as one.
4. The two arms cost 2.01 USD, under the mark of 3 USD.

## Background

The [plan](2026-11-06-judge-no-expected-plan.md) fixed three marks before any call. The probe repeats the [leave-one-out probe](2026-11-05-judge-loo-results.md) with one change. The input of each call has no expected answer. Item 1 of the instruction asks whether the label fits the work, with the five domain definitions of the marking page.

## Relevance

The expected answer of the test pulls the judges away from the user's view. So the domain rates of past runs measure fit to the test, and that is a different question from fit to the work [inference].

## Information

This section gives the marks, the rows that moved, and the rows still missed.

### The marks

| Mark                                   | Result                  | Pass |
| -------------------------------------- | ----------------------- | ---- |
| First judge, label kappa 0.40 or more  | 0.24, from -0.01        | no   |
| Second judge, label kappa 0.40 or more | 0.18, from -0.01        | no   |
| Cost under 3 USD                       | 1.28 and 0.73, 2.01 USD | yes  |

[1]

### The rows that moved

- **Three rows moved to the user.** On row 24, both judges now reject the Chaotic label with the user. On row 17, both now accept the Clear label with the user. On row 3, the first judge now accepts the Confused label with the user.
  [1]
- **Two rows moved away from the user.** On row 11, the first judge now calls a Clear step Complicated. On row 23, the second judge now calls a Complex probe Complicated. The user accepted both labels.
  [1]

### The rows still missed

- **Three "no" rows of the user stay missed.** On rows 7, 16, and 20, the user named Complicated because the step needs expertise or analysis. Both judges still accept the label. For example, on row 16 the judge accepts a Complex probe of a retrospective, and the user names the facilitation expertise.
  [1]
- **Two "yes" rows of the user stay missed.** On rows 12 and 13 the user accepted a Clear label, and both judges call the step Complicated. On row 13, the judge names an expert contract review, and the user's note names a risk of cost overruns but still accepts Clear.
  [1]

So the rows left are close calls on how much expertise makes a step Complicated [inference]. On rows 16 and 20 the user names expertise that the judges do not see. On rows 12 and 13 the judges name analysis that the user accepts as Clear.

### Limits

- **Few "no" answers.** The user said no in 5 of 24 rows, so each of those rows moves the kappa by a large step.
- **One sheet, three probes.** Each probe used the same 24 rows. So a fourth change chosen on this sheet risks a fit to these rows alone.
- **One marker.** A pass would still have needed a second sheet.

## End

I recommend that we:

1. Stop paid probes on this sheet, and mark a second sheet of 24 rows with more steps that need expertise.
   Increment: one sheet of 24 rows, about 30 minutes of the user's time. Blocker removed: three probes on the same 24 rows, with only 5 "no" answers.
   Test (evaluative): the sheet holds at least 8 rows where a judge with no expected answer calls the step Complicated.
   Domain: Complicated. Reason: analysis, because the sample can be chosen from the judged rows.
2. Write on the evaluations page that the domain rates measure fit to the expected answer of the test, not fit to the work.
   Increment: one paragraph on the page. Blocker removed: a reader who takes the rates as the user's view.
   Test (deterministic, Gherkin):
   Given the evaluations page
   When a reader looks for the domain rates
   Then the page says that the judges see the expected answer.
   Domain: Clear. Reason: deduction, because the results files show it.
3. On the second sheet, judge with `--no-expected` and the first sheet as examples, as a held-out test.
   Increment: 48 calls, about 2 USD. Blocker removed: no held-out test of the judge.
   Test (stochastic): the label kappa with the user reaches 0.40 or more for either judge over the 24 new rows.
   Domain: Complex. Reason: induction from one marker, and the new rows could hold other close calls.
   Step 3 MUST NOT start until the sheet of Step 1 is marked.

## Follow-up

References:

[1] `2026-11-06-judge-no-expected/noexp-first.csv` and `noexp-argon.csv`, judged 2026-11-06, with the user's marks in `2026-11-05-human-marking/sheet.csv`. [P]
