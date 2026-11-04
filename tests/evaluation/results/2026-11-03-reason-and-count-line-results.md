# The reason form alone, and a self-test without the count line: results of two probes

## Headline

The reason form lifts how sure the reasons of Complex actions are. Removing the count line does not pass its test.

1. With the reason form, both judges pass how sure the reason is in 23 of 39 Complex actions, against 2 of 40 at rules 0.7. The gain is 54 points, with a 95% interval of 37 to 71.
2. The cost of the reason form is longer reasons. Answers with no long sentence fell from 35 to 29 of 72, and the interval includes 0.
3. Without the count line, answers with no long sentence fell from 63 to 56 of 108, a drop of 6 points. The pass mark allowed less than 5.
4. The two probes cost 16.86 USD. The rules stay at 0.7 until a release.

## Background

The Cynefin questions probe asked a reason to name its inference, and asked five ordered questions for the domain. Domains did not move, but reasons of Complex actions seemed to improve on only 7 actions. Separately, the models write 0 on the count line of the self-test whatever the real count. So the checker owns that count.

## Relevance

Understand needs reasons that say how sure they are, and Complex work is where they fail. A line in the self-test that the models ignore costs words on every prompt.

## Information

This section gives the runs, the results of each probe, and the known issues.

### The runs

E1. Three arms ran with no judge, each with the six main executors and three samples of each prompt.
[1]
[2]
[3]

| Arm | Rules | Prompts | Answers |
| --- | --- | --- | --- |
| Baseline | 0.7 | C1, K1, X1, X2, H1, H2, U1, T1, T2 | 162 |
| Reason form | 0.7.5: the reason item of Section 6.3 names its inference | X1, X2, T2, H2 | 72 |
| No count line | 0.7.6: the self-test drops "Sentences over the limit" | C1, K1, X1, H1, U1, T1 | 108 |

E2. The reason form drops the ordered questions of 0.7.4. Its reason item reads: "The reason names the inference: deduction from a known rule or analysis, induction from trials, or acting first. For induction, it names what could break the pattern." [2]

E3. Both judges checked 40 actions labelled Complex in each arm, on X1, X2, T2, and H2 only. A new option of judge-actions.py, --label with --prompts, keeps only those actions.
[1]
[2]

### The reason form

E4. The table gives the Complex actions that pass each check with both judges.
[1]
[2]

| Check | Baseline | Reason form | Gain (95% interval) |
| --- | --- | --- | --- |
| Reason says how sure the link is | 2 of 40 | 23 of 39 | +54 (+37 to +71) |
| Reason states cause and effect | 38 of 40 | 38 of 39 | +2 (-6 to +11) |
| Domain right | 39 of 40 | 39 of 39 | +3 (-2 to +7) |

E5. Argon is the strict judge of the new question. It passed 2 reasons before and 23 after, and the first judge passed 28 before and 37 after.
[1]
[2]

E6. The script rates of the same four prompts moved down, but each interval includes 0.
[1]
[2]

| Script rate | Baseline | Reason form | Change (95% interval) |
| --- | --- | --- | --- |
| No long sentence | 35 of 72 | 29 of 72 | -8 (-25 to +8) |
| LANGUAGE | 33 of 72 | 24 of 72 | -12 (-28 to +3) |
| Every label with a reason | 65 of 72 | 60 of 72 | -7 (-18 to +4) |
| Self-test right, without word counts | 56 of 72 | 56 of 72 | 0 |

E7. The new form led models to write a field "Reason:" after the domain. The checker read that field as the next field, not as a reason. This branch fixes the checker, which lifts the rate from 52 to 60 of 72. E6 gives the fixed rates. [2]

### The self-test without the count line

E8. The table gives the answers that pass each script check on the six prompts.
[1]
[3]

| Script rate | Baseline | No count line | Change (95% interval) |
| --- | --- | --- | --- |
| No long sentence | 63 of 108 | 56 of 108 | -6 (-20 to +7) |
| LANGUAGE | 59 of 108 | 50 of 108 | -8 (-22 to +5) |
| Self-test right, without word counts | 95 of 108 | 99 of 108 | +4 (-4 to +12) |
| Self-test right, every line | 55 of 108 | 99 of 108 | +41 (+30 to +52) |

The last row rises only because the line that the models get wrong is gone.

E9. The pass mark asked that no long sentence and Evaluate each drop by less than 5 points. Evaluate passes, and no long sentence fails by 1 point. The interval runs from -20 to +7, so the line may help or do nothing [inference].

### Known issues

- Seven executor calls of 342 failed with "upstream model is overloaded". Six were kimi and one was gpt. Each was sent again in a run of its own and passed, and its answer was copied into its arm.
- One Argon call of 160 failed the same way, so the reason form has 39 actions with both judges.
- The runner retries an HTTP error, but not a job that ends as failed. So an overload is lost unless it is sent again by hand.
- "Verdict" is now a banned word, and the checker finds it in model answers. Rescored runs flip LANGUAGE in 3 earlier answers, and 2 answers of each new arm hold the word.
- The baseline action checks sample Complex actions only. So its Understand and Analyze rates of bin/ladder-scores.py do not compare with other runs.

### Alternative considered

Release the reason form together with the removal of the count line. It loses, because the removal failed its pass mark, and the two changes would mix their effects on long sentences.

## End

I recommend that we release the reason form and keep the count line.

1. Release the reason form as rules 0.8.
   - Increment: the reason item of Section 6.3 from rules 0.7.5, with the version and changelog.
   - Blocker removed: Complex reasons that do not say how sure they are.
   - Kind: deterministic. Test:
     - Given the release branch
     - When task ci runs
     - Then the version line, version.json, and the changelog agree
   - Domain: Clear, because the release guide gives each step.
2. Probe a shorter reason form on long sentences.
   - Increment: a copy of 0.7.5 that limits the reason to one sentence of 20 words.
   - Capability added: the gain of E4 without the loss of E6.
   - Kind: stochastic. Metric: answers with no long sentence. Baseline: the reason form arm. Pass threshold: back within 3 points of rules 0.7, with E4 kept. Sample size: 72 answers. Budget: 3 USD. Stop condition: the spend passes 5 USD.
   - Domain: Complex, because how models shorten a reason shows only after a trial.
3. Retry a job that fails as overloaded.
   - Increment: run-evaluation.py retries a failed job whose message says overloaded, with the backoff of HTTP errors.
   - Blocker removed: lost calls that need a manual run.
   - Kind: deterministic. Test:
     - Given a job that fails as overloaded, then passes
     - When call runs
     - Then it returns the answer of the second job
   - Domain: Clear, because the retry of HTTP errors is the pattern.

## Follow-up

If the user prefers no release before Step 2, rules 0.8 waits for the shorter form.

### References

[1] tests/evaluation/results/2026-11-03-base-07: rules.md, responses, calls.csv, script-checks.csv, action-checks.csv, and action-checks-argon.csv, 2026. [P]

[2] tests/evaluation/results/2026-11-03-reason-form: the same files, 2026. [P]

[3] tests/evaluation/results/2026-11-03-no-count-line: rules.md, responses, calls.csv, and script-checks.csv, 2026. [P]

## Self-test

```text
Self-test
Questions asked: 0 of 3
Assumptions logged: 0
Claims with evidence or [judgment] label: yes
References: 3, all from session or identified with confidence: yes
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
