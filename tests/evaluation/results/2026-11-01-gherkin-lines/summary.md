# Evaluation run 2026-11-01-gherkin-lines

| Executor | Judge | Responses | Pass | Mean total | Lowest criterion |
| -------- | ----- | --------- | ---- | ---------- | ---------------- |

Calls: 234, 0 failed. Cost: 8.17 USD.

## Tokens and cost

| Role | Model | Calls | Input | Cache write | Cache read | Output | Reasoning | Cost USD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| executor | anthropic/claude-sonnet-5-5@medium | 39 | 303993 | 55098 | 248739 | 156185 | 71958 | 1.72 |
| executor | google/gemini-3.8-flash@medium | 39 | 217272 | 0 | 10165 | 203278 | 149228 | 0.92 |
| executor | openai/gpt-6.1-sol@medium | 39 | 204783 | 199722 | 4944 | 69863 | 22442 | 1.20 |
| executor | perplexity/glm-5.3-flash@medium | 39 | 205383 | 0 | 110208 | 169064 | 108443 | 0.10 |
| executor | perplexity/kimi-k3@low | 39 | 208343 | 0 | 122240 | 111387 | 11405 | 1.97 |
| executor | xai/grok-4.7@low | 39 | 252615 | 0 | 161920 | 333571 | 281043 | 2.26 |

## Human test

Score these responses in human-test.csv, then run `bin/run-evaluation.py --agreement` on this folder.

- none
