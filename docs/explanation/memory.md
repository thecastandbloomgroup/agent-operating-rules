# Memory

Agents keep more than one type of memory, and each type has one home in this system. The types follow the Psychology Today overview of memory [1], a tertiary source, so the types are background, not evidence. The [install page](../how-to/install-the-rules.md) gives the three scopes: the rules file, the repository, and one account.

## The map

| Type                   | What it holds                                              | Home in this system                                                                                                                                  | Form                                                                              |
| ---------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Sensory                | What was just seen or heard                                | Tool output inside the turn                                                                                                                          | None. It is read and dropped                                                      |
| Short-term and working | What is being worked on now                                | The context window and the response under construction                                                                                               | The response structure of Section 3                                               |
| Episodic               | Events: what ran, when, and what it cost                   | Run folders, `calls.csv`, git history, CHANGELOG, and `tests/evaluation/results/harness-log.jsonl`                                                   | CSV and JSONL, because the entries share a schema                                 |
| Semantic               | Facts, concepts, and what results mean                     | `docs/reference/`, `docs/explanation/`, README, and the write-ups                                                                                    | Markdown, because people read it                                                  |
| Procedural             | How to do things                                           | `bin/` scripts and the Taskfile first, then `docs/how-to/` and the conventions of `CLAUDE.md`. The rules file is the procedural memory for responses | Executable where a script can do it, Markdown where a person must                 |
| Prospective            | Intentions: what to do later, and the mark that decides it | Plan documents with pre-registered marks, the Unreleased changelog section, and open merge requests                                                  | Markdown. A JSONL ledger earns its place only when open plans multiply [judgment] |

An account also keeps local memory in its own harness, outside the repository. It spans the semantic and procedural types, and only one account sees it.

## The schema rule

Use a JSONL or CSV file when the entries share a schema and a script reads them. Use Markdown when a person reads them. Keep the rules file free of memory rules. The evaluation runs on the bare API, which has no memory, so no probe can score such a rule. Each added rule also lowers compliance with all the rules [2].

## The episodic log of harness sessions

`tests/evaluation/results/harness-log.jsonl` records each harness session that runs under the rules, one line per session:

```json
{"date": "2026-11-05", "harness": "claude-code", "model": "claude-fable-5", "rules_version": "0.8", "breaks": [{"rule": "4.1.1", "note": "three long sentences in a write-up, found by the checker before commit"}]}
```

A session with no break still gets a line, with an empty list, because the share of clean sessions needs a denominator. The log feeds the structural probes of the affective ladder.

## The graduation path

A memory moves up when it proves general, and each step has a gate:

1. A local memory that proves true for the whole project moves into `CLAUDE.md`, through a merge request.
2. A `CLAUDE.md` convention that proves provider neutral, and targets a measured level, becomes a probe.
3. The probe's marks decide whether the text enters the rules file. Nothing enters the rules without a passed probe.

## References

[1] Psychology Today, "Types of Memory," <https://www.psychologytoday.com/us/basics/memory/types-of-memory>, reviewed 2026-03-20. [T]

[2] tests/evaluation/results/2026-11-03-rule-changes-research.md, 2026. [S]
