# Bloom labels by models against labels by people

## Headline

A model can be the second labeller of Bloom levels only with care. Opus matches people at a kappa of 0.65, under the 0.667 floor.

1. Opus 5.5 at high effort agrees with the people on 71% of 204 questions (kappa 0.65), and Fable 5.1 on 62% (kappa 0.55).
2. The two models agree with each other more than with the people (kappa 0.69), so agreement between models overstates their accuracy.
3. Three bands of levels do not help: the kappa of Opus moves from 0.65 to 0.66.
4. The errors sit on two boundaries: Opus calls 13 of 34 Create questions Apply, and Fable calls 19 of 34 Analyze questions Understand.

## Background

The design note asks whether a model can label items as the second labeller, and whether six levels or three bands work better (A4, B4). Opus and Fable agreed on 13 of 14 labels of our items, but that measures two readers of one rubric. So both models labelled exam questions that people had labelled before.

## Relevance

Changes 4, 5, 11, and 13 of the label review wait for this result. A labeller with an unknown error rate would make every level score of the design uncertain.

## Information

This section gives the data, the results, and what they mean for the held changes.

### Data and method

E1. The questions come from four sets with labels by people, 2,341 questions in all. The repository of the AIED 2026 study holds them, at commit 786e25c, under an MIT licence. The source sets state no licence, so their questions stay in a scratch folder, and only the model labels are committed.
[1]

E2. The sample has 34 questions for each of the six levels, 204 in all, with seed 11. Each model saw only the questions, with one line of definition for each level. Neither model saw the labels of the people.
[2]

### Results

E3. The table gives the agreement of each labeller with the people.
[2]

| Labeller | Exact | Kappa | Within one level | Kappa on three bands |
| --- | --- | --- | --- | --- |
| Opus 5.5, high effort | 71% | 0.65 | 83% | 0.66 |
| Fable 5.1 | 62% | 0.55 | 75% | 0.54 |
| Opus against Fable | 74% | 0.69 | 83% | 0.70 |

E4. Studies of people who label Bloom levels report a kappa of 0.12 to 0.60. So Opus reaches the top of the range for people, and Fable sits inside it.
[3]

E5. The errors fall on two boundaries.
[2]

- Apply against Create: Opus labels 13 of 34 Create questions Apply. Fable labels 5 of them Apply.
- Understand against Analyze: Fable labels 19 of 34 Analyze questions Understand. Opus labels 2 of them Understand.

E6. Three bands do not raise agreement for a model, as they did for people in a study of pharmacy faculty. Most errors stay within a band, but the boundary between Apply and Create crosses two bands [inference].
[3]

### What this means for the held changes

- Change 5 writes the boundary between Apply and Create. E5 shows that this boundary causes the largest error of Opus.
- A boundary between Understand and Analyze is in no change yet. E5 shows that it causes the largest error of Fable.
- Change 13 settles the knowledge type of Analyze items. It does not touch these two boundaries.
- The fallback to three bands in the design note can go, because it does not help (E3).

### Limits

- The labels of the people are not a perfect truth. People agree with each other at a kappa of 0.60 or less (E4). So a model kappa of 0.65 can sit near the top that this data allows [inference].
- Exam questions differ from our items, which are prompts that ask for a full recommendation.
- Each model labelled once. A second run would show how much one model varies.

### Alternative considered

Keep two models as the label pair, because they agree at 0.69. It loses because both are less accurate against people than against each other (E3), so their agreement hides shared errors.

## End

I recommend that we write the two boundaries into the design, then label our items with Opus and one person.

1. Apply held changes 4, 5, 11, and 13 in pairs, and add the boundary between Understand and Analyze.
   - Increment: the design note and item-labels.yaml, in pairs of changes, one commit each.
   - Blocker removed: the two boundaries of E5 have no written rule.
   - Kind: evaluative. Rubric: each boundary names the evidence that separates its two levels (weight 2); the text passes the checker (weight 1). Pass threshold: both.
   - Domain: Complicated, because the wording of a boundary needs expert reading of Bloom's taxonomy.
2. Run the calibration again with the new boundaries in the instructions of the labeller.
   - Increment: the same 204 questions, labelled by Opus with the two boundaries added.
   - Capability added: a test of whether the written boundaries raise accuracy.
   - Kind: stochastic. Metric: the kappa of Opus against the people. Baseline: 0.65 (E3). Pass threshold: 0.70. Sample size: 204 questions. Budget: no API cost, one subagent run. Stop condition: none needed.
   - Domain: Complex, because the gain from a written boundary shows only after a trial. Step 2 MUST NOT start until Step 1 passes.
3. Use Opus as the second labeller of our items, beside one person.
   - Increment: a note in the design that Opus at high effort is the model labeller, and Fable is not.
   - Blocker removed: no labeller of our items had a known error rate.
   - Kind: deterministic. Test:
     - Given the design note
     - When a reader looks up the second labeller
     - Then it names Opus and its kappa of 0.65
   - Domain: Clear, because E3 decides it.

## Follow-up

If Step 2 does not reach 0.70, keep Opus as the second labeller, and treat its labels of Create and Apply as uncertain.

### References

[1] Z. Rasoulkhani et al., bloom-classification-aied2026, GitLab repository, commit 786e25c, <https://gitlab.com/zrasoulkhani/bloom-classification-aied2026>. [P]

[2] tests/evaluation/results/2026-11-01-bloom-calibration: labels-opus.csv and labels-fable.csv, scored with bin/bloom-calibration.py, 2026. [P]

[3] tests/evaluation/results/2026-10-31-eval-design-research.md, theme B4, 2026. [S]

## Self-test

```text
Self-test
Questions asked: 0 of 3
Assumptions logged: 0
Claims with evidence or [judgment] label: yes
References: 3, all from session or identified with confidence: yes
Source types tagged (P/S/T/U): yes, primary or secondary behind each driving claim: yes
Alternative considered: yes
Recommendation: 3 actions, each with increment, blocker, test: yes
Each action classified (deterministic/evaluative/stochastic) with test written first: yes
Actions in End with a Cynefin domain label: 3 of 3
Chaotic and Confused actions first, Complex actions as capped probes: yes
Banned words found: 0
Self-mention outside End: 0
Transition present where a sentence depends on the prior one: yes
Dashes (em or en): 0
Sentences over the limit of Section 4.1 item 1: 0
```
