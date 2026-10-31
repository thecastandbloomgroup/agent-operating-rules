# Assessment of the evaluation runs and of the evaluation

## Headline

The 8% pass share does not show the limit of the models: the test removes points, and no strong executor has run yet.

1. The test costs points by itself: a checker defect, four missing files, and one expected answer that conflicts with the rules.
2. All six executors are mid-tier models at low or medium effort, so the top models are untested.
3. The real weakness of the models is the domain choice: they pick a familiar action, then the domain that fits it.

## Background

You asked for each run to go to tests/evaluation/results, then for an assessment of the results and of the evaluation. The branch feat/eval-cache-tokens now writes each run to tests/evaluation/results/RUN, and local CI passes. The eleven earlier runs are now in main/tests/evaluation/results.

## Relevance

A full run costs about 45 USD. If the test is fixed first, each later run measures the models and not the test.

## Information

This section covers the defects of the test, the limits of the models, the options, the assumptions, and the alternative.

### Defects of the test

E1. The checker finds a references list only under a level-two heading with the word "References". It also splits the answer at the first line that holds that heading text.
[1]

The rules file asks for a References list at the end, but it names no form for that heading.
[2]

So the finding "citation with no reference" appears on 137 of 208 answers, and 133 of them have a list under another heading.
[3]

Without that false finding, the answers that pass all checks rise from 32 of 208 (15%) to 89 of 208 (43%).
[3]

E2. The judges read the check report, and they use it to score R9.
[4]

R9 gets its full 2 points in 3 of 205 judgments from another provider. Of those judgments, 29 pass all gates and miss the pass mark by one point.
[3]

So a correct R9 can raise the pass share from 16 of 205 (8%) to at most 45 of 205 (22%) [inference].

E3. Prompts C1, C2, K1, and K2 say that files are attached, but no file goes with them.
[5]

For example, K1 asks for an analysis of logs, traces, and a diff that the executor cannot read. So its expected Complicated answer depends on data that the test does not supply [inference].

E4. Section 0 of the rules puts the explicit request of the user first.
[2]

T2 asks for one prompt, but its expected answer refuses to give one prompt as the answer.
[5]

T2 passes 0 of 29 answers. Therefore the test punishes the answers that follow the order of precedence [inference].

E5. The expected domains are the judgment of the test author. The two judges give the same gate verdict on 150 of 175 answers (86%).
[3]

For example, K1 counts a rollback first as wrong. However, a rollback is a common first move after a release raised latency from 120 ms to 900 ms [judgment].

### Limits of the models

E6. Sonnet 5.5, GPT-6.1-Sol, Gemini 3.8 Flash, and GLM 5.3 Flash run at medium effort. Kimi K3 and Grok 4.7 run at low effort.
[6]

Opus 5.5, Fable 5.1, and GPT-6-Astra are in the pairs file, but no run used them as executors.
[6]

E7. Judges from another provider give R2 (domain is correct) a score of 0 in 68 of 205 judgments (33%).
[3]

The judge notes show one theme for all six executors: the executor picks a familiar action, then gives it the domain that fits. No executor disagrees with the theme. This defect comes from the rules and the models, not from the test [inference].

E8. Of 380 judge notes, 96 (25%) say that the self-test reports a wrong count.
[3]

Also, 89 of 208 answers have a sentence over 25 words, and most of them are tests written on one line.
[3]

A model cannot count words without a tool, so these defects stay until the model can run the checker [inference].

### Options to raise the scores

| Option | What changes | Cost | Effect |
| --- | --- | --- | --- |
| Fix the checker heading | the measure | no API call | R9 up, pass share at most 22% (E2) |
| Add the attached files, and review T2, K1, and H2 | the measure | no API call | fairer R2 and R6 on 6 of 13 prompts |
| Stronger executors at high effort | the model | about 20 USD for 5 prompts | not known, so it needs a probe |
| A domain checklist and an answer template in the rules | the rules | about 16 USD for one run | targets the R2 defect (E7) |
| A second pass in which the model runs the checker and fixes its answer | the run | about 1.5 times the tokens [judgment] | targets R9, sentence length, and the self-test (E8) |

The models are likely (66 to 100%) to score higher than 8%. The reason is that the defects in E1 to E4 cost up to 14 percentage points [inference]. The limit of the models stays unknown until a strong executor runs on the fixed test.

### Assumption log

A1. Judges give R9 its full points when the check report is clean. Why not measured: The material does not state it. Validate by: judge the 29 answers of E2 again with the fixed checker, for about 3 USD. If wrong: the R9 gain is smaller, and Step 1 has less leverage.

A2. Your scores agree with the judge from another provider. Why not measured: The user has not answered, because human-test.csv has no scores. Validate by: score 15 answers and run the agreement check. If wrong: the baseline of Step 5 changes.

A3. The expected domains of the test are right for most prompts. Why not measured: The user has not answered, because the review of the expected answers is yours. Validate by: review T2, K1, and H2 in Step 3. If wrong: R2 measures how often a model agrees with the test author.

### Alternative considered

The strongest alternative is to run the stronger executors now. It loses because the test defects hit every executor, so a strong model also scores low, and the run cannot show its limit [judgment].

## End

I recommend that we fix the test before we spend more on runs, then probe the stronger models.

1. Make the checker accept a References heading as a plain line, a bold line, a heading of any level, or a line with a colon.
   - Blocker removed: a false R9 finding on 64% of answers (E1).
   - Kind: deterministic. Test: Given an answer with the line "**References**" and two entries, When the checker runs, Then it reports no "citation with no reference".
   - Domain: Clear. The increment is one function and one unit test.
2. Add the attached files of C1, C2, K1, and K2 to tests/evaluation, and send each file with its prompt.
   - Blocker removed: four prompts ask for analysis of data that does not exist (E3).
   - Kind: deterministic. Test: Given prompt K1, When the run builds the executor input, Then the input holds the logs, the traces, and the diff.
   - Domain: Complicated. First decide which cause the K1 data shows, then write the files. Step 2 MAY run at the same time as Step 1.
3. Review the expected answers of T2, K1, and H2, and record the decision in evaluation-tests.md.
   - Blocker removed: expected answers that conflict with Section 0 of the rules (E4, E5).
   - Kind: evaluative. The rubric has three criteria. First, the expected answer follows Section 0 (weight 3). Next, it matches the domain definitions of Section 6.5 (weight 2). Last, the judges agree on it in 80% of answers (weight 1). Pass threshold: 5 of 6 points. Evidence: the rule text and the judge notes.
   - Domain: Complicated. You decide, because the test and the rules are yours.
4. Score 15 answers of human-test.csv by hand, then run the agreement check.
   - Blocker removed: no evidence shows that a judge agrees with a human (A2).
   - Kind: stochastic. Metric: the share of answers where the judge from another provider gives your gate verdict. Baseline: 86% between the two judges (E5). Pass threshold: 80%. Sample size: 15 answers.
   - Domain: Complicated. The agreement check is the analysis that picks the judge to trust.
5. Probe Opus 5.5 and GPT-6-Astra as executors at high effort on C1, K1, H2, T2, and X2.
   - Capability added: a measure of the limit of the models (E6).
   - Kind: stochastic. Metric: the pass share from judges of another provider. Baseline: the pass share of the mid-tier executors on the same 5 prompts, after Steps 1 and 2. Pass threshold: 20 percentage points above that baseline. Sample size: 20 answers. Budget: 20 USD. Stop condition: 2 or fewer passes in the first 10 answers.
   - Domain: Complex, so the leverage is a guess. Step 5 MUST NOT start until the tests in Steps 1 and 2 pass, because the test defects would hide the gain.

## Follow-up

If Step 5 shows no gain, probe the domain checklist in the rules next, at 16 USD for one run. If A1 is false, move Step 1 after Step 2.

### References

[1] bin/deterministic-tests.py, function test(), branch feat/eval-cache-tokens, 2026. [P]

[2] sources/model-operating-rules.md, version 3.2, Sections 0 and 5.4. [P]

[3] Evaluation runs 2026-10-29-tokens-s1c, 2026-10-29-rules-r2, and 2026-10-29-rules-r3 in tests/evaluation/results: scores.csv, calls.csv, and responses, 2026. [P]

[4] bin/run-evaluation.py, JUDGE_INSTRUCTIONS, branch feat/eval-cache-tokens, 2026. [P]

[5] tests/evaluation/evaluation-tests.md, version 1.1, Sections 1.1, 1.2, and 1.6. [P]

[6] tests/evaluation/pairs.json, branch feat/eval-cache-tokens, 2026. [P]

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
Each action given a Cynefin domain, Chaotic and Confused first, Complex as capped probes: yes
Banned words found: 0
Self-mention outside End: 0
Transition present where a sentence depends on the prior one: yes
Dashes (em or en): 0
Longest sentence: 25 words
```
