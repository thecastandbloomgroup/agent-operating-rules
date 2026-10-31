# What three evaluation runs show about rules v3.2

## Headline

Under rules v3.2, judges from another provider pass 8% of answers, and a wrong Cynefin domain is the main defect.

1. The pass share stays low in all three runs: 8 of 71, 4 of 66, and 4 of 68 answers.
2. A judge from the same provider as the executor passes three times as many answers: 23% against 8%.
3. Scores move about 2 to 3 points out of 18 between judges and between runs, so these runs cannot rank the six executors.
4. No human scores exist yet, so the data cannot say which judge is right.

## Background

Three runs sent all 13 prompts once through the six main pairs, with rules v3.2 as the system prompt. Each answer got two judges: a model from the same provider and a model from another provider. This summary combines 380 judgments from the run of this morning and the two new runs.

## Relevance

The next decision is whether to spend about 45 USD on the full three-sample run. These results show that the judges need a test first.

## Information

This section covers the evidence, the themes in the judge notes, the assumptions, and the alternative.

### Evidence

E1. Pass share by executor. Each cell counts answers that passed, over answers scored, in three runs. Source of the table:
[1]

| Executor | Judge from another provider | Judge from the same provider |
| --- | --- | --- |
| claude-sonnet-5-5 | 2 of 39 | 8 of 39 |
| gemini-3.8-flash | 2 of 36 | 5 of 35 |
| glm-5.3-flash | 0 of 34 | 10 of 28 |
| gpt-6.1-sol | 5 of 39 | 5 of 39 |
| grok-4.7 | 3 of 19 | 0 of 4 |
| kimi-k3 | 4 of 38 | 13 of 30 |
| All | 16 of 205 (8%) | 41 of 175 (23%) |

E2. The gap between the two judge kinds is real: a two-proportion test gives z = 4.25, so p < 0.001.
[1]

The gap is largest where a model judges itself. For example, Kimi judging Kimi passes 13 of 30, but Gemini judging Kimi passes 4 of 38.
[1]

E3. The domain gate fails most. Judges from another provider give R2 (domain is correct) a score of 0 in 68 of 205 judgments (33%).
[1]

The prompts that test the domain pass least: T2 passes 0 of 29, H2 passes 1 of 29, and K1 passes 2 of 28. In contrast, C2 passes 15 of 29.
[1]

E4. The points threshold removes most of the rest. Of 380 judgments, 245 pass all gates, but only 57 of them reach 80% of the points.
[1]

The pass rule needs 80% of the available points and every gate above 0.
[2]

R9 (conformance to the rules file) gets the full 2 points in 3 of 205 judgments from another provider. Therefore almost every answer starts one point short.
[1]

E5. The judges disagree on one answer by a mean of 1.98 points. Of 175 answers, 34 differ by more than 3 points, and 25 get opposite gate verdicts.
[1]

Only 10 answers pass with both judges.
[1]

E6. The same executor, prompt, and judge give totals that differ by a mean of 2.61 points across runs. Of 70 such cells, 14 differ by more than 3.
[1]

The executors pass between 0 of 34 and 5 of 39 with judges from another provider. With about 38 answers each, the 95% interval is about 9 points wide on each side. So no executor differs from the others [judgment].

E7. Grok calls fail most: 40 of 83 xai calls failed (48%), against 2% to 13% for the other providers. Grok as a judge scored 4 answers in three runs.
[1]

E8. The three runs cost 17.49, 14.21, and 15.44 USD, so 47.14 USD in total. The planner estimates 31.72 USD for one run, so it is about two times too high.
[1]

### Themes in the judge notes

The judges wrote one main defect for each judgment, 380 notes in total [1]. Four themes describe the domain errors. Notes on all six executors support each one.

1. A Clear task becomes Complicated (C1): the answer adds analysis before a known fix.
2. A Complicated task becomes Clear (K1): the answer commits a rollback before diagnosis.
3. A Complex task becomes Clear (T2, X2): the answer gives one fix, not parallel probes.
4. A Chaotic task becomes Confused (H2): the answer checks facts before it stabilises.

The common pattern is that the executor picks the familiar action, then gives it the domain that fits that action [inference]. C2 disagrees with the pattern, because half of its answers pass. Two smaller themes also appear. First, 96 of 380 notes (25%) say that the self-test reports a wrong count. Next, 16 notes name a file that the prompt mentions but does not supply, which matches the known issue in C1, C2, and K1.

### Assumption log

A1. A judge from another provider scores closer to a human than a judge from the same provider. Why not measured: The user has not answered, because human-test.csv has no scores. Validate by: score 15 answers by hand and run the agreement check. If wrong: the pass share is nearer 23%, and Step 2 reports the wrong number first.

A2. The Grok failures come from load on the connection, not from the prompts. Why not measured: The material does not state it. Validate by: run the xai pair with 1 worker on 3 prompts. If wrong: Grok needs a smaller output limit, and Step 4 changes.

A3. The three runs are independent samples of one distribution. Why not measured: No tool can reach it, because the API exposes no seed. Validate by: compare the mean totals of the three runs. If wrong: the spread in E6 is too low.

### Alternative considered

The strongest alternative is to run the full three-sample run now. It loses because more answers from judges without a test cannot show which executor follows the rules [judgment].

## End

I recommend that we test the judges first, then probe one change to the domain rules.

1. Score 15 answers of human-test.csv from run 2026-10-29-tokens-s1c by hand, then run the agreement check.
   - Blocker removed: no evidence shows that any judge is valid.
   - Kind: stochastic. Metric: the share of answers where the judge from another provider gives the same gate verdict as you. Baseline: the two judges agree on 150 of 175 answers (86%). Pass threshold: 80% or more, and a mean total difference of 2 points or less. Sample size: 15 answers.
   - Domain: Complicated. The agreement check is the analysis that picks the judge to trust.
2. Show the pass share of each judge kind on its own line in summary.md.
   - Blocker removed: one combined number hides the three-times gap in E2.
   - Kind: deterministic. Test: Given a run with both judge kinds, When the merge writes summary.md, Then summary.md shows one pass share for each judge kind.
   - Domain: Clear. Step 2 MAY run at the same time as Step 1.
3. Probe one change to Section 6.5: a short check that asks which cue sets the domain before the answer picks an action. You write the text, and a separate worktree runs it.
   - Blocker removed: 33% of judgments fail the domain gate (E3).
   - Kind: stochastic. Metric: the share of R2 scores of 0 from judges of another provider. Baseline: 33%. Pass threshold: 20% or less. Sample size: one run, about 68 judgments. Budget: 16 USD. Stop condition: 33% or more after 30 judgments.
   - Domain: Complex, so the leverage is a guess. Step 3 MUST NOT start until the test in Step 1 passes, because the probe needs a judge that the test supports.
4. Run the xai pair with 1 worker on 3 prompts.
   - Blocker removed: half of the Grok calls fail, so Grok gives little data (E7).
   - Kind: stochastic. Metric: the share of failed calls. Baseline: 48%. Pass threshold: 10% or less. Sample size: about 9 calls. Budget: 1 USD.
   - Domain: Complicated. The result shows whether load causes the failures.

## Follow-up

If A1 is false, put the pass share from the same-provider judge first in Step 2. If Step 1 fails, rewrite R2 and R9 in the rubric before Step 3. If Step 4 fails, remove Grok from the main pairs.

## References

[1] Evaluation runs 2026-10-29-tokens-s1c, 2026-10-29-rules-r2, and 2026-10-29-rules-r3: scores.csv and calls.csv, 380 judgments and 662 calls, 2026. [P]

[2] bin/run-evaluation.py, function score() and PASS_SHARE, branch feat/eval-cache-tokens, 2026. [P]

## Self-test

```text
Self-test
Questions asked: 0 of 3
Assumptions logged: 3 (yes)
Claims with evidence or [judgment] label: yes
References: 2, all from session or identified with confidence: yes
Source types tagged (P/S/T/U): yes, primary or secondary behind each driving claim: yes
Alternative considered: yes
Recommendation: 4 actions, each with increment, blocker, test: yes
Each action classified (deterministic/evaluative/stochastic) with test written first: yes
Each action given a Cynefin domain, Chaotic and Confused first, Complex as capped probes: yes
Banned words found: 0
Self-mention outside End: 0
Transition present where a sentence depends on the prior one: yes
Dashes (em or en): 0
Longest sentence: 24 words
```
