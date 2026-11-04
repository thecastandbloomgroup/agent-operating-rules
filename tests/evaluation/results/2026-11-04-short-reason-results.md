# A shorter reason: results of one probe

## Headline

A reason of one sentence of 20 words or fewer does not bring back answers with no long sentence.

1. Answers with no long sentence were 28 of 72 with the short reason, against 29 with the reason form and 35 at rules 0.7. The pass mark asked for 32 or more.
2. Labels with a reason fell from 60 to 52 of 72 answers, so the limit costs reasons too.
3. Sentences with a domain label are rarely long in any arm. So the long sentences come from other parts of the answers [inference].
4. The probe cost 2.22 USD. The judges did not run, because the probe failed on its first metric. The rules stay at 0.8.

## Background

The reason form of rules 0.8 lifted how sure Complex reasons are from 2 to 23 of 40 actions. In the same probe, answers with no long sentence fell from 35 to 29 of 72. That interval included 0, so the drop may be noise.

## Relevance

A short reason would keep the gain of rules 0.8 and remove its likely cost. If the cost does not sit in the reasons, a limit on them cannot remove it.

## Information

This section gives the run, the script checks, and the length of label sentences.

### The run

E1. Rules 0.8.1 limit the reason of each action to one sentence of 20 words or fewer. The rules file is in the run folder only.
[1]

E2. The run sent X1, X2, H2, and T2 to the six main executors, three samples each, with no judge. All 72 calls passed.
[1]

### Script checks

E3. The table compares the same four prompts in three arms. Each arm has 72 answers.
[1]
[2]
[3]

| Script rate | Rules 0.7 | Reason form (0.7.5) | Short reason (0.8.1) |
| --- | --- | --- | --- |
| No long sentence | 35 | 29 | 28 |
| LANGUAGE | 33 | 24 | 24 |
| Every label with a reason | 65 | 60 | 52 |
| STRUCTURE | 69 | 68 | 68 |

E4. Against the reason form, no long sentence moved by -1 point, with a 95% interval of -17 to +15. Labels with a reason fell 11 points, with an interval of -25 to +2.
[1]
[3]

### Length of label sentences

E5. A rough count split each label line of End into sentences. It kept the sentences that name a domain.
[1]
[2]
[3]

| Arm | Label sentences | Median words | Over 25 words |
| --- | --- | --- | --- |
| Rules 0.7 | 254 | 12 | 12 |
| Reason form | 201 | 9 | 6 |
| Short reason | 209 | 4 | 4 |

E6. The short reason did shorten label sentences, from a median of 9 words to 4. Yet the answers with long sentences did not fall. So the long sentences sit outside the label sentences [inference].

### Known issues

- The count of E5 splits on end marks and finds labels by domain names. It is a probe of where long sentences sit, not a script check.
- The probe ran before the overload retry, but no call failed.

### Alternative considered

Run the judges anyway, to see if the short reason keeps the gain of rules 0.8. It loses, because the probe fails on its first metric, and the judges would cost about 1.30 USD.

## End

I recommend that we keep rules 0.8 and find where the long sentences sit.

1. Record this probe and keep rules 0.8.
   - Increment: this write-up and the run folder, with a changelog entry.
   - Blocker removed: an open question on the cost of the reason form.
   - Kind: deterministic. Test:
     - Given the probe branch
     - When task ci runs
     - Then it passes
   - Domain: Clear, by deduction from the pass mark of the probe.
2. Find the sections of the answers that hold the long sentences, in the three arms.
   - Increment: a count by section of the long sentences of the checker, with no API call.
   - Capability added: a target for the next change to the rules on long sentences.
   - Kind: deterministic. Test:
     - Given the responses of the three arms
     - When the count runs
     - Then each long sentence of script-checks.csv has one section
   - Domain: Complicated, by deduction from an analysis of the answers.
3. Merge the retry of overloaded jobs.
   - Increment: the merge request of fix/eval-overload-retry.
   - Blocker removed: calls lost to an overload, which need a run by hand.
   - Kind: deterministic. Test:
     - Given a job that fails as overloaded, then passes
     - When call runs
     - Then it returns the answer of the second job
   - Domain: Clear, by deduction from the retry of HTTP errors.

### References

[1] tests/evaluation/results/2026-11-04-short-reason: rules.md, responses, calls.csv, and script-checks.csv, 2026. [P]

[2] tests/evaluation/results/2026-11-03-base-07: rules.md, responses, calls.csv, and script-checks.csv, 2026. [P]

[3] tests/evaluation/results/2026-11-03-reason-form: the same files, 2026. [P]

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
