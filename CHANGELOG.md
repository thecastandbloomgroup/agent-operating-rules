# Changelog

This file lists each change that a user of the rules file or of the scripts can see.

The format follows [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/). The version follows [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html). The major version stays at 0, which is initial development. So any release MAY break the rules file, the scripts or the tests:

- A breaking change raises the minor version, for example 0.3.0 to 0.4.0.
- A new feature or a fix raises the patch version, for example 0.3.0 to 0.3.1.

Each commit subject is a [Conventional Commit 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/). The type of a commit gives the section of its entry: `feat` goes in Added, `fix` in Fixed, and a commit with `!` in Changed. The [release guide](docs/how-to/release-a-version.md) gives the full map.

## [Unreleased]

## [0.3.0] - 2026-10-30

### Changed

- **Breaking:** the version starts again at major version 0. Versions 2.1, 3.0, 3.1 and 3.2 are now 0.1.0, 0.2.0, 0.2.1 and 0.2.2. The version line of the rules file says `Version 0.3`. The rules text has no other change from 0.2.2.
- **Breaking:** an evaluation run writes to `tests/evaluation/results/RUN/`, not to `.eval/RUN/`.
- **Breaking:** the evaluation tests are now version 1.3. T2 expects the prompt that the user asks for, as the first Complex probe. K1 accepts an analysis of its attached data as the analysis step.

### Added

- `CHANGELOG.md`. The build fails when it has no section for the version in `version.json`.
- The build fails when the major version is not 0.
- `bin/check-commits.py` and `task commits`. The review stage fails on a commit subject that is not a Conventional Commit.
- `bin/run-evaluation.py` sends each evaluation prompt to an executor through the Perplexity Agent API. Two judges score each answer with the rubric.
- `tests/evaluation/pairs.json` holds an executor and two judges for each of six providers.
- The evaluation reads `PERPLEXITY_TOKEN` from Doppler or from `pass`. `bin/connect-doppler-to-gitlab.sh` gives GitLab CI a Doppler service token.
- Each provider runs in its own process and writes a JSONL file. `task eval:merge` makes the final view of a run.
- `calls.csv` logs the tokens written to and read from the cache. `summary.md` has a table of tokens and cost.
- The files that C1, C2, K1 and K2 name as attached are in `tests/evaluation/attachments/`. The executor and the judges get them with the prompt.

### Fixed

- The checker finds the References list under any form of heading. Before, it found the list only under one exact heading, so most "citation with no reference" findings were false.
- The judge schema works with every provider.
- The evaluation does not score an answer that `max_output_tokens` cut.
- The evaluation retries a dropped connection or a timeout, up to 6 attempts in total.

## [0.2.2] - 2026-10-26

### Added

- Rule 1.5 analyzes quantitative and qualitative evidence. It compares each number with a baseline, groups statements into themes, and counts the sources of each theme. The old rule 1.5 is now rule 1.6.
- Section 5.1 accepts a theme with its supporting and disagreeing sources as evidence.

## [0.2.1] - 2026-10-26

### Added

- Rule 1.4 asks for research before a decision, with quantitative and qualitative evidence.
- Section 5.4.5 tags each source as primary, secondary, tertiary or unclassified, by how a claim uses it.
- The docs explain how each change reaches `main` through a merge request.

## [0.2.0] - 2026-10-25

### Changed

- **Breaking:** the first heading of each response is Headline, not `BLUF`. Rule 4.2 item 6 adds a table of acronyms and their aliases.
- CI runs ruff, mdformat and pymarkdown with `uvx` at pinned versions. The push mirror of GitLab copies `main` to GitHub.

## [0.1.0] - 2026-10-24

### Added

- The rules file `sources/model-operating-rules.md`, and the banned word list.
- `bin/deterministic-tests.py`, which tests a response against the rules, and `bin/check-links.py`.
- The evaluation prompts and the rubric in `tests/evaluation/evaluation-tests.md`.
- The docs, the tasks in `Taskfile.yml`, and a GitLab pipeline whose jobs call those tasks.

### Fixed

- `bin/check-links.py` prints nothing when every link has a file.
- `bin/deterministic-tests.py` gives no grade for a page with no prose.

[0.1.0]: https://gitlab.com/thecastandbloomgroup/private/agent-operating-rules/-/tags/v0.1.0
[0.2.0]: https://gitlab.com/thecastandbloomgroup/private/agent-operating-rules/-/compare/v0.1.0...v0.2.0
[0.2.1]: https://gitlab.com/thecastandbloomgroup/private/agent-operating-rules/-/compare/v0.2.0...v0.2.1
[0.2.2]: https://gitlab.com/thecastandbloomgroup/private/agent-operating-rules/-/compare/v0.2.1...v0.2.2
[0.3.0]: https://gitlab.com/thecastandbloomgroup/private/agent-operating-rules/-/compare/v0.2.2...v0.3.0
[unreleased]: https://gitlab.com/thecastandbloomgroup/private/agent-operating-rules/-/compare/v0.3.0...main
