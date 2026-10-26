# How to record an evaluation run

Use this page after a model answers the prompts of `tests/evaluation/evaluation-tests.md`. Each file of this page is in `tests/evaluation/`, and each command runs from the root of the repository. When the run comes from `task eval`, the folder `.eval/<run>/` already holds the answers, the check reports, the judge scores and your human test. The [run an evaluation](run-an-evaluation.md) page explains them.

1. Save each raw response as `results/<model>/<prompt-id>.md`, for example `results/model-a/K1.md`. From `task eval`, copy them from `responses/`.
2. Run `python3 bin/deterministic-tests.py --check` on each response. `task eval` did this already.
3. Ask two graders to score each response with the rubric in Section 3 of `evaluation-tests.md`. Each grader works alone. From `task eval`, the two judges are the graders, and your human test checks them.
4. Add one row for each prompt and each grader to `evaluation-scores.csv`. From `task eval`, copy the rows of `scores.csv`.
5. Copy the run template of `evaluation-results.md`. Fill in one table for the model and the date. It holds the criterion scores, both totals, the gates and the pass. Add one line on the main defect.
6. Update the cross-model summary table at the top of `evaluation-results.md`. It is the comparison view.
7. Copy the summary row into the results table of [evaluation](../reference/evaluation.md).

A gap of more than 3 points between the two graders means that the expected signals of the prompt need a change. It does not mean that the model failed.
