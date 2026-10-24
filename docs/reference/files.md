# Files

## Folders

| Folder   | Its job                                                                   | In git |
| -------- | ------------------------------------------------------------------------- | ------ |
| sources/ | What the repository delivers: the rules, and the data that the rules name | yes    |
| bin/     | Programs that a person or a task runs                                     | yes    |
| tests/   | The tests of the sources, and the records of each test run                | yes    |
| docs/    | Tutorials, how-to guides, reference and explanation                       | yes    |
| .build/  | The release folder that task build makes                                  | no     |
| dist/    | The release zip that task package makes                                   | no     |

## Each file

| File                                   | Purpose                                                                                          | Who reads it                   |
| -------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------ |
| sources/model-operating-rules.md       | The system prompt. Its version line matches version.json.                                        | Every model                    |
| sources/banned-words.txt               | Word list read by deterministic-tests.py, by category                                            | People, deterministic-tests.py |
| bin/deterministic-tests.py             | Tests with a fixed expected result: sentence length, dashes, banned words, citations, references | People, CI                     |
| bin/check-links.py                     | Finds each relative link to a file that does not exist                                           | task docs                      |
| tests/unit/test_bin.py                 | The unit tests of the scripts in bin/, with unittest of the standard library                     | task test                      |
| tests/evaluation/evaluation-tests.md   | Prompts and a rubric for the judgment rules in Sections 6.4 and 6.5                              | People, graders                |
| tests/evaluation/evaluation-results.md | Log of evaluation runs: one block per model per date, plus a cross-model summary                 | People                         |
| tests/evaluation/evaluation-scores.csv | One row per prompt per grader; the data behind any summary or chart                              | People, scripts                |
| tests/evaluation/results/              | Raw model responses, one folder per model, one file per prompt                                   | People, graders                |
| README.md                              | What the rules file is, and why one file serves all models                                       | People                         |
| version.json                           | The version, as its Semantic Versioning parts                                                    | People, task build             |
| Taskfile.yml                           | The tasks of each CI stage                                                                       | People, CI                     |
| .gitlab-ci.yml                         | The GitLab pipeline: one job per stage, and each job calls its task                              | GitLab                         |
| pyproject.toml                         | The exact versions of the format and lint tools, in the dev group of uv                          | uv                             |
| uv.lock                                | The versions and hashes of the tools and their dependencies                                      | uv                             |
| .python-version                        | The Python version that uv uses                                                                  | uv                             |
| .pymarkdown.json                       | The settings of the Markdown lint                                                                | task lint                      |
| .github-known-hosts                    | The public host key that GitHub publishes, so ssh refuses any other server                       | task mirror                    |
