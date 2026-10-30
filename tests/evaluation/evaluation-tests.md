# Evaluation Tests: Cynefin Classification in Recommendations

Version 1.2, 2026-10-30. Companion to model-operating-rules.md, Sections 6.4 and 6.5.

## Purpose

These tests are evaluative (rules file, 6.4). A deterministic test cannot grade a classification, because the right answer is a judgment with evidence. So each test fixes a rubric before the run. Run every prompt through every model with the rules file installed. Score each response against the rubric. Compare models on the scores, not on the prose.

## How to run

1. Install model-operating-rules.md as the system prompt.
2. Send one prompt per session. No prior context. When a prompt names an attached file, send the files of `attachments/<prompt ID>/` with it.
3. Save the full response.
4. Score it with the rubric in Section 3. Two graders, scored independently. Record both scores and the difference.
5. A test passes at 80 percent of available points, with no zero on a criterion marked "gate".

## 1. Prompts by domain

Each prompt names the domain it targets, the classification a correct response gives, the action form Section 6.5 requires, and the signals to look for.

### 1.1 Clear

**Prompt C1 (software)**
"Our Python service logs with print statements. Replace them with the standard logging module at INFO level. The service is 129 lines in one file, which I have attached."

Expected classification: Clear. Best practice exists and is known to everyone.
Expected action form: one-step actions. Each action is a deterministic increment with a Gherkin test.
Should contain: three to five actions ordered by leverage; each tagged "deterministic, Clear"; no probe, no budget, no question.
Should not contain: a question (the answer is in the material); a rubric; a request for analysis; any hedge.
Likely wrong answer: the model classifies this as Complicated to look careful. Deduct under criterion R2.

**Prompt C2 (non-software)**
"Format this reference list in IEEE style. The list is attached as plain text with author, title, publisher, year for each entry."

Expected classification: Clear.
Expected action form: one step per action. Test is deterministic: each entry matches the IEEE pattern.
Should not contain: questions, probes, or a Cynefin note longer than one line.

### 1.2 Complicated

**Prompt K1 (software)**
"Our API p95 latency rose from 120 ms to 900 ms after last week's release. The release touched the ORM layer, the cache config, and the connection pool. Logs, traces, and the diff are attached. Tell me what to do."

Expected classification: Complicated. Cause and effect are knowable with analysis of the attached material.
Expected action form: the first action names the analysis (bisect the diff, compare traces before and after). Build actions follow it and depend on it ("Step 2 MUST NOT start until Step 1 names the cause").
Should contain: an evidence section with numbers from the attachments. An assumption log if any figure is missing. A Kepner-Tregoe or Pugh layout if the model proposes a choice between fixes.
Should not contain: a fix committed before the analysis; a probe (the answer is knowable, so probing is waste).
Likely wrong answer: the model puts "revert the release" as action 1. That may be right as a stabiliser only if the prompt says production is down. It does not. Deduct under R3.

**Prompt K2 (non-software)**
"We have three vendor proposals for a data warehouse, attached. Budget is 400k over three years. Recommend one."

Expected classification: Complicated.
Expected action form: an evaluative action with a rubric fixed before scoring: criteria, weights, threshold, evidence per criterion. Then a scored comparison.
Should contain: the rubric before the scores; a stated alternative and why it loses; an assumption log for anything the proposals leave out.
Should not contain: a pick without the rubric; a probe.

### 1.3 Complex

**Prompt X1 (software)**
"We added an LLM-based summariser to our support tool. Agents say it is 'sometimes wrong'. We have no metrics. Make it better."

Expected classification: Complex. Cause and effect are visible only afterward. No metric exists.
Expected action form: safe-to-fail probes. Each probe states a measure, a stop condition, and a budget. The first probe builds the measure (a labelled sample and a scoring rubric). The response marks leverage as a guess.
Should contain: at least one action tagged "stochastic, Complex"; a sample size and threshold for the acceptance test; the sentence that leverage is a guess.
Should not contain: a committed rewrite of the prompt or model as action 1; a leverage ranking stated with confidence.
Likely wrong answer: the model treats this as Complicated and proposes "analyse the failures" as if the failures were recorded. They are not; the first step is to create the record.

**Prompt X2 (non-software)**
"Our team's retrospectives have stopped producing changes. People attend but nothing shifts. What should we do?"

Expected classification: Complex. Human systems, many interacting causes.
Expected action form: two or three small probes run in parallel, each with a measure and a stop condition. Examples: change the format for two cycles; rotate the facilitator; cap action items at one.
Should contain: probes in parallel, not ranked; a measure for each.
Should not contain: a single root cause stated as fact; a question that asks the user to diagnose it for the model.

### 1.4 Chaotic

**Prompt H1 (software)**
"Production is down. Checkout returns 500 for every user since 09:12. The on-call engineer is me and I have ten minutes before the exec call. What do I do?"

Expected classification: Chaotic for the first action, then Complicated for the rest.
Expected action form: action 1 stabilises (roll back the last deploy, or fail over) and comes first whatever its leverage. Action 2 establishes the record (capture logs and timeline). Later actions are Complicated analysis. The response tags them so.
Should contain: the stabiliser first. An explicit domain change between actions. Example: "Steps 3 to 5 are Complicated and MUST NOT start until Step 1 restores service".
Should not contain: a question; an analysis step before the stabiliser; more than one sentence of Background.
Gate: if action 1 is not a stabiliser, the response fails.

**Prompt H2 (non-software)**
"A journalist just published that our CEO's statement yesterday was false. Legal, PR, and the board are all messaging me. Nobody is aligned. What are the next steps?"

Expected classification: Chaotic for action 1 (a single owner and a hold on outbound statements), then Complex.
Expected action form: stabiliser first; then probes with stop conditions.
Should not contain: a drafted public statement (that is a committed action in a Chaotic domain).

### 1.5 Confused

**Prompt U1 (software)**
"The build is flaky."

Expected classification: Confused. The prompt does not say which build, how often, or since when.
Expected action form: Section 2 allows up to three questions, and each MUST state what the answer changes. Or: the model assumes, logs the assumption, and makes the first action "gather what is needed to classify". Example: collect the last 50 build results and the failing test names.
Should contain: either three or fewer questions with stated use, or an assumption log plus a classification action. The word "Confused", or an equivalent statement that the domain is not yet known.
Should not contain: a fix; four or more questions; a question with no stated use.

**Prompt U2 (non-software)**
"Something is off with the numbers in the Q3 report."

Expected classification: Confused.
Expected action form: as U1. The first action locates the discrepancy (recompute the three headline figures from source and diff).
Should not contain: a theory stated as the cause.

### 1.6 Prompts that invite a wrong classification

The wording of each prompt points to the wrong domain. A correct response names the real domain and says why.

**Prompt T1: a Clear task worded as Complex**
"Nobody on the team agrees on how to format our SQL. It causes friction in every review. Fix the culture problem."

Expected classification: Clear, despite the wording. A formatter with a lock file ends the dispute. The word "culture" points the wrong way.
Expected action form: one-step actions (adopt a formatter, add it to CI, run it once over the repo).
Should not contain: probes, surveys, or facilitated sessions.
Gate: a response that proposes a workshop before a formatter fails.

**Prompt T2: a Complex task worded as Clear**
"Just tell me the best prompt to make the model stop hallucinating."

Expected classification: Complex. The model should refuse the premise that one best prompt exists, in one sentence, and then propose probes with a measure.
Should contain: a measure (a labelled set and a hallucination rate), a baseline, a threshold, a sample size; the statement that leverage is a guess.
Should not contain: a single prompt presented as the answer.

**Prompt T3: Mixed domains in one ask**
"Migrate our auth service from sessions to JWT, and while you are at it make sign-up conversion better."

Expected classification: two parts. The migration is Complicated (deterministic test, known patterns, needs a design choice on token lifetime and revocation). The conversion ask is Complex (stochastic, needs a measure and probes).
Expected action form: per rule 6.7, split until each action has one kind and one domain. The two tracks are sequenced separately.
Should contain: an explicit split; different test forms for the two tracks (Gherkin for the migration, metric and sample size for conversion).
Should not contain: one undifferentiated list.

## 2. Expected response shape (all prompts)

Every response is also subject to the rules file. Grade these alongside the domain criteria:

- Headline first, End section begins "I recommend that we", Self-test last.
- Three to five actions, each with increment, blocker, test, and domain.
- Zero em or en dashes, zero banned words, no self-mention outside End.
- Citations only to the attached material or to sources identified with confidence. For these prompts, a response with zero citations and "[inference]" labels is acceptable; a response with fabricated references fails.
- Self-test block present and internally consistent with the response.

## 3. Rubric

Score each criterion 0, 1, or 2. Gate criteria must score at least 1 or the test fails.

| ID  | Criterion                                                                                | 0                              | 1                                          | 2                                                                                                      | Gate |
| --- | ---------------------------------------------------------------------------------------- | ------------------------------ | ------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ---- |
| R1  | Domain stated for every action                                                           | None stated                    | Some actions                               | Every action, with a one-line reason                                                                   | yes  |
| R2  | Domain is correct per Section 1                                                          | Wrong on the primary domain    | Right primary, wrong on a secondary action | All correct                                                                                            | yes  |
| R3  | Action form matches the domain (6.5)                                                     | Form contradicts domain        | Mostly matches                             | Every action matches: one-step, analysis-first, probe with budget, stabiliser first, or classify first | yes  |
| R4  | Ordering follows 6.5 trade-off rules                                                     | Leverage order ignores domain  | Minor misorder                             | Chaotic first, Confused next, Clear and Complicated by leverage, Complex probes parallel and capped    | no   |
| R5  | Test form matches the task kind (6.4)                                                    | Missing                        | Present but wrong kind                     | Gherkin, rubric, or metric with sample size as the kind requires                                       | yes  |
| R6  | Wrong classification avoided (1.6 prompts and prompts with a "Likely wrong answer" line) | Gave the likely wrong answer   | Partly                                     | Named the real domain and said why                                                                     | yes  |
| R7  | Questions per Section 2                                                                  | Four or more, or no stated use | Fewer than four but weak use               | Three or fewer, each with its use, or none when the material answers                                   | no   |
| R8  | Uncertainty calibrated (4.6)                                                             | Uncalibrated hedges            | Mixed                                      | Probability or IPCC term where the recommendation depends on it                                        | no   |
| R9  | Rules-file conformance (Section 2 above)                                                 | Structure missing              | Minor defects                              | Full structure, zero banned words, Self-test consistent                                                | no   |

Available points: 18 (16 for prompts without R6). Pass: 80 percent, with every gate at 1 or more.

Inter-grader difference above 3 points on any response means the rubric is unclear for that prompt. Record it and revise the prompt's expected signals before the next run.

## 4. Reporting

One row per model per prompt: prompt ID, model, grader A score, grader B score, gates passed (yes/no), one line on the main defect. Then one table per model: pass count out of 13, mean score, the criterion with the lowest mean. The criterion with the lowest mean across all models is the rule to fix first in the rules file.

## 5. Source-type note

The expected classifications in Section 1 are the author's judgment [judgment]. They were not validated against an external panel. Treat a persistent disagreement between a model and this file as a signal to review the expected answer, not only the model.
