# Cost

The rules file is about 3,950 tokens (2,850 words). Every request sends it as input. Prompt caching, where the provider offers it, cuts the cost of resending it but does not remove it from the context window.

- Rules, Sections 0 to 8: about 3,500 tokens.
- References list: about 350 tokens. Section 5.4 requires it.

Output cost: Section 3 adds Background, Relevance, and the self-test block to every response. The self-test block alone is about 180 output tokens. The four fields per action in Section 6.3 and the one-citation-per-line rule in 5.4 add lines too. Output tokens are not cached and cost more per token than input on every major provider.

Caveat: these counts are estimates from word and character counts (one token per 4 characters, or 1.35 tokens per word). The tokenizer was not reachable at the time. Real counts differ by provider by around 10 percent. To get an exact count, run the file through the provider's token counter.
