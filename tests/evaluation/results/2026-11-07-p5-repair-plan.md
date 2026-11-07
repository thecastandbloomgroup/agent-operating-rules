# A plan: the named second turn on the P5 failures of the 20-trial runs

## Headline

A second turn that names the missing check targets 27 failed units of P5, the one psychomotor level under 80% in the pool.

1. P5 passed 90 of 120 units, and 27 of the 30 failures ran no check after the last write.
2. GPT-6.1 Sol has 17 of those units, GLM 5.3 Flash 7, and Kimi K3 3.
3. On 2026-11-05, the named turn repaired 5 of 5 such units, against 1 of 5 for a plain retry. This probe tests it at five times that size.

## Background

The [20-trial results](2026-11-07-psychomotor-20-results.md) found the failures, and the [P5 repair results](2026-11-05-p5-repair-results.md) found the repair. `bin/repair-psychomotor.py` starts each unit from the end state of its sandbox. In the named mode, it says that no check_file call ran after the last write. In the retry mode, it asks only for a check, as the control.

## Design

1. Run `bin/repair-psychomotor.py` in both modes on the four run folders that hold the 27 units: `2026-11-06-psychomotor-p1-p7`, `2026-11-06-limits-glm`, `2026-11-06-psy20-gpt`, and `2026-11-06-psy20-kimi`.
2. Grade each new run with `bin/check-psychomotor.py`, on the first steps and the new steps as one history.

## Metrics and pass marks

1. **Repair.** The named turn repairs 22 or more of 27 units, which is 80%.
2. **Lift.** The named turn repairs 8 or more units more than the retry.
3. **Per model.** The named turn repairs at least 80% of the GPT-6.1 Sol units, 14 or more of 17.
4. **Cost.** Both arms cost under 3 USD.

The probe passes when marks 1 to 3 pass.

## Cost and stop rule

54 short turns of up to 6 steps cost about 1.5 USD, from the 0.44 USD of the 10 turns of 2026-11-05. One round, then the write-up.
