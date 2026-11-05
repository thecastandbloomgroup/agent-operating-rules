# Headline

The decision line is in notes/decisions.md and is not in drafts/plan.md.

drafts/plan.md still has its heading and its two other lines.

notes/decisions.md holds that decision line alone.

Checks on both files report no failures.

# Background

The task was to move one line out of drafts/plan.md.

The new file is notes/decisions.md.

The other lines in the plan had to stay the same.

# Relevance

The decision is now a separate record.

So a later reader can find it without the plan lines.

# Information

First, drafts/plan.md contains the heading, the lock-file line, and the build line.

See the file read in this session [1].

Next, notes/decisions.md contains the moved decision line and no other text.

See the file read in this session [2].

The check tool reports zero long sentences and no banned words for both files.

See the tool result in this session [3].

Alternative considered: keep the line in both files.

It loses because a move deletes the source line [judgment].

# End

I recommend that we take these three steps.

1. Treat the move as done.

Increment: accept the current two files as the result of this task.

Blocker removed: the decision line sat inside the plan.

Domain: Clear, because a known rule says to move one named line.

Test:

Given both files as read now

When a reviewer looks for the decision line

Then it appears in notes/decisions.md and not in drafts/plan.md

2. Leave every other plan line unchanged.

This step MUST NOT start until the test in Step 1 passes.

Increment: make no further edit to drafts/plan.md in this task.

Blocker removed: the risk of extra edits to the plan.

Domain: Clear, because the request states that rule.

Test:

Given the plan text after the move

When it is compared with the original minus the decision line

Then the heading and the two work lines match

3. Add no other text to notes/decisions.md.

This step MUST NOT start until the test in Step 2 passes.

Increment: keep the new file to the one moved line.

Blocker removed: extra text in the new file.

Domain: Clear, because the request names one line.

Test:

Given notes/decisions.md

When its text is read

Then the file holds the decision line and nothing else

# Follow-up

If the decision line must also stay in the plan, restore that line there.

That condition would undo the move.

# References

[1] drafts/plan.md, sandbox read after the edit, 2026. [P]

[2] notes/decisions.md, sandbox read after the edit, 2026. [P]

[3] check_file tool output for both paths, this session, 2026. [P]

# Self-test

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
