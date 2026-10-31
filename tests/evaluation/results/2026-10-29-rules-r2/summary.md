# Evaluation run 2026-10-29-rules-r2

| Executor | Judge | Responses | Pass | Mean total | Lowest criterion |
| -------- | ----- | --------- | ---- | ---------- | ---------------- |
| anthropic/claude-sonnet-5-5@medium | anthropic/claude-opus-5-5@high | 13 | 2 | 12.2 | R6 (1.00) |
| anthropic/claude-sonnet-5-5@medium | openai/gpt-6-astra@high | 13 | 0 | 10.3 | R2 (0.69) |
| google/gemini-3.8-flash@medium | anthropic/claude-opus-5-5@high | 11 | 0 | 10.0 | R6 (0.67) |
| google/gemini-3.8-flash@medium | google/gemini-4-argon@high | 10 | 1 | 11.3 | R6 (0.60) |
| perplexity/kimi-k3@low | google/gemini-4-argon@high | 12 | 1 | 10.4 | R1 (1.00) |
| perplexity/kimi-k3@low | perplexity/kimi-k3@high | 8 | 3 | 12.6 | R1 (1.12) |
| openai/gpt-6.1-sol@medium | anthropic/claude-opus-5-5@high | 13 | 1 | 10.6 | R6 (0.50) |
| openai/gpt-6.1-sol@medium | openai/gpt-6-astra@high | 13 | 2 | 10.2 | R6 (0.33) |
| xai/grok-4.7@low | google/gemini-4-argon@high | 8 | 2 | 11.2 | R9 (0.88) |
| xai/grok-4.7@low | xai/grok-4.7@high | 1 | 0 | 3.0 | R1 (0.00) |
| perplexity/glm-5.3-flash@medium | openai/gpt-6-astra@high | 9 | 0 | 8.0 | R6 (0.50) |
| perplexity/glm-5.3-flash@medium | perplexity/glm-5.3@high | 8 | 3 | 11.4 | R2 (0.88) |

Calls: 210, 25 failed. Cost: 14.21 USD.

## Tokens and cost

| Role | Model | Calls | Input | Cache write | Cache read | Output | Reasoning | Cost USD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| executor | anthropic/claude-sonnet-5-5@medium | 13 | 94776 | 8084 | 86640 | 45470 | 19620 | 0.48 |
| executor | google/gemini-3.8-flash@medium | 13 | 56897 | 0 | 0 | 28596 | 15128 | 0.15 |
| executor | openai/gpt-6.1-sol@medium | 13 | 63814 | 63775 | 0 | 18517 | 6175 | 0.34 |
| executor | perplexity/glm-5.3-flash@medium | 13 | 44305 | 0 | 9472 | 23955 | 12825 | 0.02 |
| executor | perplexity/kimi-k3@low | 13 | 60013 | 0 | 26880 | 13988 | 2225 | 0.32 |
| executor | xai/grok-4.7@low | 13 | 48926 | 0 | 38400 | 28505 | 21210 | 0.21 |
| judge | anthropic/claude-opus-5-5@high | 37 | 468750 | 468602 | 0 | 100090 | 59106 | 4.35 |
| judge | google/gemini-4-argon@high | 31 | 262299 | 0 | 0 | 111934 | 90628 | 1.64 |
| judge | openai/gpt-6-astra@high | 35 | 275787 | 138188 | 137494 | 82746 | 60323 | 6.00 |
| judge | perplexity/glm-5.3@high | 9 | 62553 | 0 | 7424 | 21779 | 13981 | 0.17 |
| judge | perplexity/kimi-k3@high | 12 | 64206 | 0 | 23040 | 23988 | 17009 | 0.49 |
| judge | xai/grok-4.7@high | 8 | 8019 | 0 | 1152 | 2905 | 2558 | 0.03 |

## Human test

Score these responses in human-test.csv, then run `bin/run-evaluation.py --agreement` on this folder.

- responses/anthropic_claude-sonnet-5-5@medium/H2-s1.md: a judge failed a gate
- responses/anthropic_claude-sonnet-5-5@medium/K1-s1.md: judges differ by more than 3 points
- responses/anthropic_claude-sonnet-5-5@medium/T1-s1.md: a judge failed a gate
- responses/anthropic_claude-sonnet-5-5@medium/T2-s1.md: a judge failed a gate
- responses/anthropic_claude-sonnet-5-5@medium/X1-s1.md: judges differ by more than 3 points
- responses/anthropic_claude-sonnet-5-5@medium/X2-s1.md: a judge failed a gate
- responses/google_gemini-3.8-flash@medium/K1-s1.md: a judge failed a gate
- responses/google_gemini-3.8-flash@medium/T2-s1.md: a judge failed a gate
- responses/google_gemini-3.8-flash@medium/U1-s1.md: a judge failed a gate
- responses/google_gemini-3.8-flash@medium/X1-s1.md: a judge failed a gate
- responses/google_gemini-3.8-flash@medium/X2-s1.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/C1-s1.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/H1-s1.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/K1-s1.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/T1-s1.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/T2-s1.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/T3-s1.md: random sample
- responses/openai_gpt-6.1-sol@medium/U1-s1.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/U2-s1.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/X1-s1.md: a judge failed a gate
- responses/perplexity_glm-5.3-flash@medium/H1-s1.md: judges differ by more than 3 points
- responses/perplexity_glm-5.3-flash@medium/K1-s1.md: judges differ by more than 3 points
- responses/perplexity_glm-5.3-flash@medium/T2-s1.md: a judge failed a gate
- responses/perplexity_glm-5.3-flash@medium/U2-s1.md: a judge failed a gate
- responses/perplexity_glm-5.3-flash@medium/X1-s1.md: judges differ by more than 3 points
- responses/perplexity_glm-5.3-flash@medium/X2-s1.md: judges differ by more than 3 points
- responses/perplexity_kimi-k3@low/H1-s1.md: a judge failed a gate
- responses/perplexity_kimi-k3@low/K1-s1.md: a judge failed a gate
- responses/perplexity_kimi-k3@low/T2-s1.md: judges differ by more than 3 points
- responses/perplexity_kimi-k3@low/U1-s1.md: judges differ by more than 3 points
- responses/perplexity_kimi-k3@low/U2-s1.md: a judge failed a gate
- responses/perplexity_kimi-k3@low/X1-s1.md: judges differ by more than 3 points
- responses/xai_grok-4.7@low/K2-s1.md: a judge failed a gate
- responses/xai_grok-4.7@low/T3-s1.md: random sample

## Failed calls

- google: K2-s1 executor google/gemini-3.8-flash: no connection: Remote end closed connection without response
- google: X1-s1 judge google/gemini-4-argon: no connection: Remote end closed connection without response
- google: U2-s1 executor google/gemini-3.8-flash: no connection: Remote end closed connection without response
- moonshot: C2-s1 judge perplexity/kimi-k3: no connection: Remote end closed connection without response
- moonshot: C1-s1 judge perplexity/kimi-k3: no connection: Remote end closed connection without response
- moonshot: K2-s1 judge perplexity/kimi-k3: no connection: Remote end closed connection without response
- moonshot: K1-s1 judge perplexity/kimi-k3: no connection: Remote end closed connection without response
- moonshot: X2-s1 executor perplexity/kimi-k3: no connection: Remote end closed connection without response
- xai: C2-s1 judge xai/grok-4.7: no connection: Remote end closed connection without response
- xai: C1-s1 judge xai/grok-4.7: no connection: Remote end closed connection without response
- xai: K1-s1 executor xai/grok-4.7: no connection: Remote end closed connection without response
- xai: X1-s1 executor xai/grok-4.7: no connection: Remote end closed connection without response
- xai: X2-s1 executor xai/grok-4.7: no connection: Remote end closed connection without response
- xai: H2-s1 executor xai/grok-4.7: no connection: Remote end closed connection without response
- xai: H1-s1 judge xai/grok-4.7: no connection: Remote end closed connection without response
- xai: U1-s1 judge xai/grok-4.7: no connection: Remote end closed connection without response
- xai: U2-s1 executor xai/grok-4.7: no connection: Remote end closed connection without response
- xai: T2-s1 judge xai/grok-4.7: no connection: Remote end closed connection without response
- xai: T1-s1 judge xai/grok-4.7: no connection: Remote end closed connection without response
- xai: T3-s1 judge xai/grok-4.7: no connection: Remote end closed connection without response
- zai: C1-s1 executor perplexity/glm-5.3-flash: no connection: Remote end closed connection without response
- zai: H2-s1 executor perplexity/glm-5.3-flash: no connection: Remote end closed connection without response
- zai: U1-s1 executor perplexity/glm-5.3-flash: no connection: Remote end closed connection without response
- zai: T3-s1 executor perplexity/glm-5.3-flash: no connection: Remote end closed connection without response
- zai: T2-s1 judge perplexity/glm-5.3: no connection: Remote end closed connection without response
