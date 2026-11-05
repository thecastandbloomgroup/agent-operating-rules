# The judges do not match a person on domain fit: results of the blind marking

## Headline

Neither judge can stand in for the user on the domain question. So the domain rates of past runs measure the judges' view, not the user's.

1. On the question of whether the label fits, the first judge matched the user in 11 of 24 rows, with a kappa of -0.20. The second judge matched in 8 of 24, with a kappa of -0.40.
1. The two judges agreed with each other in 19 of 24 rows, but the user gave the same answer in only 7 of those 19. So two judges that agree are not proof of a right answer.
1. The user said yes to the reason question in 23 of 24 rows, so that question does not split answers for this marker. Both kappas are near 0.
1. The notes of the user form four themes. The largest is that a step that needs expertise or facilitation is Complicated, not Clear or Complex.

## Background

The sheet holds 24 judged actions from five runs of 2026-11-01 to 2026-11-03. The user marked them blind on 2026-11-05 in the marking page. Each row asks two questions: does the Cynefin label fit the work, and does the reason say what it takes to know the effect? Kappa is the agreement corrected for chance: 0 is chance, 1 is full agreement, and the floor set for trust is 0.667.

## Relevance

Every "domain right" rate on the evaluations page comes from these judges. A judge that disagrees with the user more often than chance cannot tell the user whether a rule change helps.

## Information

This section gives the agreement, the direction of the misses, the themes of the notes, and the limits of the sample.

### Agreement

| Judge | Question | Rows that match | Kappa |
| ----------------------------- | ------------ | --------------- | ----- |
| First (Opus 5.5, high) | Label fits | 11 of 24 | -0.20 |
| First (Opus 5.5, high) | Reason works | 14 of 24 | 0.10 |
| Second (Gemini 4 Argon, high) | Label fits | 8 of 24 | -0.40 |
| Second (Gemini 4 Argon, high) | Reason works | 13 of 24 | 0.08 |

The first judge is Opus 5.5 in 23 rows and GPT-6 Astra in one row. No kappa reaches the floor of 0.667.
[1]
[2]

### Direction of the misses

- **The judges reject labels that the user accepts.** In 8 rows both judges called the label wrong, and the user called it right. In 4 of these 8 rows, the judges swap Clear and Complicated.
  [1]
- **The user rejects some labels that both judges accept.** In 4 rows, the user said no while both judges said yes. These are rows 7, 16, 19, and 24. In three of them, the user's note names Complicated, because the step needs expertise.
  [1]
- **The judges are stricter on the reason.** The user said yes in 23 of 24 rows. The judges said yes in 13 and 12 rows. So the agreement on the reason is close to the judges' own yes rate.
  [1]

### Themes of the notes

The user wrote notes on 10 rows. They form four themes \[inference\]:

| Theme | Rows | Notes |
| ------------------------------------------------------------------- | ------------- | ----- |
| A step that needs expertise or facilitation is Complicated | 7, 16, 19, 20 | 4 |
| Judge against evidence: desk research, standards, or cited sources | 3, 4, 10 | 3 |
| The fit depends on context the action leaves out: preference, cost | 5, 13 | 2 |
| A Clear label holds only when its assumptions hold | 24 | 1 |

No note disagrees with another. The first theme explains 3 of the 4 rows where the user rejects a label that both judges accept.
[1]

### Limits

- **The sample is not random.** The sheet holds every judge split and some random agreements, so the judges split on at least one question in 18 of 24 rows. So the rates here are not a population rate. They do show that the judges' shared answer misses this user.
- **One marker.** One person marked the sheet, so the result says how far the judges match this user, not every user.
- **The reason question has almost no spread.** With 23 of 24 yes answers, one changed answer moves its kappa by a large step.
- **A save bug touched the sheet.** The marking page lost the last click on 14 rows, and the user answered those questions again after the fix ([MR !70](https://gitlab.com/thecastandbloomgroup/private/agent-operating-rules/-/merge_requests/70)). The user changed one earlier answer on purpose: on row 19, the label answer became no, with the note "Complicated".

## End

I recommend that we:

1. Mark the domain rates on the evaluations page as the judges' rate, not as the user's.
   Increment: one edit to the page. Blocker removed: rates that read as truth.
   Test (deterministic, Gherkin):
   Given the evaluations page
   When it states a domain rate
   Then it says that a judge set the rate and links this note.
   Domain: Clear. Reason: deduction, because the agreement is measured.
1. Add the four themes to the judge instruction, most of all the rule that a step that needs expertise is Complicated. Then judge the 24 rows again.
   Increment: one judge run of 24 rows. Blocker removed: a judge whose view of Complicated differs from the user's.
   Test (stochastic): the kappa on the label question rises from -0.20 to 0.40 or more over the same 24 rows, for under 2 USD.
   Domain: Complex. Reason: induction from 24 rows of one marker, and a new marker could break the pattern.
1. Drop the reason question from human marking until it is reworded. A question that gets yes 23 times in 24 does not split the answers.
   Increment: one change to the sheet template. Blocker removed: marks that carry no signal.
   Test (evaluative): a reworded question gets a no in at least 4 of 24 rows on the next sheet.
   Domain: Complicated. Reason: analysis, because the wording needs a look at what the user means by cause and effect.

## Follow-up

References:

[1] tests/evaluation/results/2026-11-05-human-marking/sheet.csv, the user's marks of 2026-11-05. [P]

[2] The action-checks.csv and action-checks-argon.csv files of each run folder named in the sheet. [P]
