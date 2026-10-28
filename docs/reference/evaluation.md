# Evaluation

The classifications in Sections 6.4 and 6.5 are judgments. Judgments need evaluative tests (rules file, 6.4). `tests/evaluation/evaluation-tests.md` holds the prompts and the rubric. `tests/evaluation/evaluation-results.md` holds the runs. The steps to record a run are in [record an evaluation run](../how-to/record-an-evaluation-run.md).

## Prompts

Thirteen prompts, in `evaluation-tests.md` Section 1. Two per Cynefin domain (one software, one not), and three worded to invite a wrong classification. Each prompt states the expected domain and the action form that Section 6.5 requires. It also states what the response should contain and should not contain. Where one exists, it states the likely wrong answer.

| ID         | Domain            | Ask, in short                                                                                    |
| ---------- | ----------------- | ------------------------------------------------------------------------------------------------ |
| C1, C2     | Clear             | Replace print with logging; format a reference list                                              |
| K1, K2     | Complicated       | Diagnose a latency rise from attached traces; pick one of three vendor proposals                 |
| X1, X2     | Complex           | Improve an LLM summariser with no metrics; revive retrospectives that change nothing             |
| H1, H2     | Chaotic           | Checkout is down, ten minutes to the exec call; a public statement has been called false         |
| U1, U2     | Confused          | "The build is flaky"; "something is off in the Q3 numbers"                                       |
| T1, T2, T3 | Worded to mislead | A Clear task worded as culture; a Complex task worded as "the best prompt"; a mixed ask to split |

## Rubric

In `evaluation-tests.md` Section 3. Nine criteria, each scored 0, 1, or 2.

| ID  | Criterion                                                                                                 | Gate |
| --- | --------------------------------------------------------------------------------------------------------- | ---- |
| R1  | Domain stated for every action                                                                            | yes  |
| R2  | Domain is correct                                                                                         | yes  |
| R3  | Action form matches the domain (one step, analysis first, capped probe, stabiliser first, classify first) | yes  |
| R4  | Ordering follows the 6.5 trade-off rules                                                                  | no   |
| R5  | Test form matches the task kind (Gherkin, rubric, or metric with sample size)                             | yes  |
| R6  | Wrong classification avoided (five prompts only)                                                          | yes  |
| R7  | Questions per Section 2                                                                                   | no   |
| R8  | Uncertainty calibrated                                                                                    | no   |
| R9  | Rules-file conformance of the whole response                                                              | no   |

Pass: 80 percent of available points (18, or 16 without R6) and every gate at 1 or more. Two graders score each response independently. A gap over 3 points means the prompt's expected signals need revision, not the model.

## Executors and judges

`bin/run-evaluation.py` sends the prompts through the Perplexity Agent API. `tests/evaluation/pairs.json` sets the pairs. In each pair, the judge reasons more than the executor. The judge is a model higher in the order of its provider, or the same model at a higher effort. A second judge from another provider scores each answer too. So the two graders of the rubric are two models, and a model does not grade only the work of its own provider.

The order of the models in each provider follows the price per million tokens on the models page of Perplexity, on 2026-10-26. That order is a judgment \[judgment\]: Perplexity does not publish a rank of reasoning.

| Provider  | Order, highest first                       | Main pair: executor, judge                       | Second judge   |
| --------- | ------------------------------------------ | ------------------------------------------------ | -------------- |
| Anthropic | Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5 | Sonnet 5.5 (medium), Opus 5.5 (high)             | GPT-6 Astra    |
| OpenAI    | GPT-6 Astra, GPT-6.1 Sol, GPT-6 Luna       | GPT-6.1 Sol (medium), GPT-6 Astra (high)         | Opus 5.5       |
| Google    | Gemini 4 Argon, Gemini 3.8 Flash           | Gemini 3.8 Flash (medium), Gemini 4 Argon (high) | Opus 5.5       |
| Moonshot  | Kimi K3                                    | Kimi K3 (low), Kimi K3 (high)                    | Gemini 4 Argon |
| Z.AI      | GLM 5.3, GLM 5.3 Flash                     | GLM 5.3 Flash (medium), GLM 5.3 (high)           | GPT-6 Astra    |
| xAI       | Grok 4.7                                   | Grok 4.7 (low), Grok 4.7 (high)                  | Gemini 4 Argon |

Anthropic and OpenAI have more pairs, which `ALL_PAIRS=true` runs. A pair of one model at two efforts is valid only when the API uses the effort. Run `task eval:probe` to see the effort in `calls.csv` before a full run. Through Perplexity, Kimi K3 takes the efforts up to `high` and refuses `xhigh` and `max`.

The judges return their scores in a JSON schema. Anthropic models refuse a schema with `minimum` or `maximum`, and Gemini models refuse a schema with `enum`. So the schema allows any integer, and `bin/run-evaluation.py` refuses a score that is not 0, 1, 2 or null.

The judges check. They do not test. Each run lists answers for a human test. The list holds each answer where the judges differ by more than 3 points or a gate failed, and two more at random. The human scores show how far each judge can be trusted on each criterion.

## Results

No run has been recorded. When the first run is in, copy the cross-model summary row here.

| Model | Provider | Rules version | Date | Pass (of 13) | Mean score | Lowest criterion |
| ----- | -------- | ------------- | ---- | ------------ | ---------- | ---------------- |
|       |          |               |      |              |            |                  |

The criterion with the lowest mean across all models names the rule to fix first in the rules file.
