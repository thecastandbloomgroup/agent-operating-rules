# Evaluation design: prior art and options

## Headline

Replace the single 18-point score with separate measures per Cynefin domain, and move human judgment from scoring every criterion to three narrow jobs.

1. The current score mixes three skills: naming the domain, acting on it, and following the writing rules. So a fail does not say which skill failed.
2. The two judges agree well only on R1. Seven of nine criteria fall below the floor that content analysis accepts for tentative conclusions.
3. Prior art splits a grade into binary checks, grades the output rather than the stated reasoning, and reports error bars over many items.
4. Human judgment is worth the most when it is blind. Its three jobs are gold domain labels, notes on failed answers, and pass or fail marks for the judge.

## Background

The request asks for desk research on prior art for LLM evaluation, with numbers and themes. It also asks for options that make the results easier to read and that define the role of the user's judgment. The goal is an objective measure of how well models think and respond in each Cynefin domain.

## Relevance

The user is about to score 34 answers by hand on a rubric that two judges apply inconsistently. A better design now saves those hours and gives a result that names the failing skill.

## Information

This section gives the local numbers first, then the themes from the prior art, then the options.

### Evidence from the record

E1. The two judges scored 245 answers in common. The table gives their exact agreement and Cohen's kappa (agreement above chance) for each criterion.
[1]

| Criterion | What it measures | Exact agreement | Kappa |
| --- | --- | --- | --- |
| R1 | A domain on every action | 0.94 | 0.84 |
| R2 | The right domain | 0.78 | 0.67 |
| R6 | The misleading wording avoided | 0.77 | 0.61 |
| R4 | Order of the actions | 0.68 | 0.45 |
| R3 | Action form fits the domain | 0.67 | 0.43 |
| R7 | Questions | 0.87 | 0.43 |
| R9 | Rules-file conformance | 0.84 | 0.39 |
| R5 | Test form | 0.65 | 0.33 |
| R8 | Calibrated uncertainty | 0.53 | 0.23 |
| Pass | The whole verdict | 0.82 | 0.37 |

E2. Content analysis treats agreement of 0.800 or more as reliable. It accepts 0.667 to 0.800 for tentative conclusions only, and it discards data below 0.667.
[2]

So only R1 is reliable, and R2 is at the floor. Kappa and Krippendorff's alpha differ in method, but they give close values for two raters [judgment]. Also, 39 of the 245 answers (16%) have judge totals more than 3 points apart.
[1]

E3. The tests have 13 prompts: two per domain, and three prompts with misleading wording. For one model and one sample, a domain score rests on two items.
[3]

At an accuracy of 70%, the 95% interval is about 20 points each way with 20 items [inference]. It is 14 points with 40 items, and 9 points with 100 items. So two items per domain cannot separate one domain from another.

E4. The criteria mix three skills. R2 and R6 measure whether the model names the right domain. R1, R3, and R4 measure whether it acts on that domain. R5, R7, R8, and R9 measure general rules that do not depend on the domain.
[3]

Of 205 judgments by judges of another provider, 16 pass. Full points on R2 alone would raise that to 26, and full points on R1, R8, and R9 to 95. So the pass rate measures writing discipline more than the choice of domain.
[4]

E5. The plan for hand scoring shows a model's suggested score next to an empty column for the user. That layout invites the anchoring that theme T4 describes.
[5]

### Themes from the prior art

The search covered LLM judges, rubric design, human labelling, statistics of evaluations, and the Cynefin literature. Each theme lists the sources that support it and the sources that disagree.

T1. LLM judges are useful, but they carry bias, so they need calibration against people. Four sources support this theme. A strong judge reaches over 80% agreement with human preference, about the level between two people. Judges also favor the first position and their own answers.
[6]

A judge model scores its own text higher than human raters do, and this bias grows with the ability to recognise its own text.
[7]

Kappa separates judges better than percent agreement, and a high percent agreement can hide divergent scores.
[8]

Model graders need calibration against human graders, while code graders suit fixed criteria.
[9]

One source partly disagrees: in a medical benchmark, agreement between a model grader and doctors matches agreement between two doctors.
[10]

That result shows that calibration can succeed. It does not remove the need for it.

T2. Many small yes or no checks give more reliable grades than one holistic scale. Three sources support this theme. Checklists of yes or no questions raised the agreement between people from 0.194 to 0.256. They raised exact agreement between judge and people from 46.4% to 52.2%.
[11]

A practitioner guide advises binary pass or fail labels over 1 to 5 scales, with a separate check for each part of the task.
[12]

The medical benchmark grades 5,000 conversations against 48,562 written criteria, each with its own point value.
[10]

One source disagrees in part: a well calibrated judge on a scale of 7 or more points recovers model rankings as well as pairwise votes. That source was read in abstract only.
[13]

T3. The criteria come from reading real outputs, and the human role is to read and label. Three sources support this theme. People need criteria to grade outputs, but grading outputs also changes the criteria ("criteria drift").
[14]

Error analysis starts with free notes on failed outputs (open coding). Then the notes are grouped into failure modes (axial coding) and counted, until no new mode appears.
[15]

Reading transcripts is how a team checks that the graders are fair.
[9]

No source disagrees with this theme.

T4. A suggestion shown to a human labeller pulls the label toward the suggestion. One source with a sample of 2,784 people supports this theme directly. Annotators accepted wrong AI suggestions more often when the task leaned toward automation.
[16]

Two smaller studies in the same search found the same pull. This theme has few sources, but it matters here, because the hand-scoring plan shows a suggestion next to every cell (E5).

T5. An evaluation needs many items, repeated trials, and error bars. Three sources support this theme. Report a standard error with each mean, cluster the errors when items share a scenario, and compare models on paired differences per item.
[17]

Consistency over repeated trials (pass^k) falls fast. One agent passed under 50% of tasks in one trial, and under 25% in all of 8 trials.
[18]

With item response theory, 100 chosen items estimate a score on 14,000 items within about 2%.
[19]

T6. Minimal pairs test whether a model finds the real boundary between two labels. One source supports this theme. A small change that flips the gold label cut model accuracy by up to 25%.
[20]

The three prompts with misleading wording (T1 to T3) already use this idea, but they have no matched pair.

T7. A model's stated reasoning is not a faithful record of its thinking, so grade the behavior. Two sources support this theme. Explanations in chain of thought left out the cue that changed the answer, and accuracy dropped by up to 36% under such cues.
[21]

Grade what the agent produced, not the path it took.
[9]

So measure "thinking" as the domain a model names when asked alone [inference]. Measure "responding" as the form of the actions it then writes.

T8. No source measures how reliably people, or models, assign a Cynefin domain. The searches found framework papers and case reports, but no agreement study [inference]. The framework describes the domains, not a test for them.
[22]

So the gold labels are themselves a measurement, and their agreement MUST be measured before a model is graded against them [inference].

### Options

The options differ in what they measure, who grades, and how the result is reported.

| Option | What changes | Strength | Weakness |
| --- | --- | --- | --- |
| O1. Repair the rubric | Define each 0, 1, and 2 with examples | Keeps the old runs comparable | Seven criteria start below 0.667 (E1); the score still mixes skills (E4) |
| O2. Layered measures | Four separate measures, each with its own grader | Names the failing skill per domain | Needs a new gold set and a new harness step |
| O3. Pairwise votes | People pick the better of two answers | Easy for people; ranks models | No absolute level; many votes per pair |
| O4. Reference answers | Compare each answer with a model answer | Fast to grade | Punishes valid alternatives (T7) |
| O5. Item response theory | Fit item difficulty across models | Fewer items per run (T5) | Needs a large item bank first |

O2 has four layers, and each layer answers one question.

1. Classify: name the domain of a short scenario, with no rules file. Grade by exact match with the gold label. Report a confusion matrix per model. This measures thinking (T7).
2. Label: extract the domain of each action from a full answer. Rules 0.4 asks for one of five names, so a script can read it. Report the share that matches the gold label.
3. Act: answer one yes or no check per domain from the failure modes (T2, T3). Example for Chaotic: "Is action 1 a stabiliser?" A calibrated judge answers it.
4. Write: the checker grades the writing rules (banned words, dashes, sentence length), with no judge.

The gap between layers 1 and 2 answers the earlier question about the root cause. A model that classifies well alone but labels wrongly in a full answer fails to apply what it knows. A model that fails both does not know the domain [inference].

The human role under O2 has three jobs, and each job is blind:

- Label the gold domain of each scenario before any model output is seen. A second labeller, or the same labeller after seven days, measures agreement.
- Write free notes on 30 failed answers, then group them into failure modes. Each mode becomes one yes or no check.
- Mark 60 judge checks as pass or fail without the judge's answer in view. These marks give the judge's true positive and true negative rates.

### Assumption log

A1. No second person is available to label the scenarios. Why not measured: the user has not answered. Validate by: ask once (Follow-up). If wrong: measure agreement between two people, not between two sessions of one person.

A2. A script can read the domain of each action from answers at rules 0.4. Why not measured: no run at rules 0.4 exists yet. Validate by: run the extraction on 20 answers and check by eye. If wrong: a judge extracts the labels in layer 2, with a yes or no check per action.

A3. The API account gets funds. Why not measured: the user has not answered. Validate by: one call to the API. If wrong: Steps 2 and 4 wait, and Steps 1 and 3 still run, because they use answers on disk.

### Alternative considered

O1, repair the rubric, keeps the old runs comparable. It loses because the score would still mix three skills (E4), and seven of its nine criteria start below the agreement floor (E1).

## End

I recommend that we build the layered measures (O2) and give human judgment three blind jobs in place of the hand scoring.

1. Write a gold set of 60 short scenarios, 12 per domain, in matched pairs, and label it blind.
   - Increment: 30 pairs where one changed fact moves the domain (T6), for example "checkout is down" against "checkout is slow".
   - Blocker removed: no ground truth with a measured agreement exists (T8).
   - Kind: evaluative. Rubric: each scenario has one gold label and a one-line reason (weight 1); agreement between two labellings is 0.667 or more (weight 2). Pass threshold: both.
   - Domain: Complicated, because the labels need expert analysis, and T8 shows no prior labels.
2. Add a classify-only step to the harness and score it by script.
   - Increment: one prompt per scenario that asks for the domain name alone, and a confusion matrix per model.
   - Capability added: a measure of thinking per domain, free of the writing rules (layer 1).
   - Kind: deterministic. Test: Given a gold label of Complex and the answer "Complicated", When the scoring runs, Then the matrix counts one Complex scenario as Complicated.
   - Domain: Clear. Step 2 MUST NOT start until Step 1 passes.
3. Write free notes on 30 failed answers from the runs on disk, then group them into failure modes.
   - Increment: one note per answer, then one list of modes with a count each, until 10 answers in a row add no new mode.
   - Blocker removed: the checks of layer 3 have no source in real failures (T3).
   - Kind: evaluative. Rubric: every mode has at least two answers behind it (weight 1); each mode names one domain (weight 1). Pass threshold: both.
   - Domain: Complicated. Step 3 MAY run in parallel with Steps 1 and 2.
4. Probe whether yes or no checks raise judge agreement, against the current rubric.
   - Increment: the checks from Step 3, run by both judges on 40 answers, plus 60 blind pass or fail marks by the user.
   - Capability added: a judge whose error rates are known, for layer 3.
   - Kind: stochastic. Metric: kappa between the judges on each check. Baseline: 0.43 for R3 (E1). Pass threshold: 0.667 on every check. Sample size: 40 answers. Budget: 10 USD. Stop condition: the median kappa stays below 0.43 after 20 answers.
   - Domain: Complex. Leverage is a guess. Step 4 MUST NOT start until Step 3 passes.
5. Report each layer per model and per domain, with error bars, in place of the single pass rate.
   - Increment: one table per model in the record, with one row per layer. Each rate has a 95% interval clustered by scenario (T5).
   - Capability added: a result that names the failing skill and the domain (E4).
   - Kind: deterministic. Test: Given two runs with the same answers, When task eval:record runs, Then both tables match, and every rate shows its interval.
   - Domain: Clear. Step 5 MUST NOT start until Step 2 passes.

## Follow-up

Open question (1 of 3): can a second person label the 60 scenarios blind? If yes, Step 1 measures agreement between two people. If no, the user labels them again after seven days (A1).

If Step 4 fails, keep layers 1, 2, and 4, and report layer 3 from the user's blind marks alone. If A2 is false, a judge extracts the labels in layer 2.

This plan replaces Step 2 of the learning plan. The 34 answers of human-test.csv can still serve Step 3, as free notes rather than scores.

### References

[1] tests/evaluation/results, scores.csv of each run, agreement computed in this session, 2026-10-31. [P]

[2] K. Krippendorff, Content Analysis: An Introduction to Its Methodology, 2nd ed. Thousand Oaks, CA: Sage, 2004, p. 241. [S]

[3] tests/evaluation/evaluation-tests.md, version 1.4, 2026. [P]

[4] Root-cause analysis of the runs at rules 0.2.2, this session, 2026-10-31. [P]

[5] Hand-scoring sheet, batch 1, in the gitignored .scratch folder, 2026-10-31. [P]

[6] L. Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena," NeurIPS 2023, arXiv:2306.05685. [S]

[7] A. Panickssery, S. R. Bowman, and S. Feng, "LLM Evaluators Recognize and Favor Their Own Generations," NeurIPS 2024, arXiv:2404.13076. [S]

[8] A. S. Thakur et al., "Judging the Judges: Evaluating Alignment and Vulnerabilities in LLMs-as-Judges," GEM2 workshop 2025, arXiv:2406.12624. [S]

[9] Anthropic, "Demystifying evals for AI agents," Engineering at Anthropic, Jan. 2026, <https://anthropic.com/engineering/demystifying-evals-for-ai-agents>. [S]

[10] R. K. Arora et al., "HealthBench: Evaluating Large Language Models Towards Improved Human Health," arXiv:2505.08775, 2025. [S]

[11] J. Cook, T. Rocktäschel, J. Foerster, D. Aumiller, and A. Wang, "TICKing All the Boxes: Generated Checklists Improve LLM Evaluation and Generation," arXiv:2410.03608, 2024. [S]

[12] H. Husain, "Why do you recommend binary (pass/fail) evaluations instead of 1-5 ratings (Likert scales)?," <https://hamel.dev/blog/posts/evals-faq/why-do-you-recommend-binary-passfail-evaluations-instead-of-1-5-ratings-likert-scales.html>. [S]

[13] "Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking," arXiv:2604.11581, 2026. [S]

[14] S. Shankar, J. D. Zamfirescu-Pereira, B. Hartmann, A. Parameswaran, and I. Arawjo, "Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences," UIST 2024, arXiv:2404.12272. [S]

[15] H. Husain and S. Shankar, "LLM Evals: Everything You Need to Know," <https://hamel.dev/blog/posts/evals-faq/>. [S]

[16] J. Beck et al., "Bias in the Loop: How Humans Evaluate AI-Generated Suggestions," arXiv:2509.08514, 2025. [S]

[17] E. Miller, "Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations," arXiv:2411.00640, 2024. [S]

[18] S. Yao, N. Shinn, P. Razavi, and K. Narasimhan, "τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains," ICLR 2025, arXiv:2406.12045. [S]

[19] F. M. Polo et al., "tinyBenchmarks: evaluating LLMs with fewer examples," ICML 2024, arXiv:2402.14992. [S]

[20] M. Gardner et al., "Evaluating Models' Local Decision Boundaries via Contrast Sets," Findings of EMNLP 2020, pp. 1307-1323. [S]

[21] M. Turpin, J. Michael, E. Perez, and S. R. Bowman, "Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting," NeurIPS 2023, arXiv:2305.04388. [S]

[22] D. J. Snowden and M. E. Boone, "A Leader's Framework for Decision Making," Harvard Business Review, vol. 85, no. 11, pp. 68-76, Nov. 2007. [P]

## Self-test

```text
Self-test
Questions asked: 1 of 3
Assumptions logged: 3
Claims with evidence or [judgment] label: yes
References: 22, all from session or identified with confidence: yes
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
