# Rule changes for the higher levels of Bloom's taxonomy: desk research

## Headline

Published evals support four changes to the wording of the rules, each aimed at one weak level. A fifth result warns against more rules.

1. Evaluate: check the self-test item by item from a list, not in one pass. Checklists and separate checks lifted self-review by 4 to 8 points.
2. Understand: give each reason a contrast with the nearest other domain. Contrastive examples beat plain examples by 4 to 16 points.
3. Understand and Analyze: state the principle of cause and effect once, then derive each domain from it. Step-back prompting gained 7 to 27 points.
4. Organization: wording alone has weak support. Repeating the precedence rule at the end has some support, and only for models that do not reason.
5. Each added rule lowers compliance with all the rules. So each change above SHOULD replace text, not add to it.

## Background

The user asked which changes to the rules would lift reasoning to the higher levels of Bloom's taxonomy. Three earlier probes changed wording, and only the form of answers moved.

## Relevance

Each probe costs 3 to 12 USD, and about 0.96 USD remain. So the evidence picks the order of the probes, and the cheapest test comes first.

## Information

This section gives the weak levels, the evidence for each lever, and the results that argue against some levers.

### The weak levels, from the record

| Level | Measure | Rate at rules 0.6 | What has failed to move it |
| --- | --- | --- | --- |
| Understand | Reason states cause and effect, both judges | 11 of 40 | A required reason; one example reason for each domain |
| Evaluate | Self-test counts right | 88 of 234 | None tried |
| Analyze | Domain right, both judges | 27 of 40 | Split the problem first |
| Organization | A3 keeps the rules the request leaves alone | 8 of 18 | A line in Section 0: 12 of 18, short of 14 |

E1. A required reason moved its presence from 12% to 78% of labels. Positive example reasons moved its content by about 5 of 40 actions.
[1]

### Evaluate: separate checks against a list

E2. Self-refinement against a generated checklist gained 7.8 points on LiveBench reasoning. The checklist also raised a judge's agreement with people from 46.4% to 52.2%.
[2]

E3. Chain-of-Verification answers each check in a separate pass. Separate checks beat one joint check on every task. FactScore rose from 55.9 to 63.7, and to 71.4 with a revision.
[3]

So the self-test SHOULD come from a list of the actions, each checked alone, and not from a glance at the draft. The script checks the self-test, so this probe needs no judge.

### Understand: a contrast in each reason

E4. Contrastive Chain-of-Thought shows a right and a wrong reason, and why the wrong one fails. With GPT-3.5-Turbo, it beat standard Chain-of-Thought on GSM8K (69.2 to 79.0) and StrategyQA (55.8 to 66.2).
[4]

E5. Step-back prompting asks first for the principle behind a problem. With PaLM-2L, it gained 7 points on MMLU Physics, 11 on Chemistry, and 27 on TimeQA.
[5]

E6. Metacognitive prompting runs five stages: understand, judge, re-evaluate, decide, and state confidence. It beat Chain-of-Thought variants on 10 datasets of language understanding.
[6]

E4 to E6 measure the accuracy of answers, not the quality of explanations. So the effect on reasons is an extrapolation [judgment].

### Evaluate: stated confidence

E7. For models tuned on human feedback, a stated confidence was better calibrated than token probabilities. The relative calibration error often fell by about 50%.
[7]

E8. Reasoning models stated better calibrated confidence than other models in 33 of 36 settings.
[8]

### Organization: position and repetition

E9. Repeating the prompt gave 47 significant wins and no losses in 70 pairs of model and benchmark, for models that do not reason. With reasoning on, the effect was neutral to slightly positive.
[9]

E10. Prompt-only fixes did not make models hold a system prompt against a user. Gains came mainly from fine-tuning.
[10]

### Evidence against more rules

E11. On a list of 500 instructions, the best models followed 62% to 69%. Models broke instructions late in the list 1.7 to 2.3 times as often as early ones, mostly by omission.
[11]

E12. Compliance fell steadily with each added instruction, up to 10.
[12]

E13. Combining simple instructions cut frontier models by 40% to 50%.
[13]

E14. Over 1,218 comparisons, Chain-of-Thought gained 14.2 points on symbolic tasks and 0.7 points on soft reasoning.
[14]

E15. On 3 of 6 tasks, Chain-of-Thought cut accuracy by up to 36.3 points.
[15]

So a Cynefin label, which is soft reasoning, gains little from "think step by step" [judgment]. Section 7 and Section 8 sit late in the rules, where E11 puts the most omissions.

### Candidate changes, ranked

| Rank | Level | Change to the rules | Evidence | Measure | Judge needed |
| --- | --- | --- | --- | --- | --- |
| 1 | Evaluate | Section 7: before the block, list each action with its label and test; count from the list | E2, E3 | Self-test counts right | No |
| 2 | Understand | Section 6.3: the reason says how cause and effect relate, and why the nearest other domain does not fit | E4 | Reason states cause and effect | Yes |
| 3 | Understand, Analyze | Section 6.5: state once how cause and effect relate in the problem; derive each domain from it | E5, E6 | Domain right; reason states cause and effect | Yes |
| 4 | Organization | End of the rules: repeat the precedence line of Section 0 | E9, E11 | A3 structure | No |
| 5 | Evaluate | Section 6.3: name the one fact that would move the action to another domain | E7, E8 | Calibration against the judge | Yes |

Rank 1 comes first because the script measures it, so it costs about 3 USD with no judge. Rank 4 comes last of the cheap probes, because E10 found prompt-only fixes weak.

### Limits

- No source measures the quality of a causal explanation. Claim, evidence, and reasoning templates, and the self-explanation effect of education research, have no published numbers for language models.
- E4 to E6 used models from 2023. Current models reason more, and E14 and E15 show that rules for reasoning help them less.
- A probe of 18 answers cannot detect 15 points. A paired design needs about 70 answers in each arm to detect 44% against 67%.

### Alternative considered

Cut the rules to a shorter template before any new wording, as E11 to E13 suggest. It loses for now, because it changes every level at once, so no result points to one cause. It is the right next step if two probes of new wording fail.

## End

I recommend that we probe the factored self-test first, because the script measures it with no judge.

1. Probe rank 1, the self-test from a list of actions.
   - Increment: one rules file in a run folder, and one run of 6 core prompts with no judge.
   - Capability added: a first lever on the Evaluate level (E2, E3).
   - Kind: stochastic. Metric: answers whose self-test counts are right. Baseline: 38% (88 of 234). Pass threshold: 53%, with the interval above 0. Sample size: 108 answers. Budget: 3 USD. Stop condition: the spend passes 4 USD.
   - Domain: Complex, because no change has touched this level, so leverage is a guess.
2. Probe rank 2, the contrast in each reason, once Step 1 ends.
   - Increment: one line in Section 6.3 of a rules file in a run folder, and the action checks by two judges.
   - Capability added: a test of the strongest lever for reasons (E4).
   - Kind: stochastic. Metric: actions whose reason states cause and effect, by both judges. Baseline: 11 of 40. Pass threshold: 20 of 40. Sample size: 40 actions. Budget: 6 USD. Stop condition: the spend passes 7 USD.
   - Domain: Complex, because E4 measured answers, not reasons.
3. Mark the 40 actions of human-actions.md blind.
   - Increment: 80 marks by a person.
   - Blocker removed: Step 2 trusts the judges on reasons, and no person has checked them.
   - Kind: evaluative. Rubric: two marks for every action (weight 1); no verdict read first (weight 2). Pass threshold: both.
   - Domain: Complicated, because the marks need expert reading.

## Follow-up

Step 1 fits the funds only after a top-up of about 3 USD. If Steps 1 and 2 both fail, cut the rules to a shorter template, as the alternative says.

### References

[1] tests/evaluation/results/2026-11-01-wording-results.md and 2026-11-01-reason-examples-results.md, 2026. [S]

[2] J. Cook et al., "TICKing All the Boxes: Generated Checklists Improve LLM Evaluation and Generation," 2024, <https://arxiv.org/abs/2410.03608>. [P]

[3] S. Dhuliawala et al., "Chain-of-Verification Reduces Hallucination in Large Language Models," 2023, <https://arxiv.org/abs/2309.11495>. [P]

[4] Y. K. Chia et al., "Contrastive Chain-of-Thought Prompting," 2023, <https://arxiv.org/abs/2311.09277>. [P]

[5] H. S. Zheng et al., "Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models," 2023, <https://arxiv.org/abs/2310.06117>. [P]

[6] Y. Wang and Y. Zhao, "Metacognitive Prompting Improves Understanding in Large Language Models," 2023, <https://arxiv.org/abs/2308.05342>. [P]

[7] K. Tian et al., "Just Ask for Calibration," 2023, <https://arxiv.org/abs/2305.14975>. [P]

[8] D. Yoon et al., "Reasoning Models Better Express Their Confidence," 2025, <https://arxiv.org/abs/2505.14489>. [P]

[9] Y. Leviathan et al., "Prompt Repetition Improves Non-Reasoning LLMs," 2025, <https://arxiv.org/abs/2512.14982>. [P]

[10] N. Mu et al., "A Closer Look at System Prompt Robustness," 2025, <https://arxiv.org/abs/2502.12197>. [P]

[11] D. Jaroslawicz et al., "How Many Instructions Can LLMs Follow at Once?," 2025, <https://arxiv.org/abs/2507.11538>. [P]

[12] K. Harada et al., "When Instructions Multiply," 2025, <https://arxiv.org/abs/2509.21051>. [P]

[13] R. Murthy et al., "KCIF: Knowledge-Conditioned Instruction Following," 2024, <https://arxiv.org/abs/2410.12972>. [P]

[14] Z. Sprague et al., "To CoT or not to CoT?," 2024, <https://arxiv.org/abs/2409.12183>. [P]

[15] R. Liu et al., "Mind Your Step (by Step)," 2024, <https://arxiv.org/abs/2410.21333>. [P]

## Self-test

```text
Self-test
Questions asked: 0 of 3
Assumptions logged: 0
Claims with evidence or [judgment] label: yes
References: 15, all from session or identified with confidence: yes
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
