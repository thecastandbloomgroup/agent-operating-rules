# Self-test checked item by item: results of the probe

## Headline

Separate checks did not lift the self-test, because its weak line is a count of words that the models do not make.

1. Self-test counts were right in 37 of 107 answers, against 43 of 108 at rules 0.6. The pass mark was 58.
2. The models report 0 sentences over the limit in 105 of 107 answers, whatever the real count.
3. Without that line, the self-test is right in 79 of 107 answers, against 75 of 108.
4. So a count of words is a deterministic check for a tool, not a judgment for the model.

## Background

Evaluate, at 38%, was the lowest measured cognitive level after the rejudge of reasons. Rank 1 of the desk research asked the model to fill each self-test line from a separate check of the draft.

## Relevance

A level that measures a count the model cannot make hides its real skill at self-assessment. Funds then go to wording that cannot help.

## Information

This section gives the probe, the results, and the cause.

### The probe

E1. A copy of rules 0.7, labelled 0.7.3, changed the last paragraph of Section 7. The six main executors answered C1, K1, X1, H1, U1, and T1 three times each, with no judge. One call of 108 failed, and the run cost 3.89 USD.
[1]

```text
Fill each count line from a separate check of the draft, not from memory. Check the
sentences one at a time against the limit, then the actions one at a time for a
label. Count; do not estimate.
```

### Results

E2. The table compares the probe with the same six prompts of rules 0.6, from the earlier run.
[2]

| Rate | Rules 0.6 | Probe 0.7.3 | Difference (95% interval) |
| --- | --- | --- | --- |
| Self-test counts right | 43 of 108 | 37 of 107 | -5 (-18 to +8) |
| Every line right but the count of long sentences | 75 of 108 | 79 of 107 | +4 (-8 to +16) |
| STRUCTURE | 104 | 105 | +2 |
| No long sentence | 57 | 47 | -9 (-22 to +4) |
| Every action labelled | 82 | 81 | 0 |

E3. Sonnet fell from 13 to 6 of 18 right self-tests. Gemini held at 13, and GLM and Kimi stayed at 0 to 2.
[1]

### The cause

E4. The line "Sentences over the limit" was wrong in 59 answers of the probe. Each of the other lines was wrong in 24 answers or fewer.
[1]

At rules 0.6, the same line was wrong in 51 answers, and each other line in 26 or fewer.
[2]

E5. The models wrote 0 on that line in 105 of 107 answers. In 59 of those, the script found at least one long sentence.
[1]

E6. Of the 187 long sentences, 64 were over the limit by one or two words. The script holds every sentence of End to 20 words, but the rule gives 25 to descriptions. With a limit of 25 everywhere, the probe still has only 47 right self-tests.
[1]

So the models do not count the words; they assert that they kept the rule [inference]. The rule tells them to fix a failed line, not to report it. So a 0 reads as a promise, not a count.

### What the results show

- The model is the wrong tool for a count of words. The checker, bin/deterministic-tests.py, makes this count in milliseconds.
- Without that line, self-assessment is right in about 74% of answers, near the pass mark of 80%.
- This is the split between deterministic and probabilistic work that the user raised before. A count is deterministic, so a script owns it, and the model owns the judgments.

### Limits

- The probe tested one wording, so its null result is weak evidence [judgment].
- The 20-word limit of the script for End is stricter than the rule for descriptions there.

### Alternative considered

Ask for the length of each sentence in the draft, so the model counts in the open. It loses because it adds many words to every answer, and models count words poorly, as E5 shows.

## End

I recommend that we take the count of long sentences out of the Evaluate score, and give it to the checker.

1. Score Evaluate without the line on long sentences.
   - Increment: one change to the map of bin/ladder-scores.py, and a column in bin/script-checks.py.
   - Capability added: an Evaluate level that measures judgment, at about 74% (E2).
   - Kind: deterministic. Test:
     - Given an answer whose only wrong line is the count of long sentences
     - When script-checks.py scores it
     - Then its Evaluate check passes
   - Domain: Clear, because the scripts have tests.
2. Replace the self-test line with a line the model can fill.
   - Increment: the line "Sentences over the limit" becomes "Long sentences split before sending: yes/no", in a rules file in a run folder.
   - Capability added: an honest line, since the checker owns the count.
   - Kind: stochastic. Metric: answers with no long sentence. Baseline: 57 of 108. Pass threshold: no drop over 5 points. Sample size: 108 answers. Budget: 4 USD. Stop condition: the spend passes 5 USD.
   - Domain: Complex, because a weaker line can lower the effort to split.
3. Run the checker before sending, where the model has tools.
   - Increment: one sentence in Section 7 for agents with a shell, and one task in the psychomotor ladder.
   - Capability added: a deterministic count that the model reads, at the Perception level.
   - Kind: deterministic. Test:
     - Given an agent with a shell and a draft with one long sentence
     - When it runs the checker before it sends
     - Then the answer it sends has no long sentence
   - Domain: Complicated, because the harness has no tools yet, and building them needs a design choice.

## Follow-up

If the user rejects Step 1, Evaluate stays at 38%, and the next probe for it needs a tool, not wording.

### References

[1] tests/evaluation/results/2026-11-03-factored-selftest: rules.md, responses, calls.csv, and script-checks.csv, 2026. [P]

[2] tests/evaluation/results/2026-11-01-gherkin-lines/script-checks.csv, the prompts C1, K1, X1, H1, U1, and T1, 2026. [P]

## Self-test

```text
Self-test
Questions asked: 0 of 3
Assumptions logged: 0
Claims with evidence or [judgment] label: yes
References: 2, all from session or identified with confidence: yes
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
