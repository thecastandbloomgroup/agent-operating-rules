# Evaluation run 2026-11-05-rule-sequence

| Executor | Judge | Responses | Pass | Mean total | Lowest criterion |
| -------- | ----- | --------- | ---- | ---------- | ---------------- |

Calls: 126, 0 failed. Cost: 4.30 USD.

## Tokens and cost

| Role | Model | Calls | Input | Cache write | Cache read | Output | Reasoning | Cost USD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| executor | anthropic/claude-sonnet-5-5@medium | 21 | 157362 | 37793 | 119485 | 82450 | 37784 | 0.93 |
| executor | google/gemini-3.8-flash@medium | 21 | 111798 | 0 | 6099 | 120791 | 95051 | 0.53 |
| executor | openai/gpt-6.1-sol@medium | 21 | 106281 | 106218 | 0 | 32899 | 11452 | 0.59 |
| executor | perplexity/glm-5.3-flash@medium | 21 | 106533 | 0 | 77824 | 73243 | 43976 | 0.04 |
| executor | perplexity/kimi-k3@low | 21 | 108202 | 0 | 30080 | 54858 | 3224 | 1.07 |
| executor | xai/grok-4.7@low | 21 | 131619 | 0 | 84096 | 166536 | 141812 | 1.14 |

## Human test

Score these responses in human-test.csv, then run `bin/run-evaluation.py --agreement` on this folder.

- none
