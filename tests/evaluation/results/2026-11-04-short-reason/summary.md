# Evaluation run 2026-11-04-short-reason

| Executor | Judge | Responses | Pass | Mean total | Lowest criterion |
| -------- | ----- | --------- | ---- | ---------- | ---------------- |

Calls: 72, 0 failed. Cost: 2.22 USD.

## Tokens and cost

| Role | Model | Calls | Input | Cache write | Cache read | Output | Reasoning | Cost USD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| executor | anthropic/claude-sonnet-5-5@medium | 12 | 89655 | 15154 | 74453 | 51340 | 25012 | 0.56 |
| executor | google/gemini-3.8-flash@medium | 12 | 63621 | 0 | 6099 | 39569 | 24680 | 0.19 |
| executor | openai/gpt-6.1-sol@medium | 12 | 60468 | 60432 | 0 | 20860 | 7535 | 0.36 |
| executor | perplexity/glm-5.3-flash@medium | 12 | 60612 | 0 | 24320 | 50792 | 32148 | 0.03 |
| executor | perplexity/kimi-k3@low | 12 | 61572 | 0 | 19712 | 14677 | 1270 | 0.35 |
| executor | xai/grok-4.7@low | 12 | 74946 | 0 | 47616 | 107142 | 92474 | 0.72 |

## Human test

Score these responses in human-test.csv, then run `bin/run-evaluation.py --agreement` on this folder.

- none
