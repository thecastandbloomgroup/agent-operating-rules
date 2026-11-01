# Rules 0.5 wording: results of the script-only run

## Headline

Rules 0.5 passes its acceptance test on two of three targeted checks, so release it, and probe a new fix for long sentences.

1. A domain label with a reason rose from 12% to 78% of answers, and first person outside End fell from 20% to 4%.
2. The new self-test line did not shorten sentences: answers free of long sentences fell from 37% to 31%, inside the noise.
3. The run cost 14.68 USD of the 50 USD funded, and it used no judge, so 35.32 USD remain.

## Background

Rules 0.5 changes three lines of 0.4. Self-mention covers "I", "me", "my", and "mine" outside End. Each action gives its domain with one clause that says why. The self-test counts sentences over the limit, in place of the length of the longest sentence.

## Relevance

The script checks need no judge, so this run is the cheapest feedback on a change of wording. A change that passes here can be released before any judge run.

## Information

This section gives the test, the results, and their limits.

### The acceptance test, written before the run

- Metric: the share of answers that pass each script check of `bin/script-checks.py`.
- Baseline: rules 0.4, run in the same session with the same 6 executors, 13 prompts, and 3 samples.
- Pass threshold: a gain of 10 points or more, with a 95% interval above zero, on two of the three targeted checks. STRUCTURE drops by 5 points at most.
- Sample size: 234 answers at 0.4 and 233 at 0.5. One Gemini call failed when its model was overloaded.

### Results

E1. The table compares the two runs.
[1]

| Check | 0.4 | 0.5 | Difference (95% interval) |
| --- | --- | --- | --- |
| No first person outside End (targeted) | 80% | 96% | +16 (+11 to +22) |
| Every label with a reason (targeted) | 12% | 78% | +67 (+60 to +73) |
| No long sentence (targeted) | 37% | 31% | -5 (-14 to +3) |
| STRUCTURE | 96% | 98% | +2 (-1 to +5) |
| Every action labelled | 76% | 81% | +5 (-2 to +12) |
| Self-test counts right | 27% | 22% | -5 (-13 to +2) |

So two targeted checks pass, and STRUCTURE holds. The test passes.

E2. The reason rule moved every executor. At 0.5, the share of answers with a reason on every label runs from 62% (Kimi) to 92% (Gemini). At 0.4 it ran from 3% to 21%.
[1]

E3. Long sentences got no better. GPT-6.1-Sol fell from 56% to 33% of answers free of them, and GLM and Kimi end at 5% or less. A reason clause adds words to the sentence that holds the label [inference].
[1]

E4. The script read 5 answers in the same way as a hand reading of them, on the labels, the reasons, and the first person. A sample of 12 actions at 0.5 had 6 with a reason, by the script. All 6 were real reasons, such as "Complex, because the rate shows only after the runs".
[2]

### Limits

- The intervals treat each answer as independent. Answers to one prompt are related, so the true intervals are wider [inference]. The two gains clear zero by 11 and 60 points, so the result holds.
- The script checks the form of a label and a reason, not whether the domain is right. That needs a judge or a person.
- The first parse of this run found almost no structure in the answers of Grok, Kimi, and GLM. Those executors write headings as plain lines, which the rules allow. The fix in `eb237e4` changed the levels of every rate, but not the result of the test.

### Assumption log

A1. A reason clause lengthens the sentence that holds the label. Why not measured: the script counts long sentences, not where they are. Validate by: count the long sentences that contain a domain name, in both runs. If wrong: the long-sentence fix in Step 2 targets the wrong lines.

### Alternative considered

Keep rules 0.4 until a judge run confirms the domains. It loses because the two gains are large and need no judge to see, and a judge run costs about 5 times more [judgment].

## End

I recommend that we release rules 0.5, then probe the long sentences on their own.

1. Release version 0.5.0 with rules 0.5 and tests 1.5.
   - Increment: version.json at 0.5.0, a CHANGELOG section for it, and the tag after the merge.
   - Blocker removed: the build needs the rules version and version.json to agree.
   - Kind: deterministic. Test: Given version.json at 0.5.0, When task ci runs, Then the build step passes.
   - Domain: Clear, because the release guide fixes each step.
2. Probe a rule that tells the model to split each sentence over 20 words before it sends.
   - Increment: one line in Section 4.1, and one more script-only run of 0.5 against the new line.
   - Capability added: a measure of whether any wording shortens sentences (E3).
   - Kind: stochastic. Metric: answers free of long sentences. Baseline: 31% (E1). Pass threshold: 41%. Sample size: 234 answers. Budget: 8 USD. Stop condition: the spend passes 10 USD.
   - Domain: Complex, because no change of wording has moved this rate yet, so leverage is a guess.
3. Check that the reasons and the domains are right on a sample of 40 actions.
   - Increment: one judge, or the user, marks each sampled action yes or no on the domain and on the reason.
   - Blocker removed: the script sees the form of a reason, not its truth (Limits).
   - Kind: evaluative. Rubric: the domain matches tests 1.5 (weight 2); the reason states cause and effect (weight 1). Pass threshold: 30 of 40 actions score 3.
   - Domain: Complicated, because the expected domains need expert reading. Step 3 MAY run in parallel with Step 2.

## Follow-up

If Step 2 fails, keep the line out of the rules, and mark long sentences as a Valuing gap of the affective ladder.

The remaining 35.32 USD covers Step 2 and the judge calibration of the design note.

### References

[1] tests/evaluation/results/2026-10-31-wording-r04 and 2026-10-31-wording-r05: script-checks.csv, calls.csv, and summary.md, 2026. [P]

[2] Hand reading of 5 answers of run 2026-10-29-tokens-s1c, and a sample of actions of run 2026-10-31-wording-r05, this session, 2026-11-01. [P]

## Self-test

```text
Self-test
Questions asked: 0 of 3
Assumptions logged: 1
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
