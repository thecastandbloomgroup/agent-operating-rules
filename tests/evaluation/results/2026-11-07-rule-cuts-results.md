# Results: two cuts of the rules, alone and together

## Headline

All three variants pass every mark of their plans. So the combined file is ready for a release, if the user agrees. It has no self-test counts, no Section 1, and no references list.

1. **Self-test counts:** with the four count lines removed, answers with a false self-test line fall from 59.5% to 11.1%.
2. **Section 1 and references:** with both removed, mean input tokens per call fall by 20%, and no script check falls by more than 2 points.
3. **Both cuts together:** false lines fall to 7.1%, input tokens fall by 21%, and every check stays within 10 points of the control.

## Background

The [first plan](2026-11-07-rule-cuts-plan.md) set the control and the two single cuts. The [second plan](2026-11-07-rule-cuts-both-plan.md) added the arm with both cuts. Each arm ran 126 answers: six models, seven prompts, and three samples, with no judge. The rules files sit in `2026-11-07-rule-cuts-plan/`.

## Results

The numbers are shares of the 126 answers, except the last two rows.

| Check | Control | No counts | No Section 1 or references | Both |
| --- | --- | --- | --- | --- |
| Self-test with a false line | 59.5% | 11.1% | 55.6% | 7.1% |
| Structure | 88.9% | 88.1% | 88.9% | 88.9% |
| No long sentence | 40.5% | 40.5% | 48.4% | 41.3% |
| No first person outside End | 94.4% | 93.7% | 96.0% | 94.4% |
| Labels on every action | 88.1% | 86.5% | 91.3% | 90.5% |
| Reasons on every action | 81.0% | 77.0% | 81.7% | 84.9% |
| Self-test right | 34.1% | 83.3% | 36.5% | 86.5% |
| No banned word | 88.1% | 86.5% | 87.3% | 86.5% |
| No dash | 100% | 100% | 98.4% | 98.4% |
| Mean input tokens per call | 5,725 | 5,677 | 4,564 | 4,496 |
| Cost (USD) | 3.92 | 3.51 | 3.35 | 3.73 |

The Wilson 95% intervals for the share of answers with a false line:

| Arm | False lines | Interval |
| --- | --- | --- |
| Control | 75 of 126 | 50.8% to 67.7% |
| No counts | 14 of 126 | 6.7% to 17.8% |
| No Section 1 or references | 70 of 126 | 46.8% to 63.9% |
| Both | 9 of 126 | 3.8% to 13.0% |

The intervals of the two arms without counts do not overlap the control. In the control, GLM gave a false line in 20 of 21 answers and Sonnet in 15 of 21. In the arm with both cuts, no model gave more than 3 of 21.

## Marks

| Arm | Mark | Result |
| --- | --- | --- |
| No counts | False lines fall by 20 points or more | Pass: 48.4 points |
| No counts | Six guards within 10 points | Pass: the largest fall is 1.6 points, labels on every action and no banned word |
| No Section 1 or references | Eight checks within 10 points | Pass: the largest fall is 1.6 points, no dash |
| No Section 1 or references | Input tokens fall by 10% or more | Pass: 20.3% |
| First plan | Three arms under 15 USD | Pass: 10.78 USD |
| Both | False lines fall by 20 points or more | Pass: 52.4 points |
| Both | Seven checks within 10 points | Pass: the largest fall is 1.6 points, no banned word and no dash |
| Both | Input tokens fall by 10% or more | Pass: 21.5% |
| Both | Arm under 5 USD | Pass: 3.73 USD |

## A break in the run

The user paused the work on 2026-11-07, when the arm with both cuts held 106 of 126 answers. Five models had all 21 answers, and Grok had 1. On 2026-11-09, all 21 Grok answers ran again with the same rules file. They replaced the one paused answer, which stays in the git history at commit 36df78c. So 21 of the 126 answers in that arm come from a day two days after the control.

## What this shows

1. The count lines asked the model to count its own long sentences, banned words, dashes, and self-mentions. The models got these counts wrong, and the script checks still catch every one of these faults. So the lines cost trust and add no check.
2. Section 1 and the references list cost about 1,200 input tokens per call, and no script check fell by more than 2 points without them.
3. The two cuts show no interaction on any script check [judgment].

## Limits

1. No arm had a judge, so these runs do not measure the quality of judgment. Section 1 states how to think, and a judge could still find a loss there.
2. A pass changes the rules only in a release, and only with the user's agreement.
