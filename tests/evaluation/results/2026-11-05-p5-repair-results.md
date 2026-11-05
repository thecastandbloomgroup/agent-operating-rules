# A named second turn repairs the unchecked final write: results of one probe

## Headline

A second turn that names the missing check repairs 5 of 5 units, against 1 of 5 for a plain retry. So the probe passes every mark.

1. The named turn repaired all five units, over the mark of 4.
2. The retry repaired one, so the named turn beats it by 4, over the mark of 2.
3. Under the retry, GPT-6.1 Sol checked its work by reading the files back, not with check_file. Naming the tool is what the named turn adds.
4. The two arms cost 0.44 USD, with no failed call and no broken end state.

## Background

Complex overt response failed at 14 of 24 in the P1 to P6 run. Five of its ten failures were one behavior: a correct move, then an answer with no check after the last write. The plan set the marks before any run and sent two second turns to the same five units.

## Relevance

The structure probe showed that a named turn repairs a broken answer. This probe shows the same for a tool task, at the level where most models stop. So a harness that names the missing step can lift Complex overt response with one more turn, and no rule text changes.

## Information

This section gives the run, the marks, and the behavior of each arm.

### The run

E1. The five units were GPT-6.1 Sol 4 of 4 and GLM 5.3 Flash 1. Each started from the end state of its sandbox, with the prompt, its first answer, and the new message, for up to 6 more steps.
[1]
[2]

E2. The named arm cost 0.22 USD and the retry arm 0.22 USD, with 16 calls each and no failure.
[2]
[3]

### The marks

E3. The table gives each mark of the plan and its result.
[1]
[2]
[3]

| Mark | Result | Pass |
| --- | --- | --- |
| The named turn repairs 4 or more of 5 | 5 of 5 | yes |
| It beats the retry by 2 or more | 5 against 1 | yes |
| Guard: no repaired unit breaks the end state | 0 broken | yes |

### The behavior of each arm

E4. Under the named turn, every unit ran check_file on both files, then read them, then answered. The message named the tool and the gap, so the models closed that gap.
[2]

E5. Under the retry, GPT-6.1 Sol listed the files and read both back in all four units, with no check_file call. It checked by eye, which the P5 test does not count. The check tool finds banned words and long sentences that a reader can miss [inference].
[3]

E6. GLM 5.3 Flash repaired its unit under both arms, so the retry's one repair came from the model that missed the check once in four.
[2]
[3]

## Limits

- Five units from two models give a direction, not a rate.
- The named message states the exact gap. A harness can state it only because a script finds it first, so the repair needs the grader as well as the turn.
- The four Gemini units that hit the step cap and the Grok scratch file have no repair here.

### References

[1] tests/evaluation/results/2026-11-05-p5-repair-plan.md, 2026. [P]

[2] tests/evaluation/results/2026-11-05-p5-repair-named: run.json, transcripts, calls.csv, and tool-checks.csv, 2026. [P]

[3] tests/evaluation/results/2026-11-05-p5-repair-retry: the same files for the retry arm, 2026. [P]

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
