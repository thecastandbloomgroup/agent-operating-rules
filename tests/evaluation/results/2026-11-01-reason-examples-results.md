# Example reasons and the Clear line: results of the probe

## Headline

Do not release the probe lines, because they moved the content of reasons a little and the domains not at all.

1. Actions with both a right domain and a reason of cause and effect rose from 9 to 10 and 12 of 40. The pass threshold was 18.
2. Reasons of cause and effect rose from 13 to 18 and 17 of 40, so example reasons help at the Understand level, but little.
3. The domain was right in 21 and 18 of 40, against 22 and 16 before. So the line between Clear and Complicated did not move it.
4. The probe cost 9.08 USD, so about 16.71 USD of the 50 USD remain.

## Background

The action checks of rules 0.5.1 found 9 of 40 actions with a right domain and a reason of cause and effect (2026-11-01-action-checks-results.md). So the probe, labelled 0.6.1, changed three things in rules 0.6. Section 6.3 asks how cause and effect relate. Section 6.5 gives one example reason for each domain, from fields outside the test set. The Clear and Complicated items say when a task with many steps is still Clear.

## Relevance

The domain of an action decides its form under Section 6.5. A change of wording that does not move the domain leaves the main skill of the rules where it was.

## Information

This section gives the test, the results, and what they show.

### The acceptance test, written before the run

- Metric: actions with score 3 by both judges, on 40 actions sampled with seed 1.
- Baseline: 9 of 40, by each judge.
- Pass threshold: 18 of 40.
- Guards: the script rates drop by 5 points at most, against the 0.5.1 run.
- Budget: 12 USD, with a stop at 15 USD.

### Results

E1. The table compares the probe with the 0.5.1 run, by each judge.
[1]

| Check | 0.5.1, first judges | 0.5.1, Argon | 0.6.1, first judges | 0.6.1, Argon |
| --- | --- | --- | --- | --- |
| Domain right | 22 | 16 | 21 | 18 |
| Reason states cause and effect | 13 | 13 | 18 | 17 |
| Score 3 | 9 | 9 | 10 | 12 |

Both judges give score 3 to 8 of the 40 actions of the probe. So the test fails.

E2. No script rate moved by more than 2 points. So the guards hold.
[1]

E3. The executors cost 7.80 USD for 234 calls, and the two judges 1.28 USD.
[1]

### What the results show

- Example reasons raised reasons of cause and effect by about 5 of 40. A model copies the shape of an example more than its logic [inference].
- A written line between Clear and Complicated left the domains where they were. In Bloom's terms, naming the domain is Analyze, and wording at the Understand level did not reach it [inference].
- The Bloom calibration found a similar limit in models that label exam questions: errors sit on the boundaries between levels (2026-11-01-bloom-calibration.md).

### Limits

- The samples of 40 actions differ between the two runs, because they come from different answers.
- Forty actions give wide intervals. A gain of 3 actions is inside the noise [inference].

### Alternative considered

Release the probe lines for the gain in reasons (E1). It loses because the gain is small, the domains did not move, and each line adds words to every prompt [judgment].

## End

I recommend that we keep rules 0.6, and move the next work from wording to the tests and the executors.

1. Write the rule for support steps in tests 1.6.
   - Increment: one sentence for each of H1, H2, and X1 in evaluation-tests.md.
   - Blocker removed: 11 of 26 right domains in the blind marks depend on this rule (2026-11-01-action-checks-results.md, E7).
   - Kind: evaluative. Rubric: each sentence names the domain of a support step and its reason (weight 1). The judges apply it in the next check (weight 1). Pass threshold: both.
   - Domain: Complicated, because the right label of a support step needs expert reading.
2. Probe the domain choice of strong executors on the same 40 checks.
   - Increment: Opus 5.5 and GPT-6-Astra as executors at rules 0.6, on the prompts of the 40 sampled actions.
   - Capability added: a test of whether the domain limit is the model or the rules.
   - Kind: stochastic. Metric: domain right, by both judges. Baseline: 22 and 16 of 40. Pass threshold: 30 of 40. Sample size: 40 actions. Budget: 12 USD. Stop condition: the spend passes 14 USD.
   - Domain: Complex, because whether a stronger model moves this rate shows only after a trial. Step 2 MAY run in parallel with Step 1.
3. Apply held changes 4, 5, 11, and 13 in pairs, with a line between Understand and Analyze.
   - Increment: the design note and item-labels.yaml, two changes for each commit.
   - Blocker removed: the two boundaries that the Bloom calibration found have no written rule.
   - Kind: evaluative. Rubric: each boundary names the evidence that separates its two levels (weight 2). The text passes the checker (weight 1). Pass threshold: both.
   - Domain: Complicated, because the wording of a boundary needs expert reading of Bloom's taxonomy.

## Follow-up

If Step 2 passes, the domain limit is the model, and the rules can stay as they are. If it fails, the expected domains of the tests need a review by a person.

### References

[1] tests/evaluation/results/2026-11-01-reason-examples (rules.md, action-checks.csv, action-checks-argon.csv, summary.md) and 2026-11-01-gherkin-lines, 2026. [P]

## Self-test

```text
Self-test
Questions asked: 0 of 3
Assumptions logged: 0
Claims with evidence or [judgment] label: yes
References: 1, all from session or identified with confidence: yes
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
