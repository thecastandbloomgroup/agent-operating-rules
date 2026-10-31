# Evaluation run 2026-10-29-tokens-s1b

| Executor | Judge | Responses | Pass | Mean total | Lowest criterion |
| -------- | ----- | --------- | ---- | ---------- | ---------------- |
| anthropic/claude-sonnet-5-5@medium | anthropic/claude-opus-5-5@high | 4 | 1 | 11.5 | R1 (1.00) |
| anthropic/claude-sonnet-5-5@medium | openai/gpt-6-astra@high | 4 | 0 | 11.0 | R8 (0.75) |
| google/gemini-3.8-flash@medium | anthropic/claude-opus-5-5@high | 3 | 1 | 12.3 | R8 (0.67) |
| google/gemini-3.8-flash@medium | google/gemini-4-argon@high | 3 | 2 | 13.0 | R1 (1.00) |
| perplexity/kimi-k3@low | google/gemini-4-argon@high | 13 | 1 | 11.1 | R1 (1.00) |
| perplexity/kimi-k3@low | perplexity/kimi-k3@high | 11 | 7 | 13.3 | R9 (1.09) |
| openai/gpt-6.1-sol@medium | anthropic/claude-opus-5-5@high | 2 | 2 | 14.5 | R6 (1.00) |
| openai/gpt-6.1-sol@medium | openai/gpt-6-astra@high | 2 | 1 | 14.5 | R6 (1.00) |
| xai/grok-4.7@low | google/gemini-4-argon@high | 4 | 1 | 11.8 | R2 (0.75) |
| perplexity/glm-5.3-flash@medium | openai/gpt-6-astra@high | 8 | 0 | 10.9 | R8 (0.62) |
| perplexity/glm-5.3-flash@medium | perplexity/glm-5.3@high | 5 | 3 | 13.6 | R1 (1.00) |

Calls: 111, 17 failed. Cost: 6.75 USD.

## Tokens and cost

| Role | Model | Calls | Input | Cache write | Cache read | Output | Reasoning | Cost USD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| executor | anthropic/claude-sonnet-5-5@medium | 4 | 29133 | 7457 | 21660 | 12034 | 4764 | 0.14 |
| executor | google/gemini-3.8-flash@medium | 3 | 15549 | 0 | 0 | 11038 | 7428 | 0.05 |
| executor | openai/gpt-6.1-sol@medium | 2 | 9825 | 9819 | 0 | 3524 | 1120 | 0.06 |
| executor | perplexity/glm-5.3-flash@medium | 9 | 39354 | 0 | 4736 | 29684 | 19723 | 0.02 |
| executor | perplexity/kimi-k3@low | 13 | 65010 | 0 | 34560 | 16777 | 3371 | 0.35 |
| executor | xai/grok-4.7@low | 10 | 30603 | 0 | 20352 | 21052 | 15779 | 0.16 |
| judge | anthropic/claude-opus-5-5@high | 9 | 114008 | 113972 | 0 | 25645 | 15945 | 1.08 |
| judge | google/gemini-4-argon@high | 21 | 175852 | 0 | 0 | 73287 | 58878 | 1.08 |
| judge | openai/gpt-6-astra@high | 14 | 111216 | 87262 | 23912 | 37227 | 28252 | 2.98 |
| judge | perplexity/glm-5.3@high | 8 | 38140 | 0 | 19264 | 14627 | 5635 | 0.10 |
| judge | perplexity/kimi-k3@high | 13 | 88512 | 0 | 18432 | 33810 | 24640 | 0.72 |
| judge | xai/grok-4.7@high | 5 | 0 | 0 | 0 | 0 | 0 | 0.00 |

## Human test

Score these responses in human-test.csv, then run `bin/run-evaluation.py --agreement` on this folder.

- responses/anthropic_claude-sonnet-5-5@medium/T2-s1.md: a judge failed a gate
- responses/google_gemini-3.8-flash@medium/X2-s1.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/C2-s1.md: random sample
- responses/perplexity_glm-5.3-flash@medium/H2-s1.md: a judge failed a gate
- responses/perplexity_glm-5.3-flash@medium/T1-s1.md: judges differ by more than 3 points
- responses/perplexity_kimi-k3@low/H1-s1.md: random sample
- responses/perplexity_kimi-k3@low/H2-s1.md: judges differ by more than 3 points
- responses/perplexity_kimi-k3@low/K1-s1.md: a judge failed a gate
- responses/perplexity_kimi-k3@low/K2-s1.md: judges differ by more than 3 points
- responses/perplexity_kimi-k3@low/U1-s1.md: judges differ by more than 3 points
- responses/perplexity_kimi-k3@low/U2-s1.md: a judge failed a gate
- responses/perplexity_kimi-k3@low/X1-s1.md: judges differ by more than 3 points
- responses/perplexity_kimi-k3@low/X2-s1.md: a judge failed a gate
- responses/xai_grok-4.7@low/T2-s1.md: a judge failed a gate

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
