# How to record an evaluation run

Use this page after a model answers the prompts of `tests/evaluation/evaluation-tests.md`. Each file of this page is in `tests/evaluation/`, and each command runs from the root of the repository. When the run comes from `task eval`, the folder `tests/evaluation/results/<run>/` already holds the answers, the check reports, the judge scores and your human test. The [run an evaluation](run-an-evaluation.md) page explains them.

1. Save each raw response as `results/<model>/<prompt-id>.md`, for example `results/model-a/K1.md`. From `task eval`, skip this step: the run folder holds them in `responses/`.
2. Run `python3 bin/deterministic-tests.py --check` on each response. `task eval` did this already.
3. Ask two graders to score each response with the rubric in Section 3 of `evaluation-tests.md`. Each grader works alone. From `task eval`, the two judges are the graders, and your human test checks them.
4. From `task eval`, run `task eval:record`, and skip steps 5 to 7. It writes the rows of steps 5 to 7 from the `scores.csv` of every run folder. When a run combines partial runs, list their folders in its `combined-from.txt`, one on each line, so that their scores count once.
5. Add one row for each prompt and each grader to `evaluation-scores.csv`.
6. Copy the run template of `evaluation-results.md`. Fill in one table for the model and the run. It holds the criterion scores, both totals, the gates and the pass. Add one line on the main defect.
7. Update the cross-model summary table at the top of `evaluation-results.md`, and the results table of [evaluation](../reference/evaluation.md).

A gap of more than 3 points between the two graders means that the expected signals of the prompt need a change. It does not mean that the model failed.
