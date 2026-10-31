# Evaluation run 2026-10-28T1843Z

| Executor | Judge | Responses | Pass | Mean total | Lowest criterion |
| -------- | ----- | --------- | ---- | ---------- | ---------------- |
| anthropic/claude-sonnet-5-5@medium | anthropic/claude-opus-5-5@high | 1 | 0 | 13.0 | R1 (1.00) |
| anthropic/claude-sonnet-5-5@medium | openai/gpt-6-astra@high | 1 | 0 | 11.0 | R2 (0.00) |
| openai/gpt-6.1-sol@medium | openai/gpt-6-astra@high | 1 | 0 | 14.0 | R1 (1.00) |
| openai/gpt-6.1-sol@medium | anthropic/claude-opus-5-5@high | 1 | 0 | 14.0 | R1 (1.00) |
| google/gemini-3.8-flash@medium | google/gemini-4-argon@high | 1 | 0 | 4.0 | R1 (0.00) |
| google/gemini-3.8-flash@medium | anthropic/claude-opus-5-5@high | 1 | 0 | 4.0 | R1 (0.00) |
| perplexity/kimi-k3@low | perplexity/kimi-k3@high | 1 | 0 | 13.0 | R1 (1.00) |
| perplexity/kimi-k3@low | google/gemini-4-argon@high | 1 | 0 | 13.0 | R1 (1.00) |
| perplexity/glm-5.3-flash@medium | perplexity/glm-5.3@high | 1 | 0 | 12.0 | R1 (1.00) |
| perplexity/glm-5.3-flash@medium | openai/gpt-6-astra@high | 1 | 0 | 9.0 | R8 (0.00) |
| xai/grok-4.7@low | xai/grok-4.7@high | 1 | 0 | 11.0 | R2 (0.00) |
| xai/grok-4.7@low | google/gemini-4-argon@high | 1 | 0 | 14.0 | R1 (1.00) |

Calls: 18. Cost: 1.59 USD.

## Human test

Score these responses in human-test.csv, then run `bin/run-evaluation.py --agreement` on this folder.

- responses/anthropic_claude-sonnet-5-5@medium/C1-s1.md: a judge failed a gate
- responses/google_gemini-3.8-flash@medium/C1-s1.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/C1-s1.md: random sample
- responses/perplexity_kimi-k3@low/C1-s1.md: random sample
- responses/xai_grok-4.7@low/C1-s1.md: a judge failed a gate
