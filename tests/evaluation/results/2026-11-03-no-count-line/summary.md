# Evaluation run 2026-11-03-no-count-line

| Executor | Judge | Responses | Pass | Mean total | Lowest criterion |
| -------- | ----- | --------- | ---- | ---------- | ---------------- |

Calls: 108, 3 failed. Cost: 4.83 USD.

## Tokens and cost

| Role | Model | Calls | Input | Cache write | Cache read | Output | Reasoning | Cost USD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| executor | anthropic/claude-sonnet-5-5@medium | 18 | 144456 | 30348 | 114036 | 70574 | 29777 | 0.79 |
| executor | google/gemini-3.8-flash@medium | 18 | 103983 | 0 | 10172 | 94657 | 67617 | 0.43 |
| executor | openai/gpt-6.1-sol@medium | 18 | 97302 | 97248 | 0 | 38345 | 12323 | 0.63 |
| executor | perplexity/glm-5.3-flash@medium | 18 | 97620 | 0 | 52992 | 70120 | 40660 | 0.04 |
| executor | perplexity/kimi-k3@low | 18 | 82371 | 0 | 51712 | 119861 | 631 | 1.91 |
| executor | xai/grok-4.7@low | 18 | 119790 | 0 | 73472 | 150620 | 125871 | 1.03 |

## Human test

Score these responses in human-test.csv, then run `bin/run-evaluation.py --agreement` on this folder.

- none

## Failed calls

- moonshot: K1-s1 executor perplexity/kimi-k3: failed: upstream model is overloaded, please try again later
- moonshot: U1-s1 executor perplexity/kimi-k3: failed: upstream model is overloaded, please try again later
- moonshot: T1-s1 executor perplexity/kimi-k3: failed: upstream model is overloaded, please try again later
