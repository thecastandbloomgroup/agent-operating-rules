# The themes instruction moves the judges together, not toward the user: results of one probe

## Headline

The themes instruction failed both label marks, because the judges applied the expertise theme to steps that the user called Clear.

1. With the themes instruction, both judges matched the user on the label in 11 of 24 rows, with a kappa of -0.20. The mark asked for 0.40.
2. The control, the old instruction run again, gave a kappa of -0.32, so the control mark held. However, it has nothing to compare against, because the themes arm did not rise.
3. The two judges now agree with each other in 22 of 24 rows, against 19 before. So the instruction makes the judges consistent, but it does not make them match the user.
4. The three arms cost 1.48 USD, under the mark of 2 USD.

## Background

The [plan](2026-11-05-judge-themes-plan.md) fixed four marks before any call. The themes instruction asks whether the label fits the work of the action. It adds the four themes of the user's notes as tests of fit. Both judges marked the same 24 rows with it. The first judge also marked them with the old instruction as a control.

## Relevance

The judge instruction is not the lever for the label question. So the next probe has to give the judge the user's own answers, not a summary of them.

## Information

This section gives the marks, the rows that moved, and the reason question.

### The marks

| Mark                                 | Result                       | Pass |
| ------------------------------------ | ---------------------------- | ---- |
| First judge, label kappa 0.40 or more | -0.20, the same as the baseline | no   |
| Second judge, label kappa 0.40 or more | -0.20, from -0.40           | no   |
| Control, label kappa under 0.20      | -0.32                        | yes  |
| Cost under 2 USD                     | 1.48 USD                     | yes  |

[1]

### The rows that moved

- **The theme fixed 3 rows.** On rows 5 and 15, the judges now accept a Complicated label that the user accepts. On row 7, both judges now reject a Clear label with the user, and they expect Complicated.
  [1]
- **The theme broke 4 rows.** On rows 1, 11, 12, and 22, the user and the control accepted a Clear label. Under the themes instruction, at least one judge now calls each of them Complicated.
  [1]
- **The theme missed 4 rows where the user said no.** On rows 16, 19, and 20 the user named Complicated, and on row 24 the user named Clear. Both judges still accept the label under both instructions.
- **Four more rows stay missed in every arm.** On rows 3, 9, 13, 14, and 21 the user accepted the label, and every judge run rejected it.
  [1]

So the judges read "needs expertise" more broadly than the user [inference]. The user's view of a step depends on its content, and four lines of instruction do not carry that.

### The reason question

The kappa on the reason question rose to 0.47 and 0.23 under the themes instruction. However, the control rose to 0.36 with the old instruction, from 0.10 in the first run. The first run used an older instruction than today's built-in one, so the reason rise comes from that change, not from the themes. The user said yes in 23 of 24 rows, so this kappa moves by a large step for each row.
[1]

### Limits

- **In-sample.** The themes came from these 24 rows, so a fail here is strong evidence that the instruction does not carry the user's view. A pass would have needed a held-out sheet.
- **One run per arm.** The control moved by 0.12 on the label with no change of instruction. So a change smaller than that is noise.

## End

I recommend that we:

1. Keep the built-in judge instruction, and do not adopt the themes instruction.
   Increment: none, the file stays in this folder as a record. Blocker removed: a change that makes the judges consistent but not right.
   Test (deterministic, Gherkin):
   Given `bin/judge-actions.py` on main
   When it runs with no `--instructions`
   Then it sends the built-in instruction.
   Domain: Clear. Reason: deduction, because the unit test checks it.
2. Probe a judge that sees the user's answers. For each row, give the judge the other 23 rows with the user's answers and notes as examples, then judge the one left out.
   Increment: 24 calls for each judge, about 1.2 USD. Blocker removed: no held-out sheet, because each row is held out once.
   Test (stochastic): the label kappa with the user reaches 0.40 or more for either judge, over 24 left-out rows.
   Domain: Complex. Reason: induction from one marker, and a second marker could break the pattern.
3. Report the domain rates of past runs as the judges' rates until a judge passes.
   Increment: already done on the evaluations page. Blocker removed: none new.
   Test (evaluative): each domain rate on the page names the judge that set it.
   Domain: Clear. Reason: deduction, because the page states it.

## Follow-up

References:

[1] The action-checks-themes.csv, action-checks-argon-themes.csv, and action-checks-control.csv files of the five run folders named in `2026-11-05-judge-themes/`, judged 2026-11-05, with the user's marks in `2026-11-05-human-marking/sheet.csv`. [P]
