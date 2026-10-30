# How to run an evaluation

A run sends the prompts of `tests/evaluation/evaluation-tests.md` to models through the Perplexity Agent API. Each run has four steps:

1. An executor answers each prompt, with the rules file as its system prompt.
2. `bin/deterministic-tests.py --check` checks each answer.
3. Two judges score each answer with the rubric. The first judge is a stronger model of the same provider. The second judge is a model of another provider.
4. You test a part of the answers, and you compare your scores with the judges.

The judges check the answers against the rubric. They do not test. Only the fourth step is a test, so a run is not complete without it.

## Before you start

Set up Doppler as the [Doppler setup](set-up-doppler-for-evaluation.md) page shows. The pairs of executor and judge are in `tests/evaluation/pairs.json`. The [evaluation](../reference/evaluation.md) page lists them.

## See the cost first

```sh
task eval:plan PROVIDER=anthropic
```

The task prints each call and an estimate of the cost. It calls no API. Each real call logs its real cost in `calls.csv`.

## How a run works

Each provider runs in its own process, at the same time as the others. Each process adds its results to `tests/evaluation/results/<run>/results/<provider>.jsonl` as soon as it has them. Each line of the file is one score, one call or one failed call. A failed call is a line of the file, so it does not stop the other providers.

Each call runs in the background mode of the Agent API. The API answers at once with an ID, and the runner asks for the result every 5 seconds until the call ends. So no connection stays open while a model reasons.

When the providers end, `task eval:merge` reads all the JSONL files of the run. It writes the final view: `summary.md`, `scores.csv`, `calls.csv` and `human-test.csv`. The merge calls no API, so you can run it again at any time.

## Run on your machine

The key is in `pass` as `perplexity-token`, or in Doppler.

1. Send prompt C1 one time through each main pair. This shows that each model answers and each judge returns its scores:

   ```sh
   PERPLEXITY_TOKEN="$(pass show perplexity-token | head -1)" task eval:probe
   ```

2. Run all the prompts of all the providers, three times each:

   ```sh
   PERPLEXITY_TOKEN="$(pass show perplexity-token | head -1)" task eval
   ```

With Doppler, start each command with `doppler run --only-secrets PERPLEXITY_TOKEN --` in place of the `PERPLEXITY_TOKEN=` part.

Use `PROVIDER=anthropic` to run one provider, and `PROMPTS=C1,K1` to send fewer prompts. Use `SAMPLES=1` to send each prompt one time, and `ALL_PAIRS=true` to add the pairs that are not main. `RUN=<name>` names the run folder. Without it, the folder name is the UTC time.

To merge a run again, for example after you remove a JSONL file:

```sh
task eval:merge RUN=<run>
```

## Run in GitLab

1. Open **Build**, then **Pipelines**, and open a pipeline of `main`.
2. In the stage **evaluate**, start the job of each provider that you want, for example `evaluate: [anthropic]`. Add job variables when you need them: `SAMPLES`, `PROMPTS` and `ALL_PAIRS`. Then select **Run job**. The jobs run at the same time.
3. When the provider jobs end, start the job `evaluate:report` in the stage **report**. It merges the JSONL files of all the provider jobs of the pipeline.
4. Download the artifact of `evaluate:report`. It holds the final view in `tests/evaluation/results/pipeline-<ID>/` for 3 months.

If you start one more provider job later, start `evaluate:report` again. A pipeline schedule on `main` runs all six provider jobs, then the report. A full run of all six providers costs about 95 USD, so add a schedule only when you plan to read each run.

## Read a run

Each run makes one folder in `tests/evaluation/results/`:

| File             | Content                                                                      |
| ---------------- | ---------------------------------------------------------------------------- |
| `results/`       | One JSONL file for each provider: each score, call and failed call           |
| `summary.md`     | Pass count, mean score, lowest criterion, and the tokens and cost of a model |
| `scores.csv`     | One row for each answer and judge, in the columns of `evaluation-scores.csv` |
| `calls.csv`      | Provider, status, model, effort, tokens with cache, cost and time of a call  |
| `human-test.csv` | The answers that you must score                                              |
| `responses/`     | The answers, one file for each prompt and sample                             |
| `judgments/`     | The JSON of each judge, with the evidence for each score                     |

## Do the human test

`human-test.csv` lists three kinds of answer:

- Answers where the two judges differ by more than 3 points.
- Answers where a judge scored a gate below 1.
- Two more answers, picked at random.

For each answer, read the response and the rubric. Fill in R1 to R9, `total`, `available`, `gates_passed`, `pass` and `main_defect`. Do not read the judgments first. Then compare your scores with the judges:

```sh
python3 bin/run-evaluation.py --agreement tests/evaluation/results/<run>
```

The command prints, for each judge, the mean gap between its total and yours. It also prints how often it gave your score on each criterion. When a judge often gives a different score from yours on a criterion, do not use its scores on that criterion. When you and both judges disagree with the expected answer of a prompt, change the prompt, as Section 6 of `evaluation-tests.md` says. Log the change in its Section 5.

## Keep the result

Each run folder is in `tests/evaluation/results/`, which is in git. To keep a run, commit its folder on a branch, follow the [record an evaluation run](record-an-evaluation-run.md) page, and merge the result through a merge request. To drop a run, delete its folder.
