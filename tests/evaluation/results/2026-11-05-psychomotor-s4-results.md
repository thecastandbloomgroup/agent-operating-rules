# The psychomotor ladder at four samples: results of one run

## Headline

Set is the level that splits the models: the pooled ladder reaches 80% on Perception and Mechanism, and Set stays at 71%.

1. Perception, Guided response, and Mechanism passed 24 of 24 each, at the pass bar of 80% of at least 20 trials.
2. Set passed 17 of 24. Every failure is a write with no look first: a wrong path, a loop that hit the step cap, or no write at all.
3. The levels are not cumulative, because Set sits under both of its neighbors. So the pooled score is the mean of the levels, 0.93.
4. The run cost 3.42 USD for 478 calls, and the cache served 54% of the input tokens, the first cache measurement.

## Background

The first psychomotor run had one sample and 6 trials per level, too few for a pass call. This run raised the samples to four, so each level has 24 pooled trials. The P1 check was fixed after the first run, and this run tests it blind.

## Relevance

Set is the precondition level: look before you act. Its failures are blind writes, the behavior that damages a real project. So the level works as a measure, and the models that fail it are now named.

## Information

This section gives the run, the levels, the failures, and the tokens.

### The run

E1. Rules 0.8 went to the six main executors with prompts P1 to P4, four samples each, 96 units.
[1]

E2. All six providers ran the tool loop again. Two Gemini units hit the 12-step cap on P2 and gave no answer, the only failed calls.
[1]

### The levels

E3. The table gives each level, pooled over the six executors.
[1]

| Level | Passed | Passed at 80% of 20 or more |
| --- | --- | --- |
| Perception (P1) | 24 of 24 | yes |
| Set (P2) | 17 of 24 | no, 71% |
| Guided response (P3) | 24 of 24 | yes |
| Mechanism (P4) | 24 of 24 | yes |

E4. The blind P1 result confirms the fixed check: 24 of 24, after 6 of 6 on the post-hoc fix.
[1]
[2]

E5. Sonnet, GLM 5.3 Flash, and GPT-6.1 Sol passed every unit, 16 of 16 each. However, 4 trials per level per model stay under the 20 that a per-model pass call needs.
[1]

### The failures

E6. All 7 Set failures are one behavior. Gemini wrote plan.md to a wrong path twice and looped to the step cap twice. Grok wrote to a wrong path twice, and Kimi made no write once.
[1]

E7. One Guided response unit first failed on a violation: a write_file call with an empty path. An empty path names no file, so the checker now counts it as an error, and the unit passes on its other checks.
[1]

### The tokens

E8. The run sent 2,931,985 input tokens, and the cache served 1,571,423 of them, 54%. The output was 131,289 tokens, of which 34,697 were reasoning tokens.
[1]

E9. The cost was 3.42 USD against the estimate of 9.96. So the estimate stays about three times the bill, as in the first run.
[1]
[2]

## Limits

- Four trials per level per model cannot give a per-model pass call. The pass call here is pooled over the six executors.
- The Set prompt names no folder, by design. A reader can call a root-level plan.md a fair answer. However, the fixture holds one plan.md, and the check follows the tests page.
- The levels above Mechanism are still unmeasured.

### References

[1] tests/evaluation/results/2026-11-05-psychomotor-s4: run.json, responses, transcripts, calls.csv, run.log, and tool-checks.csv, 2026. [P]

[2] tests/evaluation/results/2026-11-05-psychomotor-probe-results.md, 2026. [P]

## Self-test

```text
Self-test
Questions asked: 0 of 3
Assumptions logged: 0
Claims with evidence or [judgment] label: yes
References: 2, all from session or identified with confidence: yes
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
