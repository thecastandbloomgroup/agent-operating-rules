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

To add the run to the record of all runs in `evaluation-results.md`, `evaluation-scores.csv` and the [evaluation reference](../reference/evaluation.md):

```sh
task eval:record
```

## Run the psychomotor prompts

The psychomotor prompts need tools, so `bin/run-psychomotor.py` runs them, not `task eval`:

```sh
doppler run --only-secrets PERPLEXITY_TOKEN -- \
  python3 bin/run-psychomotor.py --samples 3 --run-id <run>
```

Use `--plan` to see the cost first, and `--prompts P1,P2` to send fewer prompts. Grade the run with `bin/check-psychomotor.py tests/evaluation/results/<run>`. It writes `tool-checks.csv`, which `bin/ladder-scores.py` reads as the psychomotor trials. The [psychomotor tests](../../tests/evaluation/psychomotor-tests.md) page gives the prompts and the checks.

Each unit stops after 12 tool steps, and P7 after 20, because it works on four files. Three options change a unit, and each one stays off by default, so runs stay comparable:

| Option           | What it changes                                                     | Result                                                                                                                                                           |
| ---------------- | ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--check-text`   | Adds `check_text`, a check of a text that writes no file            | It cost Sonnet passes on P5 ([check text results](../../tests/evaluation/results/2026-11-06-check-text-results.md))                                              |
| `--sandbox-note` | Adds a note after the prompt: the sandbox holds the task files only | It ends the Gemini loop at the cap, but it names a fail of P2 and P5 ([sandbox note results](../../tests/evaluation/results/2026-11-06-sandbox-note-results.md)) |
| `--answer-note`  | Adds only a note that the answer goes in the reply                  | It does not end the loop, and it cost Sonnet passes on P5 ([answer note results](../../tests/evaluation/results/2026-11-06-answer-note-results.md))              |

When the API refuses units, for example for lack of credits, add credits first. Then run `bin/run-psychomotor.py --rerun-failed tests/evaluation/results/<run>`. It runs again, in place, only the units with an HTTP 401 or 402 error, and it keeps every other unit.

After the grade, `bin/judge-procedures.py tests/evaluation/results/<run>` has a judge score the procedure of each passed P7 unit. It writes `procedure-checks.csv`. A procedure passes at 85 of 100 or more, with no criterion at 0.

## Check the domain of the actions

`bin/judge-actions.py tests/evaluation/results/<run>` samples 40 labelled actions of a run. A judge of another provider than the executor checks the domain and the reason of each, and the script writes `action-checks.csv`. Each call shows the judge the expected answer of the test, so its domain rate measures fit to the test.

Add `--work tests/evaluation/results/2026-11-05-human-marking` to measure fit to the work in place of fit to the test. Then each call has no expected answer, and the 24 marks of the user come as examples. The script `bin/judge-loo.py` tests a judge against a marking sheet, with each row held out once. The [evaluations page](../explanation/what-the-evaluations-show.md) gives how far each judge matches the user.

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
