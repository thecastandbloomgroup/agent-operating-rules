# README: Operating Rules for LLMs

This file is for human readers. It explains `model-operating-rules.md`, the system prompt installed on every model. Agents receive only the rules file. Nothing here is a rule.

## What the rules file is

A shared system prompt. The author installs it on every LLM they use, from any provider. It sets how a model reasons, when it asks a question, how it structures a response, what language it uses, what evidence it must show, and how it forms a recommendation.

## Why one file for all models

The same request gets the same shape of answer from every model, so a reader can compare answers. Each rule maps to an artifact in the response, so a reader can grade compliance from the output alone, without access to the model's reasoning. Where a rule comes from a published standard, the file names the standard. A reader can then test the rule against its source instead of taking the author's word.

## Use the rules

1. Paste `sources/model-operating-rules.md` into the system prompt of your model. The [tutorial](docs/tutorials/check-a-response.md) shows each step.
2. Test a response with `python3 bin/deterministic-tests.py --check FILE`. Add `--instructions` to apply the 20-word sentence limit instead of the 25-word limit.
3. Run every check of CI on your machine with `task ci`. The [how-to guide](docs/how-to/run-the-checks.md) explains each stage.

## Dependencies

The rules file has no dependency: paste it into a system prompt. Each other task needs the tools in its row. The checker scripts use only the Python standard library.

| Task                 | Tool                                       | Version                     | Where the version is set |
| -------------------- | ------------------------------------------ | --------------------------- | ------------------------ |
| Test a response      | Python                                     | 3.10 or later; CI uses 3.12 | `.gitlab-ci.yml`         |
| Run the checks of CI | Task                                       | 3.53.1 or later             | `.gitlab-ci.yml`         |
| Run the checks of CI | uv, with `uvx`                             | 0.12.23 in CI               | `.gitlab-ci.yml`         |
| Format and lint      | ruff                                       | 0.16.10                     | `Taskfile.yml`           |
| Format and lint      | mdformat, with mdformat-gfm                | 1.0.0 and 1.0.0             | `Taskfile.yml`           |
| Format and lint      | pymarkdownlnt                              | 0.9.40                      | `Taskfile.yml`           |
| Run an evaluation    | a Perplexity API key in `PERPLEXITY_TOKEN` | not versioned               | Doppler or `pass`        |
| Run an evaluation    | the Doppler CLI, or `pass`                 | any                         | your machine             |
| Make a change        | `git`, and the GitLab CLI `glab`           | any                         | your machine             |

`uvx` fetches each format and lint tool at its pinned version, so you install only Python, Task and uv. The first run needs a network connection.

## Harnesses used for testing

The rules were tested in one harness only: the Perplexity Agent API at `https://api.perplexity.ai/v1/agent`, through `bin/run-evaluation.py`. Each call works as follows:

- The rules file is the system prompt, in the field `instructions`.
- One prompt of `tests/evaluation/evaluation-tests.md` is the input, with its attached files. The call has no earlier messages.
- The call gives the model no tools, so the model cannot search the web or run code.
- Each model reasons at a set effort, and its answer can have at most 32,000 tokens.
- The call runs in the background mode of the API, and the runner polls it every 5 seconds until it ends.

Six models were the executors. Claude Sonnet 5.5, GPT-6.1-Sol, Gemini 3.8 Flash and GLM 5.3 Flash ran at medium effort. Kimi K3 and Grok 4.7 ran at low effort. The judges are Claude Opus 5.5, GPT-6-Astra, Gemini 4 Argon, Kimi K3, GLM 5.3 and Grok 4.7, at high effort. `tests/evaluation/pairs.json` holds each pair, and `tests/evaluation/results/` holds each run.

The rules were not tested in other harnesses. These include a chat app, the API of each provider, and agent harnesses such as Claude Code, Codex or Cursor. Each of those adds its own system prompt, tools or memory, so a result there can differ from the results here [judgment].

The scripts of `bin/` have unit tests in `tests/unit/`, which run with `unittest` of the Python standard library. CI runs them in the image `ghcr.io/astral-sh/uv:0.12.23-python3.12-alpine`, with Task 3.53.1.

## Documentation

The [documentation](docs/README.md) has four kinds of page:

- Tutorials: [check the first response of a model](docs/tutorials/check-a-response.md).
- How-to guides: [make a change](docs/how-to/make-a-change.md), [run the checks](docs/how-to/run-the-checks.md), [set up Doppler for the evaluation](docs/how-to/set-up-doppler-for-evaluation.md), [run an evaluation](docs/how-to/run-an-evaluation.md), [record an evaluation run](docs/how-to/record-an-evaluation-run.md), [release a new version](docs/how-to/release-a-version.md).
- Reference: [files](docs/reference/files.md), [tasks and CI](docs/reference/tasks-and-ci.md), [deterministic tests](docs/reference/deterministic-tests.md), [evaluation](docs/reference/evaluation.md).
- Explanation: [standards used](docs/explanation/standards.md), [cost](docs/explanation/cost.md), [banned word list](docs/explanation/banned-word-list.md), [conformity assessment](docs/explanation/conformity-assessment.md).

## Version

The version follows [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html), with the major version at 0. Major version 0 is initial development, so expect a breaking change in any release. A breaking change raises the minor version, and a feature or a fix raises the patch version.

`version.json` holds the version, and the version line of the rules file matches it. The file [CHANGELOG.md](CHANGELOG.md) lists the changes of each version, in the format of Keep a Changelog. Each commit subject is a Conventional Commit, and the type of the commit gives its section in the changelog. The [release guide](docs/how-to/release-a-version.md) explains each step.
