# results/

One folder for each evaluation run, named by its run ID. `task eval` writes each folder here. A run folder holds:

- `results/`: one JSONL file for each provider, with each score, call and failed call.
- `summary.md`, `scores.csv`, `calls.csv` and `human-test.csv`: the merged view of the run.
- `responses/`: the answers, one file for each prompt and sample.
- `judgments/`: the JSON of each judge.

A response that you score by hand, without `task eval`, goes in `<model>/<prompt-id>.md`. Its first line is `<model>, <provider>, <date>, <prompt-id>`. Paste the response unchanged below that line. Scores go in evaluation-results.md and evaluation-scores.csv.
