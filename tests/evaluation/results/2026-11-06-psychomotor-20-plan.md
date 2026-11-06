# A plan: 20 psychomotor trials per level for the other four models

## Headline

Sixteen more samples of P1 to P7 for the other four models give all six models a per-model psychomotor score.

1. Sonnet 5.5 and GLM 5.3 Flash have 20 trials per level, and score 1.00 and 0.89 ([limits results](2026-11-06-limits-results.md)).
2. The other four models have 4 trials per level, under the 20 that a mastery call needs.
3. The user chose to fund this run on 2026-11-06, above the 3.75 USD left of the earlier budget.

## Background

The first 4 samples of each model come from the [P1 to P7 run](2026-11-06-psychomotor-p1-p7-results.md) of the same day. The runs use rules 0.9, the four file tools, and no note, as the earlier runs did. So the Gemini loop at the step cap counts as a failure, and the write-up reports it apart.

## Design

1. Run `bin/run-psychomotor.py` with P1 to P7 and 16 samples for Gemini 3.8 Flash, GPT-6.1 Sol, Kimi K3, and Grok 4.7: 448 units.
2. Rerun once each unit that fails on the network or the API.
3. Grade each run with `bin/check-psychomotor.py`, and score all six models with `bin/ladder-scores.py` over the five runs of the day.
4. Report the units at the step cap for each model.

## Metrics and pass marks

1. **Trials.** Each of the four models has 20 or more graded trials at each of the seven levels.
2. **Score.** `bin/ladder-scores.py` gives each of the six models a psychomotor score.
3. **Cost.** The four runs cost under 25 USD. The P1 to P7 run cost 0.0402, 0.0848, 0.0292, and 0.0457 USD per unit of Gemini, GPT, Kimi, and Grok, so the estimate is 22.38 USD.

## Cost and stop rule

A watchdog stops a run when its cost passes its share of the cap. The shares are 6 USD for Gemini, 12 for GPT, 4 for Kimi, and 7 for Grok. One run per model and one rerun of network failures, then the write-up.
