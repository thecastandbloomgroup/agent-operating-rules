# Evaluation run 2026-11-03-base-07

| Executor | Judge | Responses | Pass | Mean total | Lowest criterion |
| -------- | ----- | --------- | ---- | ---------- | ---------------- |

Calls: 162, 1 failed. Cost: 6.51 USD.

## Tokens and cost

| Role | Model | Calls | Input | Cache write | Cache read | Output | Reasoning | Cost USD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| executor | anthropic/claude-sonnet-5-5@medium | 27 | 211500 | 30682 | 180710 | 123896 | 61701 | 1.33 |
| executor | google/gemini-3.8-flash@medium | 27 | 151563 | 0 | 14245 | 143871 | 105099 | 0.64 |
| executor | openai/gpt-6.1-sol@medium | 27 | 142524 | 142443 | 0 | 49824 | 15059 | 0.85 |
| executor | perplexity/glm-5.3-flash@medium | 27 | 142950 | 0 | 66560 | 128938 | 85418 | 0.08 |
| executor | perplexity/kimi-k3@low | 27 | 139884 | 0 | 85696 | 123622 | 4260 | 2.04 |
| executor | xai/grok-4.7@low | 27 | 175860 | 0 | 100992 | 225382 | 188636 | 1.55 |

## Human test

Score these responses in human-test.csv, then run `bin/run-evaluation.py --agreement` on this folder.

- none

## Failed calls

- moonshot: X2-s2 executor perplexity/kimi-k3: failed: upstream model is overloaded, please try again later
