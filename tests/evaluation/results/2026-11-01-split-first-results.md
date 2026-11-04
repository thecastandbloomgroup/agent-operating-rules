# Split first, domain intact: results of the probe

## Headline

Splitting first with the domain kept intact did not move the domains. The gain that first appeared came from the judging rule of tests 1.6.

1. Under one judging rule, both judges found a right domain in 27 of 40 actions of rules 0.6. They found 28 of 40 in the probe.
2. Under the old rule, rules 0.6 had scored 15 of 40, so tests 1.6 explains the gain.
3. The parts did not get smaller: 3.3 actions for each answer in both runs, and reasons of cause and effect stayed near 14 of 40.
4. A network outage cut the first run short, so the probe cost 11.35 USD, and 2.28 USD of the 50 USD remain.

## Background

The domain of an action mirrored its task kind in 70% of actions at rules 0.6. So the probe, labelled 0.7.1, added three lines to Section 6.5. The model splits the problem first into parts of one task kind. Each part keeps the domain of its problem, unless its own cause and effect differ.

## Relevance

A rule that moves the domain would lift the Analyze level, which no change of wording had moved. A false gain would put a useless rule into every prompt.

## Information

This section gives the test, the confound, and the results.

### The acceptance test, written before the run

- Metric: actions with a right domain, by each of two judges, on 40 actions sampled with seed 1.
- Baseline: 22 and 16 of 40, from the run of rules 0.6.
- Pass threshold: 26 of 40 by each judge. Script rates drop by 5 points at most.
- Sample size: the 13 core prompts, 6 executors, 3 samples.
- Budget: 10 USD, with a stop at 12 USD.

### The run

E1. A loss of DNS on the host failed 70 calls of the first run. Sonnet and GLM finished all 39 answers there. A second run repeated Gemini, GPT, Kimi, and Grok in full with no failure. Folder 2026-11-01-split-first-c combines the complete answers.
[1]

### The confound

E2. The probe was judged with the rule of tests 1.6, which lets a support step carry its own domain. The run of rules 0.6 had been judged before that rule. So the same 40 actions of rules 0.6 were judged again under tests 1.6.
[2]

### Results

E3. The table compares the runs, each judged under tests 1.6 unless the row says so.
[1]

| Run | Domain right, first judges | Domain right, Argon | Both judges | Reason of cause and effect |
| --- | --- | --- | --- | --- |
| Rules 0.6, old judging rule | 22 | 16 | 15 | 13 and 13 |
| Rules 0.6 | 27 | 29 | 27 | 14 and 15 |
| Split first (0.7.1) | 31 | 30 | 28 | 14 and 13 |

Under the same rule, the gain is 1 action of 40, with a 95% interval of -18 to +23 points. So the probe has no effect that this sample can show, and the test fails.

E4. The domain mirrored the task kind in 66% of actions, against 70%. The answers had 3.30 actions each, against 3.34, and 90 words in each action, against 85.
[1]

E5. No script rate dropped. STRUCTURE rose from 96% to 98%, and LANGUAGE from 48% to 50%.
[1]

### What the results show

- Tests 1.6 changed the measure, not the models. Under it, about 70% of domains at rules 0.6 are right, so the Analyze level is higher than the old judging showed.
- Reasons of cause and effect stay near 35% in every run. So the Understand level, not Analyze, is now the lowest measured level of the cognitive ladder.
- A rule that changes how the model splits did not make the parts smaller or clearer.

### Alternative considered

Keep the probe lines, because the domains rose from 22 and 16 to 31 and 30. It loses because the same judges found 27 and 29 in the old answers under the same rule (E3).

## End

I recommend that we keep rules 0.7, and point the next work at the Understand level.

1. Record the probe and judge the baseline under tests 1.6 as its main results.
   - Increment: this write-up, the three run folders, and the files of the baseline renamed.
   - Blocker removed: two sets of results under two rules made the gain look real.
   - Kind: deterministic. Test:
     - Given the baseline folder
     - When ladder-scores.py reads it
     - Then it uses the results under tests 1.6
   - Domain: Clear, because the rename has one right result.
2. Fund a probe that feeds back failed reasons to the model, at the Understand level.
   - Increment: one run where each answer gets the judge note on its reasons, then a second answer.
   - Capability added: a test of feedback in place of wording, which the design note names (B6).
   - Kind: stochastic. Metric: reasons of cause and effect, by both judges. Baseline: 14 of 40 (E3). Pass threshold: 24 of 40. Sample size: 40 actions. Budget: 15 USD. Stop condition: the spend passes 18 USD.
   - Domain: Complex, because no change has moved this rate yet, so leverage is a guess.
3. Mark the 40 actions of human-actions.md by hand, under tests 1.6.
   - Increment: 80 yes or no marks by a person, and a kappa for each judge.
   - Blocker removed: every result so far comes from a model.
   - Kind: evaluative. Rubric: every action has two marks (weight 1); the marks come before any judge result is read (weight 2). Pass threshold: both.
   - Domain: Complicated, because the marks need expert reading of the tests.

## Follow-up

Step 2 needs more funds than the 2.28 USD that remain.

### References

[1] tests/evaluation/results/2026-11-01-split-first, 2026-11-01-split-first-b, and 2026-11-01-split-first-c, 2026. [P]

[2] tests/evaluation/results/2026-11-01-gherkin-lines: action-checks.csv and action-checks-argon.csv under tests 1.6, and the files that end in -tests15, 2026. [P]

## Self-test

```text
Self-test
Questions asked: 0 of 3
Assumptions logged: 0
Claims with evidence or [judgment] label: yes
References: 2, all from session or identified with confidence: yes
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
