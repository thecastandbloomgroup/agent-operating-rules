# Long sentences: results of the Gherkin-line probe

## Headline

Release the two probe lines as rules 0.6, because answers free of long sentences rose from 31% to 50%.

1. The Gherkin line did most of the work: one-line Gherkin tests over the limit fell from 0.87 to 0.08 per answer.
2. The split line trimmed the other long sentences in End from 0.84 to 0.70 per answer, and changed nothing outside End.
3. The guards held, and self-test counts were right in 38% of answers, against 22% before.
4. The probe cost 8.17 USD, so 27.15 USD of the 50 USD remain.

## Background

Rules 0.5 did not shorten sentences (2026-11-01-wording-results.md). A count of the 0.5 answers found that most long sentences sat in End, and half of those were Gherkin tests in one sentence. So the probe, labelled 0.5.1, added two lines to rules 0.5.

- Section 4.1 item 1: "Before you send, split each sentence over the limit."
- Section 6.4: "Put Given, When, and Then each on its own line."

## Relevance

Long sentences failed more answers than any other script check at 0.5. A rule that removes half of those failures raises the LANGUAGE rate with no judge cost.

## Information

This section gives the test, the results, and the cause of the gain.

### The acceptance test, written before the run

- Metric: answers with no long sentence, as `bin/script-checks.py` scores them.
- Baseline: 31%, from the 0.5 run of 2026-10-31 with the same executors, prompts, and samples.
- Pass threshold: 41% or more, with a 95% interval above zero. STRUCTURE, first person, and reasons drop by 5 points at most.
- Sample size: 234 answers. No call failed.
- Budget: 8 USD, with a stop at 10 USD.

### Results

E1. The table compares the probe with rules 0.5.
[1]

| Check | 0.5 | 0.5.1 | Difference (95% interval) |
| --- | --- | --- | --- |
| No long sentence (targeted) | 31% | 50% | +19 (+10 to +28) |
| LANGUAGE | 28% | 48% | +20 (+11 to +29) |
| Self-test counts right | 22% | 38% | +16 (+8 to +24) |
| STRUCTURE (guard) | 98% | 96% | -2 (-5 to +1) |
| No first person outside End (guard) | 96% | 96% | 0 (-4 to +3) |
| Every label with a reason (guard) | 78% | 73% | -5 (-13 to +2) |

So the test passes. The reason rate sits at the edge of its guard, so the next run MUST watch it.

E2. The table splits the long sentences by kind, per answer.
[1]

| Kind | 0.5 | 0.5.1 |
| --- | --- | --- |
| Gherkin test in one sentence | 0.87 | 0.08 |
| Other sentence in End | 0.84 | 0.70 |
| Other sentence outside End | 0.60 | 0.60 |

So the Gherkin line explains most of the gain. The split line had a small effect in End, and none outside it [inference].

E3. Answers with Given and When on separate lines rose from 75 of 233 to 210 of 234.
[1]

E4. The probe cost 8.17 USD for 234 calls. That is 0.17 USD over the budget, and under the stop.
[1]

### Limits

- The baseline ran on 2026-10-31, and the probe on 2026-11-01. A change in the models between the two days would show as an effect [inference].
- The two lines were tested together, so rules 0.6 keeps both. The split line alone would need its own run to justify it.
- The intervals treat each answer as independent, so the true intervals are wider [inference].

### Alternative considered

Release the Gherkin line alone, because E2 shows that it did most of the work. It loses because that rule set was not tested, and the split line costs 9 words [judgment].

## End

I recommend that we release rules 0.6, then spend the remaining funds on judge checks.

1. Release version 0.6.0 with the two probe lines.
   - Increment: the two lines in sources/model-operating-rules.md, version.json at 0.6.0, and a CHANGELOG section.
   - Blocker removed: the build needs the rules version and version.json to agree.
   - Kind: deterministic. Test: Given version.json at 0.6.0, When task ci runs, Then the build step passes.
   - Domain: Clear, because the release guide fixes each step.
2. Check that domains and reasons are right on 40 actions of the 0.5.1 run.
   - Increment: one judge marks each sampled action yes or no on the domain and on the reason.
   - Blocker removed: the script sees the form of a reason, not its truth.
   - Kind: evaluative. Rubric: the domain matches tests 1.5 (weight 2); the reason states cause and effect (weight 1). Pass threshold: 30 of 40 actions score 3.
   - Domain: Complicated, because the expected domains need expert reading.
3. Calibrate the main judges on 100 items of a public set with human labels, such as InFoBench.
   - Increment: 100 items, each judge answers their yes or no checks, and a kappa against the human labels.
   - Capability added: a known error rate for each judge, before its checks count in a score.
   - Kind: stochastic. Metric: kappa between judge and human labels. Baseline: 0.43 between the two judges on R3. Pass threshold: 0.667. Sample size: 100 items. Budget: 15 USD. Stop condition: the spend passes 18 USD.
   - Domain: Complicated, because known methods measure judge error. Step 3 MUST NOT start until the licence of the set allows this use.

## Follow-up

If the reason rate falls more than 5 more points in the next run, review the split line first. It is the line that the gain in E2 needs least.

### References

[1] tests/evaluation/results/2026-11-01-gherkin-lines (script-checks.csv, calls.csv, summary.md) and 2026-10-31-wording-r05, 2026. [P]

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
