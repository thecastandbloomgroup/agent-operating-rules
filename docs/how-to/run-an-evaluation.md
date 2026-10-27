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

## Run on your machine

1. Send prompt C1 one time through each main pair. This shows that each model answers and each judge returns its scores:

   ```sh
   doppler run --only-secrets PERPLEXITY_TOKEN -- task eval:probe
   ```

2. Run all the prompts for one provider, three times each:

   ```sh
   doppler run --only-secrets PERPLEXITY_TOKEN -- task eval PROVIDER=anthropic
   ```

Use `PROMPTS=C1,K1` to send fewer prompts, `SAMPLES=1` to send each prompt one time, and `ALL_PAIRS=true` to add the pairs that are not main.

## Run in GitLab

1. Open **Build**, then **Pipelines**, and open a pipeline of `main`.
2. In the stage **evaluate**, select the job of one provider, for example `evaluate: [anthropic]`.
3. Add job variables when you need them: `SAMPLES` and `PROMPTS`. Then select **Run job**.
4. When the job ends, download its artifact. It holds the folder `.eval/` for 3 months.

A pipeline schedule on `main` runs all six jobs. A full run of all six providers costs about 95 USD, so add a schedule only when you plan to read each run.

## Read a run

Each run makes one folder in `.eval/`:

| File             | Content                                                                      |
| ---------------- | ---------------------------------------------------------------------------- |
| `summary.md`     | Pass count, mean score and lowest criterion of each pair and judge           |
| `scores.csv`     | One row for each answer and judge, in the columns of `evaluation-scores.csv` |
| `calls.csv`      | Model, effort, tokens, cost and time of each call                            |
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
python3 bin/run-evaluation.py --agreement .eval/<run>
```

The command prints, for each judge, the mean gap between its total and yours. It also prints how often it gave your score on each criterion. When a judge often gives a different score from yours on a criterion, do not use its scores on that criterion. When you and both judges disagree with the expected answer of a prompt, change the prompt, as Section 5 of `evaluation-tests.md` says.

## Keep the result

The folder `.eval/` is not in git. To keep a run, follow the [record an evaluation run](record-an-evaluation-run.md) page, and merge the result through a merge request.
