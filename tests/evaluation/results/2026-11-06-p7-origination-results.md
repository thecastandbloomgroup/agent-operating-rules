# Prompt P7 is fit for the Origination level: results of its first run

## Headline

P7 passed all three marks, so it joins the psychomotor ladder as the first prompt of Origination.

1. **Feasible.** 19 of 24 units passed, over the mark of 6.
2. **Discriminates.** Four providers passed 4 of 4, Kimi K3 passed 2 of 4, and GLM 5.3 Flash passed 1 of 4.
3. **Grader.** Each of the 5 failure notes matches its transcript and its procedure file.
4. **Cost.** The run cost 1.97 USD, under the mark of 3 USD.

## Background

The [plan](2026-11-06-p7-origination-plan.md) fixed four marks before any call. P7 asks the model to write `notes/procedure.md` first, then to follow it on three notes files. Each file fails the checks in another way. The run used rules 0.9, the four file tools, 4 samples per provider, and a cap of 20 steps.

## Relevance

The psychomotor ladder now has a prompt for each of its seven levels. So a model can score above six of seven on it for the first time.

## Information

This section gives the passes, the failures, and the limits.

### The passes

| Provider        | Passed | Steps per unit |
| --------------- | ------ | -------------- |
| Sonnet 5.5      | 4 of 4 | 13 to 14       |
| Gemini 3.8 Flash | 4 of 4 | 15 to 21       |
| GPT-6.1 Sol     | 4 of 4 | 16 to 17       |
| Grok 4.7        | 4 of 4 | 12 to 15       |
| Kimi K3         | 2 of 4 | 12 to 14       |
| GLM 5.3 Flash   | 1 of 4 | 13 to 20       |

[1]

No unit hit the cap, and no unit wrote a scratch file. The steps count tool calls, and one API step can carry more than one call, so a unit can pass 20 calls.
[1]

### The failures

- **Another order on one file, in 3 units.** For example, one GLM unit wrote notes/a.md with no check first, then checked notes/b.md before its write. So the procedure was not reused the same way on each file.
  [1]
- **A procedure with no write step, in 2 units.** One GLM procedure names `check_file` but never says to write the file. One Kimi procedure names no tool and has no write step.
  [1]

### Limits

- **Form, not quality.** The script checks the form of the procedure and its reuse. The design note asks a judge, then a person, to score its quality, and neither has run.
- **Easier than the level below.** P7 passed 19 of 24, the same as the control of P5 that day and above its 14 of 24 of 2026-11-05. So the levels are not cumulative here. The ladder reports the Guttman coefficient for this reason.
- **Four samples per provider.** A level needs 20 trials per model for a mastery call, so each provider has 4 of the 20.

## End

I recommend that we:

1. Include P7 in the next full psychomotor run, so every level has trials from the same day.
   Increment: one run of P1 to P7, about 6 USD. Blocker removed: levels that come from different days.
   Test (stochastic): the run reports a pass rate for all seven levels and the Guttman coefficient of each provider.
   Domain: Complex. Reason: induction from runs, and the day to day spread of P5 could break the order of the levels.
2. Add a judge score of the procedure quality, as the design note asks.
   Increment: a judge rubric of three criteria and one call per passed unit, about 0.5 USD. Blocker removed: a level that the script grades on form alone.
   Test (evaluative): the rubric states the criteria, weights, and pass mark before any call, and a person scores 6 of the procedures blind.
   Domain: Complicated. Reason: analysis, because the rubric follows from the definition of Origination.
3. Keep the form checks of the script as they are.
   Increment: none. Blocker removed: none new.
   Test (deterministic, Gherkin):
   Given a P7 unit whose procedure has no write step
   When `bin/check-psychomotor.py` grades it
   Then the unit fails with a note that names the missing tool.
   Domain: Clear. Reason: deduction, because the unit tests check it.

## Follow-up

References:

[1] `2026-11-06-p7-origination/`: tool-checks.csv, calls.csv, the transcripts, and the procedure file of each sandbox, run 2026-11-06. [P]
