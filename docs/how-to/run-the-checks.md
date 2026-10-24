# How to run the checks on your machine

Run the checks before you push a change. They are the same checks that CI runs.

## Before you start

Install Task 3.53.1 or later from <https://taskfile.dev/installation/>. Install uv from <https://docs.astral.sh/uv/getting-started/installation/>. Install Python 3.10 or later.

The first task that needs a tool runs `uv run`. uv makes the folder `.venv` and installs the tools of `pyproject.toml` into it. This step needs a network connection. When `uv.lock` does not exist, uv writes it. Commit `uv.lock`, because CI fails without it.

## Run every stage

```sh
task ci
```

The task runs review, build, test, docs and package, in that order. It stops at the first stage that fails.

## Run one stage

Run `task <stage>`, for example `task test`. The [tasks and CI](../reference/tasks-and-ci.md) page lists each task.

## Fix a format failure

`task review` fails when a file needs a format change. Run `task format`. It changes the files. Then run `task review` again.

## Read a failure of the test or docs stage

The script prints one JSON report for each file. Find the report of the failed file. Its list `failures` names each failed test with its rule number in `sources/model-operating-rules.md`.
