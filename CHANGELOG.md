# Changelog

This file lists each change that a user of the rules file or of the scripts can see.

The format follows [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/). The version follows [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html). The major version stays at 0, which is initial development. So any release MAY break the rules file, the scripts or the tests:

- A breaking change raises the minor version, for example 0.3.0 to 0.4.0.
- A new feature or a fix raises the patch version, for example 0.3.0 to 0.3.1.

Each commit subject is a [Conventional Commit 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/). The type of a commit gives the section of its entry: `feat` goes in Added, `fix` in Fixed, and a commit with `!` in Changed. The [release guide](docs/how-to/release-a-version.md) gives the full map.

## [Unreleased]

### Added

- Prompt P7 tests Origination, the top psychomotor level. The model writes a procedure, then reuses it on three files, and `bin/check-psychomotor.py` grades its form and reuse. P7 gets a cap of 20 steps. Its first run passed 19 of 24.
- `bin/run-psychomotor.py --check-text` also offers `check_text`, a check of a draft answer that writes no file. A probe found that it costs passes on P5, so the default tools stay the four file tools.

## [0.9.0] - 2026-11-06

### Added

- `bin/judge-actions.py --work MARKING_DIR` judges fit to the work: no expected answer, and the human marks as examples. On 104 actions it found 76% of domains right, against 69% for fit to the test.
- `bin/judge-loo.py --no-expected` leaves the expected answer out of each judge call, and asks whether the label fits the work. A probe lifted the judges to a label kappa of 0.24 and 0.18, under the mark of 0.40.
- `bin/judge-loo.py` judges each marked row with the user's marks on the other rows as examples. A probe on the 24 marked rows lifted both judges to a label kappa of -0.01. The mark was 0.40, so the built-in instruction stays.
- `bin/judge-actions.py` takes `--instructions FILE` in place of its built-in instruction. A probe used it to judge the 24 marked rows with the themes of the user's notes. Both label marks failed at kappa -0.20, so the built-in instruction stays.
- The judge trust results compare both judges with a blind marking of 24 actions by the user. Neither judge matches the user on domain fit: kappa -0.20 and -0.40. The evaluations page now calls the domain rates the judges' view.
- `task marking-check` clicks the marking page in headless Chrome against a blank copy of the sheet. It fails unless each answer reaches the file, and `task marking` runs it first. It fails on the page from before the save fix.

### Fixed

- The marking page sent each answer one click late, so the last answer on a row never reached the file. The page now waits for its form to update before it sends it. It shows "Saved" only when the file holds the answers on screen.

### Changed

- **Breaking:** The rules drop coded labels such as "A2" and "E1". An assumption line now starts with "Assumption:", and a response points to its own parts by name. The user could not recall what the codes stood for.

## [0.8.2] - 2026-11-05

### Fixed

- `bin/tool-sandbox.py` refuses a tool call with an empty path as an error, not a violation. An empty path names no file, so it cannot leave the sandbox. Two runs had failed a Gemini unit on that call. Also, `bin/check-psychomotor.py` ignores the empty-path violations of old transcripts, so the four-sample run now scores Guided response at 24 of 24.
- `bin/run-psychomotor.py` writes `calls.csv` and `run.log` as each unit ends. Before, a run showed no calls until its end. So a slow run could look dead, as the first P1 to P6 run did at 108 of 144 units.

### Added

- `bin/repair-psychomotor.py` sends a second turn to the failed psychomotor units of a run, from the end state of each sandbox. A named mode states the failure. A retry mode asks for a check as its control. Also, `bin/run-psychomotor.py` can start a unit from such a seed, and `bin/check-psychomotor.py` grades the earlier steps and the new ones as one history.
- `task marking` starts a local web page for the blind marking sheet. The page shows one action at a time and saves each Yes or No answer to `sheet.csv`. It shows the agreement of each judge only after the last mark. The app in `tools/marking` uses Svelte 5, SvelteKit 2, Tailwind CSS 4, and shadcn-svelte, and `bin/marking-items.py` writes its items.
- Prompts P5 and P6 extend the psychomotor ladder to Complex overt response and Adaptation. P5 moves a line across two files with no wasted action. For P6, `bin/run-psychomotor.py` injects one failed write, and the task must still complete. `bin/check-psychomotor.py` grades both, per the plan of 2026-11-05.

## [0.8.1] - 2026-11-05

### Added

- `bin/second-turn.py --mode structure` sends a second turn that names each broken structure part of an answer, from a script-checks CSV. It sends a turn only for the rows whose structure column is False, per the repair plan of 2026-11-05.
- `install.sh` installs the rules file for one agent harness: a pointer for Claude Code, and a copy for Codex, opencode, Gemini CLI, Cursor, and Copilot. It runs from a clone or from curl with `--repo`, detects Claude Code from its environment, and never overwrites a file with other content. The release zip ships it.
- `bin/run-psychomotor.py` sends the prompts of `tests/evaluation/psychomotor-tests.md` to the executors with the file tools of `bin/tool-sandbox.py`. Each unit acts in its own copy of its sandbox fixture. The tools refuse any path outside the sandbox, and the refused call is a violation. The grader `bin/check-psychomotor.py` writes `tool-checks.csv` from the transcripts and the end states, and `bin/ladder-scores.py` reads it as the psychomotor trials. Before, no sandbox existed, so nothing measured the psychomotor ladder.

### Fixed

- `bin/check-psychomotor.py` grades P1 on the defect file alone. The P1 prompt asks for the file count, so a good answer names every file. Also, `bin/run-psychomotor.py` now logs the cache and reasoning token columns of `calls.csv`, which the first run lost.
- `bin/run-evaluation.py` sends a job again when it fails because the model is overloaded, with the backoff of HTTP errors. Before, such a call was lost until it was sent again by hand. `bin/judge-actions.py` and `bin/second-turn.py` share the retry.

## [0.8.0] - 2026-11-04

### Changed

- **Breaking:** rules 0.8. The reason of each action names its inference: deduction from a known rule or analysis, induction from trials, or acting first. A reason from trials names what could break the pattern. In the probe, Complex reasons that say how sure they are rose from 2 to 23 of 40 actions.

### Added

- `tests/evaluation/results/2026-11-03-reason-and-count-line-results.md`: two probes against a new baseline at rules 0.7. A reason that names its inference lifts how sure Complex reasons are from 2 to 23 of 40 actions. Removing the count line of the self-test fails its pass mark by 1 point.
- `bin/judge-actions.py --label DOMAIN --prompts IDS` samples only the actions with that label, or of those prompts.
- `sources/banned-words.txt` bans "verdict" and "verdicts" as attitude markers, because the word reads as hostile. Write "result" or "check".
- The script checks of all 10 run folders were run again with the fixed checker. Only the label and self-test columns change. The write-ups of those runs keep the numbers of the old checker, and no probe changes its result. The factored self-test probe now has 44 of 107 against 48 of 108, still short of 58.
- `bin/ladder-scores.py` scores Evaluate without the self-test lines that count words, because the checker owns those counts. At rules 0.6, Evaluate rises from 38% to 71% of 234 answers, and the cognitive score from 0.62 to 0.71.
- `tests/evaluation/results/2026-11-03-cynefin-questions-results.md`: a probe of ordered domain questions and named inferences, from desk research by the user. Domains stayed at 26 of 40, short of 33. Reasons named an inference in 369 of 710 actions.
- `bin/judge-actions.py` asks a third question: does the reason say how sure the link is? A reason from trials passes only when it names what could break the pattern.
- `tests/evaluation/results/2026-11-03-factored-selftest-results.md`: a probe that checks the self-test item by item. Right self-tests fell from 43 to 37, short of 58. The models write 0 long sentences whatever the count, so the checker SHOULD own that count.
- `tests/evaluation/results/2026-11-03-reason-rejudge-results.md`: the first blind marks by a person, and a rejudge of 40 actions. Both judges pass the reason in 33 of 40 actions, not 11, so Evaluate is now the lowest level.
- `tests/evaluation/results/2026-11-03-rule-changes-research.md`: desk research on changes to the rules for the higher Bloom levels. It ranks five changes, with a self-test checked item by item first, because the script measures it.
- `tests/evaluation/results/2026-11-03-second-turn-results.md`: desk research on levers for each Bloom ladder, and two pilots. A line in Section 0 lifted A3 structure from 8 to 12 of 18, short of 14. Under plain pushback, 17 of 18 answers to A2 kept their form.
- `bin/second-turn.py` sends a second turn after answers of a run, under the same rules. Pushback tests the Characterization level. A judge note on one action, against a plain retry, tests feedback at the Understand level.
- `bin/judge-actions.py --actions CSV` judges the same file and action as each row of a CSV. So the second answers are judged on the actions of the first.
- `tests/evaluation/results/2026-11-01-split-first-results.md`: a probe that splits the problem first and keeps the domain. Under one judging rule, domains were right in 28 of 40 actions, against 27 at rules 0.6. So the rules stay at 0.7.
- The 40 actions of rules 0.6 were judged again under tests 1.6. The main files of that run now hold those checks, and the files that end in -tests15 hold the old ones.
- `bin/ladder-scores.py` scores each model on the Bloom ladders from the script checks and the judge checks of runs. A taxonomy gets no score while a measured level has fewer than 20 trials. A ladder whose rates rise gets the mean rate in place of L.

### Fixed

- `bin/script-checks.py` reads a field named Reason after a domain label as its reason, as in "Domain: Clear. Reason: a known rule applies."
- `bin/script-checks.py` reads more forms of domain labels and steps, such as "Clear:", "(Clear domain: ...)", and "**Step 1.**". Numbered fields under a step are no longer actions. At rules 0.6, wrong label counts fall from 53 to 10 of 234 self-tests. So Evaluate rises from 71% to 88%, and Apply from 62% to 72%.
- `bin/judge-actions.py` judges a reason on its own, so a wrong domain no longer fails it. A reason that says what effort it takes to know the effect states cause and effect.

## [0.7.0] - 2026-11-01

### Added

- `tests/evaluation/results/2026-11-01-affective-baseline.md`: the first run of A1 to A3. Responding passes 18 of 18 answers, Valuing 17 of 18, and Organization 8 of 18.
- `bin/script-checks.py` scores the answers to A3, which asks for no headings, by their own structure checks.
- `tests/evaluation/results/2026-11-01-reason-examples-results.md`: a probe with one example reason for each domain, and a line between Clear and Complicated. Actions with both a right domain and a reason of cause and effect rose from 9 to 10 and 12 of 40. The pass threshold was 18. So the rules stay at 0.6.
- `bin/bloom-calibration.py` samples questions with Bloom labels by people at a pinned commit, and scores model labels against them. The questions stay in a scratch folder.
- `tests/evaluation/results/2026-11-01-bloom-calibration.md`: on 204 questions, Opus 5.5 matches people at a kappa of 0.65, and Fable 5.1 at 0.55. The two models agree with each other at 0.69.
- Blind marks of the 40 actions by Fable 5.1, as an addendum to the action checks. By a majority of three graders, 11 of 40 actions score 3.
- `bin/judge-actions.py` samples labelled actions of a run and asks a judge whether each domain is right and whether its reason states cause and effect. A judge never checks its own provider.
- `tests/evaluation/results/2026-11-01-action-checks-results.md`: of 40 actions of the 0.5.1 probe, 9 had a right domain and a reason of cause and effect, under each of two judges. On these yes or no checks, the judges reach a kappa of 0.61 to 0.71.
- `human-actions.md` in the run folder holds the same 40 actions for blind marks by a person.

### Changed

- The rules file says version 0.7. Its text is the same as 0.6, because this release changes the tests and the scripts.
- **Breaking:** the evaluation tests are now version 1.6. A support step, such as paging a responder or building a measure, MAY carry its own domain. H1, H2, and X1 each name one. `bin/judge-actions.py` gives its judges the same rule.
- Label review changes 4 and 5, in the design note. Evaluate covers judging options against fixed criteria, as well as grading an answer. Two tie-break rules separate Apply from Create, and Analyze from Apply.
- Label review change 13, in the design note. The knowledge type of an Analyze item follows its object: a classification or a cause is conceptual, and a method is procedural. A new boundary separates Understand from Analyze.
- **Breaking:** label review change 11. Section 1.7 of the tests adds prompts A1 to A3 for the affective levels Responding, Valuing, and Organization. Each run now sends 16 prompts. Characterization waits for a harness that sends a second turn.
- `bin/record-evaluation.py` counts a run as full when it has all 13 core prompts, so runs with A1 to A3 still count.

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
[0.7.0]: https://gitlab.com/thecastandbloomgroup/private/agent-operating-rules/-/compare/v0.6.0...v0.7.0
[0.8.0]: https://gitlab.com/thecastandbloomgroup/private/agent-operating-rules/-/compare/v0.7.0...v0.8.0
[0.8.1]: https://gitlab.com/thecastandbloomgroup/private/agent-operating-rules/-/compare/v0.8.0...v0.8.1
[0.8.2]: https://gitlab.com/thecastandbloomgroup/private/agent-operating-rules/-/compare/v0.8.1...v0.8.2
[0.9.0]: https://gitlab.com/thecastandbloomgroup/private/agent-operating-rules/-/compare/v0.8.2...v0.9.0
[unreleased]: https://gitlab.com/thecastandbloomgroup/private/agent-operating-rules/-/compare/v0.9.0...main
