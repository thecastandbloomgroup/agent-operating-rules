# Evaluation Results

Companion to evaluation-tests.md (prompts and rubric) and model-operating-rules.md v2.1. This file holds the runs. Add one run block per model per date. Raw responses go in `results/<model>/<prompt-id>.md`, one file per response, so this log stays readable.

## How to record a run

1. Copy the "Run template" block below. Fill the header.
2. For each prompt, paste the response into `results/<model>/<prompt-id>.md`. Put the model name, date, and prompt ID on the first line of that file.
3. Score with the rubric in evaluation-tests.md, Section 3. Two graders, independently. Enter both scores.
4. Enter the same scores in evaluation-scores.csv, one row per prompt per grader. The CSV is the source for any chart or summary.
5. Mark pass or fail: 80 percent of available points, and every gate at 1 or more.
6. Write one line per prompt on the main defect. Write three lines at the end: the lowest-scoring criterion, the rule in the rules file it points to, and the change you intend.

Gate criteria: R1, R2, R3, R5, R6. Available points: 18 for prompts with an R6 line (K1, X1, T1, T2, T3), 16 for the rest.

## Cross-model summary

Fill one row per model after each full run. Mean score is over the 13 prompts, grader A and B averaged.

| Model | Provider | Rules version | Date | Pass (of 13) | Mean score | Lowest criterion | Grader gap over 3 (count) | Notes |
| ----- | -------- | ------------- | ---- | ------------ | ---------- | ---------------- | ------------------------- | ----- |
|       |          | 2.1           |      |              |            |                  |                           |       |
|       |          | 2.1           |      |              |            |                  |                           |       |
|       |          | 2.1           |      |              |            |                  |                           |       |
|       |          | 2.1           |      |              |            |                  |                           |       |

## Run template

Copy from here to the end of the block.

______________________________________________________________________

### Run: `<model name>`, `<provider>`, `<date>`

Rules version: 2.1. Temperature or reasoning setting: `<value>`. Grader A: `<name>`. Grader B: `<name>`. Responses: `results/<model>/`.

| Prompt | Domain                 | A: R1 | R2  | R3  | R4  | R5  | R6  | R7  | R8  | R9  | A total | B total | Gates | Pass | Main defect |
| ------ | ---------------------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ----- | ---- | ----------- |
| C1     | Clear                  |       |     |     |     |     | n/a |     |     |     | /16     | /16     |       |      |             |
| C2     | Clear                  |       |     |     |     |     | n/a |     |     |     | /16     | /16     |       |      |             |
| K1     | Complicated            |       |     |     |     |     |     |     |     |     | /18     | /18     |       |      |             |
| K2     | Complicated            |       |     |     |     |     | n/a |     |     |     | /16     | /16     |       |      |             |
| X1     | Complex                |       |     |     |     |     |     |     |     |     | /18     | /18     |       |      |             |
| X2     | Complex                |       |     |     |     |     | n/a |     |     |     | /16     | /16     |       |      |             |
| H1     | Chaotic                |       |     |     |     |     | n/a |     |     |     | /16     | /16     |       |      |             |
| H2     | Chaotic                |       |     |     |     |     | n/a |     |     |     | /16     | /16     |       |      |             |
| U1     | Confused               |       |     |     |     |     | n/a |     |     |     | /16     | /16     |       |      |             |
| U2     | Confused               |       |     |     |     |     | n/a |     |     |     | /16     | /16     |       |      |             |
| T1     | Clear (worded Complex) |       |     |     |     |     |     |     |     |     | /18     | /18     |       |      |             |
| T2     | Complex (worded Clear) |       |     |     |     |     |     |     |     |     | /18     | /18     |       |      |             |
| T3     | Mixed                  |       |     |     |     |     |     |     |     |     | /18     | /18     |       |      |             |

The table shows grader A's criterion scores. Grader B's criterion scores go in the CSV. Enter both totals here.

Lowest-scoring criterion: `<R-id>`, mean `<n>`.
Rule it points to: `<section in model-operating-rules.md>`.
Change intended: `<one sentence>`.

Deterministic tests on the responses: from the root of the repository, run `python3 bin/deterministic-tests.py tests/evaluation/results/<model>/<prompt-id>.md` on each response. Record the count of responses with zero banned words and zero dashes: `<n>` of 13.

______________________________________________________________________

## Runs

(Add runs below this line, newest first.)
