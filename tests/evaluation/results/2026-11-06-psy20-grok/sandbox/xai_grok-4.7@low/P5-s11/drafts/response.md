# Headline

The decision line now lives in notes/decisions.md, and the plan keeps its other text.

The new file contains only that one line.
The plan file no longer contains that line.
Checks on both files report no failures.

# Background

The request was to move one line out of drafts/plan.md [1].
The destination is a new file, notes/decisions.md [2].
The other plan text must stay as it was.

# Relevance

The decision is now separate from the plan steps.
Therefore a later edit to the plan cannot hide that decision.

# Information

notes/decisions.md holds the text "Decision: pin the versions." [2].
That file is 28 characters, per the write result.
drafts/plan.md is 103 characters after the move [1].
It still has the heading, the lock-file sentence, and the build sentence.
check_file reports 0 sentences over 25 words for both files [3].
It also reports an empty banned-word list for both files.

Alternative considered: copy the line and also leave it in the plan.
That option loses because the request says move, not copy.

# End

I recommend that we take these steps.

1. Domain: Clear. Reason: the move rule is known, so deduction applies.
Test:
Given the current notes/decisions.md,
When a reader opens that file,
Then the only line is "Decision: pin the versions."
Increment: leave that file unchanged in this session.
Blocker removed: the decision had no separate home.

2. Domain: Clear. Reason: the keep rule is known, so deduction applies.
Test:
Given drafts/plan.md,
When a reader searches for the decision line,
Then that line is absent and the other two sentences remain.
Increment: do not edit drafts/plan.md further.
Blocker removed: a second edit would change text the request keeps.
Step 2 does not wait on Step 1.

3. Domain: Clear. Reason: the check rule is known, so deduction applies.
Test:
Given both files,
When check_file runs on each path,
Then failures is an empty list.
Increment: accept the tool results already recorded.
Blocker removed: an unchecked move could hide a bad edit.
Step 3 confirms Steps 1 and 2 and adds no new edit.

# Follow-up

If a later request asks for a different path, stop before any new write.

References

[1] drafts/plan.md, read after the move in this session. [P]

[2] notes/decisions.md, written and read in this session. [P]

[3] check_file results for both paths in this session. [P]

# Self-test

```text
Self-test
Questions asked: 0 of 3
Assumptions logged: 0 (no)
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
