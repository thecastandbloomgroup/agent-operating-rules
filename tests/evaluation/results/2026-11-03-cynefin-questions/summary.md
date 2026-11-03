# Evaluation run 2026-11-03-cynefin-questions

| Executor | Judge | Responses | Pass | Mean total | Lowest criterion |
| -------- | ----- | --------- | ---- | ---------- | ---------------- |

Calls: 234, 1 failed. Cost: 7.55 USD.

## Tokens and cost

| Role | Model | Calls | Input | Cache write | Cache read | Output | Reasoning | Cost USD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| executor | anthropic/claude-sonnet-5-5@medium | 39 | 309687 | 22964 | 286567 | 169324 | 81542 | 1.78 |
| executor | google/gemini-3.8-flash@medium | 39 | 221367 | 0 | 24408 | 158362 | 103674 | 0.74 |
| executor | openai/gpt-6.1-sol@medium | 39 | 203917 | 198750 | 5053 | 67607 | 20862 | 1.17 |
| executor | perplexity/glm-5.3-flash@medium | 39 | 209685 | 0 | 131840 | 178657 | 116965 | 0.11 |
| executor | perplexity/kimi-k3@low | 39 | 212598 | 0 | 130176 | 90784 | 7407 | 1.65 |
| executor | xai/grok-4.7@low | 39 | 256866 | 0 | 166016 | 305013 | 252463 | 2.09 |

## Human test

Score these responses in human-test.csv, then run `bin/run-evaluation.py --agreement` on this folder.

- none

## Failed calls

- openai: H1-s1 executor openai/gpt-6.1-sol: failed: upstream model is overloaded, please try again later
