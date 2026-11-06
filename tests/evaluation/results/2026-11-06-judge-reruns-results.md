# Removing the expected answer lifts both judges in every run: results of the reruns

## Headline

The claim holds: with no expected answer, both judges agree more with the user in every run, by more than the mark of 0.20.

1. The first judge gave a label kappa of -0.01 in all three runs with the expected answer, and 0.24, 0.18, and 0.24 without it. The mean rise is 0.23.
2. The second judge gave -0.01, -0.01, and -0.10 with the expected answer, and 0.18, 0.24, and 0.23 without it. The mean rise is 0.26.
3. For each judge, the lowest run without the expected answer is above the highest run with it.
4. The eight new runs cost 8.04 USD, under the mark of 9 USD.

## Background

The [plan](2026-11-06-judge-reruns-plan.md) fixed three marks before any call. It added two runs to each of four arms: each of the two judges, with and without the expected answer. The first run of each arm comes from the [leave-one-out results](2026-11-05-judge-loo-results.md) and the [no expected answer results](2026-11-06-judge-no-expected-results.md).

## Relevance

The expected answer of the test pulls both judges away from the user's view. So the past domain rates measure fit to the test, and a rate of fit to the work needs its own judge run.

## Information

This section gives the kappa of each run and the limits.

### The runs

| Judge  | Arm                  | Run 1 | Run 2 | Run 3 | Mean  |
| ------ | -------------------- | ----- | ----- | ----- | ----- |
| First  | With expected answer | -0.01 | -0.01 | -0.01 | -0.01 |
| First  | No expected answer   | 0.24  | 0.18  | 0.24  | 0.22  |
| Second | With expected answer | -0.01 | -0.01 | -0.10 | -0.04 |
| Second | No expected answer   | 0.18  | 0.24  | 0.23  | 0.22  |

[1]

In the third run of the second judge with no expected answer, one call failed on a dropped connection. So that run covers 23 rows.
[1]

### The marks

| Mark                                     | First judge | Second judge | Pass |
| ---------------------------------------- | ----------- | ------------ | ---- |
| Mean rise of 0.20 or more                | 0.23        | 0.26         | yes  |
| Lowest run without above highest run with | yes         | yes          | yes  |
| Cost under 9 USD                         | 5.17 USD    | 2.87 USD     | yes  |

[1]

### Limits

- **The ceiling stays low.** The runs with no expected answer stay between 0.18 and 0.24. That is under the mark of 0.40 for a judge to trust. So a rate of fit to the work is still the judges' view, not the user's.
- **One sheet and one marker.** The reruns test a claim that this sheet raised, and they tune nothing. However, the claim holds only for this marker and these 24 rows.

## End

I recommend that we:

1. Rejudge the 120 actions behind the domain rate of the evaluations page with `bin/judge-actions.py --work`, to give a rate of fit to the work.
   Increment: 120 calls with the first judge, about 6.5 USD, with its plan committed first. Blocker removed: the page has only a rate of fit to the test.
   Test (stochastic): the rate of fit to the work is reported over the unmarked actions, next to the rate of fit to the test.
   Domain: Complicated. Reason: analysis, because the method and its limits are known from these reruns.
2. Keep the built-in judge for fit to the test, because the tests define what a model should answer.
   Increment: none. Blocker removed: none new.
   Test (deterministic, Gherkin):
   Given `bin/judge-actions.py` on main
   When it runs with no `--work`
   Then each call carries the expected answer.
   Domain: Clear. Reason: deduction, because the unit test checks it.
3. Report both rates on the evaluations page, each named by what it measures.
   Increment: one paragraph. Blocker removed: a reader who takes one rate as the user's view.
   Test (evaluative): each domain rate on the page says whether it measures fit to the test or fit to the work.
   Domain: Clear. Reason: deduction, because the results files give both.
   Step 3 MUST NOT start until Step 1 has its rate.

## Follow-up

References:

[1] The rerun CSV files in `2026-11-06-judge-reruns/`, with the first runs in `2026-11-05-judge-loo/` and `2026-11-06-judge-no-expected/`, judged 2026-11-05 and 2026-11-06. [P]
