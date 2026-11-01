# Affective ladder: first baseline

## Headline

The executors keep the format when reminded and when rushed, but half of them break rules that a conflicting request did not touch.

1. Responding (A1) passes STRUCTURE in 18 of 18 answers, and Valuing (A2) in 17 of 18.
2. Organization (A3) passes in 8 of 18. All but one answer drop the headings as asked, but only 12 keep the self-test last.
3. The rates fall level by level, so the affective ladder is cumulative in this baseline [inference].

## Background

Tests 1.7 added three prompts for the affective ladder. A1 names the rules, A2 invites a short answer, and A3 asks for no headings. Each prompt is Clear, so a wrong domain does not hide the level.

## Relevance

Before this run, no item measured an affective level above Receiving. The run cost 1.67 USD, so the ladder can be measured on every change of the rules.

## Information

This section gives the run, the results, and their limits.

### The run

E1. The six main executors answered A1 to A3 three times each at rules 0.6, with no judge. `bin/script-checks.py` scored the 54 answers. No call failed.
[1]

### Results

E2. The table gives the answers that pass each check, out of 18 for each prompt.
[1]

| Check | A1, Responding | A2, Valuing | A3, Organization |
| --- | --- | --- | --- |
| STRUCTURE (A3: its own checks) | 18 | 17 | 8 |
| Self-test last | 18 | 18 | 12 |
| No first person outside End | 17 | 18 | 14 |
| Every action labelled | 13 | 15 | 8 |
| Self-test counts right | 5 | 12 | 0 |

E3. On A3, 17 of 18 answers had no heading, 13 had a paragraph that begins "I recommend that we", and 12 had the self-test last. So the models obey the request, then drop rules that the request did not touch.
[1]

E4. On A3, Gemini and Grok passed all 3 answers. GLM and Kimi passed none.
[1]

### Limits

- Each prompt has 18 answers, so one answer moves a rate by 6 points.
- STRUCTURE checks the form only. A judge checks that A3 keeps the parts of BRIEF in order, and that check has not run.
- The run tests one turn. Characterization needs a second turn of pushback.

### Alternative considered

Score A3 by STRUCTURE like the other prompts. It loses because every right answer to A3 has no heading, so STRUCTURE would fail all of them.

## End

I recommend that we add the affective rates to every script-only run, and probe the Organization level.

1. Run A1 to A3 with every script-only run of a rules change.
   - Increment: the three prompt IDs in the run command of each probe.
   - Capability added: a guard on the affective ladder at 0.03 USD for each answer.
   - Kind: deterministic. Test:
     - Given a probe run
     - When script-checks.py scores it
     - Then the table has a row for each of A1, A2, and A3
   - Domain: Clear, because the run command fixes the prompts.
2. Probe a line in Section 0 that says the rules that a request does not touch still apply.
   - Increment: one sentence in Section 0 of a rules file in a run folder, and one run of A3.
   - Capability added: a measure of whether wording reaches the Organization level.
   - Kind: stochastic. Metric: A3 answers that pass their structure checks. Baseline: 8 of 18 (E2). Pass threshold: 14 of 18. Sample size: 18 answers. Budget: 1 USD. Stop condition: the spend passes 2 USD.
   - Domain: Complex, because wording has not moved a judgment level yet, so leverage is a guess.
3. Add a second turn of pushback to the harness, for Characterization.
   - Increment: one option of run-evaluation.py that sends a second message after the answer.
   - Capability added: the first measure of the top affective level.
   - Kind: deterministic. Test:
     - Given a prompt with a second turn
     - When the run sends it
     - Then the response file holds both answers
   - Domain: Complicated, because the second turn of the Agent API needs a design choice.

## Follow-up

If Step 2 passes, the same sentence goes into the rules in the next release.

### References

[1] tests/evaluation/results/2026-11-01-affective-baseline: script-checks.csv, calls.csv, and summary.md, 2026. [P]

## Self-test

```text
Self-test
Questions asked: 0 of 3
Assumptions logged: 0
Claims with evidence or [judgment] label: yes
References: 1, all from session or identified with confidence: yes
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
