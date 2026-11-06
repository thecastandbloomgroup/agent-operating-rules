# Fit to the work and fit to the test give close rates but judge different actions: results of one rejudge

## Headline

On the 104 unmarked actions, the judges found the domain right in 76% for fit to the work and 69% for fit to the test. So the gap is 7 points, but the two arms differ on 37 actions.

1. Fit to the work: 79 of 104 actions. Fit to the test, with today's instruction: 72 of 104. The original judges of these runs gave 71 of 104.
2. The gap of 7 points is under the mark of 10 points, so the page can keep one overall rate.
3. However, the arms give another answer on 37 of 104 actions, and the differences cancel by label. The work judge accepts all 30 Complicated labels, against 19 for the test judge, and it rejects 4 of 5 Chaotic labels.
4. The two arms cost 5.35 USD, under the mark of 10 USD.

## Background

The [plan](2026-11-06-judge-work-plan.md) set three numbers to report before any call. The work arm judged the 120 actions behind the domain rate of the evaluations page with `bin/judge-actions.py --work`. Each call had no expected answer, and the user's 24 marks came as examples. The test arm judged the same actions with today's built-in instruction, as the control.

## Relevance

The overall domain rate barely moves when the judge looks at the work in place of the test. So a reader can keep the rate, but a rate for one label depends on which question the judge answers.

## Information

This section gives the rates, the differences by label, and the limits.

### The rates

| Group                  | Fit to the work | Fit to the test | Original judges |
| ---------------------- | --------------- | --------------- | --------------- |
| 104 unmarked actions   | 79 (76%)        | 72 (69%)        | 71 (68%)        |
| 16 marked actions      | 13              | 11              | 9               |

[1]

The test arm and the original judges differ by one action. So the newer built-in instruction did not move the rate of fit to the test.
[1]

### The differences by label

| Label       | Actions | Fit to the work | Fit to the test | Work only | Test only |
| ----------- | ------- | --------------- | --------------- | --------- | --------- |
| Clear       | 48      | 34              | 37              | 6         | 9         |
| Complicated | 30      | 30              | 19              | 11        | 0         |
| Complex     | 16      | 9               | 9               | 2         | 2         |
| Chaotic     | 5       | 1               | 5               | 0         | 4         |
| Confused    | 5       | 5               | 2               | 3         | 0         |

[1]

- **Complicated is accepted every time.** A step that needs analysis is Complicated in the user's notes, and the work judge follows that view. The test judge rejects 11 of these labels, because the expected answer of the test names another domain for the prompt.
  [1]
- **Chaotic is rejected 4 of 5 times.** All four are first steps of prompt H2: name one lead and freeze replies. The work judge calls three of them a known crisis practice, so Clear, and one a step that needs facilitation. Its notes cite the user's calls on similar steps of the sheet. The test judge accepts all five, because the expected answer names Chaotic for that step.
  [1]
- **Clear moves both ways.** The arms swap 15 of 48 Clear labels, so on Clear the two questions disagree the most.
  [1]

### Limits

- **The work judge is not the user.** On the marked sheet it reached a kappa of 0.18 to 0.24 with the user, under the mark of 0.40 for trust. So its rate is still the judges' view.
- **One run per arm.** The reruns found that one run moves by up to 0.06 in kappa. A rate on 104 actions moves by a few points for the same reason [inference].
- **The examples come from these runs.** 16 of the 120 actions are rows that the user marked, so they are reported apart.

## End

I recommend that we:

1. Keep one overall domain rate on the evaluations page, and add that the two questions differ by label.
   Increment: one paragraph on the page. Blocker removed: a reader who reads a rate for one label as the user's view.
   Test (evaluative): the page gives the rate of each question and names Complicated and Chaotic as the labels where they split.
   Domain: Clear. Reason: deduction, because this file gives the numbers.
2. Keep the built-in judge for the ladders, because the tests define what a model should answer.
   Increment: none. Blocker removed: none new.
   Test (deterministic, Gherkin):
   Given `bin/judge-actions.py` on main
   When it runs with no `--work`
   Then each call carries the expected answer.
   Domain: Clear. Reason: deduction, because the unit test checks it.
3. Review the expected answers of the prompts behind the 11 Complicated and 4 Chaotic splits, to see whether the tests or the labels are wrong.
   Increment: read 15 actions and their tests, and write one table. Blocker removed: a test whose expected answer could disagree with the user's view.
   Test (evaluative): each of the 15 rows names the prompt, the expected domain, and whether the expected answer allows the label.
   Domain: Complicated. Reason: analysis, because each test can be read against the Cynefin definitions.

## Follow-up

References:

[1] The action-checks-work.csv, action-checks-test.csv, and action-checks.csv files of the runs 2026-11-01-reason-examples, 2026-11-03-cynefin-questions, and 2026-11-01-split-first-c, judged 2026-11-06, with the marks in `2026-11-05-human-marking/sheet.csv`. [P]
