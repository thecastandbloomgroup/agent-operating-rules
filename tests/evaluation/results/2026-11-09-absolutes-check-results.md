# Results: a script check for unmeasured absolutes

## Headline

The check fails its pass mark: 4 of its 46 flags are faults, or 9% against a mark of 80%. So the check stays out of `bin/deterministic-tests.py`, and no rule names the fault.

1. **The fault is rare.** Only 4 of the 126 control answers hold an unmeasured absolute, about 3%.
2. **A word pattern cannot find it.** Most uses of the four words are facts about the case in the prompt, counts of none, or conditions.
3. **A rule would need a judge.** At a rate of 3%, a judge costs more than the fault [judgment].

## Background

The [plan](2026-11-09-absolutes-check-plan.md) was committed before any marking. It set the check, its unit test, the rubric, and the pass mark of 80%. The answers are the 126 control answers of the rule-cut probe, on the branch `test/rule-cuts`.

## Results

The unit test of the plan passed, so the check did what the plan said. On the answers, it gave 46 flags in 126 answers.

| Class | Flags |
| --- | --- |
| Fault | 4 |
| False alarm: the word "none", mostly in "Open questions: none." | 30 |
| False alarm: a fact about the case in the prompt | 6 |
| False alarm: a condition, a definition, or quoted text | 6 |

The four faults:

1. Sonnet, X2 sample 1: "Teams that skip "decide what to do" or never review it produce talk without change."
2. GLM, X2 sample 2: "Most stuck retros list many actions and complete none."
3. Kimi, T2 sample 2: "Models trained to always answer produce confident filler when evidence is absent [judgment]."
4. Grok, X2 sample 2: "Retrospectives stop working when agreed changes never enter the next work cycle."

The check skipped 9 sentences with one of the four words. None of them is a fault. Two carry a citation. The rest are counts, instructions, quoted text, or facts about the case.

## What this shows

1. Three of the four faults come from the retrospective prompt X2. So the fault appears where the prompt invites advice about teams in general.
2. The word "none" causes 30 of the 42 false alarms. A check without "none" would give 15 flags with 3 faults, or 20%. That still fails the mark.
3. An unmeasured absolute does not need one of the four words. For example, "Most stuck retros" makes a claim of the same class. So any check on words misses the class.

## Decision

The check code and its unit tests are not merged. The proposed item in Section 4.6 is not added, because the measured rate does not pay for its length or a judge.

## Limits

1. The marker is the model that wrote the check, so the marks are not blind.
2. The answers come from one day and seven prompts. A prompt set with more general advice could show a higher rate.
