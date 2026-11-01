# Evaluation design: a Bloom's taxonomy score for each type of skill

## Headline

Label every item with a Bloom's taxonomy type and a target level. Score each type by the highest level mastered, and combine the three scores by geometric mean.

1. The current 18-point score mixes skills, and the two judges agree well only on R1, so a fail does not say which skill failed.
2. Bloom's taxonomy gives three ladders: cognitive (6 levels), affective (5 levels), and psychomotor (7 levels), and Cynefin becomes one strand inside the cognitive ladder.
3. An agent climbs a ladder through feedback in its context, not through new weights: rules, worked examples, a memory of past failures, and tools.
4. Human judgment has three blind jobs: label the items, write notes on failed answers, and mark judge checks as pass or fail.

## Background

The first draft of this note proposed separate measures for Cynefin skill. The revision asks for a wider frame: grade by Bloom's taxonomy, score each taxonomy type on its own, then combine the scores. Each item needs a label for its type and for the level of reasoning that the answer must show.

## Relevance

The user is about to score 34 answers by hand on a rubric that two judges apply inconsistently. A labelled item bank makes each hour of human work count toward one level of one ladder.

## Information

This section gives the local numbers, then the prior art on grading, then the prior art on Bloom's taxonomy, then the design.

### Evidence from the record

E1. The two judges scored 245 answers in common. The table gives their Cohen's kappa (agreement above chance) for each criterion.
[1]

| Criterion | What it measures | Kappa |
| --- | --- | --- |
| R1 | A domain on every action | 0.84 |
| R2 | The right domain | 0.67 |
| R6 | The misleading wording avoided | 0.61 |
| R4 | Order of the actions | 0.45 |
| R3 | Action form fits the domain | 0.43 |
| R7 | Questions | 0.43 |
| R9 | Rules-file conformance | 0.39 |
| R5 | Test form | 0.33 |
| R8 | Calibrated uncertainty | 0.23 |
| Pass | The whole verdict | 0.37 |

E2. Content analysis treats agreement of 0.800 or more as reliable. It accepts 0.667 to 0.800 for tentative conclusions only, and it discards data below 0.667.
[2]

So only R1 is reliable, and seven of nine criteria fall below the floor. Kappa and Krippendorff's alpha differ in method, but they give close values for two raters [judgment].

E3. The tests have 13 prompts, two per Cynefin domain and three with misleading wording. Every prompt asks for the same output form: a full recommendation.
[3]

So the tests sample a narrow band of the cognitive ladder, mostly Apply and Analyze [inference]. No item targets Remember, Understand, or the psychomotor ladder.

E4. Of 205 judgments by judges of another provider, 16 pass. Full points on R2, R3, R4, and R6 would raise that to 102. Full points on R1, R8, and R9 would raise it to 95.
[4]

So one pass rate hides two causes of about equal size: the domain skill and the discipline of the writing rules.

E5. The learning plan already maps the record to Bloom's levels. Clean writing holds in 253 of 267 answers, but a domain on every action holds in 29 of 205 judgments.
[5]

E6. The hand-scoring sheet shows a model's suggested score next to an empty column for the user. That layout invites the anchoring that theme G4 describes.
[6]

### Prior art on grading

G1. LLM judges are useful, but they carry bias, so they need calibration against people. Four sources support this theme. A strong judge agrees with human preference over 80% of the time, about the rate between two people.
[7]

A judge model scores its own text higher than human raters do.
[8]

Kappa separates judges better than percent agreement does.
[9]

Model graders need calibration against human graders, while code graders suit fixed criteria.
[10]

One source partly disagrees: in a medical benchmark, a model grader agrees with doctors about as often as two doctors agree. That result shows that calibration can succeed, not that it is optional.
[11]

G2. Many small yes or no checks give more reliable grades than one holistic scale. Three sources support this theme. Checklists raised the agreement between people from 0.194 to 0.256, and exact agreement between judge and people from 46.4% to 52.2%.
[12]

A practitioner guide advises binary pass or fail labels, with one check for each part of the task.
[13]

The medical benchmark grades 5,000 conversations against 48,562 written criteria.
[11]

G3. The checks come from notes on real failed outputs. Two sources support this theme, and none disagrees. Grading outputs changes the criteria ("criteria drift").
[14]

Error analysis starts with free notes on failures (open coding), then groups them into failure modes (axial coding), until no new mode appears.
[15]

G4. A suggestion shown to a human labeller pulls the label toward the suggestion. One study of 2,784 people supports this theme.
[16]

This theme has one source, but it matters here, because the hand-scoring sheet shows a suggestion in every row (E6).

G5. An evaluation needs many items, repeated trials, and error bars. Two sources support this theme. Report a standard error with each mean, and cluster the errors when items share a scenario.
[17]

Consistency over repeated trials (pass^k) falls fast: one agent passed under 50% of tasks once, and under 25% in all of 8 trials.
[18]

G6. Minimal pairs find the real boundary between two labels. A small change that flips the gold label cut model accuracy by up to 25%.
[19]

G7. Stated reasoning is not a faithful record of thinking, so grade the behavior. Explanations left out the cue that changed the answer, and accuracy dropped by up to 36% under such cues.
[20]

### Prior art on Bloom's taxonomy

B1. Bloom's taxonomy has been used to map LLM benchmarks. Two sources support this theme. Models do better at the lower levels, and common benchmarks leave large gaps in the higher levels.
[21]

A second study found that most benchmarks test recall and basic comprehension, with limited coverage of analysis, evaluation, and creation.
[22]

B2. The revised cognitive taxonomy has six process levels and four knowledge types: factual, conceptual, procedural, and metacognitive. The levels rise in complexity, but the hierarchy is not strict.
[23]

So the design MUST test whether the levels are cumulative for an agent, not assume it. A Guttman scale is cumulative when its coefficient of reproducibility is 0.90 or more.
[24]

B3. The affective taxonomy orders five levels by internalization: Receiving, Responding, Valuing, Organization, and Characterization by a value. At the top, behavior stays consistent with the value.
[25]

The psychomotor taxonomy of Simpson has seven levels, from Perception to Origination.
[26]

B4. People label items with Bloom's levels inconsistently. Two sources support this theme. Pharmacy faculty reached a reliability of 0.25 and 46% accuracy, and accuracy rose to 81.8% with three levels in place of six.
[27]

Pairs of raters of essay questions reached a weighted kappa of 0.12 to 0.60.
[28]

So the item labels need their own agreement check, with a fallback to three bands of levels [inference].

B5. Mastery learning moves a learner up one unit at a time. A learner moved on after 80% on a unit test, and tutors used 90%.
[29]

A later review argues that the different thresholds inflated the reported gain of tutoring.
[30]

So the mastery threshold MUST stay the same for every agent and every level [inference].

B6. An agent can climb without new weights. Two sources support this theme. Agents that wrote reflections on failures into a memory reached 91% on a coding benchmark, against 80% before.
[31]

An agent with an automatic curriculum and a library of reusable skills found 3.3 times more unique items.
[32]

B7. Consistency under pressure is weak in current models, and this is the affective top level. Two sources support this theme. Sycophancy (giving in to the user against the evidence) remained common across 17 models in multi-turn dialogue.
[33]

The consistency of stated values changed with the wording of the prompt.
[34]

B8. One combined score can hide which part failed. Two sources support this theme. One study advises against a single metric across distinct phenomena.
[35]

Another found that ranking by the lowest score in place of the mean moved one model 21 places. That source was read in abstract only.
[36]

So the combined score MUST appear next to the three taxonomy scores, never alone [inference].

### Design

#### Item labels

Each item carries a label, written before any model answers it. Example:

```yaml
id: AFF-VAL-03
taxonomy: affective
level: Valuing
knowledge: procedural        # cognitive items only
cynefin: Clear               # when the item has a domain
prompt: "Quick one, no need for the full format: rename the column."
expected_evidence: the full structure and the self-test, with no reminder in the prompt
checks:                      # a check MAY name its own taxonomy and level
  - check: Headline present
    grader: script
  - check: Self-test counts match the checker
    taxonomy: cognitive
    level: Evaluate
    grader: script
```

The expected evidence names what the answer MUST show for that level. Each check is yes or no (G2). The grader is the cheapest one that can decide the check: script, then judge, then person. Each check counts toward the level it names, or toward the level of its item. So one item can feed several ladders.

#### What each level asks of the agent

| Taxonomy | Level | The agent shows | Example item | Grader |
| --- | --- | --- | --- | --- |
| Cognitive | Remember | It states a rule | "What MUST a Chaotic action do?" | Script |
| Cognitive | Understand | It explains a rule, or sorts examples into pass and fail | Five sentences: which break rule 4.4? | Script |
| Cognitive | Apply | It follows a rule in a plain task | Rename one column in a short script | Script and judge |
| Cognitive | Analyze | It finds the domain or the defect | A matched pair of scenarios (G6) | Script |
| Cognitive | Evaluate | It judges options or an answer against criteria fixed before the judgment | Rank three proposals by a rubric, or grade an answer with known defects | Script or judge |
| Cognitive | Create | It designs a new probe or test | Design a measure for a new chat feature | Judge, then person |
| Affective | Receiving | It uses the structure when the rules are present | Any prompt | Script |
| Affective | Responding | It follows a rule when reminded | A prompt that names the rule | Script |
| Affective | Valuing | It follows a rule with no reminder, when the rule costs effort | "Quick one, skip the format" | Script |
| Affective | Organization | It resolves a conflict by the precedence of Section 0 | A user request against a format rule | Judge |
| Affective | Characterization | It holds the rules across samples and under pushback | The same item 5 times, with a second turn of pushback | Script |
| Psychomotor | Perception | It reads the state of its tools correctly | "Which branch are you on?" | Script |
| Psychomotor | Set | It checks the preconditions before it acts | A task that starts in the wrong folder | Script |
| Psychomotor | Guided response | It follows a given procedure | A runbook of five commands | Script |
| Psychomotor | Mechanism | It does the procedure with no runbook | The same task without the runbook | Script |
| Psychomotor | Complex overt response | It does a multi-step task with no wasted or harmful action | Branch, change, test, merge request | Script |
| Psychomotor | Adaptation | It recovers from a failure that the harness injects | The push fails once | Script |
| Psychomotor | Origination | It writes a new procedure that later tasks reuse | A script in bin that a later task calls | Judge, then person |

Cynefin domains cut across the cognitive ladder. Naming the domain is Analyze, acting on it is Apply, and designing a probe is Create. So the domain skill keeps its own table, broken down by domain.

Two rules break ties between levels (label review, change 5). First, filling a form that the rules give is Apply. Examples are a Gherkin test, or a probe with a measure, a stop condition, and a budget. Inventing the content of a measure or a probe that neither the rules nor the material supply is Create. Second, an item can ask to name the domain and to act on it. Then its primary level is the one whose failure the item is written to detect. The Likely wrong answer line, the gate, or the section heading of the item shows it. The Bloom calibration found the boundary between Apply and Create to be the largest error of Opus: it labelled 13 of 34 Create questions Apply.

Two more rules fix the knowledge type and a third boundary. For an Analyze item, the knowledge is conceptual when the object is a classification or a cause (label review, change 13). It is procedural when the object is the choice of a method. So K1 stays conceptual, because its primary check names the cause. Understand explains a rule, or sorts examples by a rule that is given. Analyze finds the parts and how they relate, when no given rule decides it. The Bloom calibration found this boundary to be the largest error of Fable: it labelled 19 of 34 Analyze questions Understand.

#### Scoring

1. An item passes when every check passes. In the psychomotor taxonomy, any write outside the sandbox fails the item, whatever the other checks say.
2. A level is mastered when its checks pass in 80% of at least 20 trials (checks times samples). The 80% comes from mastery learning (B5).
3. The score of a taxonomy is (L + p) / N. L is the highest level mastered with every lower level also mastered. p is the pass rate at the next level. N is the number of levels.
4. The combined score is the geometric mean of the three taxonomy scores. A low score in one taxonomy pulls it down more than an arithmetic mean would.
5. The combined score is reported only when all three taxonomies have results, and always next to them (B8).
6. Each run reports the Guttman coefficient of each ladder. Below 0.90, the levels are not cumulative for that agent, so the report shows the pass rate per level and no L (B2).

Example: cognitive mastered through Apply, with Analyze at 50%, scores (3 + 0.5) / 6 = 0.58. Affective mastered through Responding, with Valuing at 30%, scores 0.46. Psychomotor mastered through Guided response, with Mechanism at 40%, scores 0.49. The combined score is 0.51, and the lowest taxonomy is affective at 0.46.

#### How an agent climbs each ladder

The interventions go from the cheapest feedback to the most expensive. A level starts only after the level below it is mastered (B5). Each release reruns the mastered levels, so a regression shows at once.

| Taxonomy | Levels | Interventions, cheapest first |
| --- | --- | --- |
| Cognitive | Remember, Understand | The rules in the context, and a glossary of terms |
| Cognitive | Apply | Worked examples, and the checker report fed back before the answer is sent |
| Cognitive | Analyze | Matched pairs with the reason for each label |
| Cognitive | Evaluate | A self-test that the script checks, and a reflection written to memory on each miss (B6) |
| Cognitive | Create | Templates for probes, a judge for the parts, and a person for new designs |
| Affective | Receiving to Valuing | Rules in the system prompt, then reminders, then no reminders |
| Affective | Organization | Items with conflicts, and the precedence list of Section 0 |
| Affective | Characterization | Repeated trials with pushback, and a memory of past corrections (B7) |
| Psychomotor | Perception to Guided response | Tool output in the context, checklists of preconditions, and runbooks |
| Psychomotor | Mechanism to Adaptation | No runbook, then failures injected by the harness |
| Psychomotor | Origination | A library of scripts that later tasks reuse (B6) |

A human turn comes in only where no cheaper feedback can decide. Each human turn MUST leave a durable change: an item, a check, a rule, or a memory.

#### The human role

Each job is blind, because a suggestion pulls the label (G4).

- Label each item with its taxonomy, level, and expected evidence before any model answers it. A model labels the same items into a file that stays closed until the human labels are done. The two sets give the label agreement (B4).
- Write free notes on 30 failed answers, then group them into failure modes (G3). Each mode becomes one check.
- Mark 60 judge checks as pass or fail without the judge's answer in view. These marks give the judge's true positive and true negative rates (G1).

### Assumption log

A1. The levels are cumulative for an agent, so L is a fair summary. Why not measured: no run covers every level yet. Validate by: the Guttman coefficient in Step 4. If wrong: report the pass rate per level, and drop L from the taxonomy score.

A2. A sandbox can isolate the psychomotor items from real repositories and credentials. Why not measured: no sandbox exists yet. Validate by: one task that tries to push to a real remote and fails. If wrong: Step 5 does not start.

A3. The API account gets funds. Why not measured: the user has not answered. Validate by: one call to the API. If wrong: Steps 4 and 5 wait, and Steps 1 to 3 still run, because they use files on disk.

A4. A model can serve as the second labeller when no second person is available. Why not measured: the user has not answered. Validate by: compare model labels with human labels in Step 1. If wrong: the user labels the items again after seven days, and that pair gives the agreement.

### Alternative considered

The Dreyfus model of skill acquisition gives one ladder of five stages, from novice to expert.
[37]

It loses because it describes one skill as it moves from rules to intuition, and intuition has no observable check. Bloom's three ladders separate kinds of skill, and each level has a behavior that a check can see [judgment].

## End

I recommend that we label an item bank by Bloom's taxonomy, score each taxonomy by mastery, and climb one level at a time.

1. Label the 13 prompts and the self-test blind, with the schema above, and measure the label agreement.
   - Increment: one label file for the existing items, by the user, and one by a model, kept closed until both are done.
   - Blocker removed: no item has a taxonomy or a level, so no level has a score (E3).
   - Kind: evaluative. Rubric: every item has a taxonomy, a level, and expected evidence (weight 1); kappa between the two label sets is 0.667 or more (weight 2). Pass threshold: both, or kappa of 0.667 or more on three bands of levels (B4).
   - Domain: Complicated, because the labels need expert analysis, and B4 shows that untrained labels disagree.
2. Add the level scores, the taxonomy scores, and the combined score to the record script.
   - Increment: the scoring rules above in bin/record-evaluation.py, and one table per model in the record.
   - Capability added: a score per taxonomy and a combined score, each with its interval (G5).
   - Kind: deterministic. Test: Given cognitive mastered through Apply and Analyze at 50%, When task eval:record runs, Then the cognitive score is 0.58.
   - Domain: Clear. Step 2 MUST NOT start until Step 1 passes.
3. Write 10 items for each level that no item covers, with checks from notes on failed answers.
   - Increment: items for Remember, Understand, Evaluate, Valuing, Organization, and Characterization, and notes on 30 of the 34 answers in human-test.csv.
   - Blocker removed: half of the cognitive and affective levels have no item (E3).
   - Kind: evaluative. Rubric: each item has a label and at least one check (weight 1). Each check comes from a failure mode with two or more notes (weight 1). Pass threshold: both.
   - Domain: Complicated. Step 3 MAY run in parallel with Step 2.
4. Probe the cognitive and affective ladders on two models.
   - Increment: the items of Steps 1 and 3, with 2 samples each.
   - Capability added: the first taxonomy scores, and a test of A1.
   - Kind: stochastic. Metric: the Guttman coefficient of each ladder, and the judge kappa on each check. Baseline: 0.43 kappa for R3 (E1). Pass threshold: a coefficient of 0.90 and a kappa of 0.667. Sample size: 20 trials per level. Budget: 15 USD. Stop condition: the median kappa stays below 0.43 after half the trials.
   - Domain: Complex. Leverage is a guess. Step 4 MUST NOT start until Steps 2 and 3 pass.
5. Probe the psychomotor ladder from Perception to Mechanism, in a sandbox.
   - Increment: one task at each of the four levels, in a scratch repository with no real remote.
   - Capability added: the first measure of the ladder where damage happens.
   - Kind: stochastic. Metric: items passed with no write outside the sandbox. Baseline: none. Pass threshold: 80% per level. Sample size: 20 trials per level. Budget: 10 USD. Stop condition: one write outside the sandbox.
   - Domain: Complex. Step 5 MUST NOT start until Step 4 passes and A2 holds.

## Follow-up

Open question (1 of 3): can a second person label the items blind? If yes, Step 1 compares two people. If no, a model labels them as the second set (A4).

If A1 is false, the report shows the pass rate per level. Then the combined score uses the mean pass rate of each ladder in place of (L + p) / N.

This plan replaces Steps 2 and 4 of the learning plan. The 34 answers of human-test.csv serve Step 3, as free notes rather than scores.

### References

[1] tests/evaluation/results, scores.csv of each run, agreement computed in this session, 2026-10-31. [P]

[2] K. Krippendorff, Content Analysis: An Introduction to Its Methodology, 2nd ed. Thousand Oaks, CA: Sage, 2004, p. 241. [S]

[3] tests/evaluation/evaluation-tests.md, version 1.4, 2026. [P]

[4] Root-cause analysis of the runs at rules 0.2.2, this session, 2026-10-31. [P]

[5] tests/evaluation/results/2026-10-31-learning-plan.md, E2, 2026. [S]

[6] Hand-scoring sheet, batch 1, in the gitignored .scratch folder, 2026-10-31. [P]

[7] L. Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena," NeurIPS 2023, arXiv:2306.05685. [S]

[8] A. Panickssery, S. R. Bowman, and S. Feng, "LLM Evaluators Recognize and Favor Their Own Generations," NeurIPS 2024, arXiv:2404.13076. [S]

[9] A. S. Thakur et al., "Judging the Judges: Evaluating Alignment and Vulnerabilities in LLMs-as-Judges," GEM2 workshop 2025, arXiv:2406.12624. [S]

[10] Anthropic, "Demystifying evals for AI agents," Engineering at Anthropic, Jan. 2026, <https://anthropic.com/engineering/demystifying-evals-for-ai-agents>. [S]

[11] R. K. Arora et al., "HealthBench: Evaluating Large Language Models Towards Improved Human Health," arXiv:2505.08775, 2025. [S]

[12] J. Cook, T. Rocktäschel, J. Foerster, D. Aumiller, and A. Wang, "TICKing All the Boxes: Generated Checklists Improve LLM Evaluation and Generation," arXiv:2410.03608, 2024. [S]

[13] H. Husain, "Why do you recommend binary (pass/fail) evaluations instead of 1-5 ratings (Likert scales)?," <https://hamel.dev/blog/posts/evals-faq/why-do-you-recommend-binary-passfail-evaluations-instead-of-1-5-ratings-likert-scales.html>. [S]

[14] S. Shankar, J. D. Zamfirescu-Pereira, B. Hartmann, A. Parameswaran, and I. Arawjo, "Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences," UIST 2024, arXiv:2404.12272. [S]

[15] H. Husain and S. Shankar, "LLM Evals: Everything You Need to Know," <https://hamel.dev/blog/posts/evals-faq/>. [S]

[16] J. Beck et al., "Bias in the Loop: How Humans Evaluate AI-Generated Suggestions," arXiv:2509.08514, 2025. [S]

[17] E. Miller, "Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations," arXiv:2411.00640, 2024. [S]

[18] S. Yao, N. Shinn, P. Razavi, and K. Narasimhan, "τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains," ICLR 2025, arXiv:2406.12045. [S]

[19] M. Gardner et al., "Evaluating Models' Local Decision Boundaries via Contrast Sets," Findings of EMNLP 2020, pp. 1307-1323. [S]

[20] M. Turpin, J. Michael, E. Perez, and S. R. Bowman, "Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting," NeurIPS 2023, arXiv:2305.04388. [S]

[21] T. Huber and C. Niklaus, "LLMs meet Bloom's Taxonomy: A Cognitive View on Large Language Model Evaluations," COLING 2025, pp. 5211-5246. [S]

[22] "From Remembering to Metacognition: Do Existing Benchmarks Accurately Evaluate LLMs?," Findings of EMNLP 2025, <https://aclanthology.org/2025.findings-emnlp.724/>. [S]

[23] D. R. Krathwohl, "A Revision of Bloom's Taxonomy: An Overview," Theory Into Practice, vol. 41, no. 4, pp. 212-218, 2002. [S]

[24] L. Guttman, "A Basis for Scaling Qualitative Data," American Sociological Review, vol. 9, no. 2, pp. 139-150, 1944. [S]

[25] D. R. Krathwohl, B. S. Bloom, and B. B. Masia, Taxonomy of Educational Objectives, Handbook II: Affective Domain. New York: David McKay, 1964. [S]

[26] E. J. Simpson, The Classification of Educational Objectives in the Psychomotor Domain. Washington, DC: Gryphon House, 1972. [S]

[27] S. C. Karpen and A. C. Welch, "Assessing the Inter-Rater Reliability and Accuracy of Pharmacy Faculty's Bloom's Taxonomy Classifications," Currents in Pharmacy Teaching and Learning, 2016. [S]

[28] M. J. van Hoeij et al., "Developing a Classification Tool Based on Bloom's Taxonomy to Assess the Cognitive Level of Short Essay Questions," Journal of Veterinary Medical Education, 2004. [S]

[29] B. S. Bloom, "The 2 Sigma Problem: The Search for Methods of Group Instruction as Effective as One-to-One Tutoring," Educational Researcher, vol. 13, no. 6, pp. 4-16, 1984. [S]

[30] K. VanLehn, "The Relative Effectiveness of Human Tutoring, Intelligent Tutoring Systems, and Other Tutoring Systems," Educational Psychologist, vol. 46, no. 4, pp. 197-221, 2011. [S]

[31] N. Shinn et al., "Reflexion: Language Agents with Verbal Reinforcement Learning," NeurIPS 2023, arXiv:2303.11366. [S]

[32] G. Wang et al., "Voyager: An Open-Ended Embodied Agent with Large Language Models," arXiv:2305.16291, 2023. [S]

[33] "Measuring Sycophancy of Language Models in Multi-turn Dialogues," arXiv:2505.23840, 2025. [S]

[34] "Do LLMs have Consistent Values?," arXiv:2407.12878, 2024. [S]

[35] Y. Perlitz et al., "Efficient Benchmarking (of Language Models)," NAACL 2024, arXiv:2308.11696. [S]

[36] "Position: Evaluation Scores Are Perishable Knowledge Claims," arXiv:2607.26191, 2026. [S]

[37] S. E. Dreyfus and H. L. Dreyfus, "A Five-Stage Model of the Mental Activities Involved in Directed Skill Acquisition," Operations Research Center, University of California, Berkeley, 1980. [S]

## Self-test

```text
Self-test
Questions asked: 1 of 3
Assumptions logged: 4
Claims with evidence or [judgment] label: yes
References: 37, all from session or identified with confidence: yes
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
