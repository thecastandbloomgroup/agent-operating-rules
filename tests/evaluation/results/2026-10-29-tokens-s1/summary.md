# Evaluation run 2026-10-29-tokens-s1

| Executor | Judge | Responses | Pass | Mean total | Lowest criterion |
| -------- | ----- | --------- | ---- | ---------- | ---------------- |
| anthropic/claude-sonnet-5-5@medium | anthropic/claude-opus-5-5@high | 9 | 3 | 12.2 | R6 (0.75) |
| anthropic/claude-sonnet-5-5@medium | openai/gpt-6-astra@high | 9 | 2 | 9.7 | R6 (0.25) |
| google/gemini-3.8-flash@medium | anthropic/claude-opus-5-5@high | 10 | 1 | 10.1 | R2 (1.00) |
| google/gemini-3.8-flash@medium | google/gemini-4-argon@high | 10 | 1 | 11.6 | R2 (1.00) |
| openai/gpt-6.1-sol@medium | anthropic/claude-opus-5-5@high | 11 | 0 | 9.5 | R6 (0.60) |
| openai/gpt-6.1-sol@medium | openai/gpt-6-astra@high | 11 | 0 | 10.1 | R2 (0.45) |
| xai/grok-4.7@low | google/gemini-4-argon@high | 3 | 0 | 10.3 | R6 (0.00) |
| xai/grok-4.7@low | xai/grok-4.7@high | 3 | 0 | 11.0 | R6 (0.00) |
| perplexity/glm-5.3-flash@medium | openai/gpt-6-astra@high | 4 | 0 | 8.8 | R2 (0.50) |
| perplexity/glm-5.3-flash@medium | perplexity/glm-5.3@high | 4 | 0 | 12.8 | R9 (1.00) |

Calls: 127, 16 failed. Cost: 10.75 USD.

## Tokens and cost

| Role | Model | Calls | Input | Cache write | Cache read | Output | Reasoning | Cost USD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| executor | anthropic/claude-sonnet-5-5@medium | 11 | 65643 | 7847 | 57760 | 31932 | 14434 | 0.34 |
| executor | google/gemini-3.8-flash@medium | 13 | 51670 | 0 | 0 | 42277 | 30291 | 0.20 |
| executor | openai/gpt-6.1-sol@medium | 13 | 53989 | 53956 | 0 | 15476 | 4892 | 0.29 |
| executor | perplexity/glm-5.3-flash@medium | 7 | 19741 | 0 | 4736 | 22338 | 16194 | 0.01 |
| executor | perplexity/kimi-k3@low | 2 | 0 | 0 | 0 | 0 | 0 | 0.00 |
| executor | xai/grok-4.7@low | 7 | 18362 | 0 | 8320 | 18474 | 15001 | 0.14 |
| judge | anthropic/claude-opus-5-5@high | 30 | 378124 | 378004 | 0 | 82995 | 49977 | 3.55 |
| judge | google/gemini-4-argon@high | 13 | 114082 | 0 | 6102 | 49968 | 40692 | 0.72 |
| judge | openai/gpt-6-astra@high | 24 | 189241 | 117433 | 71736 | 70305 | 54758 | 5.06 |
| judge | perplexity/glm-5.3@high | 4 | 32482 | 0 | 11264 | 18700 | 8184 | 0.11 |
| judge | xai/grok-4.7@high | 3 | 28238 | 0 | 3456 | 46009 | 44263 | 0.33 |

## Human test

Score these responses in human-test.csv, then run `bin/run-evaluation.py --agreement` on this folder.

- responses/anthropic_claude-sonnet-5-5@medium/C1-s1.md: a judge failed a gate
- responses/anthropic_claude-sonnet-5-5@medium/H1-s1.md: judges differ by more than 3 points
- responses/anthropic_claude-sonnet-5-5@medium/H2-s1.md: a judge failed a gate
- responses/anthropic_claude-sonnet-5-5@medium/K1-s1.md: judges differ by more than 3 points
- responses/anthropic_claude-sonnet-5-5@medium/T1-s1.md: judges differ by more than 3 points
- responses/anthropic_claude-sonnet-5-5@medium/X1-s1.md: a judge failed a gate
- responses/anthropic_claude-sonnet-5-5@medium/X2-s1.md: a judge failed a gate
- responses/google_gemini-3.8-flash@medium/H1-s1.md: random sample
- responses/google_gemini-3.8-flash@medium/K2-s1.md: random sample
- responses/google_gemini-3.8-flash@medium/T2-s1.md: a judge failed a gate
- responses/google_gemini-3.8-flash@medium/U1-s1.md: judges differ by more than 3 points
- responses/openai_gpt-6.1-sol@medium/K1-s1.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/K2-s1.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/T1-s1.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/T2-s1.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/U1-s1.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/U2-s1.md: a judge failed a gate
- responses/perplexity_glm-5.3-flash@medium/H1-s1.md: judges differ by more than 3 points
- responses/perplexity_glm-5.3-flash@medium/K1-s1.md: a judge failed a gate
- responses/perplexity_glm-5.3-flash@medium/X1-s1.md: judges differ by more than 3 points
- responses/perplexity_glm-5.3-flash@medium/X2-s1.md: judges differ by more than 3 points
- responses/xai_grok-4.7@low/X2-s1.md: a judge failed a gate

## Failed calls

- anthropic: C2-s1 executor anthropic/claude-sonnet-5-5: HTTP 429: {"error":{"message":"Request rate limit exceeded, please try again later.","type":"request_rate_limit_exceeded","code":429}}
- anthropic: K2-s1 executor anthropic/claude-sonnet-5-5: HTTP 429: {"error":{"message":"Request rate limit exceeded, please try again later.","type":"request_rate_limit_exceeded","code":429}}
- google: C1-s1 executor google/gemini-3.8-flash: HTTP 429: {"error":{"message":"Request rate limit exceeded, please try again later.","type":"request_rate_limit_exceeded","code":429}}
- google: K1-s1 executor google/gemini-3.8-flash: HTTP 429: {"error":{"message":"Request rate limit exceeded, please try again later.","type":"request_rate_limit_exceeded","code":429}}
- google: X2-s1 executor google/gemini-3.8-flash: HTTP 429: {"error":{"message":"Request rate limit exceeded, please try again later.","type":"request_rate_limit_exceeded","code":429}}
- moonshot: C2-s1 executor perplexity/kimi-k3: HTTP 429: {"error":{"message":"Request rate limit exceeded, please try again later.","type":"request_rate_limit_exceeded","code":429}}
- moonshot: C1-s1 executor perplexity/kimi-k3: HTTP 429: {"error":{"message":"upstream model is overloaded, please try again later","type":"overloaded","code":429}}

- openai: C2-s1 executor openai/gpt-6.1-sol: HTTP 429: {"error":{"message":"Request rate limit exceeded, please try again later.","type":"request_rate_limit_exceeded","code":429}}
- openai: X1-s1 executor openai/gpt-6.1-sol: HTTP 429: {"error":{"message":"Request rate limit exceeded, please try again later.","type":"request_rate_limit_exceeded","code":429}}
- xai: C2-s1 executor xai/grok-4.7: HTTP 429: {"error":{"message":"Request rate limit exceeded, please try again later.","type":"request_rate_limit_exceeded","code":429}}
- xai: K1-s1 executor xai/grok-4.7: HTTP 429: {"error":{"message":"Request rate limit exceeded, please try again later.","type":"request_rate_limit_exceeded","code":429}}
- xai: C1-s1 executor xai/grok-4.7: HTTP 429: {"error":{"message":"Request rate limit exceeded, please try again later.","type":"request_rate_limit_exceeded","code":429}}
- xai: H1-s1 executor xai/grok-4.7: HTTP 429: {"error":{"message":"Request rate limit exceeded, please try again later.","type":"request_rate_limit_exceeded","code":429}}
- zai: K2-s1 executor perplexity/glm-5.3-flash: HTTP 429: {"error":{"message":"Request rate limit exceeded, please try again later.","type":"request_rate_limit_exceeded","code":429}}
- zai: C1-s1 executor perplexity/glm-5.3-flash: HTTP 429: {"error":{"message":"Request rate limit exceeded, please try again later.","type":"request_rate_limit_exceeded","code":429}}
- zai: C2-s1 executor perplexity/glm-5.3-flash: HTTP 429: {"error":{"message":"Request rate limit exceeded, please try again later.","type":"request_rate_limit_exceeded","code":429}}
