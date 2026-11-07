# All seven psychomotor levels on one day: results of one run, with a judge of P7 quality

## Headline

The run measured every level, but the guard failed on Perception, because the Gemini loop at the step cap came back on P1 to P3.

1. The pooled pass rates were 21, 19, 22, 24, 18, 24, and 24 of 24, from Perception to Origination. So the rates do not fall from level to level.
2. Gemini hit the cap in 7 of 28 units, all on P1 to P3. Each time, it wrote drafts of its answer to scratch files. So the loop that the check text probe missed is not rare.
3. GPT-6.1 Sol passed P5 in 0 of 4 units again, and passed every other level in 4 of 4.
4. The judge scored all 43 passed P7 procedures of two runs at 70 or more. However, 4 procedures scored 0 on one criterion and still passed, so the pass mark is too low.

## Background

The [plan](2026-11-06-psychomotor-p1-p7-plan.md) fixed the marks before the run: 168 units of P1 to P7 with rules 0.9, 4 samples, and the four file tools. The [quality plan](2026-11-06-p7-quality-plan.md) fixed a rubric of three criteria for the procedure of each passed P7 unit, and `bin/judge-procedures.py` applied it.

## Relevance

The Gemini loop now costs it three low levels in one run, so it is the largest single cause of failed psychomotor trials. The P7 rubric needs a stricter pass mark before its rates can mean anything.

## Information

This section gives the marks, the rates per provider, the loop, and the P7 judge.

### The marks

| Mark                                            | Result                     | Pass |
| ----------------------------------------------- | -------------------------- | ---- |
| Coverage: 22 or more of 24 units with no API error per level | 24 of 24 on every level | yes  |
| Guard: P1 22 or more                            | 21 of 24                   | no   |
| Guard: P4 22 or more                            | 24 of 24                   | yes  |
| Guard: P6 22 or more                            | 24 of 24                   | yes  |
| Cost under 9 USD                                | 6.50 USD, and 0.50 USD for the judge | yes  |

[1]

No unit failed on the network, so no unit ran again.
[1]

### The rates per provider

| Provider        | P1 | P2 | P3 | P4 | P5 | P6 | P7 |
| --------------- | -- | -- | -- | -- | -- | -- | -- |
| Sonnet 5.5      | 4  | 4  | 4  | 4  | 4  | 4  | 4  |
| Gemini 3.8 Flash | 1  | 0  | 2  | 4  | 4  | 4  | 4  |
| GPT-6.1 Sol     | 4  | 4  | 4  | 4  | 0  | 4  | 4  |
| GLM 5.3 Flash   | 4  | 4  | 4  | 4  | 3  | 4  | 4  |
| Kimi K3         | 4  | 4  | 4  | 4  | 3  | 4  | 4  |
| Grok 4.7        | 4  | 3  | 4  | 4  | 4  | 4  | 4  |

Each cell counts passes of 4 units.
[1]

- **Origination moved.** P7 passed 24 of 24, against 19 of 24 in its first run the same day. GLM rose from 1 to 4, and Kimi from 2 to 4.
  [1]
- **Complex overt response holds near the mark.** P5 passed 18 of 24, against 14 and 19 in the two earlier runs.
  [1]

### The loop at the step cap

All 7 Gemini units at the cap follow one pattern. The model does or starts the task, then writes a draft of its answer to a file such as `test_output.md` or `test_resp.md`. It checks that file, and it writes and checks again until the cap. The scratch file stays in the sandbox.
[1]

The loop hit 8 of 24 Gemini units on 2026-11-05. It hit 1 of 8 in the check text control, and 7 of 28 here. So it comes and goes by run, and four samples per prompt cannot predict it [inference].

### The judge of P7 quality

| Run                      | Procedures | Score 70 or more | Score 100 | Mean |
| ------------------------ | ---------- | ---------------- | --------- | ---- |
| First P7 run             | 19         | 19               | 7         | 86.3 |
| This run                 | 24         | 24               | 11        | 88.3 |

[2]

- **The criteria spread, but the pass mark does not.** The scores took four values, from 70 to 100. However, every procedure passed.
  [2]
- **The pass mark lets a weak procedure through.** Four procedures of this run scored 0 on executable, which means two or more steps need a guess. Each scored 70, the pass mark, from the other two criteria.
  [2]

So a pass of the rubric does not mean that another agent can follow the procedure. The mark stays as planned for these results, and a later plan sets a stricter one [judgment].

### Limits

- **Four samples per provider.** Each provider has 4 trials per level, under the 20 that a pass call needs.
- **The judge has no person check.** The plan asks a person to score 6 procedures blind before the judge can be trusted.

## Addendum: a stricter pass mark

`bin/judge-procedures.py` now passes a procedure at 85 or more, with no criterion at 0. The scores above stay as they were, and only the pass changes. Under the new mark, 11 of 19 procedures of the first P7 run pass, and 17 of 24 of this run. So 28 of 43 pass, against 43 of 43 at the old mark.
[2]

## End

I recommend that we:

1. Probe a short harness note for the Gemini loop. The note says that the sandbox holds the task files only, and the answer goes in the reply.
   Increment: one line in the first user turn of each unit. Run P1 to P3 for Gemini, 24 units with the note and 24 without, about 1 USD. Blocker removed: the largest single cause of failed psychomotor trials.
   Test (stochastic): Gemini units at the cap fall to 2 or fewer of 24, against the same-day control. Sonnet keeps 12 of 12 on a guard run of P1 to P3.
   Domain: Complex. Reason: induction from runs, and the loop comes and goes by run, so the control must run the same day.
2. Change the P7 pass mark to 85 with no criterion at 0, in a new plan, and apply it to the scores that exist.
   Increment: one constant and one test in `bin/judge-procedures.py`, with no new call. Blocker removed: a pass mark that passes a procedure with two steps that need a guess.
   Test (deterministic, Gherkin):
   Given a procedure scored 2, 0, and 2
   When `bin/judge-procedures.py` weighs it
   Then it does not pass.
   Domain: Clear. Reason: deduction, because the rule is fixed.
3. Ask a person to score 6 P7 procedures blind with the rubric, when a marking session suits.
   Increment: 6 procedures, about 10 minutes. Blocker removed: a judge that no person has checked.
   Test (evaluative): the person and the judge agree on the pass of 5 or more of 6.
   Domain: Complicated. Reason: analysis, because the rubric states each criterion.

## Follow-up

References:

[1] `2026-11-06-psychomotor-p1-p7/`: tool-checks.csv, calls.csv, run.log, and the transcripts, run 2026-11-06. [P]

[2] The procedure-checks.csv files of `2026-11-06-p7-origination/` and `2026-11-06-psychomotor-p1-p7/`, judged 2026-11-06. [P]
