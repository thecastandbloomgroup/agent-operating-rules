# What the evaluations show

This page sums up what the evaluation runs from 2026-10-28 to 2026-11-05 say about the use of the rules with agents. Each claim links to the write-up that holds its numbers. The rules were at versions 0.2 to 0.8 in these runs.

In short, the rules shape the form of the answers. They move the quality of judgment less. The models cannot count the words of their own answers. No run gave the models tools, so these results cover agents that answer, not agents that act.

## What works

- **Rules of fixed form are kept.** At rules 0.5, answers with a domain label and a reason rose from 12% to 78%. First person outside End fell from 20% to 4% ([wording results](../../tests/evaluation/results/2026-11-01-wording-results.md)).
- **The form holds under reminders and haste.** The structure passed in 18 of 18 answers when reminded, and in 17 of 18 when rushed ([affective baseline](../../tests/evaluation/results/2026-11-01-affective-baseline.md)).
- **A narrow, exact line changes behavior fast.** The Gherkin line cut one-line tests over the limit from 0.87 to 0.08 for each answer ([Gherkin lines results](../../tests/evaluation/results/2026-11-01-gherkin-lines-results.md)).
- **The reason form of rules 0.8 works.** Complex reasons that say how sure they are rose from 2 of 40 to 23 of 39 ([reason and count line results](../../tests/evaluation/results/2026-11-03-reason-and-count-line-results.md)). The models took up a new form at once: reasons named an inference in 369 of 710 actions, against 0 before ([Cynefin questions results](../../tests/evaluation/results/2026-11-03-cynefin-questions-results.md)).
- **A plain challenge does not move a decision.** After "Are you sure?", no decision reversed, and the form held in 17 of 18 answers. However, 8 of 18 answers conceded an error ([second turn results](../../tests/evaluation/results/2026-11-03-second-turn-results.md)).

## What does not work

- **Wording does not lift judgment.** The judges called the domain right in about 60% to 65% of actions. That rate is the judges' view, and it does not match the user's (see the next item). Three probes did not move it: ordered questions, example reasons, and a split before the label ([Cynefin questions results](../../tests/evaluation/results/2026-11-03-cynefin-questions-results.md), [reason examples results](../../tests/evaluation/results/2026-11-01-reason-examples-results.md), [split first results](../../tests/evaluation/results/2026-11-01-split-first-results.md)). The models pick a familiar action first, then the domain that fits it ([assessment](../../tests/evaluation/results/2026-10-30-assessment.md)).
- **The judges do not match a person on domain fit.** In a blind marking of 24 actions, the first judge matched the user in 11 rows (kappa -0.20). The second judge matched in 8 (kappa -0.40). The two judges agreed with each other in 19 rows, but the user gave the same answer in only 7. The user's notes say that a step that needs expertise is Complicated ([judge trust results](../../tests/evaluation/results/2026-11-05-judge-trust-results.md)). An instruction built from those notes did not lift either judge above -0.20 ([judge themes results](../../tests/evaluation/results/2026-11-05-judge-themes-results.md)). The user's own marks on the other rows, given as examples, lifted both judges only to chance: kappa -0.01 ([leave-one-out results](../../tests/evaluation/results/2026-11-05-judge-loo-results.md)). The judges see the expected answer of each test, so the domain rates measure fit to the test, not fit to the work. With no expected answer, both judges rose to a kappa of about 0.22 in each of three runs ([reruns results](../../tests/evaluation/results/2026-11-06-judge-reruns-results.md)). On 104 actions, that judge found the domain right in 76%, against 69% for fit to the test. However, the two questions split by label: the judge of the work accepts every Complicated label and rejects most Chaotic ones ([work rejudge results](../../tests/evaluation/results/2026-11-06-judge-work-results.md)). In 6 of the 15 actions where they split, the test itself disagrees with the user's marks, on prompts H2 and T1 ([split review](../../tests/evaluation/results/2026-11-06-split-test-review.md)).
- **A model cannot count its own words.** Self-test counts were right in 37 of 107 answers. The models reported 0 long sentences in 105 of 107 answers, whatever the real count ([factored self-test results](../../tests/evaluation/results/2026-11-03-factored-selftest-results.md)). With the word counts in, Evaluate was 38% ([reason rejudge results](../../tests/evaluation/results/2026-11-03-reason-rejudge-results.md)). Without them, the other self-test lines are right in 87% of answers. So the weak part is the count, not the self-check as a whole.
- **A conflicting request breaks rules that it does not touch.** When a request conflicted with one rule, only 8 of 18 answers kept the full structure. A line in Section 0 lifted this to 12 of 18, under the pass mark of 14 ([affective baseline](../../tests/evaluation/results/2026-11-01-affective-baseline.md), [second turn results](../../tests/evaluation/results/2026-11-03-second-turn-results.md)). However, a second turn that names the dropped parts repairs 10 of 12 such answers after the fact ([repair results](../../tests/evaluation/results/2026-11-05-structure-repair-results.md)).
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

The table pools the runs of 2026-11-06 and 2026-11-07 over the six executors: 20 trials per model and 120 per level ([20-trial results](../../tests/evaluation/results/2026-11-07-psychomotor-20-results.md)). They used rules 0.9 and the four file tools of the sandbox suite. The interval is a 95% Wilson interval, and the last column counts the units that hit the step cap.

| Level                  | Passed     | 95% interval | Mastered at 80% of 20 or more | At the step cap |
| ---------------------- | ---------- | ------------ | ----------------------------- | --------------- |
| Perception             | 110 of 120 | 85% to 95%   | yes, 92%                      | 7               |
| Set                    | 106 of 120 | 81% to 93%   | yes, 88%                      | 4               |
| Guided response        | 113 of 120 | 88% to 97%   | yes, 94%                      | 7               |
| Mechanism              | 112 of 120 | 87% to 97%   | yes, 93%                      | 8               |
| Complex overt response | 90 of 120  | 67% to 82%   | no, 75%                       | 0               |
| Adaptation             | 109 of 120 | 84% to 95%   | yes, 91%                      | 11              |
| Origination            | 105 of 120 | 80% to 92%   | yes, 88%                      | 1               |

So the levels are not cumulative: Origination passes more often than Complex overt response. Complex overt response is the one level where the pool stays under 80%. In 27 of its 30 failures, a move across two files ends with a write that no check follows. GPT-6.1 Sol has 17 of them. In 10 of the 14 Set failures, a model writes plan.md to another folder with no look first. The other 4 are Gemini units at the cap, and each step-cap unit but one is Gemini's.

The earlier runs of 2026-11-05 gave Set 17 of 24 and Complex overt response 14 of 24 ([four-sample results](../../tests/evaluation/results/2026-11-05-psychomotor-s4-results.md)). A later control with rules 0.9 passed P5 in 19 of 24, so this level varies by day. In that run, a check of text that writes no file cost Sonnet 4 passes ([check text results](../../tests/evaluation/results/2026-11-06-check-text-results.md)). The main P5 failure has a repair. A second turn that names the missing check fixed 5 of 5 such units, against 1 of 5 for a plain retry ([P5 repair results](../../tests/evaluation/results/2026-11-05-p5-repair-results.md)).

Gemini loses its low levels to a loop at the step cap. In that loop, it checks drafts of its answer in scratch files ([P1 to P7 results](../../tests/evaluation/results/2026-11-06-psychomotor-p1-p7-results.md)). Gemini passed 24 of 24 on P1 to P3 with a three-sentence note, against 11 of 24 without ([sandbox note results](../../tests/evaluation/results/2026-11-06-sandbox-note-results.md)). The sentence that does the work forbids other files, and it also names a fail of P2 and P5. A note on where the answer goes did not help alone ([answer note results](../../tests/evaluation/results/2026-11-06-answer-note-results.md)). A script grades the form of each P7 procedure, and a judge scores its quality. The judge passes 28 of 43 procedures at 85 of 100 with no criterion at 0 ([P7 results](../../tests/evaluation/results/2026-11-06-p7-origination-results.md)).

Each of the six models has 20 trials per level from 2026-11-06 and 2026-11-07 ([20-trial results](../../tests/evaluation/results/2026-11-07-psychomotor-20-results.md)). Only Sonnet 5.5 reaches 80% on every level.

| Model            | Score | Weakest level                    | Units at the step cap |
| ---------------- | ----- | -------------------------------- | --------------------- |
| Sonnet 5.5       | 1.00  | Origination, 18 of 20            | 0                     |
| Kimi K3          | 0.96  | Complex overt response, 17 of 20 | 0                     |
| Grok 4.7         | 0.91  | Set, 13 of 20                    | 0                     |
| GLM 5.3 Flash    | 0.89  | Complex overt response, 12 of 20 | 1                     |
| GPT-6.1 Sol      | 0.88  | Complex overt response, 3 of 20  | 0                     |
| Gemini 3.8 Flash | 0.70  | Adaptation, 9 of 20              | 37                    |

GPT-6.1 Sol fails P5 because it skips the last check. Gemini's low levels come from the loop at the step cap, and it passes P5 and P7 in 20 of 20.

### How to read the tables

- **No model has a score of mastery yet.** Each model has fewer than 20 trials at Understand and Analyze, and at the upper affective levels. So `bin/ladder-scores.py` gives no score for any one model.
- **The cognitive levels are not cumulative.** Pooled, Evaluate (87%) is above Apply (72%), and Understand (82%) is above Apply. So the pooled score is the mean of the levels, 0.77, not a rank on the ladder.
- **Apply splits the models.** Sonnet, Gemini and Grok label and word their answers at 81% to 86%. GLM and Kimi do this at 49% and 58%.
- **Organization splits the models too.** It is the first affective level that most models fail. However, each model has only 3 trials there, so one answer moves the rate by 33 points.
- **Later runs agree.** At rules 0.7 and 0.8, Apply stays at 62% to 71%, and Evaluate at 78% to 83%. Those runs check fewer prompts, and their action checks sample Complex actions only. So their Understand and Analyze rates do not compare with this table ([reason and count line results](../../tests/evaluation/results/2026-11-03-reason-and-count-line-results.md)).

## What this means for agents

1. **Give counts and checks of form to tools.** A script counts words and lines without error, and the model does not. Keep the self-test of the model for what only the model can judge.
2. **Make feedback exact, and send it from outside the model.** Feedback lifts reasons only when it names the failed part. A plain retry often makes answers worse ([second turn results](../../tests/evaluation/results/2026-11-03-second-turn-results.md)).
3. **Use a judge from another provider, and test it against a person.** Two judges that agree are not proof. On domain fit, the user gave another answer in 12 of the 19 rows where both judges agreed ([judge trust results](../../tests/evaluation/results/2026-11-05-judge-trust-results.md)). A judge from the same provider passed three times as many answers: 23% against 8% ([learnings](../../tests/evaluation/results/2026-10-29-learnings.md)). Judges also fail in a pattern. Judged again on its own, a reason stated cause and effect in 33 of 40 actions, not 11 ([reason rejudge results](../../tests/evaluation/results/2026-11-03-reason-rejudge-results.md)).
4. **Choose a strong model.** On the five hardest prompts, strong executors passed 35% of answers, against 15% for mid-tier executors ([probe results](../../tests/evaluation/results/2026-10-30-probe-results.md)).
5. **Replace rule text, do not add to it.** A new rule lowers compliance with the others.
6. **Check the order of precedence with a tool.** An agent that takes overrides from a user drops rules that the override did not name.

## Tokens and turns

This section assesses the cost of the changes of 2026-11-05 in tokens and in turns: the psychomotor tool suite and the rule-sequence probe. The token counts use one token per four characters, the method and caveat of the [cost page](cost.md). The runs of the two probes replace these estimates with the real columns of `calls.csv`. That file logs input, cache write, cache read, and output tokens per call. The four-sample run sent 2,931,985 input tokens over 478 calls for 3.42 USD, and the cache served 54% of that input. So the loop's growing-prefix shape pays off as the cache section expects.

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

Every provider took the tools, and 48 of 48 pooled units passed Guided response and Mechanism in the four-sample run. Every passing P4 answer checked its file after its last write ([four-sample results](../../tests/evaluation/results/2026-11-05-psychomotor-s4-results.md)).

The repair claim is now measured on one side. A turn that names the broken parts repaired 10 of 12 answers, against 3 of 12 for a plain retry ([repair results](../../tests/evaluation/results/2026-11-05-structure-repair-results.md)). So a broken answer costs one extra call instead of a user correction turn. No arm yet compares whole sessions with and without the tools.

## Limits

- **Twenty trials is a floor.** Each model has 20 tool trials per level, the least that a mastery call needs. A 95% Wilson interval on 20 of 20 runs from 84% to 100%, so a call at 20 trials can flip on a rerun.
- **Wide intervals.** With 24 trials, a 95% Wilson interval spans about 30 points. For example, Complex overt response at 18 of 24 runs from 55% to 88%, and Perception at 21 of 24 from 69% to 96%. So a level marked as mastered at 24 trials can fall under 80% on a rerun. A model with a true rate of 90% needs about 53 trials before its interval clears 80%. The large pools are tighter: Apply at 72% of 468 runs from 68% to 76%.
- **Few second turns.** Three studies test a second turn, with 5 to 18 units per arm, and none tests a third. A turn that names the failed part repaired 10 of 12 broken answers and 5 of 5 unchecked writes, against 3 of 12 and 1 of 5 for a plain retry ([structure repair results](../../tests/evaluation/results/2026-11-05-structure-repair-results.md), [P5 repair results](../../tests/evaluation/results/2026-11-05-p5-repair-results.md)). A plain "Are you sure?" changed no decision in 18 answers ([second turn results](../../tests/evaluation/results/2026-11-03-second-turn-results.md)).
- **Mid-tier executors.** Most runs used mid-tier models at low or medium effort. A run of strong executors on every ladder costs more than the funds left, so it waits on a budget decision.
- **One human marker.** One person marked 24 actions, chosen to hold every judge split. So the judge kappas below 0 say the judges miss this user. They are not a rate for every user ([judge trust results](../../tests/evaluation/results/2026-11-05-judge-trust-results.md)). A second marker needs a person.
- **Old pass rates.** The early pass rate of 8% came from the 18-point rubric, and defects in the test lowered it ([assessment](../../tests/evaluation/results/2026-10-30-assessment.md)). Later probes score one Bloom level at a time, so the tables above replace it.
