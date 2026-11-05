# CLAUDE.md

The rules below apply to every response in this repository. So each session self-tests the rules while it changes them, and a rule that hurts the work shows up here first. The [install page](docs/how-to/install-the-rules.md) says how to install the rules for every provider.

## Conventions

1. Do branch work in a sibling worktree, one per branch. Do not switch branches in `main/`.
2. Merge a merge request when its pipeline passes. Then remove its worktree and its branches.
3. Log each break of the rules in `tests/evaluation/results/harness-log.jsonl`, one line per session.

The [memory page](docs/explanation/memory.md) says where each type of memory lives.

@sources/model-operating-rules.md
