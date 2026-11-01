# Evaluation run 2026-10-31-wording-r05

| Executor | Judge | Responses | Pass | Mean total | Lowest criterion |
| -------- | ----- | --------- | ---- | ---------- | ---------------- |

Calls: 234, 1 failed. Cost: 7.45 USD.

## Tokens and cost

| Role | Model | Calls | Input | Cache write | Cache read | Output | Reasoning | Cost USD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| executor | anthropic/claude-sonnet-5-5@medium | 39 | 302706 | 28374 | 274176 | 156637 | 69862 | 1.67 |
| executor | google/gemini-3.8-flash@medium | 39 | 210791 | 0 | 22378 | 144024 | 91662 | 0.68 |
| executor | openai/gpt-6.1-sol@medium | 39 | 203769 | 198734 | 4918 | 67501 | 20618 | 1.17 |
| executor | perplexity/glm-5.3-flash@medium | 39 | 204369 | 0 | 137856 | 198048 | 135896 | 0.11 |
| executor | perplexity/kimi-k3@low | 39 | 207337 | 0 | 132992 | 82232 | 11701 | 1.50 |
| executor | xai/grok-4.7@low | 39 | 251601 | 0 | 171904 | 345172 | 293012 | 2.32 |

## Human test

Score these responses in human-test.csv, then run `bin/run-evaluation.py --agreement` on this folder.

- none

## Failed calls

- google: C2-s1 executor google/gemini-3.8-flash: failed: upstream model is overloaded, please try again later
