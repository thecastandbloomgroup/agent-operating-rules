# Evaluation run 2026-11-03-reason-form

| Executor | Judge | Responses | Pass | Mean total | Lowest criterion |
| -------- | ----- | --------- | ---- | ---------- | ---------------- |

Calls: 72, 3 failed. Cost: 2.42 USD.

## Tokens and cost

| Role | Model | Calls | Input | Cache write | Cache read | Output | Reasoning | Cost USD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| executor | anthropic/claude-sonnet-5-5@medium | 12 | 89439 | 15039 | 74352 | 48550 | 21259 | 0.53 |
| executor | google/gemini-3.8-flash@medium | 12 | 63465 | 0 | 6099 | 55526 | 40106 | 0.25 |
| executor | openai/gpt-6.1-sol@medium | 12 | 55290 | 55257 | 0 | 17180 | 5264 | 0.31 |
| executor | perplexity/glm-5.3-flash@medium | 12 | 60468 | 0 | 43776 | 41916 | 23960 | 0.02 |
| executor | perplexity/kimi-k3@low | 12 | 51161 | 0 | 19392 | 41052 | 1497 | 0.72 |
| executor | xai/grok-4.7@low | 12 | 74802 | 0 | 48768 | 85147 | 69942 | 0.59 |

## Human test

Score these responses in human-test.csv, then run `bin/run-evaluation.py --agreement` on this folder.

- none

## Failed calls

- moonshot: X1-s1 executor perplexity/kimi-k3: failed: upstream model is overloaded, please try again later
- moonshot: H2-s1 executor perplexity/kimi-k3: failed: upstream model is overloaded, please try again later
- openai: X1-s1 executor openai/gpt-6.1-sol: failed: upstream model is overloaded, please try again later
