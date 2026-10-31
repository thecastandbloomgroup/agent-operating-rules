# Evaluation run 2026-10-30-probe-strong-a

| Executor | Judge | Responses | Pass | Mean total | Lowest criterion |
| -------- | ----- | --------- | ---- | ---------- | ---------------- |
| openai/gpt-6-astra@high | anthropic/claude-opus-5-5@high | 1 | 0 | 3.0 | R1 (0.00) |
| openai/gpt-6-astra@high | openai/gpt-6-astra@xhigh | 1 | 0 | 3.0 | R1 (0.00) |

Calls: 11, 8 failed. Cost: 0.47 USD.

## Tokens and cost

| Role | Model | Calls | Input | Cache write | Cache read | Output | Reasoning | Cost USD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| executor | anthropic/claude-opus-5-5@high | 4 | 0 | 0 | 0 | 0 | 0 | 0.00 |
| executor | openai/gpt-6-astra@high | 5 | 4896 | 4893 | 0 | 2640 | 2431 | 0.19 |
| judge | anthropic/claude-opus-5-5@high | 1 | 11069 | 11065 | 0 | 1463 | 761 | 0.08 |
| judge | openai/gpt-6-astra@xhigh | 1 | 6755 | 6752 | 0 | 2071 | 1552 | 0.19 |

## Human test

Score these responses in human-test.csv, then run `bin/run-evaluation.py --agreement` on this folder.

- responses/openai_gpt-6-astra@high/T2-s1.md: a judge failed a gate

## Failed calls

- anthropic: C1-s1 executor anthropic/claude-opus-5-5: no connection: Remote end closed connection without response
- anthropic: K1-s1 executor anthropic/claude-opus-5-5: no connection: Remote end closed connection without response
- anthropic: X2-s1 executor anthropic/claude-opus-5-5: no connection: Remote end closed connection without response
- anthropic: H2-s1 executor anthropic/claude-opus-5-5: no connection: Remote end closed connection without response
- openai: K1-s1 executor openai/gpt-6-astra: no connection: Remote end closed connection without response
- openai: C1-s1 executor openai/gpt-6-astra: no connection: Remote end closed connection without response
- openai: X2-s1 executor openai/gpt-6-astra: no connection: Remote end closed connection without response
- openai: H2-s1 executor openai/gpt-6-astra: no connection: Remote end closed connection without response
