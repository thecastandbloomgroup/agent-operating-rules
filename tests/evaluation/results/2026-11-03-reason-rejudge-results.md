# Reasons judged on their own: blind marks and a rejudge

## Headline

The low rate of reasons came mostly from the judges. Judged on its own, a reason states cause and effect in 33 of 40 actions, not 11.

1. Blind marks by a person on 10 actions agreed with the old judges on 3 and 2 of 7 clear marks.
2. The old judges failed a reason when its domain was wrong.
3. The new instruction judges the reason alone, and counts the effort that it takes to know the effect. Both judges then agreed with the person on 6 of 7.
4. So Understand is at 82% of 40 trials, and Evaluate, at 38%, is now the lowest measured cognitive level.

## Background

The feedback probe and the Rank 2 probe both aimed at reasons, the lowest level at 35%. A person marked reasons blind for the first time, to check the judges first.

## Relevance

A judge that fails good reasons sends funds to the wrong level. Two probes for reasons would have cost about 11 USD.

## Information

This section gives the marks, the change, and the rejudge.

### The blind marks

E1. The person marked 10 actions of rules 0.6, yes or no on the reason only, with no verdict in view. Eight of the 10 were actions where the three model graders disagreed.
[1]

| Grader | Agrees with the 7 clear marks |
| --- | --- |
| Astra or Opus, old instruction | 3 |
| Argon, old instruction | 2 |
| Fable, blind marks | 5 |

E2. The person passed 6 of the 7 reasons. The old judges failed 3 that the person passed. Two marks were "maybe", because the reason does not ask whether a special cause could throw off the estimate. One mark was a note on the method of the action.
[1]

E3. The notes of the old judges named a wrong domain, then failed the reason as "only describes the task". So the domain check leaked into the reason check.
[2]

### The change

E4. The person ruled that a reason can be right when the domain is wrong. The effort that it takes to get there implies the domain. So the judge instruction gained two sentences:

```text
A reason that says what effort it takes to know the effect (a known practice,
analysis or expertise, a trial, or acting first) states it. Judge the reason on its
own: a wrong domain does not make it fail.
```

### The rejudge

E5. Both judges checked the same 40 actions again, at a cost of 1.21 USD.
[2]

| Measure | Old instruction | New instruction |
| --- | --- | --- |
| Reason, first judge | 14 | 36 |
| Reason, Argon | 15 | 35 |
| Reason, both judges | 11 | 33 |
| Domain, first judge | 27 | 27 |
| Domain, Argon | 29 | 28 |
| Agrees with the person, each judge | 3 and 2 of 7 | 6 and 6 of 7 |

The domain verdicts did not move, so the change reached only the reason check. The judges agree on 98% of domains (kappa 0.94) and 88% of reasons (kappa 0.38). The kappa of reasons is low because 33 of 40 are yes.

E6. On the run of rules 0.6, bin/ladder-scores.py now gives these rates, pooled over the six executors:
[2]

| Level | Rate |
| --- | --- |
| Understand | 82% of 40 |
| Analyze | 68% of 40 |
| Apply | 62% of 468 |
| Evaluate | 38% of 234 |

The pooled cognitive score rises from 0.49 to 0.62, still as a mean, because the rates do not fall in order up the ladder.

### Limits

- Seven clear marks by one person can show a direction, not a rate. Eight of the 10 actions came from disagreements, so they are the hard cases.
- The new check passes 82% of reasons, so it can no longer show much gain. The "maybe" marks point to a stricter test for later: whether the reason names what could break the link.
- The action checks of other runs still use the old instruction.

### Alternative considered

Keep the old instruction, since it is stricter. It loses because it failed reasons that the person passed, and it mixed the domain into the reason.

## End

I recommend that we point the next probes at Evaluate, and drop the probes for reasons.

1. Finish the Rank 1 probe, the self-test from a separate check of each item.
   - Increment: the run of 108 answers in progress, scored by the script.
   - Capability added: a first lever on Evaluate, now the lowest level (E6).
   - Kind: stochastic. Metric: answers whose self-test counts are right. Baseline: 43 of 108 on the same prompts. Pass threshold: 58 of 108. Sample size: 108 answers. Budget: 4 USD. Stop condition: the spend passes 5 USD.
   - Domain: Complex, because no change has touched this level yet.
2. Drop the feedback probe and the Rank 2 probe.
   - Increment: one line in the Follow-up of this write-up.
   - Blocker removed: both probes aimed at a rate that was mostly a judge defect (E5).
   - Kind: deterministic. Test:
     - Given this write-up
     - When a later plan names a probe for reasons
     - Then it cites a measure stricter than E4
   - Domain: Clear, because the rejudge settled the rate.
3. Write a stricter reason check, one that asks what could break the link.
   - Increment: one question for the judge, and 10 more marks by the person.
   - Capability added: room above 82% for the Understand level.
   - Kind: evaluative. Rubric: the person agrees with each judge on 8 of 10 (weight 2); the check asks one thing (weight 1). Pass threshold: both.
   - Domain: Complicated, because the person's "maybe" marks set the criterion, and it needs expert reading.

## Follow-up

Step 2 drops the feedback probe and the Rank 2 probe. If Step 3 finds a stricter check that passes fewer than half of reasons, then those probes return.

### References

[1] tests/evaluation/results/2026-11-01-gherkin-lines/human-reasons-10.md, blind marks by the user, 2026. [P]

[2] tests/evaluation/results/2026-11-01-gherkin-lines: action-checks.csv and action-checks-argon.csv under the new instruction, and the files that end in -reason1 under the old one, 2026. [P]

## Self-test

```text
Self-test
Questions asked: 0 of 3
Assumptions logged: 0
Claims with evidence or [judgment] label: yes
References: 2, all from session or identified with confidence: yes
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
