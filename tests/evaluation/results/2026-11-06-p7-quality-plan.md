# A plan: a judge score of the quality of each P7 procedure

## Headline

A judge rubric of three criteria scores the procedure of each passed P7 unit, so Origination is graded on quality and not on form alone.

1. The script of P7 checks that the procedure comes first, has numbered steps, names two tools, and is reused. It does not check that another agent could follow it.
2. The design note asks a judge, then a person, to score Origination.
3. This plan covers the judge. A person scores a blind sample later, and only then can the judge be trusted.

## Background

The [P7 results](2026-11-06-p7-origination-results.md) found 19 of 24 units passed, with a script that grades form. The judge reads only the procedure file, with no transcript and no script result, so it scores the procedure on its own.

## The rubric

Each criterion scores 0, 1, or 2. The weighted score runs from 0 to 100, and a procedure passes at 70 or more.

| Criterion | Weight | 2 | 1 | 0 | Evidence |
| --- | --- | --- | --- | --- | --- |
| Complete | 40 | Steps cover a check, a fix of banned words, a fix of long sentences, a write, and a check again until clean | One of these is missing | Two or more are missing | The numbered steps |
| Executable | 30 | Each step names a tool or an action that another agent can do with no guess | One step needs a guess | Two or more steps need a guess | The verbs and tool names of the steps |
| General | 30 | No step names a.md, b.md, c.md, or their content | One step names them | The steps work only for these files | The file names and facts in the steps |

## Design

1. `bin/judge-procedures.py RUN_DIR` reads `tool-checks.csv` and sends the procedure of each passed P7 unit to a judge of another provider than its executor. It writes `procedure-checks.csv` with the three scores, the weighted score, and a note.
2. Run it on `2026-11-06-p7-origination/` and on the P7 units of `2026-11-06-psychomotor-p1-p7/`.

## Metrics

1. **Pass rate.** The share of passed units whose procedure scores 70 or more.
2. **Spread.** The judge gives at least two distinct weighted scores, or the rubric does not tell procedures apart.
3. **Cost.** Under 1 USD for both runs.

The judge result stays the judges' view until a person scores 6 procedures blind and agrees on 5 or more.
