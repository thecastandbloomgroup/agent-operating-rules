# Evaluation run 2026-10-30-probe-strong-a2

| Executor | Judge | Responses | Pass | Mean total | Lowest criterion |
| -------- | ----- | --------- | ---- | ---------- | ---------------- |
| anthropic/claude-opus-5-5@high | openai/gpt-6-astra@high | 5 | 2 | 12.4 | R9 (1.00) |
| openai/gpt-6-astra@high | anthropic/claude-opus-5-5@high | 5 | 2 | 12.2 | R2 (1.00) |
| openai/gpt-6-astra@high | openai/gpt-6-astra@xhigh | 5 | 1 | 11.8 | R2 (0.80) |

Calls: 30, 5 failed. Cost: 6.57 USD.

## Tokens and cost

| Role | Model | Calls | Input | Cache write | Cache read | Output | Reasoning | Cost USD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| executor | anthropic/claude-opus-5-5@high | 5 | 40310 | 11410 | 28880 | 80149 | 61563 | 1.67 |
| executor | openai/gpt-6-astra@high | 5 | 27105 | 22234 | 4856 | 26991 | 19875 | 1.63 |
| judge | anthropic/claude-fable-5-1@high | 5 | 0 | 0 | 0 | 0 | 0 | 0.00 |
| judge | anthropic/claude-opus-5-5@high | 5 | 70068 | 70048 | 0 | 13678 | 8504 | 0.62 |
| judge | openai/gpt-6-astra@high | 5 | 49199 | 43206 | 5978 | 14856 | 11378 | 1.29 |
| judge | openai/gpt-6-astra@xhigh | 5 | 43119 | 37126 | 5978 | 17737 | 14756 | 1.36 |

## Human test

Score these responses in human-test.csv, then run `bin/run-evaluation.py --agreement` on this folder.

- responses/anthropic_claude-opus-5-5@high/H2-s1.md: a judge failed a gate
- responses/anthropic_claude-opus-5-5@high/K1-s1.md: random sample
- responses/anthropic_claude-opus-5-5@high/X2-s1.md: a judge failed a gate
- responses/openai_gpt-6-astra@high/C1-s1.md: random sample
- responses/openai_gpt-6-astra@high/T2-s1.md: a judge failed a gate
- responses/openai_gpt-6-astra@high/X2-s1.md: a judge failed a gate

## Failed calls

- anthropic: C1-s1 judge anthropic/claude-fable-5-1: failed: echolot: model refused the request: llm-api returned finish_reason=refusal
- anthropic: K1-s1 judge anthropic/claude-fable-5-1: failed: echolot: model refused the request: llm-api returned finish_reason=refusal
- anthropic: X2-s1 judge anthropic/claude-fable-5-1: failed: echolot: model refused the request: llm-api returned finish_reason=refusal
- anthropic: T2-s1 judge anthropic/claude-fable-5-1: failed: echolot: model refused the request: llm-api returned finish_reason=refusal
- anthropic: H2-s1 judge anthropic/claude-fable-5-1: failed: echolot: model refused the request: llm-api returned finish_reason=refusal
