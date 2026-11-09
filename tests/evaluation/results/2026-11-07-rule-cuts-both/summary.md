# Evaluation run 2026-11-07-rule-cuts-both

| Executor | Judge | Responses | Pass | Mean total | Lowest criterion |
| -------- | ----- | --------- | ---- | ---------- | ---------------- |

Calls: 126, 0 failed. Cost: 3.73 USD.

## Tokens and cost

| Role | Model | Calls | Input | Cache write | Cache read | Output | Reasoning | Cost USD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| executor | anthropic/claude-sonnet-5-5@medium | 21 | 122523 | 23758 | 98681 | 72532 | 30452 | 0.79 |
| executor | google/gemini-3.8-flash@medium | 21 | 86409 | 0 | 2072 | 192463 | 167661 | 0.79 |
| executor | openai/gpt-6.1-sol@medium | 21 | 83265 | 83202 | 0 | 32290 | 10995 | 0.53 |
| executor | perplexity/glm-5.3-flash@medium | 21 | 83265 | 0 | 52224 | 71230 | 46134 | 0.04 |
| executor | perplexity/kimi-k3@low | 21 | 84976 | 0 | 53888 | 48692 | 4650 | 0.84 |
| executor | xai/grok-4.7@low | 21 | 106119 | 0 | 73472 | 106532 | 85914 | 0.74 |

## Human test

Score these responses in human-test.csv, then run `bin/run-evaluation.py --agreement` on this folder.

- none
