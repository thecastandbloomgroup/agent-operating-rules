# Evaluation run 2026-11-01-split-first-b

| Executor | Judge | Responses | Pass | Mean total | Lowest criterion |
| -------- | ----- | --------- | ---- | ---------- | ---------------- |

Calls: 156, 0 failed. Cost: 5.62 USD.

## Tokens and cost

| Role | Model | Calls | Input | Cache write | Cache read | Output | Reasoning | Cost USD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| executor | google/gemini-3.8-flash@medium | 39 | 219573 | 0 | 8140 | 244927 | 191133 | 1.08 |
| executor | openai/gpt-6.1-sol@medium | 39 | 207084 | 201964 | 5003 | 71827 | 23023 | 1.22 |
| executor | perplexity/kimi-k3@low | 39 | 210660 | 0 | 153600 | 53558 | 6319 | 1.02 |
| executor | xai/grok-4.7@low | 39 | 254916 | 0 | 171776 | 340216 | 285958 | 2.29 |

## Human test

Score these responses in human-test.csv, then run `bin/run-evaluation.py --agreement` on this folder.

- none
