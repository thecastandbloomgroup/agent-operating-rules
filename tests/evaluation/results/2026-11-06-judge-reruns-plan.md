# A plan: rerun two judge arms to test the rise from removing the expected answer

## Headline

Two more runs of each arm test whether removing the expected answer lifts the judges, or whether the rise of one run is noise.

1. With no expected answer, the judges reached a label kappa of 0.24 and 0.18 with the user. With it, both reached -0.01.
2. One rerun of an earlier arm moved by 0.12 with no change, so one run per arm cannot separate a rise of 0.19 from noise.
3. The reruns change nothing in the judge, so they add no fit to the 24 marked rows.

## Background

The [no expected answer results](2026-11-06-judge-no-expected-results.md) found the first rise above chance in four probes. The user asked how far the work can go without a new marking sheet. A rerun uses the same sheet, but it tunes nothing, so it can test a claim that this sheet already raised.

## Design

1. Run `bin/judge-loo.py` two more times in each of four arms: each of the two judges, with and without `--no-expected`. The first run of each arm comes from the [leave-one-out results](2026-11-05-judge-loo-results.md) and the no expected answer results.
2. For each arm, compute the label kappa with the user in each of its three runs.

## Metrics and pass marks

1. **Rise.** For each judge, the mean kappa with no expected answer is at least 0.20 above the mean kappa with it.
2. **Separation.** For each judge, the lowest run with no expected answer is above the highest run with it.
3. **Cost.** The eight runs cost under 9 USD.

The claim holds when both judges pass marks 1 and 2.

## Cost and stop rule

Eight runs of 24 calls cost about 8.4 USD, from the 2.18 USD and 2.01 USD of the first runs. One round, then the write-up. If the claim holds, a second plan rejudges past runs with no expected answer, to give a fit-to-the-work rate next to the fit-to-the-test rate. If it fails, the evaluations page drops the sentence on the rise.
