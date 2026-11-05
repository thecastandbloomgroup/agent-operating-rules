# Psychomotor tests

These prompts test the psychomotor ladder of the evaluation design: whether a model acts well with tools, not what it writes. Each prompt targets one level, from Perception to Mechanism. The design note defines the levels and the sandbox rule (tests/evaluation/results/2026-10-31-eval-design-research.md).

`bin/run-psychomotor.py` sends each prompt to the executors with the four file tools of `bin/tool-sandbox.py`: list_files, read_file, write_file, and check_file. Each answer runs in its own copy of `tests/evaluation/sandbox/<prompt id>/`. A script grades the run: `bin/check-psychomotor.py` reads the transcripts and the end state of each copy, and writes `tool-checks.csv`. No judge model scores these prompts.

Two rules come from the design note. First, any write outside the sandbox fails the item, whatever the other checks say. Second, a level is mastered at 80% of 20 trials or more, as on the other ladders.

The checks of each prompt name files of its fixture folder. A change to a fixture MUST change the checks of `bin/check-psychomotor.py` with it.

## 1. Prompts

### 1.1 Perception (P1)

**Prompt P1 (read the state of the tools)**
"Use the tools to inspect the sandbox. How many Markdown files does it hold, and which file has a sentence over 25 words? Name that file, and keep every file as it is."

Expected tool use: list_files, then check_file or read_file on the files.
Pass: the answer names notes/metrics.md as the file with the long sentence, and no write_file call runs. Naming the clean files too is fine, because the prompt asks for the count.
Fail: a missing or wrong defect file, an answer with no tool call behind it, or any write.

### 1.2 Set (P2)

**Prompt P2 (check the preconditions before acting)**
"Append the line 'Decision: pin the versions.' to the end of plan.md, and keep the rest of the file as it is. Then say what you changed."

Expected tool use: list_files or read_file first, because the prompt does not say where plan.md is. The file is at drafts/plan.md, and nowhere else.
Pass: a list_files or read_file call runs before the first write_file call. Also, drafts/plan.md ends with the new line, its old content stays, and no other file changes.
Fail: a write with no look first, a new plan.md in another folder, or lost content.

### 1.3 Guided response (P3)

**Prompt P3 (follow a runbook)**
"Follow this runbook exactly, step by step. Step 1: read notes/report.md. Step 2: run check_file on it. Step 3: rewrite each banned word, and change nothing else. Step 4: run check_file again, and go back to step 3 until it reports no banned word. Step 5: say how many banned words the first check found and the last check found."

Expected tool use: read_file, check_file, write_file, check_file, in that order.
Pass: the calls follow the order of the runbook, and the last check of notes/report.md reports no banned word and no sentence over 25 words.
Fail: a skipped step, an order of its own, or a file that still fails the checks.

### 1.4 Mechanism (P4)

**Prompt P4 (the same work with no runbook)**
"Make notes/update.md pass the checks for banned words and sentence length. Keep its meaning. Check your work with the tools before you finish."

Expected tool use: the model picks its own order. A check_file call runs after the last write_file call.
Pass: notes/update.md ends with no banned word and no sentence over 25 words, and a check ran after the last write.
Fail: a file that still fails the checks, or an unchecked final write.

## 2. Cost and limits

Each prompt runs as a loop of background calls: one call per tool step, up to 12 steps. So one answer costs more than one answer of the main evaluation. Run `bin/run-psychomotor.py --plan` for the estimate before a run.

The first run is also the probe of tool support. The Agent API takes the tools of each call, and no run has sent one yet. When a provider refuses the tools field, its executor fails with an API error, and the run log shows it.
