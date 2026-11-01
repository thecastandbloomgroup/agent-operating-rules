# Domains and reasons: results of the action checks

## Headline

The models label actions in the right form, but the content is weak. So the next fix targets reasons and the line between Clear and Complicated.

1. Of 40 sampled actions, 9 had both a right domain and a reason that states cause and effect, under each of two judges.
2. The domain was right in 22 of 40 by one judge and in 16 by the other.
3. A reason stated cause and effect in 13 of 40, so most reasons that the script counts only restate a domain or a task.
4. On these yes or no checks, the two judges reach a kappa of 0.61 to 0.71, against 0.43 on the old rubric.

## Background

Rules 0.5 raised the share of answers with a reason on every domain label to 78% (2026-11-01-wording-results.md). The script sees the form of a reason, not its truth. So `bin/judge-actions.py` sampled 40 labelled actions of the 0.5.1 probe, about 7 from each executor, and asked a judge two yes or no questions.

## Relevance

A rate of reasons that measures only their form would mislead the next change of the rules. This check costs about 0.70 USD for each judge, so it can run after every rules change.

## Information

This section gives the test, the results, the agreement of the judges, and what the errors show.

### The acceptance test, written before the run

- Rubric: the domain matches tests 1.5 (weight 2); the reason states cause and effect (weight 1).
- Pass threshold: 30 of 40 actions score 3.
- Judges: Opus 5.5 checked the actions of the five executors that are not Anthropic. GPT-6-Astra checked the actions of Sonnet. Then Gemini 4 Argon checked all 40 as a second judge.

### Results

E1. Both judges give 9 of 40 actions a score of 3, so the test fails.
[1]

| Check | First judges, yes | Gemini 4 Argon, yes | Agreement | Kappa |
| --- | --- | --- | --- | --- |
| Domain right | 22 | 16 | 80% | 0.61 |
| Reason states cause and effect | 13 | 13 | 85% | 0.66 |
| Score 3 | 9 | 9 | 90% | 0.71 |

E2. The script marked a reason on 27 actions where the first judges found none of cause and effect. Typical reasons restate the domain or the task: "because reconciliation requires analysis of formulas, scope, and dates".
[1]

E3. Some domain errors are plain errors of the model. Two actions label IEEE formatting Complicated (C2), two label a formatter step Complicated (T1), and one labels a flaky build Chaotic (U1).
[1]

E4. Other domain errors depend on how the judge reads the tests. In H1, a judge failed a Clear step after the stabiliser, because the expected answer calls all later actions Complicated. A step such as "page a second responder" can be Clear [judgment].
[1]

E5. The two runs of judges cost 1.36 USD in total.
[1]

### Limits

- Neither judge is calibrated against a person yet. The file `human-actions.md` holds the same 40 actions with no verdict, for blind marks.
- Forty actions give wide intervals. A kappa of 0.66 on 40 items has an interval of about plus or minus 0.25 [inference].
- The expected answers of tests 1.5 give one domain list per prompt. They do not say how to label a small step inside a larger domain (E4).

### Addendum: blind marks by a third model

E6. Fable 5.1 marked the 40 actions in a fresh context, with no view of the verdicts, in `action-checks-fable-blind.csv`. These are marks by a model, not by a person. So `human-actions.md` stays blank for a person.
[1]

| Check | First judges | Gemini 4 Argon | Fable, blind | Fable against first judges (kappa) |
| --- | --- | --- | --- | --- |
| Domain right | 22 | 16 | 26 | 0.79 |
| Reason states cause and effect | 13 | 13 | 21 | 0.41 |
| Score 3 | 9 | 9 | 17 | |

E7. Fable had one rule that the judges did not: a small support step may carry its own domain. Of its 26 marks of a right domain, 11 rely on that rule. So the rule for support steps (Step 3) moves this rate more than any other choice [inference].
[1]

E8. On 10 reasons, both judges said no and Fable said yes. So its standard for a reason is looser. By a majority of the three graders, 11 of 40 actions score 3, and the test still fails.
[1]

### Assumption log

A1. A person marks the 40 actions in about 40 minutes. Why not measured: the user has not answered. Validate by: time the first 10 marks. If wrong: mark 20 actions, and accept the wider interval.

### Alternative considered

Trust the script rate of reasons, because the two judges agree well. It loses because both judges reject most of the reasons that the script accepts (E2).

## End

I recommend that we get blind human marks first, then probe a fix for the content of reasons and domains.

1. Mark the 40 actions of `human-actions.md` blind, then compare the marks with both judges.
   - Increment: 80 yes or no marks by the user, and a kappa for each judge against them.
   - Blocker removed: no judge has a known error rate against a person (Limits).
   - Kind: evaluative. Rubric: every action has two marks (weight 1); the marks were made before any verdict was opened (weight 2). Pass threshold: both.
   - Domain: Complicated, because the marks need expert reading of the tests.
2. Probe two lines of rules: one example reason for each domain in 6.5, and the line between Clear and Complicated.
   - Increment: rules 0.6.1 in a run folder, one script-only run, and both judges on 40 sampled actions.
   - Capability added: a measure of whether wording can move the content of reasons, at the Understand level.
   - Kind: stochastic. Metric: actions with score 3, by both judges. Baseline: 9 of 40 (E1). Pass threshold: 18 of 40. Sample size: 40 actions. Budget: 12 USD. Stop condition: the spend passes 15 USD.
   - Domain: Complex, because no change of wording has moved the content of a reason yet, so leverage is a guess. Step 2 MAY run in parallel with Step 1.
3. Write how to label a small step inside a larger domain in the expected answers of H1, H2, and X1.
   - Increment: one sentence for each of the three prompts in evaluation-tests.md, and tests 1.6.
   - Blocker removed: judges fail some right labels because the tests give no rule for them (E4).
   - Kind: evaluative. Rubric: each sentence names the domain of a support step and its reason (weight 1). The human marks of Step 1 agree with it (weight 1). Pass threshold: both.
   - Domain: Complicated, because the right label of a support step needs expert reading. Step 3 MUST NOT start until Step 1 passes.

## Follow-up

If the human marks of Step 1 disagree with both judges, fix the judge instructions before Step 2 counts.

About 25.79 USD of the 50 USD remain.

### References

[1] tests/evaluation/results/2026-11-01-gherkin-lines: action-checks.csv, action-checks-argon.csv, and action-checks-fable-blind.csv, 2026. [P]

## Self-test

```text
Self-test
Questions asked: 0 of 3
Assumptions logged: 1
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
