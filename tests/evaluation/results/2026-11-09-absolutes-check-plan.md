# A plan: a script check for unmeasured absolutes

## Headline

A new script check flags a general claim with "always", "never", "none", or "impossible" that has no count behind it. This plan tests the check on stored answers before any rule names it. No step calls a model, so the plan costs no money.

1. The rules ban uncalibrated hedges (Section 4.4 item 2), but no rule bans the opposite fault: certainty with no evidence.
2. A first scan on 2026-11-09 found about 8 such claims in the 126 control answers of the rule-cut probe.
3. A plain word list would fail, because most uses of these words are instructions, counts, or quoted text.

## Background

The answers come from the control arm of the rule-cut probe, `tests/evaluation/results/2026-11-07-rule-cuts-control/responses/`, on the branch `test/rule-cuts`. That arm ran rules 0.10 on six models, with 126 answers.

## The check

`bin/deterministic-tests.py` reports each sentence that holds one of the four words, unless one of these holds:

1. The sentence holds a digit or a bracket citation such as "[3]".
2. The word sits inside double quotes or backticks.
3. The sentence is an instruction. It starts with the word itself ("Never invent facts"), or the word follows "do", "must", "should", or "MUST".
4. The line is a table row, a code block, or a heading. The checker skips these already.

The check reports a count only. It is not a failure in `--check` until a rule names it.

## Unit test, written first

Given the sentences "Retrospectives always fail.", "Never invent facts.", and "All 126 answers passed."
When the check runs
Then it flags the first sentence only.

## Marking rubric

Each flagged sentence is marked by hand as one of two classes:

1. **Fault:** a general claim about a class of things (teams, models, tools) as always or never true, with no count, source, or deduction in the sentence or the one before it.
2. **False alarm:** anything else. Examples are a fact about the one case in the prompt and a fact that follows from a definition or from code. An instruction the check missed is also a false alarm.

Every unflagged sentence with one of the four words is also read, to count missed faults.

## Pass mark

The check passes when at least 80% of its flags are faults. A missed fault does not fail the check, but the results report the count.

## Limits

The marker is the model that wrote the check, so the marks are not blind. A person should mark a sample before any rule rests on the result.
