# Evaluation run 2026-10-30-probe-base

| Executor | Judge | Responses | Pass | Mean total | Lowest criterion |
| -------- | ----- | --------- | ---- | ---------- | ---------------- |
| anthropic/claude-sonnet-5-5@medium | anthropic/claude-opus-5-5@high | 10 | 0 | 12.0 | R9 (1.00) |
| anthropic/claude-sonnet-5-5@medium | openai/gpt-6-astra@high | 10 | 0 | 11.5 | R9 (1.00) |
| google/gemini-3.8-flash@medium | anthropic/claude-opus-5-5@high | 10 | 0 | 9.4 | R8 (0.60) |
| google/gemini-3.8-flash@medium | google/gemini-4-argon@high | 10 | 2 | 10.5 | R2 (0.80) |
| perplexity/kimi-k3@low | google/gemini-4-argon@high | 2 | 2 | 16.5 | R9 (1.00) |
| perplexity/kimi-k3@low | perplexity/kimi-k3@high | 2 | 2 | 17.0 | R9 (1.00) |
| openai/gpt-6.1-sol@medium | anthropic/claude-opus-5-5@high | 10 | 2 | 10.2 | R2 (0.90) |
| openai/gpt-6.1-sol@medium | openai/gpt-6-astra@high | 10 | 2 | 10.1 | R2 (0.70) |
| xai/grok-4.7@low | google/gemini-4-argon@high | 2 | 2 | 15.5 | R1 (1.00) |
| xai/grok-4.7@low | xai/grok-4.7@high | 2 | 1 | 14.5 | R1 (1.00) |
| perplexity/glm-5.3-flash@medium | openai/gpt-6-astra@high | 6 | 0 | 9.8 | R8 (0.33) |
| perplexity/glm-5.3-flash@medium | perplexity/glm-5.3@high | 8 | 3 | 13.2 | R9 (1.00) |

Calls: 148, 22 failed. Cost: 11.88 USD.

## Tokens and cost

| Role | Model | Calls | Input | Cache write | Cache read | Output | Reasoning | Cost USD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| executor | anthropic/claude-sonnet-5-5@medium | 10 | 80620 | 11410 | 69170 | 35673 | 14184 | 0.39 |
| executor | google/gemini-3.8-flash@medium | 10 | 58140 | 0 | 0 | 48921 | 33213 | 0.23 |
| executor | openai/gpt-6.1-sol@medium | 10 | 54210 | 54180 | 0 | 17492 | 4770 | 0.31 |
| executor | perplexity/glm-5.3-flash@medium | 10 | 44588 | 0 | 5888 | 37377 | 24033 | 0.02 |
| executor | perplexity/kimi-k3@low | 10 | 12422 | 0 | 128 | 31394 | 0 | 0.51 |
| executor | xai/grok-4.7@low | 10 | 30118 | 0 | 4608 | 43733 | 36282 | 0.32 |
| judge | anthropic/claude-opus-5-5@high | 30 | 417884 | 417764 | 0 | 82566 | 50280 | 3.74 |
| judge | google/gemini-4-argon@high | 16 | 148333 | 0 | 0 | 48694 | 39151 | 0.78 |
| judge | openai/gpt-6-astra@high | 28 | 229358 | 121676 | 107604 | 65715 | 49094 | 4.92 |
| judge | perplexity/glm-5.3@high | 8 | 71720 | 0 | 25728 | 23924 | 16298 | 0.18 |
| judge | perplexity/kimi-k3@high | 2 | 22706 | 0 | 128 | 10093 | 0 | 0.22 |
| judge | xai/grok-4.7@high | 4 | 23946 | 0 | 2304 | 36981 | 35890 | 0.27 |

## Human test

Score these responses in human-test.csv, then run `bin/run-evaluation.py --agreement` on this folder.

- responses/anthropic_claude-sonnet-5-5@medium/C1-s2.md: random sample
- responses/anthropic_claude-sonnet-5-5@medium/X2-s1.md: a judge failed a gate
- responses/google_gemini-3.8-flash@medium/H2-s2.md: judges differ by more than 3 points
- responses/google_gemini-3.8-flash@medium/K1-s2.md: judges differ by more than 3 points
- responses/google_gemini-3.8-flash@medium/T2-s1.md: a judge failed a gate
- responses/google_gemini-3.8-flash@medium/T2-s2.md: a judge failed a gate
- responses/google_gemini-3.8-flash@medium/X2-s1.md: a judge failed a gate
- responses/google_gemini-3.8-flash@medium/X2-s2.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/K1-s1.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/K1-s2.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/T2-s1.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/T2-s2.md: a judge failed a gate
- responses/openai_gpt-6.1-sol@medium/X2-s2.md: a judge failed a gate
- responses/perplexity_glm-5.3-flash@medium/K1-s2.md: judges differ by more than 3 points
- responses/perplexity_glm-5.3-flash@medium/X2-s1.md: judges differ by more than 3 points
- responses/perplexity_glm-5.3-flash@medium/X2-s2.md: judges differ by more than 3 points
- responses/xai_grok-4.7@low/C1-s1.md: random sample

## Failed calls

- moonshot: K1-s2 executor perplexity/kimi-k3: HTTP 401: {"error":{"message":"You exceeded your current quota, add credits at https://console.perplexity.ai/project/billing.","type":"insufficient_quota","code":401}}

- moonshot: X2-s1 executor perplexity/kimi-k3: HTTP 401: {"error":{"message":"You exceeded your current quota, add credits at https://console.perplexity.ai/project/billing.","type":"insufficient_quota","code":401}}

- moonshot: X2-s2 executor perplexity/kimi-k3: HTTP 401: {"error":{"message":"You exceeded your current quota, add credits at https://console.perplexity.ai/project/billing.","type":"insufficient_quota","code":401}}

- moonshot: H2-s1 executor perplexity/kimi-k3: HTTP 401: {"error":{"message":"You exceeded your current quota, add credits at https://console.perplexity.ai/project/billing.","type":"insufficient_quota","code":401}}

- moonshot: K1-s1 executor perplexity/kimi-k3: HTTP 401: {"error":{"message":"You exceeded your current quota, add credits at https://console.perplexity.ai/project/billing.","type":"insufficient_quota","code":401}}

- moonshot: H2-s2 executor perplexity/kimi-k3: HTTP 401: {"error":{"message":"You exceeded your current quota, add credits at https://console.perplexity.ai/project/billing.","type":"insufficient_quota","code":401}}

- moonshot: T2-s1 executor perplexity/kimi-k3: HTTP 401: {"error":{"message":"You exceeded your current quota, add credits at https://console.perplexity.ai/project/billing.","type":"insufficient_quota","code":401}}

- moonshot: T2-s2 executor perplexity/kimi-k3: HTTP 401: {"error":{"message":"You exceeded your current quota, add credits at https://console.perplexity.ai/project/billing.","type":"insufficient_quota","code":401}}

- xai: K1-s1 judge xai/grok-4.7: HTTP 401: {"error":{"message":"You exceeded your current quota, add credits at https://console.perplexity.ai/project/billing.","type":"insufficient_quota","code":401}}

- xai: K1-s1 judge google/gemini-4-argon: HTTP 401: {"error":{"message":"You exceeded your current quota, add credits at https://console.perplexity.ai/project/billing.","type":"insufficient_quota","code":401}}

- xai: X2-s1 executor xai/grok-4.7: HTTP 401: {"error":{"message":"You exceeded your current quota, add credits at https://console.perplexity.ai/project/billing.","type":"insufficient_quota","code":401}}

- xai: X2-s2 executor xai/grok-4.7: HTTP 401: {"error":{"message":"You exceeded your current quota, add credits at https://console.perplexity.ai/project/billing.","type":"insufficient_quota","code":401}}

- xai: H2-s1 executor xai/grok-4.7: HTTP 401: {"error":{"message":"You exceeded your current quota, add credits at https://console.perplexity.ai/project/billing.","type":"insufficient_quota","code":401}}

- xai: K1-s2 judge xai/grok-4.7: HTTP 401: {"error":{"message":"You exceeded your current quota, add credits at https://console.perplexity.ai/project/billing.","type":"insufficient_quota","code":401}}

- xai: K1-s2 judge google/gemini-4-argon: HTTP 401: {"error":{"message":"You exceeded your current quota, add credits at https://console.perplexity.ai/project/billing.","type":"insufficient_quota","code":401}}

- xai: H2-s2 executor xai/grok-4.7: HTTP 401: {"error":{"message":"You exceeded your current quota, add credits at https://console.perplexity.ai/project/billing.","type":"insufficient_quota","code":401}}

- xai: T2-s1 executor xai/grok-4.7: HTTP 401: {"error":{"message":"You exceeded your current quota, add credits at https://console.perplexity.ai/project/billing.","type":"insufficient_quota","code":401}}

- xai: T2-s2 executor xai/grok-4.7: HTTP 401: {"error":{"message":"You exceeded your current quota, add credits at https://console.perplexity.ai/project/billing.","type":"insufficient_quota","code":401}}

- zai: H2-s2 judge openai/gpt-6-astra: failed: Your API Project has insufficient API credits. Add API credits at https://www.perplexity.ai/account/api/billing
- zai: T2-s1 executor perplexity/glm-5.3-flash: HTTP 402: {"error":{"message":"Your API Project has insufficient API credits. Add API credits at https://www.perplexity.ai/account/api/billing","type":"payment_required","code":402}}

- zai: T2-s2 executor perplexity/glm-5.3-flash: failed: Your API Project has insufficient API credits. Add API credits at https://www.perplexity.ai/account/api/billing
- zai: H2-s1 judge openai/gpt-6-astra: HTTP 402: {"error":{"message":"Your API Project has insufficient API credits. Add API credits at https://www.perplexity.ai/account/api/billing","type":"payment_required","code":402}}

