# How to install the rules

This page says how to install `sources/model-operating-rules.md` as the system prompt of each provider. The rules file has no dependency, so the install is a paste or one pointer file. The [cost page](../explanation/cost.md) gives the price: about 4,000 tokens of input on every request.

## The two install forms

1. **A pointer.** The harness reads a file that imports the rules file. Only Claude Code supports this today. The pointer follows every change to the rules file at once.

2. **A copy.** Paste the full text of the rules file where the provider reads instructions. A copy goes stale when the rules change, so check it on each release:

   ```sh
   diff sources/model-operating-rules.md <your copy>
   ```

## Per provider

| Target                       | Where the rules go                                                                    | Form    |
| ---------------------------- | ------------------------------------------------------------------------------------- | ------- |
| Any provider's API           | The `instructions` or `system` field of each request, as `bin/run-evaluation.py` does | Copy    |
| Claude Code                  | `CLAUDE.md` in the repository root, with the line `@sources/model-operating-rules.md` | Pointer |
| Claude Code, every project   | `~/.claude/CLAUDE.md`, with an absolute import path                                   | Pointer |
| Claude, a Project in the app | The project instructions field                                                        | Copy    |
| OpenAI Codex CLI             | `AGENTS.md` in the repository root                                                    | Copy    |
| Gemini CLI                   | `GEMINI.md` in the repository root                                                    | Copy    |
| Cursor                       | A rule file under `.cursor/rules/`, set to always apply                               | Copy    |
| GitHub Copilot               | `.github/copilot-instructions.md`                                                     | Copy    |

The file names above come from the docs of each product on 2026-11-05. Check the product's own page when an install does not take.

## This repository

This repository installs the rules for Claude Code through `CLAUDE.md`, as a pointer. So every session that changes the rules also runs under them, and a rule that hurts the work shows up here first. The README notes that no harness result existed before this install, so treat early sessions as the first trial. The [memory page](../explanation/memory.md) says where each type of memory lives, and the rules file holds none.

## Caveats

- An agent harness adds its own system prompt, tools, and memory on top of the rules. The evaluation results come from the bare API, so a harness result can differ [judgment].
- The rules ask for the full response structure on every answer. In a harness, that costs output tokens on each turn. The [token section](../explanation/what-the-evaluations-show.md) of the evaluations page gives the counts.
- Install one copy per target, not two. A harness that reads both a project file and a global file gets the rules twice. The models do not handle a duplicate well [judgment].
