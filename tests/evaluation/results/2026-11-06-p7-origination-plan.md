# A plan: a first prompt for Origination, the top psychomotor level

## Headline

Prompt P7 asks a model to write a procedure, then reuse it on three files, so the top psychomotor level gets its first trials.

1. The psychomotor ladder counts seven levels, but Origination has had no prompt, so no model could score above six of seven.
2. The design note defines Origination as a new procedure that later tasks reuse. P7 makes that measurable in the sandbox: a procedure file, then the same order of tools on each of three files.
3. This first run tests the prompt, not the models: whether P7 is feasible and whether it tells the models apart.

## Background

The [design note](2026-10-31-eval-design-research.md) gives Origination the check "a script in bin that a later task calls", scored by a judge, then a person. The sandbox has no tool that runs a script. So P7 uses a written procedure in place of a script, and the script checks only its form and its reuse [judgment].

## Design

1. P7 sits in `tests/evaluation/psychomotor-tests.md`, with a fixture of three notes files in `tests/evaluation/sandbox/P7/`. Each file fails the checks in another way: a banned word, a long sentence, and both.
2. `bin/check-psychomotor.py` grades P7. The procedure comes before the first write to a notes file, has three or more numbered steps, names check_file and write_file, and passes the checks. Each notes file ends clean with a check after its last write. The tools run on each file in the same order, and no other file changes.
3. `bin/run-psychomotor.py` gives P7 a cap of 20 steps, because it works on four files.
4. Run P7 with 4 samples on all six providers, with the default tools.
5. Read the note of each failed unit against its transcript, to find any fault of the grader.

## Metrics and pass marks

1. **Feasible.** At least 6 of 24 units pass.
2. **Discriminates.** At most 20 of 24 units pass, and at least two providers differ by two passes or more.
3. **Grader.** No failed unit has a note that its transcript contradicts.
4. **Cost.** The run costs under 3 USD.

P7 joins the ladder runs only when marks 1, 2, and 3 pass. Otherwise the write-up says which part of the prompt or grader to change.

## Cost and stop rule

24 units at about 0.05 USD each, with more steps than the other prompts, cost about 1.2 USD. One run, then the write-up.
