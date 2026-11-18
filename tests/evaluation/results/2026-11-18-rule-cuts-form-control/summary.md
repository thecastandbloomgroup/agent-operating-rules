# Evaluation run 2026-11-18-rule-cuts-form-control

| Executor | Judge | Responses | Pass | Mean total | Lowest criterion |
| -------- | ----- | --------- | ---- | ---------- | ---------------- |

Calls: 126, 0 failed. Cost: 3.76 USD.

## Tokens and cost

| Role | Model | Calls | Input | Cache write | Cache read | Output | Reasoning | Cost USD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| executor | anthropic/claude-sonnet-5-5@medium | 21 | 157467 | 30350 | 127033 | 84459 | 40924 | 0.93 |
| executor | google/gemini-3.8-flash@medium | 21 | 111693 | 0 | 6555 | 152543 | 127912 | 0.65 |
| executor | openai/gpt-6.1-sol@medium | 21 | 106197 | 307 | 105827 | 34140 | 12205 | 0.35 |
| executor | perplexity/glm-5.3-flash@medium | 21 | 106461 | 0 | 87552 | 87886 | 58872 | 0.05 |
| executor | perplexity/kimi-k3@low | 21 | 108126 | 0 | 69888 | 30696 | 9034 | 0.60 |
| executor | xai/grok-4.7@low | 21 | 131484 | 0 | 119040 | 181232 | 156562 | 1.17 |

## Human test

Score these responses in human-test.csv, then run `bin/run-evaluation.py --agreement` on this folder.

- none
