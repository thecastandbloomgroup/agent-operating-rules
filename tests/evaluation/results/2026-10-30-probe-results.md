# Result of the probe of strong executors

## Headline

Strong executors pass 35% of answers on the five hardest prompts, against 15% for the current executors. That meets the threshold of 20 points, but only just.

1. Opus 5.5 and GPT-6-Astra at high effort pass 7 of 20 answers. The current executors pass 6 of 40 on the same prompts and the same test.
2. The fixes to the test raised the current executors from 3% to 15% on these prompts, before any change of model.
3. H2 passes 0 answers for every executor, so it points to a defect in the rules or the test, not the models.
4. The account ran out of API credits during the baseline, so three of its six executors have few answers.

## Background

Step 5 of the assessment of 2026-10-30 probes Opus 5.5 and GPT-6-Astra as executors at high effort on C1, K1, H2, T2, and X2. The baseline is the six current executors on the same five prompts, with the fixed test and the same harness. Each run uses background mode, because the API dropped long calls before.

## Relevance

The result says whether a stronger model is worth its cost before more rules work. It also shows which prompt to review next.

## Information

This section covers the evidence, the assumptions, and the alternative.

### Evidence

E1. The strong executors pass 7 of 20 judgments from another provider (35%). Opus 5.5 passes 3 of 10, and GPT-6-Astra passes 4 of 10.
[1]

E2. The current executors pass 6 of 40 such judgments (15%) on the same prompts.
[1]

So the gap is 20 percentage points. A two-proportion test gives z = 1.77, which is below the 1.96 of a 5% test [inference].

E3. Before the fixes to the test, the current executors passed 2 of 79 judgments on these prompts (3%).
[2]

After the fixes, they pass 6 of 40 (15%), with z = 2.57. Most of the gain is on C1, which rose from 0 of 16 to 6 of 12. C1 now has its attached file, and the checker reads its references.
[1]

E4. H2 passes 0 of 4 strong judgments, 0 of 6 baseline judgments, and 0 of 15 judgments before the fixes.
[1]

E5. All 22 failed calls of the baseline report no API credits or an exceeded quota. They hit Moonshot, xAI, and Z.ai, which ran last. So Kimi K3 and Grok 4.7 have 2 judgments each, and GLM 5.3 Flash has 6.
[1]

E6. The probe cost 14.05 USD for the strong executors and 11.88 USD for the baseline. Claude Fable 5.1 refused every request as a judge, with the reason "refusal". So Opus 5.5 at xhigh effort replaced it in the second strong sample.
[1]

### Assumption log

A1. The judges from another provider apply the same standard to the strong executors and to the current ones. Why not measured: The user has not answered, because human-test.csv has no scores. Validate by: score 5 strong answers and 5 baseline answers by hand. If wrong: the gap in E2 changes size.

A2. The baseline without Kimi K3, Grok 4.7, and GLM 5.3 Flash is close to the full baseline. Why not measured: No tool can reach it, because the account has no credits. Validate by: run those three executors again after a top-up, for about 5 USD. If wrong: the baseline moves, and the gap moves with it.

### Alternative considered

The strongest alternative is to switch all executors to the strong models now. It loses because 20 answers give only z = 1.77. Also, H2 fails for every model, so a change to the rules or the test costs less to try first [judgment].

## End

I recommend that we confirm the gap, then fix H2, before we pay for strong executors on every run.

1. Add API credits, then run Kimi K3, Grok 4.7, and GLM 5.3 Flash again on the five prompts.
   - Blocker removed: three baseline executors have 2 to 6 judgments each (E5).
   - Kind: stochastic. Metric: the pass share from judges of another provider. Baseline: 15% (E2). Pass threshold: a complete baseline of 60 judgments. Sample size: 2 samples of 5 prompts for each executor. Budget: 6 USD.
   - Domain: Clear. Step 1 MUST start after the credit top-up.
2. Review H2 against the judge notes of all 25 failed answers, and record the decision in Section 5 of evaluation-tests.md.
   - Blocker removed: a prompt that no model passes (E4).
   - Kind: evaluative. The rubric has two criteria. First, the expected answer matches the Chaotic definition of Section 6.5 (weight 2). Next, at least one judge note names a defect that the rules ask the model to avoid (weight 1). Pass threshold: 3 of 3 points.
   - Domain: Complicated. You decide, because the test is yours.
3. Run the strong executors for a third sample, and the full baseline for a third sample.
   - Capability added: a sample large enough to test the gap in E2 at 5%.
   - Kind: stochastic. Metric: the gap in pass share. Baseline: 20 points (E2). Pass threshold: z of 1.96 or more. Sample size: 30 strong and 90 baseline judgments in total. Budget: 20 USD. Stop condition: a gap below 10 points after the strong sample.
   - Domain: Complex, so the leverage is a guess. Step 3 MUST NOT start until Step 1 ends.

## Follow-up

If A1 is false, score the answers of Step 3 by hand before a decision on the models.

### References

[1] Evaluation runs 2026-10-30-probe-strong-a2, 2026-10-30-probe-strong-b, and 2026-10-30-probe-base in tests/evaluation/results: scores.csv and calls.csv, 2026. [P]

[2] Evaluation runs 2026-10-29-tokens-s1c, 2026-10-29-rules-r2, and 2026-10-29-rules-r3 in tests/evaluation/results: scores.csv, 2026. [P]

## Self-test

```text
Self-test
Questions asked: 0 of 3
Assumptions logged: 2 (yes)
Claims with evidence or [judgment] label: yes
References: 2, all from session or identified with confidence: yes
Source types tagged (P/S/T/U): yes, primary or secondary behind each driving claim: yes
Alternative considered: yes
Recommendation: 3 actions, each with increment, blocker, test: yes
Each action classified (deterministic/evaluative/stochastic) with test written first: yes
Each action given a Cynefin domain, Chaotic and Confused first, Complex as capped probes: yes
Banned words found: 0
Self-mention outside End: 0
Transition present where a sentence depends on the prior one: yes
Dashes (em or en): 0
Longest sentence: 24 words
```
