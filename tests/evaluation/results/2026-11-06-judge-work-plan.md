# A plan: a rate of fit to the work for the 120 actions behind the domain rate

## Headline

A rejudge of the 120 actions with no expected answer gives a rate of fit to the work. It sits next to the rate of fit to the test.

1. The evaluations page gives one domain rate, about 60% to 65%, from 120 judged actions of three runs. In those runs, 80 of 120 actions passed.
2. The [reruns](2026-11-06-judge-reruns-results.md) found that the expected answer pulls both judges away from the user, in each of 12 runs. So that rate measures fit to the test.
3. This rejudge measures fit to the work with the judge setup closest to the user. It measures fit to the test again with today's instruction, as the control.

## Background

The three runs are `2026-11-01-reason-examples`, `2026-11-03-cynefin-questions`, and `2026-11-01-split-first-c`. Their judges ran with an older instruction than today's. So the control rejudges the same actions with today's built-in instruction, and the two rates come from the same day and the same judges.

## Design

1. Work arm: `bin/judge-actions.py RUN --actions RUN/action-checks.csv --work 2026-11-05-human-marking --out action-checks-work.csv`, for each of the three runs. The judge follows the rule of another provider than the executor.
2. Test arm: the same command with no `--work`, and `--out action-checks-test.csv`. This is the control.
3. Report the share of actions with domain_right in each arm, over the 104 actions that the user did not mark. Report the 16 marked actions apart, because their marks are among the examples of the work arm.
4. Report the actions where the two arms differ, grouped by label.

## Metrics

This is a measurement, so it has no pass mark. It reports three numbers:

1. **Fit to the work**: the share of the 104 unmarked actions with domain_right in the work arm.
2. **Fit to the test**: the same share in the test arm.
3. **Gap**: the work rate minus the test rate, in points. A gap of 10 points or less means the page can keep one rate. A larger gap means the page gives both.

The cost MUST stay under 10 USD.

## Cost and stop rule

The work arm costs about 6.5 USD, at 0.054 USD for each of 120 calls. The test arm costs about 2.4 USD, at 0.02 USD per call. One round, then the write-up.
