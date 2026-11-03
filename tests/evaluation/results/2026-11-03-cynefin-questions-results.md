# Domain questions and named inferences: results of the probe

## Headline

Ordered questions for the domain did not move the domains. The models adopted the new form of reason, but the probe fails its test.

1. Both judges found a right domain in 26 of 40 actions, against 24 of 38 at rules 0.6. The pass mark was 33.
2. The questions moved the errors, not their number. Before, the models labelled Clear work Complicated. After, they confused Complex and Complicated both ways.
3. Reasons named an inference in 369 of 710 labelled actions, against 0 before. Of 58 inductive reasons, 50 named what could break the pattern.
4. The probe cost 10.60 USD. Rules stay at 0.7, so no release follows.

## Background

The user gave eight sources on Cynefin and on inductive and deductive reasoning. They suggested two changes, tested together as rules 0.7.4. Section 6.5 asks five questions in order, and the first yes gives the domain. Section 6.3 asks the reason to answer that question and to name its inference.

## Relevance

Analyze, at 68%, was the weakest judged level after the rejudge of reasons. A rule that does not move it adds words to every prompt for no gain.

## Information

This section gives the run, the results, and why the domains did not move.

### The run

E1. The six main executors answered the 13 core prompts three times each, with no judge. One call of 234 failed. The two judges then checked 40 actions, sampled with seed 1.
[1]

E2. Both judges checked the same 40 actions of rules 0.6 again with the same three questions, so both runs face one judge prompt. The first judge failed on 2 calls.
[2]

### Results

E3. The table gives the actions that pass each check.
[1]

| Check | Rules 0.6, first judge | Rules 0.6, Argon | Probe, first judge | Probe, Argon |
| --- | --- | --- | --- | --- |
| Domain right | 27 of 38 | 26 of 40 | 28 of 40 | 26 of 40 |
| Reason states cause and effect | 34 | 36 | 36 | 36 |
| Reason says how sure the link is | 30 | 31 | 33 | 34 |

Both judges agree on a right domain in 24 of 38 actions before and 26 of 40 after. The gain is 2 points, with a 95% interval of -19 to +23.

E4. The pass mark for the new question was 20 of 40, set before anyone measured its baseline. The baseline already passed it at 30 and 31, so the question cannot show a gain, and it does not count toward the verdict.
[2]

E5. The new question bites only on Complex actions, where a reason from trials must name what could break the pattern. Those actions passed 3 and 0 of 4 before, and 6 and 4 of 7 after.
[1]

E6. No script rate dropped by more than 5 points. Every label with a reason fell from 73% to 69%, and every action labelled rose from 76% to 81%.
[1]

### Why the domains did not move

E7. The wrong domains, by the first judge, changed shape.
[1]

| Run | Most common errors |
| --- | --- |
| Rules 0.6 | Complicated for Clear work (4); Clear for Complex work (2) |
| Probe | Complex for Complicated work (3); Clear for Complex work (3); Complicated for Complex work (2) |

E8. The labels in the sample moved toward Clear and Complex. Clear rose from 16 to 20, Complicated fell from 15 to 10, and Complex rose from 4 to 7.
[1]

So question 2 pulled work into Clear, and the line between questions 3 and 4 is where the models now err [inference]. One source calls Complex work treated as Complicated the most common misclassification.
[3]

Another warns that the reverse leads to experiments that expertise could replace.
[4]

### Limits

- Forty actions detect only a gain of about 20 points.
- The sources are practitioner guides, and one states that few empirical studies of Cynefin exist [4].
- The sample holds only 7 Complex actions from the probe, so the stricter test of E5 rests on few cases.

### Alternative considered

Keep the reason form of Section 6.3 and drop the questions, since the models adopted it and E5 points up. It loses for now, because E5 rests on 7 actions and E3 shows no gain in reasons overall.

## End

I recommend that we keep rules 0.7, and test the reason form on Complex actions alone.

1. Record the probe and the third judge question.
   - Increment: this write-up, the run folder, and the verdicts of the baseline with three questions.
   - Blocker removed: a stricter measure of reasons, which the user's marks asked for.
   - Kind: deterministic. Test:
     - Given the probe folder
     - When judge-actions.py runs with --plan
     - Then it prints 40 actions from 6 executors
   - Domain: Clear, because the scripts have tests.
2. Probe the reason form of Section 6.3 alone, on Complex actions only.
   - Increment: the 6.3 line in a rules file, and runs of X1, X2, T2, and H2, which expect Complex work.
   - Capability added: a test of the stricter Understand level with enough cases.
   - Kind: stochastic. Metric: Complex actions whose reason names what could break the pattern, by both judges. Baseline: the same prompts at rules 0.7, judged first. Pass threshold: 20 points over the baseline, with the interval above 0. Sample size: 40 Complex actions in each arm. Budget: 8 USD. Stop condition: the spend passes 10 USD.
   - Domain: Complex, because E5 points up on only 7 actions.
3. Give the line between Complicated and Complex a test the models can apply.
   - Increment: one matched pair for each of 5 scenarios, differing only in whether an expert could predict the result.
   - Capability added: an item that isolates the error of E7.
   - Kind: evaluative. Rubric: each pair differs in one fact (weight 2); a person agrees with the expected domains (weight 1). Pass threshold: both.
   - Domain: Complicated, because writing the pairs needs expert reading.

## Follow-up

If Step 2 passes, Section 6.3 changes in rules 0.8 without the questions of Section 6.5.

### References

[1] tests/evaluation/results/2026-11-03-cynefin-questions: rules.md, responses, calls.csv, script-checks.csv, action-checks.csv, and action-checks-argon.csv, 2026. [P]

[2] tests/evaluation/results/2026-11-01-gherkin-lines: action-checks-certainty.csv and action-checks-argon-certainty.csv, 2026. [P]

[3] J. Ellis, "The Cynefin Framework: A Practical Guide for Complex Decision-Making," The Systems Thinking, 2026, <https://thesystemsthinking.com/cynefin-framework-complex-decision-making/>. [T]

[4] SI Labs, "Cynefin Framework," 2026, <https://www.si-labs.com/en/articles/cynefin-framework/>. [T]

## Self-test

```text
Self-test
Questions asked: 0 of 3
Assumptions logged: 0
Claims with evidence or [judgment] label: yes
References: 4, all from session or identified with confidence: yes
Source types tagged (P/S/T/U): yes, primary or secondary behind each driving claim: yes
Alternative considered: yes
Recommendation: 3 actions, each with increment, blocker, test: yes
Each action classified (deterministic/evaluative/stochastic) with test written first: yes
Actions in End with a Cynefin domain label: 3 of 3
Chaotic and Confused actions first, Complex actions as capped probes: yes
Banned words found: 0
Self-mention outside End: 0
Transition present where a sentence depends on the prior one: yes
Dashes (em or en): 0
Sentences over the limit of Section 4.1 item 1: 0
```
