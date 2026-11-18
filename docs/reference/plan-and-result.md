# Plan and result files

A plan of an evaluation keeps its marks in a `plan.json` file next to the plan page. The file is committed before the first paid call. It never changes after that. `bin/score-arms.py` reads it, scores two run folders, and writes `result.json`. So another repository, such as the starter kit, can read the marks and the result as data.

```sh
python3 bin/score-arms.py PLAN_JSON [--control DIR] [--candidate DIR] [--out FILE]
```

The run folders default to `control.run` and `candidate.run` of the plan. The result goes next to the plan when `--out` is left out. The script exits with 1 when a mark fails.

## The plan file

| Field                  | Meaning                                                                                |
| ---------------------- | -------------------------------------------------------------------------------------- |
| `plan`                 | The plan page that the file belongs to.                                                |
| `added_later`          | Present only when the file was written after the run. It says when and why.            |
| `control`, `candidate` | The rules file of each arm, and its run folder in `run`. The control can name a `tag`. |
| `sample`               | The prompts, the samples for each prompt, `answers_per_arm`, and `judge`.              |
| `marks`                | The list of marks. The candidate passes only when every mark passes.                   |
| `interval`             | The interval that the result reports.                                                  |

Each mark has an `id`, a `metric`, a `compare`, and one threshold.

| `id`          | `compare` | Threshold           | Passes when                                                                         |
| ------------- | --------- | ------------------- | ----------------------------------------------------------------------------------- |
| `false-lines` | `fall`    | `threshold_points`  | The share of answers with a wrong self-test line falls by this many points or more. |
| `tokens`      | `fall`    | `threshold_percent` | The mean input tokens for each call fall by this percent or more.                   |
| `cost`        | `below`   | `threshold_usd`     | The cost is under this many USD. `arms` is `both`, the default, or `candidate`.     |
| any other     | `within`  | `threshold_points`  | Each column in `metric` stays within this many points of the control.               |

A `within` mark lists columns of `script-checks.csv`. The count columns `banned`, `dashes`, `first_person` and `long` pass when the count is 0. The other columns pass when they are `True`.

## The result file

The result repeats each mark and adds `measures` and `pass`. A rate measure gives the rate, the answer count, and the 95% Wilson interval of each arm. It also gives the difference in points and the 95% Newcombe interval of the difference. A mark passes on the point value, so the interval shows how sure the call is. The top-level `pass` is true when every mark passes.

The example `tests/evaluation/results/2026-11-07-rule-cuts-plan/plan-both.json` was written after its run, and says so in `added_later`. The plan of 2026-11-18 is the first one written before its run.
