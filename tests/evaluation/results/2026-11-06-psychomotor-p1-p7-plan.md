# A plan: one run of all seven psychomotor levels on the same day

## Headline

One run of P1 to P7 gives every psychomotor level a pass rate from the same day, rules, and tools.

1. P1 to P6 last ran together on 2026-11-05 with rules 0.8.1, and P7 ran alone on 2026-11-06.
2. P5 passed 14 of 24 on 2026-11-05 and 19 of 24 in a control of 2026-11-06. So rates from different days do not show the order of the levels.
3. The run measures; it changes nothing in the prompts, tools, or grader.

## Background

The [P7 results](2026-11-06-p7-origination-results.md) found that P7 passed as often as P5. So the ladder was not cumulative on that day. The [check text results](2026-11-06-check-text-results.md) found that P5 moves by 5 passes between days.

## Design

1. Run `bin/run-psychomotor.py` with P1 to P7, 4 samples, and the six main executors: 168 units with rules 0.9 and the four file tools.
2. Rerun once, with the same prompt and sample, each unit that fails with a network or API error, as on 2026-11-05.
3. Grade with `bin/check-psychomotor.py`, and score with `bin/ladder-scores.py`.

## Metrics and pass marks

1. **Coverage.** Each level has at least 22 of 24 units free of network and API errors after the rerun.
2. **Guard.** P1, P4, and P6 each pass 22 or more of 24, as they did on 2026-11-05.
3. **Measures to report.** The pass rate of each level, with P5 against its 14 and 19 of 24, and P7 against its 19 of 24. Also whether the pooled rates fall from level to level.
4. **Cost.** The run costs under 9 USD.

A failed guard means the day or the rules moved the ladder, and the write-up says which levels moved.

## Cost and stop rule

The run of 2026-11-05 cost 4.98 USD for 144 units with its rerun, and P7 cost 1.97 USD for 24. So 168 units cost about 7 USD. One run and one rerun of failures, then the write-up.
