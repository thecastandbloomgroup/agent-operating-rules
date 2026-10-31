# Evaluation run 2026-10-30-probe-strong-b

| Executor | Judge | Responses | Pass | Mean total | Lowest criterion |
| -------- | ----- | --------- | ---- | ---------- | ---------------- |
| anthropic/claude-opus-5-5@high | anthropic/claude-opus-5-5@xhigh | 5 | 1 | 13.6 | R1 (1.20) |
| anthropic/claude-opus-5-5@high | openai/gpt-6-astra@high | 5 | 1 | 12.8 | R9 (1.00) |
| openai/gpt-6-astra@high | anthropic/claude-opus-5-5@high | 5 | 2 | 11.4 | R2 (1.00) |
| openai/gpt-6-astra@high | openai/gpt-6-astra@xhigh | 5 | 2 | 11.4 | R2 (1.00) |

Calls: 30, 0 failed. Cost: 7.48 USD.

## Tokens and cost

| Role | Model | Calls | Input | Cache write | Cache read | Output | Reasoning | Cost USD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| executor | anthropic/claude-opus-5-5@high | 5 | 40310 | 4190 | 36100 | 87801 | 68654 | 1.78 |
| executor | openai/gpt-6-astra@high | 5 | 27105 | 11056 | 16034 | 27745 | 21028 | 1.54 |
| judge | anthropic/claude-opus-5-5@high | 5 | 69327 | 69307 | 0 | 10646 | 6123 | 0.56 |
| judge | anthropic/claude-opus-5-5@xhigh | 5 | 78482 | 78462 | 0 | 34683 | 27921 | 1.09 |
| judge | openai/gpt-6-astra@high | 5 | 49266 | 37295 | 11956 | 17320 | 13982 | 1.34 |
| judge | openai/gpt-6-astra@xhigh | 5 | 42767 | 24818 | 17934 | 16707 | 13829 | 1.16 |

## Human test

Score these responses in human-test.csv, then run `bin/run-evaluation.py --agreement` on this folder.

- responses/anthropic_claude-opus-5-5@high/H2-s1.md: a judge failed a gate
- responses/anthropic_claude-opus-5-5@high/K1-s1.md: random sample
- responses/anthropic_claude-opus-5-5@high/T2-s1.md: random sample
- responses/anthropic_claude-opus-5-5@high/X2-s1.md: a judge failed a gate
- responses/openai_gpt-6-astra@high/T2-s1.md: a judge failed a gate
- responses/openai_gpt-6-astra@high/X2-s1.md: a judge failed a gate
