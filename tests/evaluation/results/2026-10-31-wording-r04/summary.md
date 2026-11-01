# Evaluation run 2026-10-31-wording-r04

| Executor | Judge | Responses | Pass | Mean total | Lowest criterion |
| -------- | ----- | --------- | ---- | ---------- | ---------------- |

Calls: 234, 0 failed. Cost: 7.23 USD.

## Tokens and cost

| Role | Model | Calls | Input | Cache write | Cache read | Output | Reasoning | Cost USD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| executor | anthropic/claude-sonnet-5-5@medium | 39 | 301341 | 45280 | 255905 | 149074 | 68182 | 1.63 |
| executor | google/gemini-3.8-flash@medium | 39 | 215127 | 0 | 10171 | 117880 | 64892 | 0.60 |
| executor | openai/gpt-6.1-sol@medium | 39 | 202638 | 202521 | 0 | 63525 | 18513 | 1.14 |
| executor | perplexity/glm-5.3-flash@medium | 39 | 203277 | 0 | 153472 | 177129 | 118900 | 0.10 |
| executor | perplexity/kimi-k3@low | 39 | 206249 | 0 | 121408 | 68321 | 14903 | 1.32 |
| executor | xai/grok-4.7@low | 39 | 250509 | 0 | 155392 | 362613 | 311573 | 2.44 |

## Human test

Score these responses in human-test.csv, then run `bin/run-evaluation.py --agreement` on this folder.

- none
