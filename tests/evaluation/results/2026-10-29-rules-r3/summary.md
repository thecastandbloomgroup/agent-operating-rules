# Evaluation run 2026-10-29-rules-r3

| Executor | Judge | Responses | Pass | Mean total | Lowest criterion |
| -------- | ----- | --------- | ---- | ---------- | ---------------- |
| anthropic/claude-sonnet-5-5@medium | anthropic/claude-opus-5-5@high | 13 | 2 | 11.9 | R6 (1.00) |
| anthropic/claude-sonnet-5-5@medium | openai/gpt-6-astra@high | 13 | 0 | 9.3 | R6 (0.67) |
| google/gemini-3.8-flash@medium | anthropic/claude-opus-5-5@high | 12 | 0 | 9.4 | R2 (0.83) |
| google/gemini-3.8-flash@medium | google/gemini-4-argon@high | 12 | 1 | 10.7 | R2 (1.00) |
| perplexity/kimi-k3@low | google/gemini-4-argon@high | 13 | 2 | 10.2 | R9 (0.92) |
| perplexity/kimi-k3@low | perplexity/kimi-k3@high | 11 | 3 | 11.8 | R1 (1.00) |
| openai/gpt-6.1-sol@medium | anthropic/claude-opus-5-5@high | 13 | 2 | 10.5 | R6 (0.50) |
| openai/gpt-6.1-sol@medium | openai/gpt-6-astra@high | 13 | 2 | 10.3 | R6 (0.33) |
| xai/grok-4.7@low | google/gemini-4-argon@high | 4 | 0 | 10.2 | R6 (0.00) |
| perplexity/glm-5.3-flash@medium | openai/gpt-6-astra@high | 13 | 0 | 9.2 | R8 (0.85) |
| perplexity/glm-5.3-flash@medium | perplexity/glm-5.3@high | 11 | 4 | 12.1 | R1 (0.91) |

Calls: 214, 18 failed. Cost: 15.44 USD.

## Tokens and cost

| Role | Model | Calls | Input | Cache write | Cache read | Output | Reasoning | Cost USD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| executor | anthropic/claude-sonnet-5-5@medium | 13 | 94776 | 15304 | 79420 | 44388 | 19092 | 0.49 |
| executor | google/gemini-3.8-flash@medium | 13 | 62051 | 0 | 0 | 44758 | 30655 | 0.21 |
| executor | openai/gpt-6.1-sol@medium | 13 | 63814 | 63775 | 0 | 19372 | 6658 | 0.35 |
| executor | perplexity/glm-5.3-flash@medium | 13 | 63984 | 0 | 23680 | 46659 | 28866 | 0.03 |
| executor | perplexity/kimi-k3@low | 13 | 65010 | 0 | 38400 | 16396 | 4399 | 0.34 |
| executor | xai/grok-4.7@low | 13 | 24455 | 0 | 24064 | 18532 | 14892 | 0.12 |
| judge | anthropic/claude-opus-5-5@high | 38 | 480405 | 480253 | 0 | 106902 | 65064 | 4.54 |
| judge | google/gemini-4-argon@high | 29 | 252855 | 0 | 0 | 107011 | 85644 | 1.58 |
| judge | openai/gpt-6-astra@high | 39 | 309831 | 160264 | 149450 | 94505 | 69967 | 6.88 |
| judge | perplexity/glm-5.3@high | 13 | 87672 | 0 | 7872 | 30199 | 19181 | 0.25 |
| judge | perplexity/kimi-k3@high | 13 | 87745 | 0 | 32256 | 31409 | 22262 | 0.65 |
| judge | xai/grok-4.7@high | 4 | 0 | 0 | 0 | 0 | 0 | 0.00 |

## Human test

Score these responses in human-test.csv, then run `bin/run-evaluation.py --agreement` on this folder.

- responses/anthropic_claude-sonnet-5-5@medium/C1-s1.md: a judge failed a gate
- responses/anthropic_claude-sonnet-5-5@medium/H1-s1.md: judges differ by more than 3 points
- responses/anthropic_claude-sonnet-5-5@medium/K1-s1.md: judges differ by more than 3 points
- responses/anthropic_claude-sonnet-5-5@medium/T1-s1.md: judges differ by more than 3 points
- responses/anthropic_claude-sonnet-5-5@medium/T2-s1.md: a judge failed a gate
- responses/anthropic_claude-sonnet-5-5@medium/U2-s1.md: judges differ by more than 3 points
- responses/anthropic_claude-sonnet-5-5@medium/X1-s1.md: a judge failed a gate
- responses/anthropic_claude-sonnet-5-5@medium/X2-s1.md: a judge failed a gate
- responses/google_gemini-3.8-flash@medium/K1-s1.md: a judge failed a gate
- responses/google_gemini-3.8-flash@medium/T2-s1.md: a judge failed a gate
- responses/google_gemini-3.8-flash@medium/U1-s1.md: judges differ by more than 3 points
- responses/google_gemini-3.8-flash@medium/X1-s1.md: a judge failed a gate
- responses/google_gemini-3.8-flash@medium/X2-s1.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/C1-s1.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/C2-s1.md: random sample
- responses/openai_gpt-6.1-sol@medium/H1-s1.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/K1-s1.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/K2-s1.md: judges differ by more than 3 points
- responses/openai_gpt-6.1-sol@medium/T1-s1.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/T2-s1.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/U1-s1.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/U2-s1.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/X1-s1.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/X2-s1.md: a judge failed a gate
- responses/perplexity_glm-5.3-flash@medium/C2-s1.md: a judge failed a gate
- responses/perplexity_glm-5.3-flash@medium/H1-s1.md: judges differ by more than 3 points
- responses/perplexity_glm-5.3-flash@medium/H2-s1.md: judges differ by more than 3 points
- responses/perplexity_glm-5.3-flash@medium/K1-s1.md: a judge failed a gate
- responses/perplexity_glm-5.3-flash@medium/K2-s1.md: judges differ by more than 3 points
- responses/perplexity_glm-5.3-flash@medium/U1-s1.md: judges differ by more than 3 points
- responses/perplexity_glm-5.3-flash@medium/U2-s1.md: judges differ by more than 3 points
- responses/perplexity_glm-5.3-flash@medium/X1-s1.md: random sample
- responses/perplexity_glm-5.3-flash@medium/X2-s1.md: a judge failed a gate
- responses/perplexity_kimi-k3@low/H1-s1.md: a judge failed a gate
- responses/perplexity_kimi-k3@low/T2-s1.md: a judge failed a gate
- responses/perplexity_kimi-k3@low/U2-s1.md: judges differ by more than 3 points
- responses/perplexity_kimi-k3@low/X1-s1.md: a judge failed a gate
- responses/perplexity_kimi-k3@low/X2-s1.md: judges differ by more than 3 points
- responses/xai_grok-4.7@low/X2-s1.md: a judge failed a gate

## Failed calls

- google: K2-s1 executor google/gemini-3.8-flash: no connection: Remote end closed connection without response
- moonshot: C2-s1 judge perplexity/kimi-k3: HTTP 429: {"error":{"message":"upstream model is overloaded, please try again later","type":"overloaded","code":429}}

- moonshot: C1-s1 judge perplexity/kimi-k3: HTTP 429: {"error":{"message":"upstream model is overloaded, please try again later","type":"overloaded","code":429}}

- xai: C1-s1 executor xai/grok-4.7: no connection: Remote end closed connection without response
- xai: C2-s1 judge xai/grok-4.7: no connection: Remote end closed connection without response
- xai: K1-s1 executor xai/grok-4.7: no connection: Remote end closed connection without response
- xai: X1-s1 executor xai/grok-4.7: no connection: Remote end closed connection without response
- xai: K2-s1 judge xai/grok-4.7: no connection: Remote end closed connection without response
- xai: H1-s1 executor xai/grok-4.7: no connection: Remote end closed connection without response
- xai: X2-s1 judge xai/grok-4.7: no connection: Remote end closed connection without response
- xai: H2-s1 executor xai/grok-4.7: no connection: Remote end closed connection without response
- xai: U1-s1 executor xai/grok-4.7: no connection: Remote end closed connection without response
- xai: T1-s1 executor xai/grok-4.7: no connection: Remote end closed connection without response
- xai: U2-s1 judge xai/grok-4.7: no connection: Remote end closed connection without response
- xai: T2-s1 executor xai/grok-4.7: no connection: Remote end closed connection without response
- xai: T3-s1 executor xai/grok-4.7: no connection: Remote end closed connection without response
- zai: C2-s1 judge perplexity/glm-5.3: no connection: Remote end closed connection without response
- zai: K1-s1 judge perplexity/glm-5.3: no connection: Remote end closed connection without response
