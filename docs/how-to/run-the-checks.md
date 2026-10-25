# How to run the checks on your machine

Run the checks before you push a change. They are the same checks that CI runs.

## Before you start

Install Task 3.53.1 or later from <https://taskfile.dev/installation/>. Install uv from <https://docs.astral.sh/uv/getting-started/installation/>. Install Python 3.10 or later.

The tasks run each format and lint tool with `uvx`, at the version that `Taskfile.yml` pins. The tools stay in the cache of uv, so no `.venv` folder appears. The first run needs a network connection. Each worktree of the repository then uses the same cache.

## Run every stage

```sh
task ci
```

The task runs review, build, test, docs and package, in that order. Review runs format with `CHECK=true` first, then lint. It skips no stage. It stops at the first stage that fails.

## Run one stage

Run `task <stage>`, for example `task test`. The [tasks and CI](../reference/tasks-and-ci.md) page lists each task.

## Fix a format failure

`task review` fails when a file needs a format change. Run `task format`. It changes the files. Then run `task review` again.

## Read a failure of the test or docs stage

The script prints one JSON report for each file. Find the report of the failed file. Its list `failures` names each failed test with its rule number in `sources/model-operating-rules.md`.
