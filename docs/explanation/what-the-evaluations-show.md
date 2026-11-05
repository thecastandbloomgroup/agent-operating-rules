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

No run measures Characterization. No run measures any level of the psychomotor ladder, because the harness gives the models no tools.

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

## Limits

- **No tools.** The harness gives the models no tools. So nothing measures the psychomotor domain, where an agent acts and damage happens ([learning plan](../../tests/evaluation/results/2026-10-31-learning-plan.md)).
- **Small samples.** Most probes have 40 to 108 items, so some intervals are wide.
- **Mostly one turn.** Only two small pilots test a second turn.
- **Mid-tier executors.** Most runs used mid-tier models at low or medium effort.
- **Few human marks.** People marked a small set of answers. So the trust in each judge is not settled.
- **Old pass rates.** The early pass rate of 8% came from the 18-point rubric, and defects in the test lowered it ([assessment](../../tests/evaluation/results/2026-10-30-assessment.md)). Later probes score one Bloom level at a time, so no single pass rate replaces it.
