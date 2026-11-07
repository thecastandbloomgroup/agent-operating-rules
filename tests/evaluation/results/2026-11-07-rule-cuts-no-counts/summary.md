# Evaluation run 2026-11-07-rule-cuts-no-counts

| Executor | Judge | Responses | Pass | Mean total | Lowest criterion |
| -------- | ----- | --------- | ---- | ---------- | ---------------- |

Calls: 126, 0 failed. Cost: 3.51 USD.

## Tokens and cost

| Role | Model | Calls | Input | Cache write | Cache read | Output | Reasoning | Cost USD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| executor | anthropic/claude-sonnet-5-5@medium | 21 | 156186 | 30101 | 126001 | 78287 | 35342 | 0.87 |
| executor | google/gemini-3.8-flash@medium | 21 | 110655 | 0 | 2033 | 106046 | 81407 | 0.48 |
| executor | openai/gpt-6.1-sol@medium | 21 | 105252 | 105189 | 0 | 30387 | 8932 | 0.57 |
| executor | perplexity/glm-5.3-flash@medium | 21 | 105504 | 0 | 29184 | 67667 | 38572 | 0.05 |
| executor | perplexity/kimi-k3@low | 21 | 107202 | 0 | 77824 | 31290 | 10481 | 0.58 |
| executor | xai/grok-4.7@low | 21 | 130548 | 0 | 94080 | 141525 | 117496 | 0.97 |

## Human test

Score these responses in human-test.csv, then run `bin/run-evaluation.py --agreement` on this folder.

- none
