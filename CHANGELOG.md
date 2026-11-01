# Changelog

This file lists each change that a user of the rules file or of the scripts can see.

The format follows [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/). The version follows [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html). The major version stays at 0, which is initial development. So any release MAY break the rules file, the scripts or the tests:

- A breaking change raises the minor version, for example 0.3.0 to 0.4.0.
- A new feature or a fix raises the patch version, for example 0.3.0 to 0.3.1.

Each commit subject is a [Conventional Commit 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/). The type of a commit gives the section of its entry: `feat` goes in Added, `fix` in Fixed, and a commit with `!` in Changed. The [release guide](docs/how-to/release-a-version.md) gives the full map.

## [Unreleased]

### Added

- `bin/judge-actions.py` samples labelled actions of a run and asks a judge whether each domain is right and whether its reason states cause and effect. A judge never checks its own provider.
- `tests/evaluation/results/2026-11-01-action-checks-results.md`: of 40 actions of the 0.5.1 probe, 9 had a right domain and a reason of cause and effect, under each of two judges. On these yes or no checks, the judges reach a kappa of 0.61 to 0.71.
- `human-actions.md` in the run folder holds the same 40 actions for blind marks by a person.

## [0.6.0] - 2026-11-01

### Added

- `tests/evaluation/results/2026-11-01-gherkin-lines-results.md` and its script-only run. Answers free of long sentences rose from 31% to 50%.

### Changed

- **Breaking:** rules 0.6. A deterministic test puts Given, When, and Then each on its own line. Gherkin tests in one sentence were half of the long sentences in End.
- **Breaking:** Section 4.1 item 1 asks the model to split each sentence over the limit before it sends.

## [0.5.0] - 2026-11-01

### Added

- `tests/evaluation/results/2026-11-01-wording-results.md` and two script-only runs compare rules 0.4 with 0.5. A reason on every domain label rose from 12% to 78% of answers.
- `bin/run-evaluation.py --rules FILE --no-judge` installs another rules file and calls the executors only.
- `bin/script-checks.py` scores answers with the script checks of `item-labels.yaml`: STRUCTURE, LANGUAGE, SELFTEST, and the domain label of each action. It compares two runs with a 95% interval.
- `tests/evaluation/item-labels.yaml` labels the 13 prompts and the self-test by Bloom's taxonomy. Opus 5.5 wrote the labels at high effort. `tests/evaluation/results/2026-10-31-labels/` keeps those labels, blind labels by Fable 5.1, and its review. The two models agree on 13 of 14 primary levels (kappa 0.90).
- `tests/evaluation/results/2026-10-31-eval-design-research.md`: desk research on prior art for LLM evaluation and for Bloom's taxonomy, and the agreement of the two judges on each criterion. It proposes items labelled with a taxonomy type and a target level. Each of the three ladders gets a mastery score, and a geometric mean combines them. Human judgment gets three blind jobs.

### Changed

- **Breaking:** rules 0.5. Self-mention covers the words I, me, my, and mine outside End, as in "I cannot".
- **Breaking:** each action gives its Cynefin domain and one clause that says why.
- **Breaking:** the self-test line `Longest sentence: <n> words` becomes `Sentences over the limit of Section 4.1 item 1: <n>`. Of 133 judge notes on the self-test, 74 fault the sentence length.
- Review changes 1 and 2. A check MAY name its own taxonomy and level, and a level counts checks, not items. T2 is now cognitive Analyze, and its first check counts toward affective Organization.
- Review changes 3 and 7. The shared items STRUCTURE and LANGUAGE score the structure and the language rules once per answer. The SELFTEST checks compare each count with the checker, with a tolerance of 2 words on the longest sentence. The evaluation tests are now version 1.5.
- Review changes 6 and 12. The H2 check passes a holding statement that commits to no facts. K1 checks that each figure missing from the attachments is in the assumption log. K2 checks each cost against the 400k budget.
- Review changes 8 and 9. Six checks are split so that each decides one thing, and two duplicate checks become judge notes. The T1 gate and the T3 track checks go to a judge. Leverage checks and the U1 and U2 domain checks fall back to a judge when the script misses.
- **Breaking:** review change 10. The expected answer of X2 now asks for a budget for each probe, and the sentence that leverage is a guess. Rule 6.5 asks for both.

## [0.4.0] - 2026-10-31

### Added

- `bin/record-evaluation.py` and `task eval:record` write the record of all runs: `evaluation-scores.csv`, the summary and run blocks of `evaluation-results.md`, and the results of the evaluation reference. A `combined-from.txt` in a run folder names the partial runs that it combines.
- The record of the runs of 2026-10-29 and 2026-10-30. Before, those three files held only their templates.

### Changed

- **Breaking:** the self-test block of Section 7 has a new line, `Actions in End with a Cynefin domain label: <n> of <n>`. The line after it checks only the order of the domains and the probe caps. In the runs at rules 0.2.2, judges of another provider gave R1 (a domain for every action) full points in 29 of 205 judgments.
- Section 6.3 asks for the domain by one of the five names of Section 6.5. Some answers gave a task kind, such as Deterministic, as the domain.
- **Breaking:** the evaluation tests are now version 1.4. H2 expects Complicated work on the facts after the Chaotic stabiliser, then Complex probes. A holding statement that commits to no facts counts as part of the stabiliser.

## [0.3.1] - 2026-10-31

### Added

- The evaluation runs of 2026-10-28 to 2026-10-30 and their three write-ups, in `tests/evaluation/results/`.

### Fixed

- Each evaluation call runs in the background mode of the Agent API, and the runner polls it. Before, the API dropped a long call that held one connection open, so most calls at high effort failed.
- A null `usage` in an answer of the API no longer stops the run of a provider.

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
[0.3.1]: https://gitlab.com/thecastandbloomgroup/private/agent-operating-rules/-/compare/v0.3.0...v0.3.1
[0.4.0]: https://gitlab.com/thecastandbloomgroup/private/agent-operating-rules/-/compare/v0.3.1...v0.4.0
[0.5.0]: https://gitlab.com/thecastandbloomgroup/private/agent-operating-rules/-/compare/v0.4.0...v0.5.0
[0.6.0]: https://gitlab.com/thecastandbloomgroup/private/agent-operating-rules/-/compare/v0.5.0...v0.6.0
[unreleased]: https://gitlab.com/thecastandbloomgroup/private/agent-operating-rules/-/compare/v0.6.0...main
