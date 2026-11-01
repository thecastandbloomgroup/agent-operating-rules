# Evaluation run 2026-11-01-reason-examples

| Executor | Judge | Responses | Pass | Mean total | Lowest criterion |
| -------- | ----- | --------- | ---- | ---------- | ---------------- |

Calls: 234, 0 failed. Cost: 7.80 USD.

## Tokens and cost

| Role | Model | Calls | Input | Cache write | Cache read | Output | Reasoning | Cost USD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| executor | anthropic/claude-sonnet-5-5@medium | 39 | 310662 | 56941 | 253565 | 162817 | 78444 | 1.80 |
| executor | google/gemini-3.8-flash@medium | 39 | 222108 | 0 | 16286 | 271784 | 217490 | 1.17 |
| executor | openai/gpt-6.1-sol@medium | 39 | 209580 | 209463 | 0 | 70924 | 23979 | 1.23 |
| executor | perplexity/glm-5.3-flash@medium | 39 | 210219 | 0 | 98304 | 179157 | 117259 | 0.11 |
| executor | perplexity/kimi-k3@low | 39 | 213156 | 0 | 138240 | 63318 | 14582 | 1.22 |
| executor | xai/grok-4.7@low | 39 | 257607 | 0 | 142208 | 328491 | 277993 | 2.27 |

## Human test

Score these responses in human-test.csv, then run `bin/run-evaluation.py --agreement` on this folder.

- none
