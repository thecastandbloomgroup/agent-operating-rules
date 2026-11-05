# What the evaluations show

This page sums up what the evaluation runs from 2026-10-28 to 2026-11-04 say about the use of the rules with agents. Each claim links to the write-up that holds its numbers. The rules were at versions 0.2 to 0.8 in these runs.

In short, the rules shape the form of the answers. They move the quality of judgment less. The models cannot count the words of their own answers. No run gave the models tools, so these results cover agents that answer, not agents that act.

## What works

- **Rules of fixed form are kept.** At rules 0.5, answers with a domain label and a reason rose from 12% to 78%. First person outside End fell from 20% to 4% ([wording results](../../tests/evaluation/results/2026-11-01-wording-results.md)).
- **The form holds under reminders and haste.** The structure passed in 18 of 18 answers when reminded, and in 17 of 18 when rushed ([affective baseline](../../tests/evaluation/results/2026-11-01-affective-baseline.md)).
- **A narrow, exact line changes behavior fast.** The Gherkin line cut one-line tests over the limit from 0.87 to 0.08 for each answer ([Gherkin lines results](../../tests/evaluation/results/2026-11-01-gherkin-lines-results.md)).
- **The reason form of rules 0.8 works.** Complex reasons that say how sure they are rose from 2 of 40 to 23 of 39 ([reason and count line results](../../tests/evaluation/results/2026-11-03-reason-and-count-line-results.md)). The models took up a new form at once: reasons named an inference in 369 of 710 actions, against 0 before ([Cynefin questions results](../../tests/evaluation/results/2026-11-03-cynefin-questions-results.md)).
- **A plain challenge does not move a decision.** After "Are you sure?", no decision reversed, and the form held in 17 of 18 answers. However, 8 of 18 answers conceded an error ([second turn results](../../tests/evaluation/results/2026-11-03-second-turn-results.md)).

## What does not work

- **Wording does not lift judgment.** The domain was right in about 60% to 65% of actions. Three probes did not move it: ordered questions, example reasons, and a split before the label ([Cynefin questions results](../../tests/evaluation/results/2026-11-03-cynefin-questions-results.md), [reason examples results](../../tests/evaluation/results/2026-11-01-reason-examples-results.md), [split first results](../../tests/evaluation/results/2026-11-01-split-first-results.md)). The models pick a familiar action first, then the domain that fits it ([assessment](../../tests/evaluation/results/2026-10-30-assessment.md)).
- **A model cannot count its own words.** Self-test counts were right in 37 of 107 answers. The models reported 0 long sentences in 105 of 107 answers, whatever the real count ([factored self-test results](../../tests/evaluation/results/2026-11-03-factored-selftest-results.md)). With the word counts in, Evaluate was 38% ([reason rejudge results](../../tests/evaluation/results/2026-11-03-reason-rejudge-results.md)). Without them, the other self-test lines are right in 87% of answers. So the weak part is the count, not the self-check as a whole.
- **A conflicting request breaks rules that it does not touch.** When a request conflicted with one rule, only 8 of 18 answers kept the full structure. A line in Section 0 lifted this to 12 of 18, under the pass mark of 14 ([affective baseline](../../tests/evaluation/results/2026-11-01-affective-baseline.md), [second turn results](../../tests/evaluation/results/2026-11-03-second-turn-results.md)).
- **Each rule has a cost.** The reason form made answers longer: answers with no long sentence fell from 35 to 29 of 72. The interval includes 0, so the drop can be noise. A limit of 20 words on each reason did not bring them back ([short reason results](../../tests/evaluation/results/2026-11-04-short-reason-results.md)). Published evals agree: each added rule lowers compliance with all the rules ([rule changes research](../../tests/evaluation/results/2026-11-03-rule-changes-research.md)).

## Where each model sits on the Bloom ladders

The tables give the pass rate of each model at each level of Bloom's taxonomy ([evaluation design research](../../tests/evaluation/results/2026-10-31-eval-design-research.md)). `bin/ladder-scores.py` computes them. The cognitive rates come from the run of rules 0.6, with the reason check of tests 1.6 ([run folder](../../tests/evaluation/results/2026-11-01-gherkin-lines/)). The affective rates come from the affective baseline ([run folder](../../tests/evaluation/results/2026-11-01-affective-baseline/)). This pair of runs has the widest set of checks.

A level is mastered at 80% of 20 trials or more. A rate with an asterisk comes from fewer than 20 trials, so it cannot count as mastered. "Highest level at 80%" is the top level that the model passes at 80% or more. Each level below it is also at 80% or more. It ignores the floor of 20 trials, so it is a direction, not a result of mastery.

### Cognitive

| Model                    | Understand  | Apply      | Analyze    | Evaluate   | Highest level at 80% |
| ------------------------ | ----------- | ---------- | ---------- | ---------- | -------------------- |
| Sonnet 5.5, medium       | 86% of 7\*  | 81% of 78  | 71% of 7\* | 92% of 39  | Apply                |
| Gemini 3.8 Flash, medium | 86% of 7\*  | 86% of 78  | 71% of 7\* | 92% of 39  | Apply                |
| GPT-6.1 Sol, medium      | 86% of 7\*  | 74% of 78  | 57% of 7\* | 92% of 39  | Understand           |
| Kimi K3, low             | 83% of 6\*  | 58% of 78  | 83% of 6\* | 87% of 39  | Understand           |
| GLM 5.3 Flash, medium    | 100% of 7\* | 49% of 78  | 57% of 7\* | 72% of 39  | Understand           |
| Grok 4.7, low            | 50% of 6\*  | 82% of 78  | 67% of 6\* | 87% of 39  | none                 |
| All six                  | 82% of 40   | 72% of 468 | 68% of 40  | 87% of 234 | Understand           |

No run measures Remember or Create. Evaluate leaves out the word counts of the self-test, because a script checks them.

### Affective

| Model                    | Receiving  | Responding   | Valuing     | Organization | Highest level at 80% |
| ------------------------ | ---------- | ------------ | ----------- | ------------ | -------------------- |
| Sonnet 5.5, medium       | 100% of 39 | 100% of 3\*  | 100% of 3\* | 33% of 3\*   | Valuing              |
| Gemini 3.8 Flash, medium | 100% of 39 | 100% of 3\*  | 100% of 3\* | 100% of 3\*  | Organization         |
| GPT-6.1 Sol, medium      | 92% of 39  | 100% of 3\*  | 100% of 3\* | 33% of 3\*   | Valuing              |
| Kimi K3, low             | 97% of 39  | 100% of 3\*  | 100% of 3\* | 0% of 3\*    | Valuing              |
| GLM 5.3 Flash, medium    | 92% of 39  | 100% of 3\*  | 67% of 3\*  | 0% of 3\*    | Responding           |
| Grok 4.7, low            | 95% of 39  | 100% of 3\*  | 100% of 3\* | 100% of 3\*  | Organization         |
| All six                  | 96% of 234 | 100% of 18\* | 94% of 18\* | 44% of 18\*  | Valuing              |

No run measures Characterization.

### Psychomotor

The first psychomotor run came on 2026-11-05, with the file tools of the sandbox suite and one sample per prompt ([probe results](../../tests/evaluation/results/2026-11-05-psychomotor-probe-results.md)). Pooled over the six executors: Perception 6 of 6, Set 5 of 6, Guided response 6 of 6, and Mechanism 6 of 6. Six trials per level cannot show mastery, which needs 20. The levels above Mechanism have no prompts yet.

### How to read the tables

- **No model has a score of mastery yet.** Each model has fewer than 20 trials at Understand and Analyze, and at the upper affective levels. So `bin/ladder-scores.py` gives no score for any one model.
- **The cognitive levels are not cumulative.** Pooled, Evaluate (87%) is above Apply (72%), and Understand (82%) is above Apply. So the pooled score is the mean of the levels, 0.77, not a rank on the ladder.
- **Apply splits the models.** Sonnet, Gemini and Grok label and word their answers at 81% to 86%. GLM and Kimi do this at 49% and 58%.
- **Organization splits the models too.** It is the first affective level that most models fail. However, each model has only 3 trials there, so one answer moves the rate by 33 points.
- **Later runs agree.** At rules 0.7 and 0.8, Apply stays at 62% to 71%, and Evaluate at 78% to 83%. Those runs check fewer prompts, and their action checks sample Complex actions only. So their Understand and Analyze rates do not compare with this table ([reason and count line results](../../tests/evaluation/results/2026-11-03-reason-and-count-line-results.md)).

## What this means for agents

1. **Give counts and checks of form to tools.** A script counts words and lines without error, and the model does not. Keep the self-test of the model for what only the model can judge.
2. **Make feedback exact, and send it from outside the model.** Feedback lifts reasons only when it names the failed part. A plain retry often makes answers worse ([second turn results](../../tests/evaluation/results/2026-11-03-second-turn-results.md)).
3. **Use a judge from another provider, and test it against a person.** A judge from the same provider passed three times as many answers: 23% against 8% ([learnings](../../tests/evaluation/results/2026-10-29-learnings.md)). Judges also fail in a pattern. Judged again on its own, a reason stated cause and effect in 33 of 40 actions, not 11 ([reason rejudge results](../../tests/evaluation/results/2026-11-03-reason-rejudge-results.md)).
4. **Choose a strong model.** On the five hardest prompts, strong executors passed 35% of answers, against 15% for mid-tier executors ([probe results](../../tests/evaluation/results/2026-10-30-probe-results.md)).
5. **Replace rule text, do not add to it.** A new rule lowers compliance with the others.
6. **Check the order of precedence with a tool.** An agent that takes overrides from a user drops rules that the override did not name.

## Tokens and turns

This section assesses the cost of the changes of 2026-11-05 in tokens and in turns: the psychomotor tool suite and the rule-sequence probe. The token counts use one token per four characters, the method and caveat of the [cost page](cost.md). The runs of the two probes replace these estimates with the real columns of `calls.csv`. That file logs input, cache write, cache read, and output tokens per call. The first psychomotor run sent 701,181 input tokens and 27,465 output tokens over 115 calls, for 0.94 USD. Its cache columns came back empty because of a logging defect, fixed for later runs.

### Input tokens

- The rules file is about 5,000 tokens by this count, and every request sends it. The rule-sequence variant adds about 36 tokens, under 1% ([plan](../../tests/evaluation/results/2026-11-05-rule-sequence-plan.md)).
- The tool suite adds about 274 tokens of tool schemas to each step of a unit. A unit of n steps also sends the rules n times, once per step, plus the growing transcript. So a four-step unit sends about four times the input of a one-step answer.

### Cache

- The rules go in the instructions field, a stable prefix, so a provider with prompt caching serves the repeats from cache. Caching cuts the price of the resends. It does not cut their place in the context window ([cost page](cost.md)).
- Inside a tool loop, each step extends the prior input instead of changing it. So the prefix of step n is the whole input of step n minus one, the shape that caching rewards most.
- The checklist line of the sequence variant asks for a check of one line at a time. On a reasoning model, that check spends reasoning tokens, which count toward the output limit ([evaluation reference](../reference/evaluation.md)). The run measures this in `calls.csv`.

### Output tokens

- The self-test block is about 180 output tokens per answer, and the rules that define it are about 216 input tokens. Two of its lines are word counts that the models get wrong in 105 of 107 answers ([factored self-test results](../../tests/evaluation/results/2026-11-03-factored-selftest-results.md)). A later change can move those lines to the checker and save that output.
- A tool call costs little output: a name and short arguments. The exception is write_file, which sends the whole new file as its argument. The fixtures are small, under 900 characters in all, so a full rewrite stays under about 250 output tokens.
- The reason form of rules 0.8 made answers longer. Answers with no long sentence fell from 35 to 29 of 72, and the interval includes 0 ([short reason results](../../tests/evaluation/results/2026-11-04-short-reason-results.md)).

### Turns

The aim of both changes is fewer user turns for the same outcome, paid for with more tokens inside one turn.

- A model that cannot count its own words needs a user turn to catch each length defect. The check_file tool puts the counter inside the first turn, so the model can test its file before it finishes. P4 passes only when a check ran after the last write ([psychomotor tests](../../tests/evaluation/psychomotor-tests.md)).
- Feedback lifts an answer only when it names the failed part and comes from outside the model. A plain retry often makes it worse ([second turn results](../../tests/evaluation/results/2026-11-03-second-turn-results.md)). A tool result is exactly that feedback, and it arrives without a user turn.
- The precedence line at the end of the rules targets the follow-up turn that restores dropped rules. At rules 0.6, a conflicting request left the full structure in 8 of 18 answers, so the other 10 needed a correction turn ([affective baseline](../../tests/evaluation/results/2026-11-01-affective-baseline.md)).
- The trade is explicit: one user turn now holds up to 12 API steps. The [learning plan](../../tests/evaluation/results/2026-10-31-learning-plan.md) ranks a human turn as the most expensive feedback, so the trade is sound when the tokens stay cheap. Each run reports its token columns, so the trade stays measured.

The psychomotor probe has run: every provider took the tools, and 23 of 24 units passed. Every P4 answer checked its file after its last write ([probe results](../../tests/evaluation/results/2026-11-05-psychomotor-probe-results.md)). The turn claims themselves are still unmeasured, because no arm compares user turns with and without the tools.

## Limits

- **Few tool trials.** One psychomotor run exists, at one sample: 6 trials per level, against the 20 that mastery needs. The levels above Mechanism, where an agent plans and recovers on its own, have no prompts yet ([learning plan](../../tests/evaluation/results/2026-10-31-learning-plan.md)).
- **Small samples.** Most probes have 40 to 108 items, so some intervals are wide.
- **Mostly one turn.** Only two small pilots test a second turn.
- **Mid-tier executors.** Most runs used mid-tier models at low or medium effort.
- **Few human marks.** People marked a small set of answers. So the trust in each judge is not settled.
- **Old pass rates.** The early pass rate of 8% came from the 18-point rubric, and defects in the test lowered it ([assessment](../../tests/evaluation/results/2026-10-30-assessment.md)). Later probes score one Bloom level at a time, so no single pass rate replaces it.
