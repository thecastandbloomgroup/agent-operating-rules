# A plan: both cuts of the rules together

## Headline

Each cut passed alone, so a third arm tests both together before either goes into a release.

1. The no-counts arm cut answers with a false self-test line from 59.5% to 11.1%, and every guard held.
2. The no-thinking arm cut the input tokens by 20%, and every script check held.
3. Two cuts that pass alone can still interact, so a release needs the pair tested as one file.

## Design

1. `2026-11-07-rule-cuts-plan/rules-both.md` is the no-thinking variant with the four count lines of the self-test removed.
2. Run it as the [first plan](2026-11-07-rule-cuts-plan.md) ran each arm: 126 answers with no judge. The control of that plan, run the same day, is the baseline.

## Metrics and pass marks

1. **False lines.** The share of answers with a false self-test line falls by 20 points or more against the control.
2. **Checks.** Each script check of the first plan, except the right self-test, stays within 10 points of the control.
3. **Tokens.** The mean input tokens per call fall by 10% or more against the control.
4. **Cost.** The arm costs under 5 USD.

## Cost and stop rule

One arm of 126 answers costs about 3.50 USD. One run, then the write-up of all four arms.
