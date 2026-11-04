# Blind marks: 40 actions of the 0.5.1 probe

Mark each action yes or no on two questions. Do not open action-checks.csv or action-checks-argon.csv until all 40 are marked, because a judge result pulls a mark toward it.

- Domain right: the domain of this action fits the expected answer of evaluation-tests.md for its prompt, in its place in the list.
- Reason states cause and effect: the reason says how cause and effect relate in this work, not only the domain name or the task.

Each answer is in the file named under its action. Write yes or no after each colon.

## 1. H2, action 2, labelled Complicated

File: `responses/anthropic_claude-sonnet-5-5@medium/H2-s2.md`

Expected classification: Chaotic for action 1 (a single owner and a hold on substantive outbound statements). Then Complicated for the facts: was the statement false, and what does the record show. Then Complex for the response to the public and the board.

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

- Domain right:
- Reason states cause and effect:

## 2. X1, action 2, labelled Clear

File: `responses/google_gemini-3.8-flash@medium/X1-s3.md`

Expected classification: Complex. Cause and effect are visible only afterward. No metric exists.

```text
2. Measure baseline summary accuracy against the benchmark. Step 2 MUST NOT start until Step 1 passes.
   - Increment: Run the current prompt on the 100 benchmark tickets and compute factual consistency scores.
   - Capability added: Establishes a numerical baseline for factual accuracy.
   - Cynefin domain: Clear, because running an established scoring script follows standard practice.
   - Test (Stochastic):
     - Metric: Factual consistency rate.
     - Baseline: 0% measured.
     - Pass threshold: 100 tickets processed with complete metric outputs.
     - Sample size: 100 benchmark tickets.
```

- Domain right:
- Reason states cause and effect:

## 3. C1, action 3, labelled Clear

File: `responses/openai_gpt-6.1-sol@medium/C1-s3.md`

Expected classification: Clear. Best practice exists and is known to everyone.

```text
3. **Check runtime output after Step 2 passes.** Deterministic; **Clear**, because startup and shutdown have fixed message paths.
   ```gherkin
   Given a temporary database and an available port
   When the service starts and receives a keyboard interrupt
   Then startup and shutdown messages appear at INFO level
   ```
   Run the service once to verify the logging configuration.
```

- Domain right:
- Reason states cause and effect:

## 4. T1, action 1, labelled Complicated

File: `responses/perplexity_glm-5.3-flash@medium/T1-s2.md`

Expected classification: Clear, despite the wording. A formatter with a lock file ends the dispute. The word "culture" points the wrong way.

```text
1. **Pick the tool by rubric.** Increment: score the three candidates in the matrix above in one 45-minute session. Blocker removed: disagreement on which tool to use. Test: the score sheet with threshold 8 of 10, filled from tool docs. Domain: **Complicated**, because analysis among several good options picks the winner.
```

- Domain right:
- Reason states cause and effect:

## 5. X2, action 4, labelled Complex

File: `responses/perplexity_kimi-k3@low/X2-s2.md`

Expected classification: Complex. Human systems, many interacting causes.

```text
4. **Probe safety with an anonymous pulse.** Increment: send three questions, one week, budget of one hour per person. Stop condition: fewer than 60% respond, in which case treat safety itself as the blocker. Domain: Complex, because reactions are visible only afterward, so this is a capped probe. Stochastic test: metric is mean safety score on a 5-point scale; baseline is none; pass threshold is a score at or below 3.5 triggering a safety intervention; sample size is all team members.

Step 3 MUST NOT conclude until three cycles pass. Steps 1, 2, and 4 can run in parallel.
```

- Domain right:
- Reason states cause and effect:

## 6. U2, action 3, labelled Clear

File: `responses/xai_grok-4.7@low/U2-s3.md`

Expected classification: Confused.

```text
3. Test first.
Given a draft corrected total,
When the three inputs are still blank,
Then the draft is not published.
Block any adjusted third-quarter figure from release.
Increment: one release gate.
Blocker: a guessed correction leaves the team.
Domain: Clear, because the gate is a known control.
Step 3 does not wait on Step 1.
```

- Domain right:
- Reason states cause and effect:

## 7. X2, action 3, labelled Complex

File: `responses/anthropic_claude-sonnet-5-5@medium/X2-s2.md`

Expected classification: Complex. Human systems, many interacting causes.

```text
3. **Run a three-retrospective probe.** Each retrospective ends with one action. The action has one named owner, one date, and a place in the sprint backlog. Step 3 MUST NOT be judged until Step 1 gives a baseline. Increment: one retrospective per cycle. Blocker removed: no follow-through. Kind: stochastic. Domain: Complex, because team response shows only afterward. Leverage is a guess. Budget: three retrospectives. Stop condition: stop early if the team rejects the format in the survey. Acceptance test: metric is the share of actions done by the next retrospective. The baseline is the Step 1 rate. The pass threshold is the baseline plus 30 points. The sample is three retrospectives, so treat the result as weak evidence.
```

- Domain right:
- Reason states cause and effect:

## 8. C2, action 3, labelled Complicated

File: `responses/google_gemini-3.8-flash@medium/C2-s1.md`

Expected classification: Clear.

```text
3. Select your preferred country code convention for publisher locations.
This removes styling variances across international publishing venues.
Test (evaluative):
Score the location strings against a consistency rubric. Criteria: presence of country codes (weight 50%), presence of state abbreviations (weight 50%). Pass threshold: 100% uniform location tags.
Cynefin domain: Complicated, because publisher location styling varies across organizational house rules. Step 3 MUST NOT start until Step 2 passes.
```

- Domain right:
- Reason states cause and effect:

## 9. K2, action 1, labelled Complicated

File: `responses/openai_gpt-6.1-sol@medium/K2-s3.md`

Expected classification: Complicated.

```text
1. **Obtain a binding Northwind cost and capacity schedule in one procurement session.**  
   Kind: deterministic. Domain: **Complicated**, because a capacity-and-billing calculation must resolve the price risk.

   **Test first:**
   ```text
   Given 14 TB initially and growth of 3 TB per year
   When the agreed billing model calculates all 36 months
   Then the schedule states capacity charges and the maximum vendor cost
   ```

   Request the schedule, including capacity measurement, partial-year charges, migration scope, and export terms.  
   This removes uncertainty about the largest known budget risk. [judgment]
```

- Domain right:
- Reason states cause and effect:

## 10. K2, action 2, labelled Clear

File: `responses/perplexity_glm-5.3-flash@medium/K2-s3.md`

Expected classification: Complicated.

```text
2. **Verify the growth rate before signature.** Increment: compute growth per quarter from the last four quarters of storage records. Blocker: this resolves A2, which guards the 20 TB cap [1]. Test (deterministic): Given the four quarterly storage figures, When the annual rate is computed, Then it is at most 3 TB. Step 3 MUST NOT start until this test and the test in Step 1 pass. Domain: Clear, because the rule is a direct check of known data.
```

- Domain right:
- Reason states cause and effect:

## 11. U1, action 3, labelled Complicated

File: `responses/perplexity_kimi-k3@low/U1-s2.md`

Expected classification: Confused. The prompt does not say which build, how often, or since when.

```text
3. **Fix the largest bucket with a targeted change.** Example: replace fixed sleeps with condition waits if timing dominates. Depends on Step 2. Domain: Complicated, because the analysis names the practice. Test (stochastic): run the previously flaky target 30 times; baseline is its historical failure rate; pass at zero failures in 30 runs.
```

- Domain right:
- Reason states cause and effect:

## 12. C2, action 2, labelled Complicated

File: `responses/xai_grok-4.7@low/C2-s3.md`

Expected classification: Clear.

```text
2. Kind: deterministic. Test:
Given a host document that cites these books,
When titles are recorded in reading order,
Then the first new title is entry 1 and each later new title takes the next number.
Increment: Renumber the six brackets to that order in one pass. Blocker removed: Numbers that do not follow first use. Cynefin domain: Complicated, because a first-citation scan must pick the numbers. Step 2 MUST NOT start until the Step 1 test passes.
```

- Domain right:
- Reason states cause and effect:

## 13. C2, action 2, labelled Clear

File: `responses/anthropic_claude-sonnet-5-5@medium/C2-s2.md`

Expected classification: Clear.

```text
2. Check each entry against references.txt, field by field. Step 3 MUST NOT start until this test passes. This removes the risk of a lost field. Domain: Clear, because the check has one correct result. Kind: deterministic.
   - Given a formatted entry and its source record
   - When each field is compared
   - Then every author, title, edition, publisher, and year matches
```

- Domain right:
- Reason states cause and effect:

## 14. X1, action 2, labelled Complicated

File: `responses/google_gemini-3.8-flash@medium/X1-s1.md`

Expected classification: Complex. Cause and effect are visible only afterward. No metric exists.

```text
2. Run an error taxonomy audit on current summariser outputs against the evaluation dataset.
   - Dependency: Step 2 MUST NOT start until Step 1 passes.
   - Increment: Evaluate current model outputs across the 50 tickets and record error counts by category.
   - Blocker: Removes the lack of quality metrics by identifying whether errors stem from hallucination, omission, or formatting.
   - Domain: Complicated, because categorising semantic errors requires structured analysis.
   - Test (Evaluative):
     - Rubric criteria: Error classification into hallucination, omission, or extraneous detail (weight: 0.5); inter-annotator agreement above 80% (weight: 0.5).
     - Pass threshold: 100% of errors classified into defined buckets with root-cause notes.
```

- Domain right:
- Reason states cause and effect:

## 15. U2, action 2, labelled Complicated

File: `responses/openai_gpt-6.1-sol@medium/U2-s3.md`

Expected classification: Confused.

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

- Domain right:
- Reason states cause and effect:

## 16. T3, action 4, labelled Complex

File: `responses/perplexity_glm-5.3-flash@medium/T3-s3.md`

Expected classification: two parts. The migration is Complicated (deterministic test, known patterns, needs a design choice on token lifetime and revocation). The conversion ask is Complex (stochastic, needs a measure and probes).

```text
4. **Run one conversion A/B test as a capped probe.** Increment: one change, for example moving email verification after first use, shipped to a flagged subset. Blocker removed: the belief that conversion needs many redesigns gets a measured answer. Test, written first (stochastic): metric is sign-up completion rate; baseline is the Step 1 number; pass threshold is a positive lift at the 95% level; sample size 1,000 users per arm before any decision; stop condition is a negative lift after the full sample. Budget: one experiment, capped at two weeks. Cynefin: Complex, because the effect is visible only after the run, so the probe stays small, [judgment].
```

- Domain right:
- Reason states cause and effect:

## 17. U2, action 4, labelled Clear

File: `responses/perplexity_kimi-k3@low/U2-s2.md`

Expected classification: Confused.

```text
4. Add regression checks before republishing. Blocker removed: repeat errors. Test: Given the rebuilt dataset, When checks fail, Then publication is blocked and the failed metric is named. Kind: deterministic. Domain: Clear, because threshold rules are knowable.
```

- Domain right:
- Reason states cause and effect:

## 18. H1, action 3, labelled Clear

File: `responses/xai_grok-4.7@low/H1-s2.md`

Expected classification: Chaotic for the first action, then Complicated for the rest.

```text
3. Write the call note from the dashboard. This step can run in parallel with Step 2. Test: Given the checkout dashboard is open. When the on-call reads that panel. Then the note has start time, error percent, and failed checkouts per minute. Increment: one six-line note. Blocker removed: a call with no impact number. Domain: Clear, because this read has one known practice. Use these lines: Checkout fails for all users since 09:12. Releases are frozen. Rollback of the nearest change is in progress, or no safe rollback exists. Next update is in 10 minutes.
```

- Domain right:
- Reason states cause and effect:

## 19. K2, action 4, labelled Complex

File: `responses/anthropic_claude-sonnet-5-5@medium/K2-s3.md`

Expected classification: Complicated.

```text
4. Probe the migration with a 1 TB subset. This tests the 10-week claim. Budget: one working week. Stop if throughput falls below 0.93 TB per week, which implies more than 15 weeks. Domain: Complex, because migration speed shows only after we try. Leverage is a guess. Kind: stochastic. Metric: TB per week. Baseline: 1.4 TB per week. Pass threshold: 0.93 TB per week or more. Sample: five loads.

If A2 is false, replace Step 2 with a Cedar cost review. If Step 2 fails, ask Bluepeak for the A3 quote. The contract MUST NOT be signed until Steps 2 to 4 pass.
```

- Domain right:
- Reason states cause and effect:

## 20. T2, action 2, labelled Complicated

File: `responses/google_gemini-3.8-flash@medium/T2-s3.md`

Expected classification: Complex. No prompt is known to stop hallucination, so a prompt is a probe, not a fix. Per Section 0 of the rules, the explicit request comes first, so the answer gives the prompt that the user asks for.

```text
2. Benchmark the prompt on fifty test questions using a pass threshold rubric.
   This action adds the capability to measure your baseline hallucination rate.
   Test:
   Rubric: factual accuracy weight 0.6, adherence to source weight 0.4.
   Pass threshold: 0.90 composite score across fifty trials.
   Evidence: human verification against source text.
   Cynefin domain: Complicated, because measurement requires systematic analysis of model outputs against ground truth.
```

- Domain right:
- Reason states cause and effect:

## 21. T1, action 2, labelled Complicated

File: `responses/openai_gpt-6.1-sol@medium/T1-s3.md`

Expected classification: Clear, despite the wording. A formatter with a lock file ends the dispute. The word "culture" points the wrong way.

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

- Domain right:
- Reason states cause and effect:

## 22. K1, action 3, labelled Complicated

File: `responses/perplexity_glm-5.3-flash@medium/K1-s2.md`

Expected classification: Complicated. Cause and effect are knowable with analysis of the attached material.

```text
3. **Add a limit guard (Complicated).** Add a boot check that fails startup when pods times `max_size` exceeds the OPS-412 limit. Step 3 waits until OPS-412 is read, because step 1, step 2 do not. 
   Given pods times `max_size` above the OPS-412 limit
   When the config loader boots
   Then startup fails with a message that names the limit.
   This prevents a repeat at the next release. Complicated domain: the correct guard needs analysis of the ticket before the practice is chosen [5].
```

- Domain right:
- Reason states cause and effect:

## 23. T1, action 1, labelled Clear

File: `responses/perplexity_kimi-k3@low/T1-s1.md`

Expected classification: Clear, despite the wording. A formatter with a lock file ends the dispute. The word "culture" points the wrong way.

```text
1. **Adopt the dbt SQL style guide as the written rule, verbatim, in a one-hour meeting.** This removes the blocker "no shared source of truth". Cynefin domain: Clear, because a published guide exists and needs no analysis. Test (evaluative): rubric is adoption by majority vote in one meeting, threshold 60% yes, evidence is the recorded vote [3].
```

- Domain right:
- Reason states cause and effect:

## 24. X1, action 1, labelled Confused

File: `responses/xai_grok-4.7@low/X1-s1.md`

Expected classification: Complex. Cause and effect are visible only afterward. No metric exists.

```text
1. Domain: Confused, because the cause pattern is not known yet.
Kind: evaluative, that is, the output is a judgment.
Test, written first.
Rubric weights: invented fact 40%, missed fact 40%, wrong label 20%.
Evidence for invented fact: a summary phrase with no support in the case.
Evidence for missed fact: a promise, product, or status in the case that the summary omits.
Evidence for wrong label: a priority, product, or sentiment that does not match the case.
Pass mark: two reviewers agree on at least 24 of 30 cases.
Then, in one session, label 30 cases with that rubric.
This removes the blocker of an undefined fault.
Step 2 MUST NOT start until this pass mark is met.
```

- Domain right:
- Reason states cause and effect:

## 25. H1, action 2, labelled Complicated

File: `responses/anthropic_claude-sonnet-5-5@medium/H1-s3.md`

Expected classification: Chaotic for the first action, then Complicated for the rest.

```text
2. **Read the error logs in parallel with Step 1.** Increment: one filtered log query. Blocker removed: the unknown failing service. Domain: Complicated, because logs make the cause knowable. Kind: deterministic. Step 2 MUST NOT delay Step 1.
   - Given the logs from 09:10 to 09:15
   - When you filter for status 500
   - Then the first error message and the failing service are posted in the incident channel
```

- Domain right:
- Reason states cause and effect:

## 26. X2, action 2, labelled Clear

File: `responses/google_gemini-3.8-flash@medium/X2-s3.md`

Expected classification: Complex. Human systems, many interacting causes.

```text
2. Step 2: Insert the retrospective action item into the sprint backlog.
Step 2 MUST NOT start until the test in Step 1 passes.
Test: Deterministic.
Given an approved retrospective action item from Step 1
When the sprint planning update occurs
Then the action item appears in the active sprint backlog with assigned estimation points
Increment: Import the single action item directly into the team issue tracker.
Capability: This step adds direct visibility by placing process work alongside feature delivery work.
Cynefin domain: Clear, because issue tracking follows known administrative procedures.
```

- Domain right:
- Reason states cause and effect:

## 27. K2, action 2, labelled Complicated

File: `responses/openai_gpt-6.1-sol@medium/K2-s1.md`

Expected classification: Complicated.

```text
2. **Complete one operations responsibility review after Step 1 passes.**

   **Test first, deterministic:**
   ```gherkin
   Given Northwind's proposed service terms
   When operations reviews the responsibility checklist
   Then each routine task and incident period has an accepted owner
   And each internal task has a cost in the cost sheet
   ```

   Produce an agreed responsibility checklist, including support outside business hours. This exposes work that the managed-service label does not define.

   **Domain: Complicated**, because an operations review must identify gaps between vendor duties and internal duties.
```

- Domain right:
- Reason states cause and effect:

## 28. U1, action 1, labelled Chaotic

File: `responses/perplexity_glm-5.3-flash@medium/U1-s2.md`

Expected classification: Confused. The prompt does not say which build, how often, or since when.

```text
1. **Stabilise the pipeline (Chaotic, because no cause is visible yet and flow must return first).** Add auto-retry capped at 2 reruns, and tag rerun events so they do not hide the real failure rate. Increment: one CI config change, one working session. Blocker removed: merges blocked by red. Test, written first:

   ```gherkin
   Given a pipeline step that fails on its first run
   When the pipeline executes the step
   Then the step reruns at most 2 times
   And the run record shows the rerun count
   ```
```

- Domain right:
- Reason states cause and effect:

## 29. H1, action 5, labelled Clear

File: `responses/perplexity_kimi-k3@low/H1-s2.md`

Expected classification: Chaotic for the first action, then Complicated for the rest.

```text
5. State on the exec call: "Mitigation started at 09:2X; rollback result at 09:30; root cause follows within one hour." Domain: Clear, because status reporting is scripted.
```

- Domain right:
- Reason states cause and effect:

## 30. U1, action 4, labelled Clear

File: `responses/xai_grok-4.7@low/U1-s3.md`

Expected classification: Confused. The prompt does not say which build, how often, or since when.

```text
4. Test first.
Given the class and the rate,
When the note is stored,
Then it states the class, the rate, and one next fix, and it has no product diff.
Write that note in one session. This removes a fix aimed at the wrong class. Domain: Clear, because the wait rule is already known. Step 4 MUST NOT start until the tests in Step 2 and Step 3 pass.
```

- Domain right:
- Reason states cause and effect:

## 31. U2, action 4, labelled Clear

File: `responses/anthropic_claude-sonnet-5-5@medium/U2-s3.md`

Expected classification: Confused.

```text
4. **Correct the report and have a second person verify it.** Increment: fix the named causes and recompute the listed figures. Blocker removed: the wrong figures stay in circulation. Kind: deterministic. Domain: Clear, because the fix follows from the named cause. Step 4 MUST NOT start until Step 3 names a cause for each gap.
   Test, written first:
   - Given the corrected report
   - When a reviewer recomputes the listed figures from source data
   - Then zero mismatches remain

If A2 is false, replace Step 2 with a check of the report's internal totals, and ask for the source data before Step 3.
```

- Domain right:
- Reason states cause and effect:

## 32. X1, action 4, labelled Clear

File: `responses/google_gemini-3.8-flash@medium/X1-s2.md`

Expected classification: Complex. Cause and effect are visible only afterward. No metric exists.

```text
4. Step 4: Deploy inline agent feedback buttons inside the support interface.
   - Test (Deterministic):
     Given an active support agent viewing a generated summary
     When the agent clicks the thumbs-down button and selects an error reason
     Then the system logs the ticket identifier, prompt version, and reason code to the analytics table
   - Increment: Build binary feedback buttons with an error dropdown in the user interface.
   - Capability added: Creates continuous production monitoring to replace periodic manual sampling.
   - Cynefin domain: Clear, because adding feedback logging follows established user interface patterns. Step 4 MUST NOT start until the test in Step 1 passes.
```

- Domain right:
- Reason states cause and effect:

## 33. X2, action 3, labelled Complex

File: `responses/openai_gpt-6.1-sol@medium/X2-s3.md`

Expected classification: Complex. Human systems, many interacting causes.

```text
### 3. Run a bounded trial and review the result

Step 3 MUST NOT start until Step 2 passes.

**Acceptance test first, stochastic, meaning results can vary:**

- **Metric:** Use the outcome measure named on the card.
- **Baseline:** Record the preceding five comparable cases.
- **Pass threshold:** Set a numeric target before the trial starts.
- **Sample:** Compare the next five comparable cases with that baseline.
- **Acceptance:** Keep the change only if it reaches the target without exceeding the agreed cost.

Cap the trial at two weeks and one hour of extra team effort. Stop earlier if it causes harm or exceeds that budget. If five cases do not occur, record insufficient evidence rather than success.

**Output:** One keep, revise, or stop decision at the next retrospective.

**Domain: Complex**, because the effect becomes visible through the trial. Its value is uncertain; five cases provide a local signal, not statistical proof. [judgment]
```

- Domain right:
- Reason states cause and effect:

## 34. K1, action 8, labelled Complicated

File: `responses/perplexity_glm-5.3-flash@medium/K1-s1.md`

Expected classification: Complicated. Cause and effect are knowable with analysis of the attached material.

```text
4. Domain: Complicated, because analysis of the ticket must pick the value first.

**Step 3.** If the limit stays at 32, file a capacity request with the demand number.
```

- Domain right:
- Reason states cause and effect:

## 35. H2, action 5, labelled Clear

File: `responses/perplexity_kimi-k3@low/H2-s2.md`

Expected classification: Chaotic for action 1 (a single owner and a hold on substantive outbound statements). Then Complicated for the facts: was the statement false, and what does the record show. Then Complex for the response to the public and the board.

```text
5. Set a single messaging channel for the next 72 hours. One spokesperson, one approved fact sheet, all inbound questions logged. Blocker removed: future drift back into three narratives. Domain: Clear, because message discipline is a known practice. Kind: deterministic.
   - Given the remedy from Step 4 is delivered,
   - When any of Legal, PR, or the Board receives a press or investor question,
   - Then it routes to the single spokesperson within one hour.

Sequencing: Step 3 and Step 2 can run in parallel. Step 4 MUST NOT start until the test in Step 2 passes. Step 5 follows Step 4.

If A1 is false, replace Step 2 with a formal request to the journalist for the basis of the claim, and extend the holding posture by 24 hours.
```

- Domain right:
- Reason states cause and effect:

## 36. U2, action 4, labelled Complicated

File: `responses/xai_grok-4.7@low/U2-s2.md`

Expected classification: Confused.

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

- Domain right:
- Reason states cause and effect:

## 37. U2, action 1, labelled Confused

File: `responses/anthropic_claude-sonnet-5-5@medium/U2-s1.md`

Expected classification: Confused.

```text
1. **List the suspect figures.** Increment: one table with figure, reported value, expected value, and the reason for doubt. Blocker removed: we cannot classify the problem without knowing which numbers are off. Domain: Confused, because the scope of the problem is unknown, so this step gathers what we need to classify. Kind: deterministic. Test:
   - Given the Q3 report and the user's list of doubts
   - When each doubtful figure is entered in the table
   - Then every row has a value, an expected value, and a reason
```

- Domain right:
- Reason states cause and effect:

## 38. X1, action 4, labelled Clear

File: `responses/google_gemini-3.8-flash@medium/X1-s1.md`

Expected classification: Complex. Cause and effect are visible only afterward. No metric exists.

```text
4. Implement a binary feedback mechanism in the support tool interface for live agent ratings.
   - Dependency: Step 4 MAY run in parallel with Step 3.
   - Increment: Add thumbs-up and thumbs-down buttons with a one-click error tag to the summary widget.
   - Blocker: Removes the lack of ongoing production quality monitoring.
   - Domain: Clear, because adding feedback buttons to an existing user interface follows standard software patterns.
   - Test (Deterministic):
     - Given a support agent views a generated summary
     - When the agent clicks thumbs-down and selects an error reason
     - Then the system logs the ticket identifier, prompt version, summary text, and error reason to the analytics table
```

- Domain right:
- Reason states cause and effect:

## 39. H2, action 3, labelled Complicated

File: `responses/openai_gpt-6.1-sol@medium/H2-s2.md`

Expected classification: Chaotic for action 1 (a single owner and a hold on substantive outbound statements). Then Complicated for the facts: was the statement false, and what does the record show. Then Complex for the response to the public and the board.

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

- Domain right:
- Reason states cause and effect:

## 40. X1, action 2, labelled Clear

File: `responses/perplexity_glm-5.3-flash@medium/X1-s1.md`

Expected classification: Complex. Cause and effect are visible only afterward. No metric exists.

```text
2. **Add a verification gate (Clear, high leverage, run in parallel from step 1).** After each generated summary, run a second pass that checks each statement against the ticket messages. If a check fails, output "No summary available". This removes the largest blocker now: a wrong summary reaches agents. Test written first (deterministic):

   ```gherkin
   Given a summary with one statement not present in the ticket
   When the verification pass runs
   Then the output is "No summary available"
   ```

   Clear domain: cause and effect are known and the step is one scripted pass.
```

- Domain right:
- Reason states cause and effect:
