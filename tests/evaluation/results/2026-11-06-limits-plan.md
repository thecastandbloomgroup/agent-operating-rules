# A plan: work on the limits of the evaluations page that needs no person

## Headline

Three of the six limits can move with no person: per-model psychomotor trials, the width of the intervals, and the count of second-turn studies.

1. **Pooled tool trials.** Sixteen more samples of P1 to P7 for Sonnet 5.5 and GLM 5.3 Flash give each 20 trials per level, the first per-model psychomotor scores.
2. **Small samples.** A 95% Wilson interval next to each rate that the page cites puts a number on "wide".
3. **Mostly one turn.** The page names two pilots, but four second-turn studies exist. A count and a summary fix the text.

## Background

The Limits section of [what the evaluations show](../../../docs/explanation/what-the-evaluations-show.md) names six limits. Two need a person or more budget: one human marker, and runs with mid-tier executors only. A run of all six executors to 20 trials per level costs about 25 USD, over the 6.71 USD left. The old pass rate of 8% needs only a pointer to the current scores.

## Design

1. Run `bin/run-psychomotor.py` with P1 to P7, 16 samples, for Sonnet 5.5 and for GLM 5.3 Flash: 224 units.
2. Grade each run with `bin/check-psychomotor.py`. Score Sonnet and GLM with `bin/ladder-scores.py` over this run and the [P1 to P7 run](2026-11-06-psychomotor-p1-p7-results.md), which holds their first 4 samples.
3. Compute a 95% Wilson interval for each pooled rate that the page cites.
4. Rewrite the Limits section: move the psychomotor findings to the Psychomotor section, and state each limit with its number.

## Metrics and pass marks

1. **Trials.** Each of the two models has 20 or more graded trials at each of the seven levels.
2. **Score.** `bin/ladder-scores.py` gives each of the two models a psychomotor score, not "too few trials".
3. **Cost.** The two runs cost under 5 USD. The P1 to P7 run cost 0.0296 USD per Sonnet unit and 0.0028 USD per GLM unit, so the estimate is 3.63 USD.

## Cost and stop rule

One run per model, and one rerun of units that fail on the network. Then the write-up, with no further spend.
