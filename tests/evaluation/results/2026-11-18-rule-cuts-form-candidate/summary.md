# Evaluation run 2026-11-18-rule-cuts-form-candidate

| Executor | Judge | Responses | Pass | Mean total | Lowest criterion |
| -------- | ----- | --------- | ---- | ---------- | ---------------- |

Calls: 126, 0 failed. Cost: 3.26 USD.

## Tokens and cost

| Role | Model | Calls | Input | Cache write | Cache read | Output | Reasoning | Cost USD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| executor | anthropic/claude-sonnet-5-5@medium | 21 | 122544 | 18025 | 104435 | 73785 | 31349 | 0.79 |
| executor | google/gemini-3.8-flash@medium | 21 | 86430 | 0 | 8270 | 179704 | 155743 | 0.73 |
| executor | openai/gpt-6.1-sol@medium | 21 | 83265 | 4274 | 78928 | 31174 | 10675 | 0.33 |
| executor | perplexity/glm-5.3-flash@medium | 21 | 83277 | 0 | 67328 | 62149 | 35606 | 0.04 |
| executor | perplexity/kimi-k3@low | 21 | 84984 | 0 | 76800 | 29806 | 10337 | 0.49 |
| executor | xai/grok-4.7@low | 21 | 108603 | 0 | 95616 | 132306 | 109932 | 0.87 |

## Human test

Score these responses in human-test.csv, then run `bin/run-evaluation.py --agreement` on this folder.

- none
