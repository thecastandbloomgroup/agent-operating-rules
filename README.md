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

## Documentation

The [documentation](docs/README.md) has four kinds of page:

- Tutorials: [check the first response of a model](docs/tutorials/check-a-response.md).
- How-to guides: [make a change](docs/how-to/make-a-change.md), [run the checks](docs/how-to/run-the-checks.md), [set up Doppler for the evaluation](docs/how-to/set-up-doppler-for-evaluation.md), [run an evaluation](docs/how-to/run-an-evaluation.md), [record an evaluation run](docs/how-to/record-an-evaluation-run.md), [release a new version](docs/how-to/release-a-version.md).
- Reference: [files](docs/reference/files.md), [tasks and CI](docs/reference/tasks-and-ci.md), [deterministic tests](docs/reference/deterministic-tests.md), [evaluation](docs/reference/evaluation.md).
- Explanation: [standards used](docs/explanation/standards.md), [cost](docs/explanation/cost.md), [banned word list](docs/explanation/banned-word-list.md), [conformity assessment](docs/explanation/conformity-assessment.md).

## Version

`version.json` holds the version, and the version line of the rules file matches it. The [release guide](docs/how-to/release-a-version.md) explains how to change it.
