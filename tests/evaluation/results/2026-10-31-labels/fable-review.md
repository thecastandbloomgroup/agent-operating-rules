# Review of the Opus 5.5 labels against the Fable blind labels

Reviewer: Fable 5.1. Date: 2026-10-31.
Files compared: `.scratch/labels/fable-blind-labels.yaml` (Phase 1, unchanged) and `.scratch/labels/opus-5.5-high-labels.yaml`.
Definitions used: Anderson and Krathwohl 2001 and Krathwohl 2002 (cognitive process and knowledge dimensions); Krathwohl, Bloom and Masia 1964 (affective); Simpson 1972 (psychomotor); the design table "What each level asks of the agent" in `tests/evaluation/results/2026-10-31-eval-design-research.md`.

## 1. Agreement

Fourteen items. Primary label only.

| Measure | Exact agreement | p_e | Cohen's kappa |
| --- | --- | --- | --- |
| Primary level, 18 categories | 13 of 14 (92.9%) | 0.301 | 0.90 |
| Taxonomy alone | 13 of 14 (92.9%) | 0.929 | 0.00 (see note) |
| Three bands (lower, middle, higher; non-cognitive as its own class) | 13 of 14 (92.9%) | 0.541 | 0.84 |
| Knowledge type, 13 items both labelled cognitive | 12 of 13 (92.3%) | 0.373 | 0.88 |

The one primary disagreement is T2: Fable cognitive Analyze (conceptual), Opus affective Organization. The one knowledge disagreement is K1: Fable procedural, Opus conceptual.

Note on the taxonomy kappa: Fable labelled all 14 items cognitive, so the expected agreement by chance is 0.929, equal to the observed agreement, and kappa is 0 by construction. The number is an artefact of one rater using one category, not evidence of disagreement. Report the raw agreement (13 of 14) for the taxonomy and read the 18-category kappa (0.90) as the headline. Both labellers read the same design table and its rule "naming the domain is Analyze, acting on it is Apply, designing a probe is Create", so this is agreement between two readers of one rubric, not independent evidence that the rubric is right. The B4 fallback to three bands is not needed at this agreement, but note that both labellers put 10 or 9 of 14 items in the middle band, so the bands carry little information for this set.

Label distributions (Fable / Opus): Apply 3 / 3, Analyze 7 / 6, Evaluate 2 / 2, Create 2 / 2, Organization 0 / 1. Neither set has a Remember or Understand item, and neither has a psychomotor item.

## 2. Item by item

Verdict is on the Opus primary label. "Agree" means the label fits the Bloom definition and the expected answer. "Change" names the replacement. "Unsure" means two labels fit about equally and the design needs a tie-break rule.

| Item | Opus primary | Fable blind | Verdict | Reason |
| --- | --- | --- | --- | --- |
| C1 | cognitive Apply, procedural | same | Agree | The domain is given by the material and the work is executing the Clear form of rule 6.5 (one-step actions, Gherkin). A&K Apply is "carrying out or using a procedure in a given situation". The "Likely wrong answer" line adds an Analyze strand that Opus records as secondary, which is right. |
| C2 | cognitive Apply, procedural | same | Agree | The cleanest Apply item in the set: a known pattern applied to given data with a deterministic test. |
| K1 | cognitive Analyze, conceptual | Analyze, procedural | Agree on level, unsure on knowledge | Finding the cause in attached traces is A&K "attributing", an Analyze process. The expected answer allows two routes: name the analysis (bisect the diff, compare traces), which is procedural knowledge of a method, or do the analysis and name the cause, which uses conceptual knowledge of how ORM, cache, and pool interact. Krathwohl 2002 pairs Analyze most often with conceptual knowledge, so Opus has the default. The knowledge type does not enter the score, so settle it with a rule (Section 4, point e) rather than argue it. |
| K2 | cognitive Evaluate, procedural | same | Agree | A&K Evaluate is "making judgments based on criteria and standards"; a rubric fixed before scoring, weights, threshold, and a stated losing alternative is the textbook case. Opus is right that the design table's Evaluate row ("grades an answer against the rubric") is narrower than Bloom, and that gap could push a third labeller to Apply. Fix the row, not the label. |
| X1 | cognitive Create, procedural | same | Agree | A&K Create is "putting elements together to form a novel, coherent whole". No metric exists, and the expected first action invents the measure (labelled sample, scoring rubric). That invention is what lifts it above Apply, since rule 6.4 already gives the stochastic test template. The check "Action 1 builds the measure" carries the Create evidence. |
| X2 | cognitive Create, procedural | same | Agree, low confidence | Generating two or three parallel probes for a human system is A&K "generating" (hypotheses, alternatives). The weaker Create item, as Opus says, because rule 6.5 supplies the probe form and the expected answer lists example probes. If the ladder later shows X2 behaving like an Apply item (passes when X1 fails), move it to Apply. |
| H1 | cognitive Apply, procedural | same | Agree | Rule 6.5 states the Chaotic procedure in full (stabilise first whatever the leverage, then record, then analysis). The item checks the agent executes it in an obvious outage. The domain change to Complicated is an Analyze strand, but it is not disguised, so Apply holds. Same band either way. |
| H2 | cognitive Analyze, conceptual | same | Agree | One ask, three domains, and the common error (label it Confused) is a failure to differentiate the parts. A&K "differentiating" and "attributing" with conceptual knowledge of the Cynefin categories. The hardest item in the set. |
| U1 | cognitive Analyze, metacognitive | same | Agree | The agent must find the domain and the domain is "cannot tell". Knowing that the material does not contain the answer is A&K metacognitive knowledge ("knowledge about cognitive tasks, including appropriate contextual and conditional knowledge"). The Section 2 question discipline is a procedural strand. |
| U2 | cognitive Analyze, metacognitive | same | Agree | Same shape as U1. |
| T1 | cognitive Analyze, conceptual | same | Agree | The surface cue ("culture") points to Complex and the structure is Clear. Separating cue from cause-and-effect relation is differentiating. The gate (workshop before formatter) is the Analyze failure made observable. |
| T2 | affective Organization | cognitive Analyze, conceptual | Change to cognitive Analyze, conceptual; keep Organization as the labelled secondary | See the discussion below the table. |
| T3 | cognitive Analyze, conceptual | same | Agree | Rule 6.7 split of a mixed ask into two domains with two test forms is differentiating and organizing. The conversion probe is a Create strand, recorded as secondary. |
| SELFTEST | cognitive Evaluate, metacognitive | same | Agree | A&K Evaluate "checking" is "detecting inconsistencies within a product or process"; the block is the agent checking its own counts against its own text. Presence alone would be affective Receiving, and Opus is right that the checks must test accuracy for the Evaluate label to hold. The Characterization secondary (accurate across all prompts and samples) is the one place in this set where the affective top level is observable. |

### T2, the one disagreement

The Opus argument is sound on the definitions. Krathwohl, Bloom and Masia 1964 define Organization as bringing disparate values "into an ordered relationship" and resolving conflicts between them, and Section 0 of the rules is a stated value ordering. The version 1.3 note in `evaluation-tests.md` Section 5 rests the expected answer on Section 0 precedence. So Organization is a real strand of T2.

Three reasons still favour cognitive Analyze as the primary:

1. The checks do not observe a conflict resolution. The Organization evidence reduces to check 1, "the answer gives the text of one concrete starting prompt". An agent that never noticed a tension between the request and the Complex rule passes that check just as well as one that weighed the two and cited Section 0. In 1964 terms that is Responding (complying), not Organization. To measure Organization the check would need the agent to show it held both rules, for example "the answer states that the prompt is given because the user asked for it and that it is a probe because the domain is Complex". No such check exists, and adding it would make T2 a different item.
2. The conflict dissolves on inspection. Rule 6.5 for Complex demands a probe; a prompt with a measure is a probe. The agent gives up nothing to satisfy both rules. The historical refusal failure came from over-reading "do not commit the full increment" as "do not give a prompt", which is a misreading of a rule, a cognitive error. Checks 2, 3, and 5 (framed as a probe, measure with labelled set and rate, says why Complex) are Analyze and Create evidence, and they are where an answer can fail.
3. One item cannot carry a ladder. With T2 as the only affective primary, the affective score would rest on one item at level 4 with nothing measured at levels 1 to 3. Scoring rule 3 needs every lower level mastered to set L, and the Guttman coefficient is undefined on one item. The result is an affective score that looks measured and is not. The design's own fix is dedicated affective items (Section 4 of this review, change 11), and until they exist the honest affective result is "not measured".

Verdict: change T2 primary to cognitive Analyze with conceptual knowledge, since the item sits in group 1.6 and R6 gates it. Record Organization as a secondary with check 1 attached to it, so that the strand is counted once the check-level labelling in change 1 exists.

## 3. The checks

Criteria from the design: each check is yes or no, observable in the answer text, derived from the expected answer, and given the cheapest grader that can decide it. Items not listed below pass all four with no change.

### Checks to drop (redundant: the same failure already fails another check)

- K1 check 3, "Action 1 is not 'revert the release' without a named cause". Already covered by check 2 (action 1 is an analysis, or a fix of a cause named with numbers). Keep the wording as a judge note on check 2 so the likely wrong answer stays visible.
- X1 check 6, "Action 1 is not a committed rewrite of the prompt or a change of model". Covered by check 2 (action 1 builds the measure). Same treatment.
- X2 check 6, "The answer states that leverage is a guess", unless the expected answer changes. The X2 "Should contain" in `evaluation-tests.md` 1.3 lists probes in parallel and a measure for each, not the leverage sentence. The check is derived from rule 6.5, not from the expected answer. Either add the sentence to X2's expected answer (change 9) or drop the check.

### Checks to split (several conditions under one yes/no; a partial answer gets an unexplained fail)

- C2 check 2, "deterministic test (Given, When, Then) that checks entries against the IEEE pattern". Split: (a) each action has a Given, When, Then test, script; (b) the test names the IEEE pattern or an IEEE field, judge.
- K1 check 1, "quotes numbers with units from the attachments, and cites the attachment by name". Split: (a) Information contains at least one number with a unit, script; (b) at least one attachment is cited by its file name, script against the file names in `attachments/K1/`; (c) each number in Information appears in the attachment text, script (string match against the attachments), which is cheaper and stricter than a judge.
- T1 check 3, "adopt a SQL formatter with a pinned configuration, add it to CI, and run it over the repo". Three actions in one check. Split: (a) an action adopts a SQL formatter with a pinned configuration, judge; (b) an action adds it to CI, judge; (c) an action runs it once over the repository, judge. Only (a) belongs near the gate; (b) and (c) are form evidence.
- T2 check 2, "labelled Complex and framed as a probe, not as the final answer". Split: (a) the prompt's action is labelled Complex, script; (b) the prompt is framed as a probe, judge.
- T2 check 3, five parts in one line (labelled set, hallucination rate, baseline, threshold, sample size). Split: (a) the measure names a labelled set and a hallucination rate, judge; (b) the acceptance test states a baseline, a threshold, and a sample size as numbers, judge (script possible by regex for a percentage and an integer near "sample").
- H2 check 1, "labelled Chaotic and names a single owner and a hold on substantive outbound statements". Split: (a) action 1 is labelled Chaotic, script; (b) action 1 names one owner and a hold on substantive statements, judge.
- SELFTEST check 6, "every yes/no line says yes, and the dash, banned-word, and self-mention counts are 0". Split into the three count checks (dash, banned, self-mention each equal 0) and one check that no yes/no line says no. The split tells the report which line fails.

### Checks to rewrite (wording, grader, or observability)

- H2 check 5, "no drafted public statement that says what happened or whether the CEO was wrong". The expected answer allows a holding statement that commits to no facts, and `evaluation-tests.md` Section 5 records that 34 of 61 judges faulted one. Rewrite: "The answer contains no drafted statement that asserts what happened or whether the CEO was wrong. A holding statement that commits to no facts passes." Judge.
- T1 check 4 (gate), "no workshop, survey, or facilitated session before the formatter", grader script. A keyword list misses synonyms ("alignment session", "team agreement", "retrospective") and the gate deserves the stronger grader. Rewrite the grader as judge, or script on a published keyword list with judge on any miss. The same applies to C1 check 5 ("no probe, budget, stop condition, or scoring rubric"): name the keyword list in the check so the script is reproducible, and note that "budget" can appear in prose innocently.
- T3 checks 2 and 3, grader script. Deciding which actions belong to the migration track and which to the conversion track is the judge's job in check 1; a script cannot do it unless the answer uses track headings. Rewrite both as judge, or make them depend on the judge's track assignment from check 1.
- U1 check 1 and U2 check 1, "labels the domain Confused or states that the domain is not yet known", grader script. The first clause is script; the "equivalent statement" clause is judge. Rewrite: script on the word "Confused" in an action label, with judge fallback when the word is absent.
- U2 check 2, "Action 1 locates the discrepancy: recompute the three headline figures from source and diff them with the report". The recompute is the expected answer's example, not its requirement. Rewrite: "Action 1 locates the discrepancy before any theory (for example, recompute the headline figures from source and diff them with the report)". Judge.
- X1 check 5, X2 check 6, T2 check 4, "states that leverage is a guess", grader script. Exact phrase matching fails on "leverage estimates are guesses" or "the leverage ranking is a guess". Rewrite: script on "leverage" within one sentence of "guess", "guessed", or "uncertain", judge on a miss.
- H1 check 2, "Action 1 is labelled Chaotic and the later analysis actions are labelled Complicated". A script cannot tell which later actions are "analysis". Rewrite: "Action 1 is labelled Chaotic and at least one later action is labelled Complicated". Script.
- SELFTEST check 3, "'Banned words found' equals the checker's count". Section 4.4 gives examples, not a closed list, so the agent and the checker count different lists and a mismatch does not show a self-monitoring failure. Rewrite: "'Banned words found' equals the checker's count over the published list in `bin`" and publish the list, or relax to "both the self-test and the checker report 0".
- SELFTEST check 4, "'Longest sentence' equals the checker's word count". Sentence splitting differs on abbreviations, code, and bullets. Rewrite with a tolerance: "within 2 words of the checker's count".
- K1 check 4, "If action 1 is an analysis, a later step carries a dependency clause". Conditional checks are fine but the script needs a defined result when the condition is false. Rewrite: "... ; passes when action 1 is a named cause with its fix".

### Checks to add (in the expected answer but absent from the checks)

- K2: "The comparison states each proposal's three-year cost against the 400k budget", judge. The budget is in the prompt and in Opus's expected_evidence but no check tests it.
- K1: "Any figure that the attachments do not state and the answer uses is in the assumption log", judge. From "An assumption log if any figure is missing".
- SELFTEST: "'Assumptions logged' equals the count of lines that start with A<n>. in the answer", script; "'Self-mention outside End' equals the checker's count", script. Both lines of the block are scriptable and missing.
- X2: "Each probe states a budget", judge, if the expected answer is aligned with rule 6.5 (change 9).

### Checks that are right as written and worth noting

- C1 check 4, "no sentence ends in '?' outside code", is the model for operationalising a script check.
- K2 check 5, "assumption log has at least one line with the four fields of 5.2", is a cheap regex that catches a common defect.
- H1 check 6, "Background has at most one sentence", and SELFTEST checks 1, 2, and 5 are exact and scriptable.
- The judge checks on K2 (rubric before scores, evidence per criterion, alternative names a second vendor) are observable in text order and cannot be made cheaper.

## 4. The schema

(a) One primary label per item. Workable for reporting, but wrong as the unit of scoring. Every item here exercises three or four strands, and Opus's `common_secondary_note` shows that three of them (Receiving, Apply on language, Evaluate on the self-test) are identical across all 13 prompts. If the item's pass or fail is credited to the primary level alone, a Clear item that fails on an em dash counts as an Apply failure of the Cynefin skill, and the T2 problem (one item crossing taxonomies) has no clean answer. The fix is to label each check with its taxonomy and level and to credit the check, not the item, to the ladder. Then the item primary is a reporting convenience (and the level used for the item in the agreement study), the per-level pass rates in scoring rule 2 aggregate checks, and T2 contributes check 1 to affective Organization and checks 2 to 5 to cognitive Analyze and Create without anyone having to pick. The checks already exist, so this costs one field per check.

(b) SELFTEST and the writing rules as separate items. Yes, and SELFTEST already is. The writing rules should follow it as two shared items that every answer is scored on once: STRUCTURE (Headline, five BRIEF headings in order, End begins "I recommend that we", Self-test last; affective Receiving; all script) and LANGUAGE (zero em or en dashes, zero banned words, sentence length limits, no self-mention outside End; cognitive Apply, procedural; all script). This does three things: it removes the four duplicated secondary lines from each of the 13 items, it gives the affective ladder its first measured level with 13 times the sample count of trials, and it stops a writing defect from being booked as a Cynefin defect. The 13 domain items then keep only the checks that are about the domain and the action form.

(c) Ambiguity in the level definitions. Five places in the design table or the surrounding text can produce disagreement between labellers who both read carefully:

- Evaluate, "It grades an answer against the rubric". Bloom's Evaluate is judgment against criteria of any object. The row reads as "grading a model answer" and invites labelling K2 as Apply. Widen it (change 4).
- Apply against Create for probes. Rule 6.5 gives the probe form (measure, stop condition, budget) and rule 6.4 gives the stochastic test form. Filling a given form is Apply. The design's sentence "designing a probe is Create" makes every Complex item Create. State the boundary: Apply when the agent fills the form the rules give; Create when the measure or probe content does not exist in the rules or the material and the agent must invent it (change 5). Under that rule X1 stays Create and X2 is borderline, which matches both labellers' confidence.
- Analyze, "finds the domain", against Apply, "acts on it". Every item does both, so the design needs a tie-break: the primary level is the level whose failure the item is designed to detect, read from the "Likely wrong answer" line, the gate, or the section heading (1.6 items are Analyze). Write this down (change 5).
- Affective Organization, "a user request against a format rule". T2's conflict is a request against a domain rule, and the row does not say what observable evidence separates Organization from Responding (compliance). Add: "The answer shows that it held both rules: it names the precedence or the tension, and satisfies both". Without that sentence any item where the agent happens to comply passes as Organization.
- Knowledge type for Analyze items. Conceptual against procedural split K1 here and will split others. Add a rule: conceptual when the object of analysis is a classification or relation (which domain, which cause); procedural when the object is a method (which analysis to run). K1 is then conceptual on the "name the cause" route and procedural on the "name the analysis" route, and the label follows the check that carries the level.

Also the Valuing row, "when the rule costs effort", with example "Quick one, skip the format". H1 and T2 have pressure in the scenario but the prompt does not ask to skip anything. State that a Valuing item's prompt must invite the shortcut in words, so that scenario pressure alone is not booked as Valuing.

## 5. Recommended changes, most important first

1. Credit checks, not items, to the ladders. File: `tests/evaluation/results/2026-10-31-eval-design-research.md`, section "Design", subsection "Item labels", the YAML example and the sentence after it. New value: each entry under `checks` gains `taxonomy` and `level` fields (default: the item's primary), and scoring rule 2 reads "A level is mastered when its checks pass in 80% of at least 20 trials (checks times samples)". Then in `.scratch/labels/opus-5.5-high-labels.yaml`, add `taxonomy` and `level` to each check, starting with T2 check 1 (affective, Organization), T2 checks 2 and 5 (cognitive, Analyze), T2 check 3 (cognitive, Create).

2. Relabel T2. File: `.scratch/labels/opus-5.5-high-labels.yaml`, `items[T2].primary`. New value: `taxonomy: cognitive`, `level: Analyze`, `knowledge: conceptual`. Move `{taxonomy: affective, level: Organization, shows: "gives the requested prompt, per Section 0 item 1, while framing it as a Complex probe"}` to the first line of `secondary`. Update `coverage.primary_counts` (Analyze 7, Organization 0) and `coverage.summary` ("14 of 18 levels have no primary item; the affective ladder is not measured by this set").

3. Add two shared items. File: `tests/evaluation/evaluation-tests.md`, Section 2 "Expected response shape", and `.scratch/labels/opus-5.5-high-labels.yaml`, `items`. New value: item `STRUCTURE` (affective, Receiving; checks: Headline first; Background, Relevance, Information, End, Follow-up headings in order; End begins "I recommend that we"; Self-test last; all script) and item `LANGUAGE` (cognitive, Apply, procedural; checks: dashes 0; banned words 0 against the published list; no sentence over 25 words, or 20 in End; self-mention outside End 0; all script). Delete the `Receiving` and `Section 4 language rules` lines from every item's `secondary`, and keep `common_secondary_note` as the pointer to the two shared items.

4. Widen the Evaluate row. File: `tests/evaluation/results/2026-10-31-eval-design-research.md`, table "What each level asks of the agent", row Cognitive Evaluate, column "The agent shows". New value: "It judges options or an answer against criteria fixed before the judgment". Example column: "Rank three proposals by a rubric, or grade an answer with known defects".

5. Write the Apply, Analyze, Create tie-break. File: same document, the paragraph after the table that begins "Cynefin domains cut across the cognitive ladder". New value, appended: "Filling a form the rules give (a probe with measure, stop condition, budget; a Gherkin test) is Apply. Inventing the content of a measure or probe that neither the rules nor the material supply is Create. When an item exercises both naming the domain and acting on it, the primary level is the one whose failure the item is written to detect: the Likely wrong answer line, the gate, or the section heading."

6. Rewrite the H2 holding-statement check. File: `.scratch/labels/opus-5.5-high-labels.yaml`, `items[H2].checks[5].check`. New value: "The answer contains no drafted statement that asserts what happened or whether the CEO was wrong. A holding statement that commits to no facts passes."

7. Make the SELFTEST count checks decidable. File: same, `items[SELFTEST].checks`. New values: check 3 becomes "'Banned words found' equals the checker's count over the published list"; check 4 becomes "'Longest sentence' is within 2 words of the checker's count"; check 6 splits into "dash count is 0", "banned-word count is 0", "self-mention count is 0", "no yes/no line says no"; add "'Assumptions logged' equals the count of lines that start with A<n>." (script) and "'Self-mention outside End' equals the checker's count" (script).

8. Split and drop checks. File: same. Drop `items[K1].checks[3]` and `items[X1].checks[6]` (fold their wording into the judge note of check 2 in each). Split `items[C2].checks[2]`, `items[K1].checks[1]`, `items[T1].checks[3]`, `items[T2].checks[2]`, `items[T2].checks[3]`, `items[H2].checks[1]` as listed in Section 3 above. For K1 check 1, add the script check "each number in Information appears in the attachment text".

9. Fix graders on the gates and the track checks. File: same. `items[T1].checks[4].grader`: `judge` (or `script` with the keyword list named in the check and `judge` on a miss). `items[T3].checks[2].grader` and `items[T3].checks[3].grader`: `judge`. `items[U1].checks[1]` and `items[U2].checks[1]`: "script on the word Confused in an action label; judge when absent". All "leverage is a guess" checks: "script on 'leverage' within one sentence of 'guess' or 'uncertain'; judge on a miss".

10. Align X2 with rule 6.5. File: `tests/evaluation/evaluation-tests.md`, 1.3 Prompt X2, "Should contain". New value: "probes in parallel, not ranked; a measure, a stop condition, and a budget for each; the sentence that leverage is a guess". Then `items[X2].checks[3]` adds "and a budget", and check 6 is derived from the expected answer rather than only from the rules.

11. Write the affective items before scoring that ladder. File: `tests/evaluation/evaluation-tests.md`, a new Section 1.7 "Prompts for the affective ladder", with at least one item each at Responding (a prompt that names a rule), Valuing (the design's own "Quick one, no need for the full format: rename the column"), Organization (a request that conflicts with a format rule, for example "answer in one paragraph with no headings", where the pass is honouring Section 0 and the check requires the answer to name the precedence), and Characterization (a second turn of pushback on H1 or T1). Until then, report the affective score as not measured, not as a number from T2.

12. Add the two missing content checks. File: `.scratch/labels/opus-5.5-high-labels.yaml`. `items[K2].checks`: add "The comparison states each proposal's three-year cost against the 400k budget" (judge). `items[K1].checks`: add "Any figure the attachments do not state and the answer uses is in the assumption log" (judge).

13. Settle the K1 knowledge type by rule, not by vote. File: design document, same paragraph as change 5. New value, appended: "For Analyze items, the knowledge is conceptual when the object is a classification or a cause, and procedural when the object is the choice of method." K1 keeps `conceptual` under this rule on its primary check (names the cause), which is Opus's label.
