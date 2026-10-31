# Evaluation run 2026-10-29-tokens-s1c

| Executor | Judge | Responses | Pass | Mean total | Lowest criterion |
| -------- | ----- | --------- | ---- | ---------- | ---------------- |
| anthropic/claude-sonnet-5-5@medium | anthropic/claude-opus-5-5@high | 13 | 4 | 12.0 | R6 (1.00) |
| anthropic/claude-sonnet-5-5@medium | openai/gpt-6-astra@high | 13 | 2 | 10.1 | R6 (0.50) |
| google/gemini-3.8-flash@medium | anthropic/claude-opus-5-5@high | 13 | 2 | 10.6 | R8 (0.92) |
| google/gemini-3.8-flash@medium | google/gemini-4-argon@high | 13 | 3 | 11.9 | R1 (1.08) |
| perplexity/kimi-k3@low | google/gemini-4-argon@high | 13 | 1 | 11.1 | R1 (1.00) |
| perplexity/kimi-k3@low | perplexity/kimi-k3@high | 11 | 7 | 13.3 | R9 (1.09) |
| openai/gpt-6.1-sol@medium | anthropic/claude-opus-5-5@high | 13 | 2 | 10.3 | R6 (0.67) |
| openai/gpt-6.1-sol@medium | openai/gpt-6-astra@high | 13 | 1 | 10.8 | R2 (0.62) |
| xai/grok-4.7@low | google/gemini-4-argon@high | 7 | 1 | 11.1 | R2 (0.71) |
| xai/grok-4.7@low | xai/grok-4.7@high | 3 | 0 | 11.0 | R6 (0.00) |
| perplexity/glm-5.3-flash@medium | openai/gpt-6-astra@high | 12 | 0 | 10.2 | R8 (0.75) |
| perplexity/glm-5.3-flash@medium | perplexity/glm-5.3@high | 9 | 3 | 13.2 | R9 (1.00) |

Calls: 238, 33 failed. Cost: 17.49 USD.

## Tokens and cost

| Role | Model | Calls | Input | Cache write | Cache read | Output | Reasoning | Cost USD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| executor | anthropic/claude-sonnet-5-5@medium | 15 | 94776 | 15304 | 79420 | 43966 | 19198 | 0.49 |
| executor | google/gemini-3.8-flash@medium | 16 | 67219 | 0 | 0 | 53315 | 37719 | 0.25 |
| executor | openai/gpt-6.1-sol@medium | 15 | 63814 | 63775 | 0 | 19000 | 6012 | 0.35 |
| executor | perplexity/glm-5.3-flash@medium | 16 | 59095 | 0 | 9472 | 52022 | 35917 | 0.03 |
| executor | perplexity/kimi-k3@low | 15 | 65010 | 0 | 34560 | 16777 | 3371 | 0.35 |
| executor | xai/grok-4.7@low | 17 | 48965 | 0 | 28672 | 39526 | 30780 | 0.29 |
| judge | anthropic/claude-opus-5-5@high | 39 | 492132 | 491976 | 0 | 108640 | 65922 | 4.63 |
| judge | google/gemini-4-argon@high | 34 | 289934 | 0 | 6102 | 123255 | 99570 | 1.80 |
| judge | openai/gpt-6-astra@high | 38 | 300457 | 204695 | 95648 | 107532 | 83010 | 8.03 |
| judge | perplexity/glm-5.3@high | 12 | 70622 | 0 | 30528 | 33327 | 13819 | 0.21 |
| judge | perplexity/kimi-k3@high | 13 | 88512 | 0 | 18432 | 33810 | 24640 | 0.72 |
| judge | xai/grok-4.7@high | 8 | 28238 | 0 | 3456 | 46009 | 44263 | 0.33 |

## Human test

Score these responses in human-test.csv, then run `bin/run-evaluation.py --agreement` on this folder.

- responses/anthropic_claude-sonnet-5-5@medium/C1-s1.md: a judge failed a gate
- responses/anthropic_claude-sonnet-5-5@medium/H1-s1.md: judges differ by more than 3 points
- responses/anthropic_claude-sonnet-5-5@medium/H2-s1.md: a judge failed a gate
- responses/anthropic_claude-sonnet-5-5@medium/K1-s1.md: judges differ by more than 3 points
- responses/anthropic_claude-sonnet-5-5@medium/T1-s1.md: judges differ by more than 3 points
- responses/anthropic_claude-sonnet-5-5@medium/T2-s1.md: a judge failed a gate
- responses/anthropic_claude-sonnet-5-5@medium/X1-s1.md: a judge failed a gate
- responses/anthropic_claude-sonnet-5-5@medium/X2-s1.md: a judge failed a gate
- responses/google_gemini-3.8-flash@medium/T2-s1.md: a judge failed a gate
- responses/google_gemini-3.8-flash@medium/U1-s1.md: judges differ by more than 3 points
- responses/google_gemini-3.8-flash@medium/X2-s1.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/K1-s1.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/K2-s1.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/T1-s1.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/T2-s1.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/U1-s1.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/U2-s1.md: a judge failed a gate
- responses/perplexity_glm-5.3-flash@medium/H1-s1.md: judges differ by more than 3 points
- responses/perplexity_glm-5.3-flash@medium/H2-s1.md: a judge failed a gate
- responses/perplexity_glm-5.3-flash@medium/K1-s1.md: a judge failed a gate
- responses/perplexity_glm-5.3-flash@medium/T1-s1.md: judges differ by more than 3 points
- responses/perplexity_glm-5.3-flash@medium/T2-s1.md: random sample
- responses/perplexity_glm-5.3-flash@medium/X1-s1.md: judges differ by more than 3 points
- responses/perplexity_glm-5.3-flash@medium/X2-s1.md: judges differ by more than 3 points
- responses/perplexity_kimi-k3@low/H2-s1.md: judges differ by more than 3 points
- responses/perplexity_kimi-k3@low/K1-s1.md: a judge failed a gate
- responses/perplexity_kimi-k3@low/K2-s1.md: judges differ by more than 3 points
- responses/perplexity_kimi-k3@low/U1-s1.md: judges differ by more than 3 points
- responses/perplexity_kimi-k3@low/U2-s1.md: a judge failed a gate
- responses/perplexity_kimi-k3@low/X1-s1.md: judges differ by more than 3 points
- responses/perplexity_kimi-k3@low/X2-s1.md: a judge failed a gate
- responses/xai_grok-4.7@low/C1-s1.md: random sample
- responses/xai_grok-4.7@low/T2-s1.md: a judge failed a gate
- responses/xai_grok-4.7@low/X2-s1.md: a judge failed a gate

## Failed calls

- moonshot: T2-s1 judge perplexity/kimi-k3: HTTP 429: {"error":{"message":"upstream model is overloaded, please try again later","type":"overloaded","code":429}}

- moonshot: T3-s1 judge perplexity/kimi-k3: no connection: Remote end closed connection without response
- xai: C2-s1 executor xai/grok-4.7: no connection: Remote end closed connection without response
- xai: C1-s1 judge xai/grok-4.7: no connection: Remote end closed connection without response
- xai: K1-s1 executor xai/grok-4.7: no connection: Remote end closed connection without response
- xai: H1-s1 judge xai/grok-4.7: no connection: Remote end closed connection without response
- xai: X1-s1 judge xai/grok-4.7: no connection: Remote end closed connection without response
- xai: X1-s1 judge google/gemini-4-argon: no connection: Remote end closed connection without response
- xai: U1-s1 executor xai/grok-4.7: no connection: Remote end closed connection without response
- xai: U2-s1 executor xai/grok-4.7: no connection: Remote end closed connection without response
- xai: T1-s1 executor xai/grok-4.7: no connection: Remote end closed connection without response
- xai: T2-s1 judge xai/grok-4.7: no connection: Remote end closed connection without response
- xai: T3-s1 judge xai/grok-4.7: no connection: Remote end closed connection without response
- zai: U1-s1 executor perplexity/glm-5.3-flash: no connection: [Errno 54] Connection reset by peer
- zai: H2-s1 judge perplexity/glm-5.3: no connection: Remote end closed connection without response
- zai: T2-s1 judge perplexity/glm-5.3: no connection: Remote end closed connection without response
- zai: T3-s1 judge perplexity/glm-5.3: no connection: Remote end closed connection without response
