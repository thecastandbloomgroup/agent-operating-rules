# Evaluation run 2026-11-03-organization-line

| Executor | Judge | Responses | Pass | Mean total | Lowest criterion |
| -------- | ----- | --------- | ---- | ---------- | ---------------- |

Calls: 18, 0 failed. Cost: 0.63 USD.

## Tokens and cost

| Role | Model | Calls | Input | Cache write | Cache read | Output | Reasoning | Cost USD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| executor | anthropic/claude-sonnet-5-5@medium | 3 | 22287 | 22275 | 0 | 11002 | 4720 | 0.17 |
| executor | google/gemini-3.8-flash@medium | 3 | 15825 | 0 | 0 | 21387 | 17912 | 0.09 |
| executor | openai/gpt-6.1-sol@medium | 3 | 15036 | 15027 | 0 | 4341 | 1337 | 0.08 |
| executor | perplexity/glm-5.3-flash@medium | 3 | 15072 | 0 | 9728 | 11763 | 8836 | 0.01 |
| executor | perplexity/kimi-k3@low | 3 | 15312 | 0 | 7680 | 3551 | 1449 | 0.08 |
| executor | xai/grok-4.7@low | 3 | 18654 | 0 | 8448 | 30354 | 26394 | 0.21 |

## Human test

Score these responses in human-test.csv, then run `bin/run-evaluation.py --agreement` on this folder.

- none
