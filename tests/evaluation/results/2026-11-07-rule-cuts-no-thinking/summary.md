# Evaluation run 2026-11-07-rule-cuts-no-thinking

| Executor | Judge | Responses | Pass | Mean total | Lowest criterion |
| -------- | ----- | --------- | ---- | ---------- | ---------------- |

Calls: 126, 0 failed. Cost: 3.35 USD.

## Tokens and cost

| Role | Model | Calls | Input | Cache write | Cache read | Output | Reasoning | Cost USD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| executor | anthropic/claude-sonnet-5-5@medium | 21 | 123783 | 6382 | 117317 | 71610 | 29722 | 0.74 |
| executor | google/gemini-3.8-flash@medium | 21 | 87438 | 0 | 10435 | 142869 | 118030 | 0.59 |
| executor | openai/gpt-6.1-sol@medium | 21 | 84210 | 84147 | 0 | 33037 | 11465 | 0.54 |
| executor | perplexity/glm-5.3-flash@medium | 21 | 84210 | 0 | 72960 | 60359 | 35408 | 0.03 |
| executor | perplexity/kimi-k3@low | 21 | 85908 | 0 | 50048 | 25409 | 4240 | 0.50 |
| executor | xai/grok-4.7@low | 21 | 109527 | 0 | 83712 | 140247 | 115977 | 0.94 |

## Human test

Score these responses in human-test.csv, then run `bin/run-evaluation.py --agreement` on this folder.

- none
