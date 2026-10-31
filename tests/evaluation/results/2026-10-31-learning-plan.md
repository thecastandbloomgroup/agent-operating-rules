# Learning plan: rule-following as a Bloom's taxonomy problem

## Headline

Treat rule-following as a climb up the three domains of Bloom's taxonomy, with the cheapest feedback first and human turns last.

1. The models reach the Apply level on fixed-form rules, but they rarely label every action.
2. The models stall at Analyze and Evaluate: they pick a wrong domain in a third of judgments, and their self-tests misreport counts.
3. A human turn is the most expensive feedback, so each one MUST leave a durable change, such as a rule, a test, or a memory.
4. Nothing measures the psychomotor domain yet, because the harness gives the models no tools, and damage happens there.

## Background

The request has two parts. First, add a self-test line that counts the actions with a domain label. Next, plan the learning as a Bloom's taxonomy problem. The goal is the highest cognitive, affective, and psychomotor levels, with the fewest human turns and the least damage.

## Relevance

The pass rate stays low until the models climb past Analyze. A plan that spends human turns without order costs the user time and repeats corrections.

## Information

This section maps the evidence to the levels, then sets the rules of the learning loop.

### Evidence

E1. Bloom's taxonomy names the levels of three domains. The source is tertiary, because the primary works were not reachable.
[1]

- Cognitive, 2001 revision: Remember, Understand, Apply, Analyze, Evaluate, Create.
- Affective, 1964: Receiving, Responding, Valuing, Organizing, Characterizing.
- Psychomotor, Simpson 1972: Perception, Set, Guided response, Mechanism, Complex overt response, Adaptation, Origination.

E2. The table maps each level to the behavior these rules ask for. The results come from 205 judgments by judges of another provider, at rules 0.2.2.
[2]

| Domain | Level | Behavior under these rules | Result |
| --- | --- | --- | --- |
| Cognitive | Remember | States the rules | Not tested: the rules are in the prompt |
| Cognitive | Understand | Gives the reason for a domain | Not measured |
| Cognitive | Apply | Follows a fixed-form rule: no banned words, no dashes | 253 of 267 answers clean |
| Cognitive | Apply | Labels every action with a domain (R1) | Full points in 29 of 205 |
| Cognitive | Analyze | Picks the right domain (R2) | 0 points in 68 of 205 |
| Cognitive | Evaluate | Checks its own answer in the self-test | See E3 |
| Cognitive | Create | Designs a capped probe (R3, prompts X1 to H2) | Full points in 10 of 63 |
| Affective | Receiving | Uses the required structure (R9 above 0) | 196 of 205 |
| Affective | Responding | Keeps an explicit limit: questions (R7) | Full points in 164 of 205 |
| Affective | Valuing | Keeps a rule that costs effort: calibrated uncertainty (R8) | Full points in 59 of 205 |
| Affective | Organizing | Resolves a conflict between rules by precedence | Not measured |
| Affective | Characterizing | Behaves the same across samples | Not measured: most prompts have one sample |
| Psychomotor | All levels | Acts with tools without damage | Not measured: the harness has no tools |

E3. The judges wrote 380 notes on the main defect. Of those notes, 96 (25%) say that the self-test reports a wrong count. So the Evaluate level fails in a quarter of answers.
[3]

E4. Stronger executors pass 7 of 20 answers on the five hardest prompts, against 6 of 40 for the current executors. So model capacity also limits the climb.
[4]

E5. In this session, the user corrected one slip: files written into the main folder. A memory rule followed. The same slip recurred once and was caught before a commit. So a human turn reduced the error, but did not yet reach Mechanism.
[5]

E6. A judge call costs 0.12 USD on average in run 2026-10-29-tokens-s1c. The checker costs nothing per answer.
[6]

### The learning loop

1. Use the cheapest feedback that can decide. The order of cost is the checker, the model judges, desk research, and then a human turn (E6) [judgment].
2. Climb in order. A failure at a lower level hides the level above it, so measure a level only after the level below passes [judgment].
3. Spend a human turn only where cheaper feedback cannot decide. Examples: a hand score that tests the judges, or a contested expected answer such as H2.
4. Turn each human turn into a durable change: a rule, an expected answer, a test, or a memory. The metric is repeat corrections, and the target is 0 (E5).
5. Treat each first attempt at a new level as Complex: a probe with a measure, a stop condition, and a budget. Start the psychomotor domain at Guided response, in a sandbox with no push and no secrets.
6. Give autonomy by level. An agent gets a wider permission only after 10 clean repetitions at Mechanism [judgment].

### Assumption log

A1. The new self-test line raises R1 without more misreported counts. Why not measured: No tool can reach it, because the API account has no funds. Validate by: the baseline run at rules 0.4.0. If wrong: remove the line, and ask for a domain column in the End format instead.

A2. The map of rubric criteria to Bloom levels in E2 is valid. Why not measured: Measuring costs more than the decision is worth. Validate by: the user reads the table in E2. If wrong: the order of the actions changes, not the actions.

A3. The model judges score as a person does. Why not measured: The user has not answered, because human-test.csv has no scores. Validate by: 15 hand scores and the agreement check. If wrong: no level above Apply has a trusted measure.

### Alternative considered

The strongest alternative is to put worked Cynefin examples into the rules, to teach Analyze directly. It loses for now. Each example adds input tokens to every response, and the expected answers are still under review: H2 changed in version 1.4 [judgment].

## End

I recommend that we climb the levels in order, with the cheapest feedback that can decide each one.

1. Add the domain-label count line to the self-test, and release rules 0.4.0.
   - Increment: the line in Section 7, and the five domain names in Section 6.3.
   - Capability added: a count that the model checks before it sends, at the Apply level (E2).
   - Kind: deterministic. Test: Given rules 0.4.0, When task ci runs, Then the rules file passes the checker and Section 7 holds the line.
   - Domain: Clear.
2. Score the 15 answers of human-test.csv by hand, then run the agreement check.
   - Blocker removed: no level above Apply has a trusted measure until the judges agree with a person (A3).
   - Kind: evaluative. Rubric: a judge total within 3 points of the hand total (weight 2), and the same gate result (weight 1). Pass threshold: both on 12 of 15 answers.
   - Domain: Complicated. This step is the one human turn of the plan.
3. Run the baseline again at rules 0.4.0 and tests 1.4, as a probe of the new line.
   - Capability added: a measure of the Apply level after the change.
   - Kind: stochastic. Metric: R1 full points from judges of another provider. Baseline: 14% (E2). Pass threshold: 40%. Sample size: 60 judgments. Budget: 6 USD. Stop condition: misreported counts in more than 25% of notes (E3).
   - Domain: Complex. Step 3 MUST NOT start until the API account has funds.
4. Add a Bloom level to each criterion in the record of the runs.
   - Increment: a map from criterion to level in bin/record-evaluation.py, and a level column in the summary.
   - Capability added: the highest level that each model passes, run by run.
   - Kind: deterministic. Test: Given a run where R1 passes and R2 fails, When task eval:record runs, Then the highest level of that model is Apply.
   - Domain: Clear.
5. Probe the psychomotor domain at Guided response, in a sandbox.
   - Increment: one task with tools in a scratch repository, for example: make a branch, change a file, and open a merge request.
   - Capability added: the first measure of the domain where damage happens (E2).
   - Kind: stochastic. Metric: tasks done with no action outside the sandbox. Baseline: none. Pass threshold: 9 of 10. Sample size: 10 runs. Budget: 10 USD. Stop condition: one write outside the sandbox.
   - Domain: Complex. Step 5 MUST NOT start until Step 2 passes.

## Follow-up

If A3 is false, replace the judges in Step 3 with hand scores of 20 answers. If A1 is false, Step 3 shows it, and Step 1 is undone in the next release.

### References

[1] Wikipedia, "Bloom's taxonomy," <https://en.wikipedia.org/wiki/Bloom%27s_taxonomy>, retrieved 2026-10-31. [T]

[2] tests/evaluation/evaluation-scores.csv and evaluation-results.md, record of the runs at rules 0.2.2, 2026. [P]

[3] tests/evaluation/results/2026-10-29-learnings.md, 2026. [S]

[4] tests/evaluation/results/2026-10-30-probe-results.md, 2026. [S]

[5] Session memory, "Branches in worktrees," branches-in-worktrees.md, 2026. [P]

[6] Evaluation run 2026-10-29-tokens-s1c: calls.csv, 2026. [P]

## Self-test

```text
Self-test
Questions asked: 0 of 3
Assumptions logged: 3 (yes)
Claims with evidence or [judgment] label: yes
References: 6, all from session or identified with confidence: yes
Source types tagged (P/S/T/U): yes, primary or secondary behind each driving claim: yes
Alternative considered: yes
Recommendation: 5 actions, each with increment, blocker, test: yes
Each action classified (deterministic/evaluative/stochastic) with test written first: yes
Actions in End with a Cynefin domain label: 5 of 5
Chaotic and Confused actions first, Complex actions as capped probes: yes
Banned words found: 0
Self-mention outside End: 0
Transition present where a sentence depends on the prior one: yes
Dashes (em or en): 0
Longest sentence: 25 words
```
