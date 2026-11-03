# Evaluation run 2026-11-03-factored-selftest

| Executor | Judge | Responses | Pass | Mean total | Lowest criterion |
| -------- | ----- | --------- | ---- | ---------- | ---------------- |

Calls: 108, 1 failed. Cost: 3.89 USD.

## Tokens and cost

| Role | Model | Calls | Input | Cache write | Cache read | Output | Reasoning | Cost USD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| executor | anthropic/claude-sonnet-5-5@medium | 18 | 145914 | 21120 | 124722 | 85645 | 44912 | 0.92 |
| executor | google/gemini-3.8-flash@medium | 18 | 105105 | 0 | 16279 | 90913 | 63859 | 0.41 |
| executor | openai/gpt-6.1-sol@medium | 18 | 98418 | 98364 | 0 | 37320 | 12041 | 0.62 |
| executor | perplexity/glm-5.3-flash@medium | 18 | 98736 | 0 | 57472 | 93786 | 63950 | 0.05 |
| executor | perplexity/kimi-k3@low | 18 | 94919 | 0 | 43072 | 42721 | 7766 | 0.81 |
| executor | xai/grok-4.7@low | 18 | 120894 | 0 | 67072 | 156393 | 131489 | 1.08 |

## Human test

Score these responses in human-test.csv, then run `bin/run-evaluation.py --agreement` on this folder.

- none

## Failed calls

- moonshot: T1-s1 executor perplexity/kimi-k3: failed: upstream model is overloaded, please try again later
