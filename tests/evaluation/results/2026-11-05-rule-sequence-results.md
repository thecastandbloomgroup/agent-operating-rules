# The sequence of two rules: results of one probe

## Headline

Moving two rules to the point of use did not lift the targeted levels, so the rules stay at 0.8.

1. A3 structure passed in 12 of 18 answers, under the mark of 14. The line in Section 0 had also scored 12, so the end position adds nothing.
2. The self-test lines without the word counts were right in 94 of 126 answers, 75%. The mark was 84%, so the checklist line fails too.
3. Both guards held. Answers with no long sentence were 32 of 72 against the mark of 29. Labels with a reason were 59 of 72 against 55.
4. The run cost 4.30 USD, with 126 answers and no failed call.

## Background

Rules 0.8.2 moved the precedence line of the organization pilot to the end of the file, as Section 8 item 4. The self-test lead gained one sentence: check the lines one at a time, in order. The plan set the marks before the run, and the run followed its command.

## Relevance

Position was the one untested lever of the research note. Both positions now score 12 of 18 on A3, so wording and position are exhausted for Organization. The next lever is structural: a tool that checks the structure, or a second turn that names the dropped part.

## Information

This section gives the run, the marks, and the model split.

### The run

E1. Rules 0.8.2 went to the six main executors with prompts A1, A2, A3, X1, X2, H2, and T2, three samples each, no judge.
[1]

E2. All 126 calls answered. The cost was 4.30 USD against the estimate of 4.10.
[1]

### The marks

E3. The table gives each pre-registered mark and its result.
[1]
[2]

| Mark | Result | Pass |
| --- | --- | --- |
| A3 structure, 14 or more of 18 | 12 of 18 | no |
| Self-test lines without word counts, 84% or more | 94 of 126, 75% | no |
| Guard: no long sentence on X1, X2, H2, T2, 29 or more of 72 | 32 of 72 | yes |
| Guard: every label with a reason, 55 or more of 72 | 59 of 72 | yes |

E4. The plan wrote the self-test mark as 76 of 90, but the seven prompts give 126 answers. So the mark reads as a rate: 84%. The run gives 75%, under the mark and under the 78% of the reason-form arm, so the result fails under either reading.
[2]
[3]

E5. The end position matched the Section 0 position: 12 of 18 on A3, against 8 of 18 with no line.
[4]

### The model split

E6. A3 drives on one model. GPT-6.1 Sol passed 0 of 3 on A3. Pooled over the six models, A1 passed 17 of 18 and A2 passed 18 of 18. Sonnet, Gemini, and Grok passed 3 of 3 each on A3.
[1]

E7. The language rate splits as in prior runs. GLM had 0% and Kimi 5% of answers with no long sentence, against 48% to 86% for the other four.
[1]

## Limits

- Eighteen answers per affective prompt give wide intervals, so a two-point gap from the mark is thin evidence against the line itself [judgment].
- The run reused the reason-form arm as the self-test baseline, and that arm ran on four prompts, not seven.
- No judge ran, so the domain content of the answers is unscored.

### References

[1] tests/evaluation/results/2026-11-05-rule-sequence: rules.md is in the plan folder; responses, calls.csv, scores from script-checks.csv, 2026. [P]

[2] tests/evaluation/results/2026-11-05-rule-sequence-plan.md and its folder 2026-11-05-rule-sequence-plan/rules.md, 2026. [P]

[3] tests/evaluation/results/2026-11-03-reason-form: responses and script-checks.csv, 2026. [P]

[4] tests/evaluation/results/2026-11-03-organization-line and 2026-11-01-affective-baseline: responses and script-checks.csv, 2026. [P]

## Self-test

```text
Self-test
Questions asked: 0 of 3
Assumptions logged: 0
Claims with evidence or [judgment] label: yes
References: 4, all from session or identified with confidence: yes
Source types tagged (P/S/T/U): yes, primary or secondary behind each driving claim: yes
Alternative considered: not applicable
Recommendation: 0 actions, each with increment, blocker, test: not applicable
Each action classified (deterministic/evaluative/stochastic) with test written first: not applicable
Actions in End with a Cynefin domain label: 0 of 0
Chaotic and Confused actions first, Complex actions as capped probes: yes
Banned words found: 0
Self-mention outside End: 0
Transition present where a sentence depends on the prior one: yes
Dashes (em or en): 0
Sentences over the limit of Section 4.1 item 1: 0
```
