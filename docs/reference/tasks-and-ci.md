# Tasks and CI

`Taskfile.yml` defines the tasks. `.gitlab-ci.yml` has one job for each stage, and each job calls the task of its stage. So CI and a person run the same step.

## Tasks

| Task           | Stage   | What it does                                                                                                                                                                                                           | It fails when                                  |
| -------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| `task format`  | none    | Formats the Python scripts with ruff, and the Markdown files with mdformat. It does not change `sources/model-operating-rules.md`, because only a new version changes the system prompt. `CHECK=true` changes no file. | `CHECK=true` and a file needs a change         |
| `task lint`    | none    | Lints the Python scripts with ruff, and the Markdown files with pymarkdown. For the rules file, it skips MD034 and MD040 until the next version of the rules fixes them.                                               | a linter finds a problem                       |
| `task review`  | review  | Runs `task format CHECK=true`, then `task lint`.                                                                                                                                                                       | either task fails                              |
| `task build`   | build   | Checks the version line of the rules file against `version.json`, then copies the release files to `.build/agent-operating-rules-<version>/`, each at its own path.                                                    | the two versions differ                        |
| `task test`    | test    | Runs `bin/deterministic-tests.py --check` on the rules file at 20 words, then on `README.md` and `tests/evaluation/evaluation-tests.md` at 25 words.                                                                   | a file has a finding                           |
| `task docs`    | docs    | Runs `bin/deterministic-tests.py --check` on each page of `docs/` at 25 words, then `bin/check-links.py` on `docs/` and `README.md`.                                                                                   | a page has a finding, or a link has no file    |
| `task package` | package | Runs `task build`, then zips the folder into `dist/agent-operating-rules-<version>.zip`.                                                                                                                               | the build fails                                |
| `task mirror`  | mirror  | Pushes the commit to `main` of the GitHub mirror, with the deploy key in the file `GITHUB_MIRROR_KEY`. Only CI runs it, on `main`.                                                                                     | the key is missing, or GitHub refuses the push |
| `task ci`      | all     | Runs review, build, test, docs and package, in that order. It leaves out mirror.                                                                                                                                       | a stage fails                                  |

`task format` and `task lint` run each tool with `uv run`. uv first syncs `.venv` with `uv.lock`. In CI, `uv run --locked` fails when `uv.lock` does not match `pyproject.toml`.

The release files are `README.md`, `version.json`, the folder `sources/`, `bin/deterministic-tests.py` and `tests/evaluation/evaluation-tests.md`. They keep their paths in the zip, so the script finds `sources/banned-words.txt`.

## CI

| Setting             | Value                                                                                                                                                             |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Image               | `ghcr.io/astral-sh/uv:0.12.23-python3.12-alpine`                                                                                                                  |
| Task                | 3.53.1, checked with its SHA-256 sum                                                                                                                              |
| uv cache            | `.uv-cache`, with `uv.lock` as its key                                                                                                                            |
| Stages              | review, build, test, docs, package, mirror                                                                                                                        |
| Mirror              | `git@github.com:thecastandbloomgroup/agent-operating-rules.git`, on `main` only. The [GitHub mirror](../how-to/set-up-the-github-mirror.md) page gives the setup. |
| Artifact of build   | `.build/`, kept for 1 week                                                                                                                                        |
| Artifact of package | `dist/*.zip`, kept for 1 month                                                                                                                                    |
