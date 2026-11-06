# Work on the limits of the evaluations page: results

## Headline

Three limits moved with no person: two models now have psychomotor scores, the intervals have numbers, and the count of second turns is right.

1. **Few trials per model.** With 20 trials per level, Sonnet 5.5 mastered all seven psychomotor levels and scores 1.00. GLM 5.3 Flash scores 0.89, as the mean of levels that are not cumulative.
2. **Wide intervals.** With 24 trials, a 95% Wilson interval spans about 30 points, so a level at 21 of 24 can fall under 80% on a rerun.
3. **Few second turns.** Three studies in five runs test a second turn, not the two pilots that the page named.
4. The two runs cost 2.96 USD, under the mark of 5 USD.

## Background

The [plan](2026-11-06-limits-plan.md) fixed three marks before any call. It added 16 samples of P1 to P7 for Sonnet, the strongest model on the ladder, and GLM, the cheapest per unit. The first 4 samples of each come from the [P1 to P7 run](2026-11-06-psychomotor-p1-p7-results.md) of the same day.

## Relevance

A per-model mastery call is now possible on the psychomotor ladder, so the page can rank two models, not only pool them. The other four models need about 22 USD more for the same.

## Information

This section gives the marks, the scores, the intervals, and a correction to the plan.

### The marks

| Mark                                              | Result                         | Pass |
| ------------------------------------------------- | ------------------------------ | ---- |
| Trials: 20 or more per level for each model       | 20 per level for both          | yes  |
| Score: a psychomotor score for each model         | Sonnet 1.00, GLM 0.89          | yes  |
| Cost under 5 USD                                  | 2.96 USD                       | yes  |

[1]

No unit failed on the network, so no unit ran again. One GLM unit of P7 hit the cap of 20 steps.
[1]

### The scores

| Level                  | Sonnet 5.5 | 95% interval | GLM 5.3 Flash | 95% interval |
| ---------------------- | ---------- | ------------ | ------------- | ------------ |
| Perception             | 20 of 20   | 84 to 100    | 20 of 20      | 84 to 100    |
| Set                    | 20 of 20   | 84 to 100    | 20 of 20      | 84 to 100    |
| Guided response        | 20 of 20   | 84 to 100    | 20 of 20      | 84 to 100    |
| Mechanism              | 20 of 20   | 84 to 100    | 20 of 20      | 84 to 100    |
| Complex overt response | 20 of 20   | 84 to 100    | 12 of 20      | 39 to 78     |
| Adaptation             | 20 of 20   | 84 to 100    | 20 of 20      | 84 to 100    |
| Origination            | 18 of 20   | 70 to 97     | 13 of 20      | 43 to 82     |

[1]

- **GLM fails where two files meet.** On P5, 7 of its 8 failures ran no check after the last write. On P7, 3 units wrote no procedure, and 2 ran the tools in another order on one file.
  [1]
- **Sonnet held P5 at 20 of 20 with no note.** The two harms to Sonnet on P5 came only with a change to the tools or the first turn ([answer note results](2026-11-06-answer-note-results.md)).
  [1]

### The intervals

The intervals are 95% Wilson intervals, computed from the counts of each table. With 24 trials, 18 of 24 runs from 55% to 88%, and 21 of 24 from 69% to 96%. A model with a true rate of 90% needs about 53 trials before its interval clears 80%. So 20 trials is the floor of a mastery call, not proof of mastery [inference].

### A correction to the plan

The plan counted four second-turn studies. The runs folder holds three: the pushback pilot, the structure repair, and the P5 repair, in five runs. The page states three.

### What still needs a person or funds

- **One human marker.** A second marker of the judge sheet needs a person.
- **Mid-tier executors.** A run of strong executors on every ladder costs more than the 3.75 USD left.
- **Four models with 4 trials per level.** They need about 22 USD more to reach 20.

## End

I recommend that we:

1. Decide whether to fund the other four models to 20 psychomotor trials per level.
   Increment: about 22 USD, one run per model. Blocker removed: a ladder that ranks only two of six models.
   Test (evaluative): the decision names the models and the budget, before any call.
   Domain: Clear. Reason: deduction, because the cost per unit is measured.
2. Ask a second person to mark the 24 rows of the judge sheet, when one is free.
   Increment: about 30 minutes of a second person. Blocker removed: judge kappas that rest on one marker.
   Test (evaluative): the two markers agree on 18 or more of 24 rows, or the page says that the users differ.
   Domain: Complicated. Reason: analysis, because the sheet and the rubric exist.
3. Probe a P5 repair turn for GLM, with the named second turn that fixed 5 of 5 units before.
   Increment: one second turn for the 8 failed P5 units, about 0.05 USD. Blocker removed: GLM's lowest level.
   Test (stochastic): the named turn repairs 6 or more of 8, against a plain retry.
   Domain: Complex. Reason: induction from 5 units, and GLM could fail in another way.

## Follow-up

References:

[1] `2026-11-06-limits-sonnet/`, `2026-11-06-limits-glm/`, and `2026-11-06-psychomotor-p1-p7/`: tool-checks.csv, calls.csv, and run.log, run 2026-11-06. [P]
