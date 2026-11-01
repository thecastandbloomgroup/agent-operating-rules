# Evaluation run 2026-11-01-split-first

| Executor | Judge | Responses | Pass | Mean total | Lowest criterion |
| -------- | ----- | --------- | ---- | ---------- | ---------------- |

Calls: 198, 70 failed. Cost: 4.49 USD.

## Tokens and cost

| Role | Model | Calls | Input | Cache write | Cache read | Output | Reasoning | Cost USD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| executor | anthropic/claude-sonnet-5-5@medium | 39 | 307035 | 41555 | 265324 | 163856 | 80275 | 1.77 |
| executor | google/gemini-3.8-flash@medium | 39 | 0 | 0 | 0 | 0 | 0 | 0.00 |
| executor | openai/gpt-6.1-sol@medium | 39 | 70674 | 70638 | 0 | 24762 | 6831 | 0.42 |
| executor | perplexity/glm-5.3-flash@medium | 39 | 207684 | 0 | 140416 | 198932 | 136873 | 0.11 |
| executor | perplexity/kimi-k3@low | 39 | 186167 | 0 | 100672 | 117325 | 10267 | 2.05 |
| executor | xai/grok-4.7@low | 3 | 21811 | 0 | 9856 | 17591 | 12150 | 0.13 |

## Human test

Score these responses in human-test.csv, then run `bin/run-evaluation.py --agreement` on this folder.

- none

## Failed calls

- google: C1-s1 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: C1-s2 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: C1-s3 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: C2-s1 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: C2-s2 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: K1-s1 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: C2-s3 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: K1-s2 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: K1-s3 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: K2-s1 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: K2-s2 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: K2-s3 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: X1-s1 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: X1-s2 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: X1-s3 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: X2-s2 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: X2-s3 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: H1-s1 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: X2-s1 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: H1-s2 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: H1-s3 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: H2-s3 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: H2-s1 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: U1-s1 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: H2-s2 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: U1-s2 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: U1-s3 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: U2-s1 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: U2-s2 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: U2-s3 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: T1-s1 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: T1-s2 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: T1-s3 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: T2-s3 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: T2-s2 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: T2-s1 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: T3-s1 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: T3-s2 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- google: T3-s3 executor google/gemini-3.8-flash: no connection: [Errno 8] nodename nor servname provided, or not known
- moonshot: C1-s1 executor perplexity/kimi-k3: no connection: [Errno 8] nodename nor servname provided, or not known
- moonshot: C1-s2 executor perplexity/kimi-k3: no connection: [Errno 8] nodename nor servname provided, or not known
- moonshot: C1-s3 executor perplexity/kimi-k3: no connection: [Errno 8] nodename nor servname provided, or not known
- moonshot: C2-s1 executor perplexity/kimi-k3: no connection: [Errno 8] nodename nor servname provided, or not known
- openai: X1-s1 executor openai/gpt-6.1-sol: no connection: [Errno 8] nodename nor servname provided, or not known
- openai: X1-s2 executor openai/gpt-6.1-sol: no connection: [Errno 8] nodename nor servname provided, or not known
- openai: X1-s3 executor openai/gpt-6.1-sol: no connection: [Errno 8] nodename nor servname provided, or not known
- openai: X2-s1 executor openai/gpt-6.1-sol: no connection: [Errno 8] nodename nor servname provided, or not known
- openai: X2-s2 executor openai/gpt-6.1-sol: no connection: [Errno 8] nodename nor servname provided, or not known
- openai: X2-s3 executor openai/gpt-6.1-sol: no connection: [Errno 8] nodename nor servname provided, or not known
- openai: H1-s1 executor openai/gpt-6.1-sol: no connection: [Errno 8] nodename nor servname provided, or not known
- openai: H1-s2 executor openai/gpt-6.1-sol: no connection: [Errno 8] nodename nor servname provided, or not known
- openai: H1-s3 executor openai/gpt-6.1-sol: no connection: [Errno 8] nodename nor servname provided, or not known
- openai: H2-s1 executor openai/gpt-6.1-sol: no connection: [Errno 8] nodename nor servname provided, or not known
- openai: H2-s2 executor openai/gpt-6.1-sol: no connection: [Errno 8] nodename nor servname provided, or not known
- openai: H2-s3 executor openai/gpt-6.1-sol: no connection: [Errno 8] nodename nor servname provided, or not known
- openai: U1-s1 executor openai/gpt-6.1-sol: no connection: [Errno 8] nodename nor servname provided, or not known
- openai: U1-s2 executor openai/gpt-6.1-sol: no connection: [Errno 8] nodename nor servname provided, or not known
- openai: U1-s3 executor openai/gpt-6.1-sol: no connection: [Errno 8] nodename nor servname provided, or not known
- openai: U2-s1 executor openai/gpt-6.1-sol: no connection: [Errno 8] nodename nor servname provided, or not known
- openai: U2-s2 executor openai/gpt-6.1-sol: no connection: [Errno 8] nodename nor servname provided, or not known
- openai: U2-s3 executor openai/gpt-6.1-sol: no connection: [Errno 8] nodename nor servname provided, or not known
- openai: T1-s1 executor openai/gpt-6.1-sol: no connection: [Errno 8] nodename nor servname provided, or not known
- openai: T1-s3 executor openai/gpt-6.1-sol: no connection: [Errno 8] nodename nor servname provided, or not known
- openai: T1-s2 executor openai/gpt-6.1-sol: no connection: [Errno 8] nodename nor servname provided, or not known
- openai: T2-s1 executor openai/gpt-6.1-sol: no connection: [Errno 8] nodename nor servname provided, or not known
- openai: T2-s2 executor openai/gpt-6.1-sol: no connection: [Errno 8] nodename nor servname provided, or not known
- openai: T2-s3 executor openai/gpt-6.1-sol: no connection: [Errno 8] nodename nor servname provided, or not known
- openai: T3-s1 executor openai/gpt-6.1-sol: no connection: [Errno 8] nodename nor servname provided, or not known
- openai: T3-s3 executor openai/gpt-6.1-sol: no connection: [Errno 8] nodename nor servname provided, or not known
- openai: T3-s2 executor openai/gpt-6.1-sol: no connection: [Errno 8] nodename nor servname provided, or not known
