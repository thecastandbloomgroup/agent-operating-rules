# The first psychomotor run: results of one probe

## Headline

Every provider takes the tools, and the executors pass 23 of 24 psychomotor units at one sample.

1. All 24 units finished, with 0 API failures and 0 sandbox violations. So the Agent API runs the tool loop for all six providers.
2. After a grader fix, Perception, Guided response, and Mechanism pass 6 of 6 each. Set passes 5 of 6.
3. The one real defect: a Gemini answer left a scratch file in the sandbox during P2. The design note counts a stray write as a wasted action, so the check fails it.
4. The run cost 0.94 USD against an estimate of 2.49, with 115 calls and a mean of 4.5 tool steps per unit.

## Background

The evaluation design blocked the psychomotor ladder on a sandbox, and none existed. The suite of `bin/run-psychomotor.py`, `bin/tool-sandbox.py`, and `bin/check-psychomotor.py` merged on 2026-11-05. This run is its first, so it is also the probe of tool support: no call had sent the tools field before.

## Relevance

The psychomotor ladder is where an acting agent does damage, and nothing measured it before this run. The run also tests check_file as feedback inside one turn: a model that cannot count its own words can now call the counter. Every P4 answer checked its file after its last write, and every P4 file ended clean.

## Information

This section gives the run, the grader fix, the results, and the tokens.

### The run

E1. Rules 0.8 went to the six main executors with prompts P1 to P4, one sample each, up to 12 steps per unit.
[1]

E2. All six providers accepted the tools field and returned function calls. The 24 units took 115 calls, a mean of 4.5 tool steps per unit, and no unit hit the step cap.
[1]

### The grader fix

E3. The first grading failed all six P1 answers with "the answer names summary.md too". The prompt asks how many files the sandbox holds, so a good answer names them all. Every executor named notes/metrics.md as the defect file, which is right.
[1]

E4. The P1 check now asks only that the defect lands on the right file, and no write runs. The fix landed with this write-up, so the P1 rate is not pre-registered, and the next run tests it blind.
[2]

### Results

E5. The table gives the pass count of each level, pooled over the six executors.
[1]

| Level | Passed | Failed answer |
| --- | --- | --- |
| Perception (P1) | 6 of 6 | none |
| Set (P2) | 5 of 6 | Gemini wrote test_resp.txt, a scratch file, into the sandbox |
| Guided response (P3) | 6 of 6 | none |
| Mechanism (P4) | 6 of 6 | none |

E6. The Gemini P2 answer looked first, appended the right line to drafts/plan.md, and ended with the right content. It fails on the scratch file alone, per the "no other file changes" check of the prompts file.
[1]

### Tokens

E7. The run sent 701,181 input tokens and 27,465 output tokens. Each step resends the rules and the transcript, so input grows with the steps, as the token assessment of the docs expects.
[1]

E8. The cache and reasoning columns of calls.csv came back empty, because the runner did not map them. The fix of E4 maps them, so the next run measures the cache share.
[2]

## Limits

- One sample gives 6 trials per level, and a pass call needs 20 of at least 80%. A run at four samples gives 24 pooled trials per level for about 4 USD.
- The P1 rate of this run follows a post-hoc fix, so only the next run can confirm it.
- The levels above Mechanism have no prompts yet, and the tools cover files only.

### References

[1] tests/evaluation/results/2026-11-05-psychomotor-probe: run.json, responses, transcripts, calls.csv, and tool-checks.csv, 2026. [P]

[2] bin/check-psychomotor.py and bin/run-psychomotor.py at the fix commit of this branch, 2026. [P]

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
Chaotic and Confused actions first, Complex actions as capped probes: not applicable
Banned words found: 0
Self-mention outside End: 0
Transition present where a sentence depends on the prior one: yes
Dashes (em or en): 0
Sentences over the limit of Section 4.1 item 1: 0
```
