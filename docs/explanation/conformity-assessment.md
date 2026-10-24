# First-party conformity assessment (self-assessment against the rules)

ISO/IEC 17000 defines first-party conformity assessment as assessment of a product by the person or organization that supplies it [1]. On 2026-10-23 I ran `deterministic-tests.py` over the three Markdown files in this repository. I tested the rules file at the instruction limit (20 words per sentence). I tested README.md and evaluation-tests.md at the description limit (25 words).

| Test (rule)                                                   | Rules file   | README   | evaluation-tests.md |
| ------------------------------------------------------------- | ------------ | -------- | ------------------- |
| Sentences over the word limit (4.1.1)                         | 0 of 258     | 0 of 134 | 0 of 174            |
| Em or en dashes (4.3.1)                                       | 0            | 0        | 0                   |
| Banned words, all categories in banned-words.txt (4.2.3, 4.4) | 0            | 0        | 0                   |
| Self-mention outside End (4.4.5)                              | 0            | 0        | 0                   |
| Nominalizations, gerund nouns (4.1.6, 4.2.4)                  | 0            | 0        | 0                   |
| Passive voice instances (4.1.2)                               | 10           | 8        | 10                  |
| Flesch-Kincaid grade (4.1.7, cap 10)                          | 5.6          | 8.3      | 7.5                 |
| Citations numbered in order of first use (5.4.1)              | yes, 1 to 15 | yes, 1   | none cited          |
| One citation per rendered line (5.4.1)                        | yes          | yes      | n/a                 |
| Blank line between reference entries (5.4.1)                  | yes          | yes      | n/a                 |
| Every entry tagged P/S/T/U (5.4.5)                            | yes          | yes      | n/a                 |
| Entries listed but never cited                                | 0            | 0        | n/a                 |

Findings and fixes:

- The first run found one sentence over the limit in the rules file and four in the README. I split them all.
- The first run found eleven avoidable passives across the two files. I rewrote them in the active voice. The remaining passives fall under the 4.1.2 exception, where the agent is unknown or irrelevant. Examples: "cannot be traced", "the threshold is met". The rest sit inside the BCP 14 boilerplate, which is quoted text.
- The Flesch-Kincaid grade of the rules file is 5.6, below the band the rule first stated (8 to 10). Short imperative sentences drive the grade down. The rule meant to cap the top, not set a floor, so I changed 4.1.7 to "MUST NOT exceed 10".
- The script flagged "very likely" and "very unlikely" as boosters. They are IPCC scale terms. The script now exempts them. It also exempts quoted counter-examples such as "make a decision" in 4.2.
- Two tests have no script. I read for them: the MECE test in 1.2 on the lists in Sections 4.4, 5.4, 6.4 and 6.5, and the one-topic-per-paragraph rule in 4.1.3. I found no defect.

Limits: a first-party assessment shares the author's blind spots. The passive-voice and syllable counters are heuristics. A second-party or third-party assessment (ISO/IEC 17000, clauses 4.3 and 4.4) needs a reviewer who has not seen the file being written. The planned cross-provider trial is that second-party assessment.

These numbers are a record of the run on 2026-10-23. Since then, the grade reads only prose sentences. The README also holds less text now. Now `task test` and `task docs` run the same tests on each change.

## References

[1] ISO/IEC 17000:2020, Conformity assessment: Vocabulary and general principles. [P]
