# A plan: two cuts of the rules, against a same-day control

## Headline

Two variants of rules 0.10 test whether a cut keeps every measured rule. One variant drops the count lines of the self-test, and one drops Section 1 and the references list.

1. The self-test count of long sentences is false in about half the answers. The models reported 0 in 105 of 107 answers, whatever the real count.
2. Section 1 and the references list cost about 700 tokens on every request, and no check grades either one.
3. A control arm with rules 0.10 runs at the same time. So each variant compares with the same day and the same models.

## Background

An assessment of the rules on 2026-11-07 found these two costs, from the [factored self-test results](2026-11-03-factored-selftest-results.md) and the size of each section. The [rule-sequence results](2026-11-05-rule-sequence-results.md) used a variant of rules 0.8.2, so they are not a baseline for rules 0.10. The variants sit in `2026-11-07-rule-cuts-plan/`:

- `rules-control.md`: rules 0.10 as they are.
- `rules-no-counts.md`: the self-test without its four count lines: banned words, self-mention, dashes, and long sentences. Every rule of Sections 4.3 and 4.4 stays.
- `rules-no-thinking.md`: no Section 1, no references list, and no bracket citations. The line of Section 0 on the order of work drops Section 1.

## Design

1. Run each of the three files with `bin/run-evaluation.py --no-judge --prompts A1,A2,A3,X1,X2,H2,T2 --samples 3`, as the rule-sequence run did: 126 answers per arm.
2. Score each arm with `bin/script-checks.py`.

## Metrics and pass marks

The no-counts variant passes when both marks hold:

1. **False lines.** The share of answers whose self-test holds a line that the script finds wrong falls by 20 points or more against the control.
2. **Guards.** Each of these checks stays within 10 points of the control: no long sentence, no banned word, no dash, no first person outside End, structure, and labels on every action.

The no-thinking variant passes when both marks hold:

1. **Checks.** Each script check stays within 10 points of the control: the six guards above, reasons on every action, and a right self-test.
2. **Tokens.** The mean input tokens per call fall by 10% or more against the control.

The three arms MUST cost under 15 USD.

## Limits

The run has no judge, so it does not measure the quality of judgment. A pass of the no-thinking variant means only that no script check falls.

## Cost and stop rule

The rule-sequence run cost 4.30 USD for 126 answers, so three arms cost about 13 USD. One run per arm, then the write-up. A pass changes the rules only in a later release, with the user's agreement.
