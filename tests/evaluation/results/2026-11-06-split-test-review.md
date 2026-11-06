# Where the two judges split, the test and the user disagree in 6 of 15 actions: a review

## Headline

The two judges split on 15 Complicated or Chaotic labels. Of those 15 actions, the test stands in 7. It says nothing about the step in 2, and it disagrees with the user's own marks in 6.

1. **The test stands in 7.** On these, the label misreads the step, and the judge of the work follows the user's theme that expertise means Complicated too far.
2. **The test says nothing about the step in 2.** Both are later steps of a Confused prompt, after the step that classifies, and the test describes only the first step.
3. **The test disagrees with the user in 6.** The user rejected Chaotic for the first step of prompt H2 twice, and accepted Complicated on prompt T1 once. The test expects the opposite on both prompts.

## Background

The [work rejudge results](2026-11-06-judge-work-results.md) found that the two judges split on 11 Complicated and 4 Chaotic labels of the 104 unmarked actions. This review reads each of the 15 actions against the expected answer of its test in `tests/evaluation-tests.md`. It uses the user's marks on the same prompts from `2026-11-05-human-marking/sheet.csv`.

## Relevance

A judge can only match the user where the tests match the user. So the 6 conflicts set a ceiling on agreement between any judge of the test and the user [inference].

## Information

This section gives the rubric, the table of the 15 actions, and the conflicts.

### The rubric

Each action gets one of three findings. The evidence for each is the expected answer of the test and the text of the action.

1. **The test stands**: the expected answer names the domain of this step, and the label misreads the step.
2. **The test is silent**: the expected answer does not cover this step.
3. **The test conflicts with the user**: the user marked a similar step on the same prompt. That mark disagrees with the expected answer.

### The 15 actions

| Run | Answer | Action | Label | Step | Expected | Finding |
| --- | --- | --- | --- | --- | --- | --- |
| reason-examples | claude-sonnet-5-5, H2-s2 | 3 | Complicated | choose the public response | Complex | test stands |
| cynefin-questions | claude-sonnet-5-5, H2-s1 | 3 | Complicated | choose the public response with a rubric | Complex | test stands |
| split-first-c | claude-sonnet-5-5, H2-s1 | 3 | Complicated | choose the public response | Complex | test stands |
| split-first-c | glm-5.3-flash, H2-s2 | 3 | Complicated | choose the public response | Complex | test stands |
| reason-examples | gemini-3.8-flash, T2-s3 | 3 | Complicated | add a citation rule to the prompt | Complex | test stands |
| cynefin-questions | grok-4.7, C2-s3 | 3 | Complicated | check country tags on title pages | Clear | test stands |
| split-first-c | grok-4.7, X2-s1 | 4 | Complicated | accept one change per cycle | Complex | test stands |
| reason-examples | grok-4.7, U1-s3 | 3 | Complicated | quarantine or open a ticket, after the label | Confused, first step only | test silent |
| cynefin-questions | claude-sonnet-5-5, U2-s2 | 4 | Complicated | fix the largest gap, after it is found | Confused, first step only | test silent |
| reason-examples | gpt-6.1-sol, H2-s3 | 1 | Chaotic | name a lead and freeze replies | Chaotic | conflicts with the user |
| cynefin-questions | kimi-k3, H2-s2 | 1 | Chaotic | name a lead and freeze replies | Chaotic | conflicts with the user |
| split-first-c | kimi-k3, H2-s1 | 1 | Chaotic | name a lead and freeze replies | Chaotic | conflicts with the user |
| split-first-c | kimi-k3, H2-s3 | 1 | Chaotic | name a lead and freeze replies | Chaotic | conflicts with the user |
| cynefin-questions | gpt-6.1-sol, T1-s1 | 1 | Complicated | agree a charter in one meeting | Clear, gate fails a session first | conflicts with the user |
| split-first-c | claude-sonnet-5-5, T1-s3 | 1 | Complicated | choose the style in one session | Clear, gate fails a session first | conflicts with the user |

[1]

### The conflicts

- **Prompt H2, the first step.** The test expects Chaotic for a single owner and a hold on statements. The user rejected that label on two marked rows of the same step. One note reads "Complicated. Expertise needed to facilitate."
  The other note reads "This is clear assuming that team members will act according to the instructions". So the test labels the situation, and the user labels the step [inference].
  [1]
- **Prompt T1, the first step.** The test expects Clear and fails a response that holds a session before the formatter. The user accepted a Complicated first step that chooses a style on prompt T1, with the note "There is also the preference of the human."
  [1]

### Limits

- **One reader.** One model read and sorted the 15 actions, with no second reader [judgment].
- **Few user marks per prompt.** The conflicts rest on 2 marks for prompt H2 and 1 for prompt T1.

## End

I recommend that we:

1. Ask the user whether the tests of prompts H2 and T1 should follow the user's marks.
   Increment: one question with two choices for each prompt. Blocker removed: a test that no judge can match with the user.
   Test (evaluative): the answer names, for each prompt, the domain of the first step that the test expects.
   Domain: Complicated. Reason: analysis, because the choice depends on whether a domain names the situation or the step.
2. Add one line to the tests of prompts U1 and U2: a later step, after the step that classifies, MAY carry its own domain.
   Increment: two lines in `tests/evaluation-tests.md`. Blocker removed: two judge misses on steps that the test does not cover.
   Test (deterministic, Gherkin):
   Given the tests of prompts U1 and U2
   When a reader looks for the domain of a later step
   Then each test says that a later step MAY carry its own domain.
   Domain: Clear. Reason: deduction, because the judge instruction already allows this for support steps.
   Step 2 MUST NOT start until the user answers the question of Step 1, because a change to the tests changes what the ladders score.
3. Keep the judge of the test for the ladders until the tests change.
   Increment: none. Blocker removed: none new.
   Test (deterministic, Gherkin):
   Given `bin/judge-actions.py` on main
   When it runs with no `--work`
   Then each call carries the expected answer.
   Domain: Clear. Reason: deduction, because the unit test checks it.

## Follow-up

References:

[1] `tests/evaluation-tests.md`, the tests of prompts C2, H2, T1, T2, U1, U2, and X2; the response files named in the table; and `2026-11-05-human-marking/sheet.csv`, rows 5, 19, and 24, read 2026-11-06. [P]
