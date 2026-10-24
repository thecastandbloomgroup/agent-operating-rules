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

## Results

No run has been recorded. When the first run is in, copy the cross-model summary row here.

| Model | Provider | Rules version | Date | Pass (of 13) | Mean score | Lowest criterion |
| ----- | -------- | ------------- | ---- | ------------ | ---------- | ---------------- |
|       |          |               |      |              |            |                  |

The criterion with the lowest mean across all models names the rule to fix first in the rules file.
