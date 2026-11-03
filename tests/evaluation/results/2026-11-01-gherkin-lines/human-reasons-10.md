# Blind marks: does the reason state cause and effect? (10 actions)

Mark each action yes or no. Do not open any action-checks file until all 10 are marked.

Yes: the reason says how cause and effect relate in this work, for example "a known fix gives the same result each time" or "the effect shows only after a trial".
No: the reason only names the domain, restates the task, or gives none.

Mark only the reason. Ignore whether the domain itself is right.

## 1. H2, action 2 (item 1)

```text
2. **Check every claim (Complicated: experts can find the answer from records).**
   - Increment: within 2 hours, build a table with the CEO's statement in one column and the article's claim in the next. Add the evidence and a verdict for each line.
   - Blocker removed: no shared facts.
   - Kind: deterministic. Test written first:

   ```gherkin
   Given the CEO statement is split into single claims
   When Legal and the statement's source team review each claim against records
   Then each claim is marked true, false, or unverified
   And each verdict links to one document
   ```
```

- Reason states cause and effect: Yes

## 2. C1, action 3 (item 3)

```text
3. **Check runtime output after Step 2 passes.** Deterministic; **Clear**, because startup and shutdown have fixed message paths.
   ```gherkin
   Given a temporary database and an available port
   When the service starts and receives a keyboard interrupt
   Then startup and shutdown messages appear at INFO level
   ```
   Run the service once to verify the logging configuration.
```

- Reason states cause and effect: No

## 3. T1, action 1 (item 4)

```text
1. **Pick the tool by rubric.** Increment: score the three candidates in the matrix above in one 45-minute session. Blocker removed: disagreement on which tool to use. Test: the score sheet with threshold 8 of 10, filled from tool docs. Domain: **Complicated**, because analysis among several good options picks the winner.
```

- Reason states cause and effect: Yes

## 4. K2, action 2 (item 10)

```text
2. **Verify the growth rate before signature.** Increment: compute growth per quarter from the last four quarters of storage records. Blocker: this resolves A2, which guards the 20 TB cap [1]. Test (deterministic): Given the four quarterly storage figures, When the annual rate is computed, Then it is at most 3 TB. Step 3 MUST NOT start until this test and the test in Step 1 pass. Domain: Clear, because the rule is a direct check of known data.
```

- Reason states cause and effect: Maybe, we don't know if there is special cause that may throw off the estimate.

## 5. C2, action 2 (item 13)

```text
2. Check each entry against references.txt, field by field. Step 3 MUST NOT start until this test passes. This removes the risk of a lost field. Domain: Clear, because the check has one correct result. Kind: deterministic.
   - Given a formatted entry and its source record
   - When each field is compared
   - Then every author, title, edition, publisher, and year matches
```

- Reason states cause and effect: Yes

## 6. U2, action 2 (item 15)

```text
2. **Compare one suspect total with its source.**  
   **Kind:** Deterministic. **Domain:** Complicated, because reconciliation requires analysis of formulas, scope, and dates.

   **Test first:**  
   Given the records from Step 1,  
   When the same scope and dates are applied,  
   Then the comparison shows either agreement or a quantified difference.

   **Action:** Recalculate that total and compare it with the reported value in one review session.  
   **Blocker removed:** No measured difference.  
   **Dependency:** Step 2 MUST NOT start until Step 1 passes.
```

- Reason states cause and effect: Maybe, we don't know if there is special cause that may throw off the estimate.

## 7. T1, action 2 (item 21)

```text
### 2. Automate the agreed format on a small SQL sample

**Test first, deterministic:**

```gherkin
Given representative SQL files and the proposed formatter configuration
When the formatter runs twice
Then the second run produces no additional changes
```

After Step 1 passes, test one formatter that supports the team's SQL dialect in a 60-minute session.

Inspect its changes before adding a shared command and an automated format check. Keep repository-wide reformat changes separate from behavior changes.

This removes manual enforcement of the rules that the tool covers. [judgment]

**Domain: Complicated**, because dialect support and output need technical inspection.

If no suitable formatter passes, retain a minimal written convention and defer automation. Do not expand the style guide to compensate.
```

- Reason states cause and effect: Yes

## 8. K1, action 8 (item 34)

```text
4. Domain: Complicated, because analysis of the ticket must pick the value first.

**Step 3.** If the limit stays at 32, file a capacity request with the demand number.
```

- Reason states cause and effect: Yes

## 9. U2, action 4 (item 36)

```text
4. Kind: evaluative.
Step 4 MUST NOT start until the tests in Step 2 and Step 3 pass.
Source match has a weight of 50 percent.
The baseline gap has a weight of 30 percent.
Same units have a weight of 20 percent.
Pass threshold: every checked total matches its source, or each miss has a cause on the list.
Evidence needed: the formula result, the baseline figure, and the unit label.
Score each total against this rubric.
Do this in one working session.
This increment is one pass or fail mark per total.
It removes the open restatement choice.
Domain: Complicated, because the score picks restatement only after the trace.
```

- Reason states cause and effect: Yes

## 10. H2, action 3 (item 39)

```text
### 3. Choose and approve one response within the next hour

**Kind:** Evaluative, meaning the output requires judgment.  
**Domain:** Complicated, because evidence review and legal analysis determine the appropriate response. [judgment]

**Rubric first:** Use this weighted decision rubric. These weights are proposed response controls, not measured predictors. [judgment]

| Criterion | Weight | Evidence required |
|---|---:|---|
| Factual support | 50% | Original records support every factual assertion |
| Legal and safety checks | 30% | Counsel identifies duties; relevant owners address urgent risks |
| Response control | 20% | Named approver, spokesperson, audience, and update time |

**Pass threshold:** 100% of applicable checks. An unresolved factual claim cannot pass.

**Current score:** No criterion is demonstrated in the supplied material: 0/100 readiness evidenced here. This does not establish that internal checks are absent.

**Action:** Do not approve a substantive response until Step 2 supplies the required evidence. Choose one route:

- **Statement false:** Correct the precise error and explain the confirmed impact and remedy.
- **Statement supported:** Respond with verifiable evidence and address the specific allegation.
- **Facts unresolved:** Issue only a verified status update and commit to a realistic next update.

If a response is needed before verification, use a narrow draft:

> “We are reviewing the specific claim raised in the report. We will provide an update by [time and time zone].”

Use that wording only after the review starts and the update deadline has an owner.

Send the board the same verified facts, open issues, decisions needed, and next update time. After approval, give the journalist the response and supporting material suitable for release.

**Output:** One approved response and a scheduled update. It prevents separate teams from presenting different factual positions. [judgment]
```

- Reason states cause and effect: Instead of weights, consider the prognosis over time horizons if the answer is wrong. Then consider that risk weighted with the others.
