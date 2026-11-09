# A plan: measure unmeasured absolutes with a judge

## Headline

A judge counts the answers that make a general claim with no count behind it. This count decides whether the rules need a line against such claims. The plan waits for the user's approval before any paid call, because a person must also mark a sample.

1. The [script check](2026-11-09-absolutes-check-results.md) failed: 4 of its 46 flags were faults. So a word pattern cannot measure the fault.
2. The 4 faults came from 4 of the 126 control answers, and 3 of them came from the retrospective prompt X2. So the rate depends on how much the prompt asks for general advice.
3. A rule is worth its length only if the fault is common and a judge can find it.

## Definition

An unmeasured absolute is a sentence with all three features:

1. It makes a claim about a class of things, such as teams, models, or tools, not about the one case in the prompt.
2. It states the claim as true always, never, for all, or for most.
3. No count, source, or deduction supports it in the sentence or the one before it.

## Design

1. **Stage one: stored answers.** A judge reads each of the 126 control answers of the [rule-cut probe](2026-11-07-rule-cuts-results.md). It quotes each sentence that meets the definition. The judge comes from a provider other than the one that wrote the answer.
2. **A person marks a sample.** The person marks 20 answers, chosen at random with seed 20261109, as "has a fault" or "has none". The person does not see the judge's marks first.
3. **Stage two: advice prompts.** Run this stage only if stage one finds a rate under 10%. Three new prompts each ask for general advice about a practice, such as code review. Six models answer each prompt three times under rules 0.10, for 54 answers. The same judge reads them.

## Metrics and pass marks

1. **Agreement.** Cohen's kappa between the judge and the person, on the 20 answers, is 0.6 or more. If kappa is under 0.6, the judge cannot measure the fault, and the plan stops.
2. **Rate.** The share of answers with at least one fault is 10% or more, in stage one or in stage two.

A line in Section 4.6 is drafted only when both marks hold. That line then needs its own arm against a same-day control before any release.

## Cost and stop rule

1. Stage one costs about 2.50 USD for 126 judge calls.
2. Stage two costs about 2.50 USD for 54 answers and their judge calls.
3. The plan stops at 6 USD.

## Limits

1. One judge model gives the marks, so a second judge would show whether the rate holds across judges.
2. The person's 20 answers give a wide interval for kappa.
