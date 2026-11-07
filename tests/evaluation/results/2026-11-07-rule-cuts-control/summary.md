# Evaluation run 2026-11-07-rule-cuts-control

| Executor | Judge | Responses | Pass | Mean total | Lowest criterion |
| -------- | ----- | --------- | ---- | ---------- | ---------------- |

Calls: 126, 0 failed. Cost: 3.92 USD.

## Tokens and cost

| Role | Model | Calls | Input | Cache write | Cache read | Output | Reasoning | Cost USD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| executor | anthropic/claude-sonnet-5-5@medium | 21 | 157446 | 30341 | 127021 | 76202 | 33617 | 0.85 |
| executor | google/gemini-3.8-flash@medium | 21 | 111672 | 0 | 0 | 112708 | 88650 | 0.51 |
| executor | openai/gpt-6.1-sol@medium | 21 | 106197 | 101132 | 5002 | 32491 | 10541 | 0.58 |
| executor | perplexity/glm-5.3-flash@medium | 21 | 106449 | 0 | 72960 | 74422 | 46237 | 0.04 |
| executor | perplexity/kimi-k3@low | 21 | 108126 | 0 | 34944 | 37171 | 15856 | 0.79 |
| executor | xai/grok-4.7@low | 21 | 131472 | 0 | 89216 | 171287 | 146040 | 1.16 |

## Human test

Score these responses in human-test.csv, then run `bin/run-evaluation.py --agreement` on this folder.

- none
