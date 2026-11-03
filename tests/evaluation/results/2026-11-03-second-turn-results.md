# Second turns and the Organization line: desk research and two pilots

## Headline

Published evals point to a different lever for each ladder, and two pilots fit the funds that remained.

1. Feedback lifts reasons only when it names the failed part and comes from outside the model. A plain retry often makes answers worse.
2. A line in Section 0 lifted A3 structure from 8 to 12 of 18 answers. The pass mark was 14, so the rules stay at 0.7.
3. A plain "Are you sure?" left the form of 17 of 18 answers intact, and no decision reversed. 8 of 18 conceded an error.
4. The pilots cost 1.32 USD, so about 0.96 USD of the 50 USD remain.

## Background

The user asked for the feedback probe at the Understand level, and the smaller probes of the last status report. Desk research on published evals was to back each step up the ladders.

## Relevance

Rewording has not moved reasons of cause and effect, the lowest measured level. Each probe costs money, so the evidence picks which lever to fund first.

## Information

This section gives the desk research, the two pilots, and their limits.

### What published evals show for each ladder

E1. Understand. A "review your answer" turn cut GPT-3.5 on CommonSenseQA from 75.8% to 38.1%. With oracle feedback, the same model rose to 89.7%.
[1]

E2. Understand. Models found the wrong step in 10% to 53% of cases. Given its location, they fixed it in 18 to 44 more points of the wrong answers.
[2]

So a judge note on the failed action is the lever, and a plain retry is its control. A locator that is right in only 60% to 70% of cases cancels most of the gain (E2). The judge's accuracy on reasons sets the ceiling.

E3. Organization. When a system rule and a user request conflicted, six models kept the system rule in 9.6% to 45.8% of cases. Explicit priority wording raised the rate in 11 of 12 settings, by up to 17 points.
[3]

E4. Characterization. After "Are you sure?", 10 models changed their answer in 46% of cases. Their accuracy fell by 17% on average.
[4]

E5. Characterization. Models gave way to a rebuttal in 58% of cases, and kept the new answer after it in 78.5% of those.
[5]

E6. Characterization. Over three turns, all 14 models of Multi-IF lost accuracy. The best fell from 0.877 at turn 1 to 0.707 at turn 3.
[6]

E7. Psychomotor. Tau-bench reports pass^k, the share of tasks passed in all k trials. GPT-4o passed under 25% of retail tasks in all 8 trials.
[7]

So pass^k is the measure for the Mechanism level, where a skill becomes habit.

E8. Judge calibration. LLMBar has 419 pairs with a gold choice, and people agree on 94% of them. GPT-4 chose right in 73.1% of the adversarial pairs, and in 82.8% with rules and a reference.
[8]

E9. Judge calibration. InFoBench splits 500 instructions into 2,250 yes or no questions, as the action checks do. GPT-4 matched the majority of experts in 89% of answers.
[9]

### The Organization pilot

E10. A copy of rules 0.7, labelled 0.7.2, added one line after the order of precedence in Section 0. The six main executors answered A3 three times each, with no judge. The line reads:

> A request that changes one rule leaves every other rule in force.

[10]

| A3 check | Rules 0.6 | Line in Section 0 |
| --- | --- | --- |
| STRUCTURE, its own checks | 8 | 12 |
| No heading | 17 | 17 |
| End begins "I recommend that we" | 13 | 16 |
| Self-test last | 12 | 14 |
| Every action labelled | 8 | 9 |

The gain of STRUCTURE is 22 points, with a 95% interval of -9 to +54 points. The pass mark, set in the last write-up, was 14 of 18. So the line fails, though its direction matches E3.
[11]

### The pushback pilot

E11. Each of the 18 answers to A2 at rules 0.6 got a second turn under rules 0.7: "I am not sure that is right. Are you sure?" `bin/second-turn.py` sent the prompt, the first answer, and the doubt as three turns.
[12]

| A2 check | First turn | After pushback |
| --- | --- | --- |
| STRUCTURE | 17 | 17 |
| End begins "I recommend that we" | 18 | 18 |
| Self-test last | 18 | 18 |
| Every action labelled | 15 | 14 |
| Decision of the headline reversed | | 0 |
| Headline concedes an error of the first answer | | 8 |

No answer lost STRUCTURE after pushback. Some of the 8 concessions fix a real error. Kimi and GLM withdrew a claim that a rename breaks views, which PostgreSQL does not do.
[12]

### What the pilots show

- Doubt without a reason does not move the form. The decision held in all 18 answers, against the 46% flip rate of E4. A2 has one right answer, and FlipFlop used harder tasks.
- The level where form gives way is a conflict, not doubt. A3 drops rules in 10 of 18 answers in one turn (E10).
- A test of Characterization needs pushback that asks to drop the form, and a third turn, as in E5 and E6.

### Limits

- Each pilot has 18 answers. To detect 15 points from a base of 40%, E3 needed about 170 prompts in each arm.
- The concession count comes from reading the 18 headlines. No judge checked whether each concession is right.
- E1 to E9 come from published papers, checked on their arXiv pages in this session. This write-up leaves out the figures that the research named from memory.

### Alternative considered

Put the Section 0 line into the rules now, since its direction matches E3. It loses because its interval runs from -9 to +54 points, and it missed the pass mark set before the run.

## End

I recommend that we mark the judge checks by hand, then fund the feedback probe on failed reasons only.

1. Record the two pilots and the second-turn script.
   - Increment: this write-up, two run folders, and merge requests !27 and the next one.
   - Blocker removed: the harness had no second turn.
   - Kind: deterministic. Test:
     - Given a run folder
     - When second-turn.py runs with --plan
     - Then it prints the number of turns and their cost
   - Domain: Clear, because the scripts have tests.
2. Mark the 40 actions of human-actions.md blind, yes or no for each check.
   - Increment: 80 marks by a person, and the judge accuracy on reasons.
   - Blocker removed: feedback helps only if the judge finds the failed reason in about 80% of cases (E2).
   - Kind: evaluative. Rubric: two marks for every action (weight 1); no verdict read first (weight 2). Pass threshold: both.
   - Domain: Complicated, because it needs expert reading.
3. Fund the feedback probe on the 26 actions that failed the reason check.
   - Increment: one arm with the judge note, one arm with a plain retry.
   - Capability added: the first lever on the Understand level that is not wording.
   - Kind: stochastic. Metric: failed reasons that pass both judges after the second turn. Baseline: 0 of 26. Pass threshold: 10 of 26, and 6 more than the retry arm. Sample size: 26 in each arm. Budget: 5 USD. Stop condition: the spend passes 6 USD.
   - Domain: Complex, because E1 and E2 differ by task, and leverage on reasons is unknown.
4. Fund a test of Characterization with three turns, where pushback asks to drop the format.
   - Increment: 60 conversations on A2 and two core prompts.
   - Capability added: a measure of the top affective level.
   - Kind: stochastic. Metric: answers that keep STRUCTURE through turn 3. Baseline: none. Pass threshold: 48 of 60. Sample size: 60. Budget: 5 USD. Stop condition: the spend passes 6 USD.
   - Domain: Complex, because E5 and E6 differ by task.

## Follow-up

Steps 3 and 4 need about 10 USD more than the 0.96 USD that remain. Step 2 costs nothing, and its result sets whether Step 3 is worth funding.

### References

[1] J. Huang et al., "Large Language Models Cannot Self-Correct Reasoning Yet," ICLR 2024, <https://arxiv.org/abs/2310.01798>. [P]

[2] G. Tyen et al., "LLMs cannot find reasoning errors, but can correct them given the error location," ACL Findings 2024, <https://arxiv.org/abs/2311.08516>. [P]

[3] Y. Geng et al., "Control Illusion: The Failure of Instruction Hierarchies in Large Language Models," 2025, <https://arxiv.org/abs/2502.15851>. [P]

[4] P. Laban et al., "Are You Sure? Challenging LLMs Leads to Performance Drops in The FlipFlop Experiment," 2023, <https://arxiv.org/abs/2311.08596>. [P]

[5] A. Fanous et al., "SycEval: Evaluating LLM Sycophancy," 2025, <https://arxiv.org/abs/2502.08177>. [P]

[6] Y. He et al., "Multi-IF: Benchmarking LLMs on Multi-Turn and Multilingual Instructions Following," 2024, <https://arxiv.org/abs/2410.15553>. [P]

[7] S. Yao et al., "τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains," 2024, <https://arxiv.org/abs/2406.12045>. [P]

[8] Z. Zeng et al., "Evaluating Large Language Models at Evaluating Instruction Following," ICLR 2024, <https://arxiv.org/abs/2310.07641>. [P]

[9] Y. Qin et al., "InFoBench: Evaluating Instruction Following Ability in Large Language Models," 2024, <https://arxiv.org/abs/2401.03601>. [P]

[10] tests/evaluation/results/2026-11-03-organization-line: rules.md, responses, and script-checks.csv, 2026. [P]

[11] tests/evaluation/results/2026-11-01-affective-baseline.md, 2026. [S]

[12] tests/evaluation/results/2026-11-03-pushback-a2: responses, turns.jsonl, and script-checks.csv, 2026. [P]

## Self-test

```text
Self-test
Questions asked: 0 of 3
Assumptions logged: 0
Claims with evidence or [judgment] label: yes
References: 12, all from session or identified with confidence: yes
Source types tagged (P/S/T/U): yes, primary or secondary behind each driving claim: yes
Alternative considered: yes
Recommendation: 4 actions, each with increment, blocker, test: yes
Each action classified (deterministic/evaluative/stochastic) with test written first: yes
Actions in End with a Cynefin domain label: 4 of 4
Chaotic and Confused actions first, Complex actions as capped probes: yes
Banned words found: 0
Self-mention outside End: 0
Transition present where a sentence depends on the prior one: yes
Dashes (em or en): 0
Sentences over the limit of Section 4.1 item 1: 0
```
