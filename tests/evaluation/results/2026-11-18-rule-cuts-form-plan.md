# A plan: the combined rule cuts against released rules 0.10, run the same day

## Headline

One form-only run tests the combined cuts against released rules 0.10, so the person can decide on the cuts from one result.

1. The combined cuts passed every mark on 2026-11-07, against a control of that day.
2. The kit now supplies the rules, so a cut ships from the kit and needs a result the kit can read.
3. Both arms run on the same day with the same models, so a change in the models does not enter the comparison.

## Background

The [rule-cut results](2026-11-07-rule-cuts-results.md) record the four arms of 2026-11-07. The combined arm cut the share of answers with a false self-test line from 59.5% to 7.1%, and the input tokens from 5,725 to 4,496 per call. The person approved one form-only run of this comparison on 2026-11-18, through the kit session.

## Design

1. The candidate is `2026-11-18-rule-cuts-form-plan/rules-candidate.md`, a copy of `2026-11-07-rule-cuts-plan/rules-both.md`. It drops Section 1, the references list, the bracket citations, and four count lines of the self-test.
2. The control is `sources/model-operating-rules.md` at tag v0.10.0, the released rules.
3. Run each file with `bin/run-evaluation.py --no-judge --prompts A1,A2,A3,X1,X2,H2,T2 --samples 3`: 126 answers per arm, from six models.
4. Score both arms with `bin/script-checks.py`, and write `2026-11-18-rule-cuts-form-result.json` with pass or fail and a 95% interval per mark.

## Metrics and pass marks

The marks are also in `2026-11-18-rule-cuts-form-plan/plan.json`. The candidate passes when all four marks hold:

1. **False lines.** The share of answers with a false self-test line falls by 20 points or more against the control.
2. **Checks.** Each of these checks stays within 10 points of the control: no long sentence, no banned word, no dash, no first person outside End, structure, labels on every action, and reasons on every action.
3. **Tokens.** The mean input tokens per call fall by 10% or more against the control.
4. **Cost.** The two arms cost under 10 USD together.

## Limits

The run has no judge, so it does not measure the quality of judgment. A pass means only that no script check falls and the two costs fall.

## Cost and stop rule

One arm cost from 3.35 to 3.92 USD on 2026-11-07, so two arms cost about 8 USD. One run per arm, then the write-up. A judged run needs the person's approval first. A pass changes no file in `sources/`, because the cut ships from the kit if the person approves it.
