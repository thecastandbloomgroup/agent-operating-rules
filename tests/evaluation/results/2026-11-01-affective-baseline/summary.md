# Evaluation run 2026-11-01-affective-baseline

| Executor | Judge | Responses | Pass | Mean total | Lowest criterion |
| -------- | ----- | --------- | ---- | ---------- | ---------------- |

Calls: 54, 0 failed. Cost: 1.67 USD.

## Tokens and cost

| Role | Model | Calls | Input | Cache write | Cache read | Output | Reasoning | Cost USD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| executor | anthropic/claude-sonnet-5-5@medium | 9 | 66690 | 44583 | 22071 | 28849 | 11797 | 0.40 |
| executor | google/gemini-3.8-flash@medium | 9 | 47352 | 0 | 4066 | 65496 | 55943 | 0.28 |
| executor | openai/gpt-6.1-sol@medium | 9 | 44997 | 44970 | 0 | 13271 | 4893 | 0.25 |
| executor | perplexity/glm-5.3-flash@medium | 9 | 45105 | 0 | 19456 | 23309 | 12788 | 0.02 |
| executor | perplexity/kimi-k3@low | 9 | 45822 | 0 | 19200 | 9804 | 1958 | 0.23 |
| executor | xai/grok-4.7@low | 9 | 55857 | 0 | 40320 | 73659 | 63088 | 0.49 |

## Human test

Score these responses in human-test.csv, then run `bin/run-evaluation.py --agreement` on this folder.

- none
