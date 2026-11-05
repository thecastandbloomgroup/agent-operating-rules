# A named second turn repairs dropped structure: results of one probe

## Headline

A second turn that names the broken parts repairs 10 of 12 answers, so the repair step passes every mark.

1. The structure turn repaired 10 of 12 broken answers. The mark asked for 9.
2. The retry control repaired 3 of 12, so the named turn beats it by 7. The mark asked for 3.
3. The guard held with room: labels with a reason rose from 5 to 10 of 12, against 8 under retry.
4. The two arms cost 0.55 USD with no failed call, and the rules text does not change.

## Background

Both wording arms had scored 12 of 18 on A3, so position and wording were exhausted for Organization. The plan pre-registered this probe. A turn that names each broken part, and a plain retry as its control, went to the same 12 broken answers of the sequence run.

## Relevance

Organization now has a working repair: the harness checks the structure, names the broken parts, and one more turn fixes most answers. So the level is reachable through feedback, not through more rule text.

## Information

This section gives the run, the marks, and the misses.

### The run

E1. The 12 broken answers of the sequence run went back to their executors twice: once with the structure message, once with the plain retry. All 24 calls answered.
[1]

E2. The arms cost 0.28 and 0.27 USD, against the plan's estimate of about 1.5 USD.
[1]
[2]

### The marks

E3. The table gives each pre-registered mark and its result.
[1]
[2]

| Mark | Result | Pass |
| --- | --- | --- |
| The structure turn repairs 9 or more of 12 | 10 of 12 | yes |
| It beats the retry control by 3 or more | 10 against 3 | yes |
| Guard: labels with a reason do not fall | 5 of 12 before, 10 of 12 after | yes |

E4. The result repeats the pilot pattern: feedback lifts an answer when it names the failed part, and a plain retry lifts far less.
[3]

### The misses

E5. Both misses are Kimi K3 on A3. Its second answers are short prose with no actions and no structure, although the message named the broken parts. So one model ignores named feedback on this prompt, and the other two repaired every answer.
[1]

## Limits

- Twelve answers from three models give a direction, not a rate per model.
- The repair uses a second turn, so it costs one more call per broken answer. The harness pays it only when the script finds a break.
- The arms reuse the first answers of one run, so a fresh run can move the base.

### References

[1] tests/evaluation/results/2026-11-05-structure-repair and 2026-11-05-structure-retry: run.json, responses, turns.jsonl, and script-checks.csv, 2026. [P]

[2] tests/evaluation/results/2026-11-05-organization-second-turn-plan.md, 2026. [P]

[3] tests/evaluation/results/2026-11-03-second-turn-results.md, 2026. [P]

## Self-test

```text
Self-test
Questions asked: 0 of 3
Assumptions logged: 0
Claims with evidence or [judgment] label: yes
References: 3, all from session or identified with confidence: yes
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
