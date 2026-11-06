# Procedure: Fix banned words and long sentences

1. Read the target file with `read_file`. Record its facts, qualifications, instructions, and structure before any edits.
2. Run `check_file` on the target file. Use its banned-word results and sentence-length results as the baseline.
3. Replace each banned word with plain, neutral text. Remove empty emphasis without changing facts or the strength of a claim.
4. Split each flagged sentence into shorter sentences. Keep each condition, exception, cause, and link to its original claim.
5. Check all instructions for a maximum of 20 words per sentence. Keep descriptions at 25 words or fewer.
6. Compare the draft with the original. Preserve names, numbers, dates, units, duties, uncertainty, and the order of events.
7. Write the complete revised file with `write_file`. Do not edit other files as part of this pass.
8. Run `check_file` again on the revised file. If it reports banned words or long sentences, repeat steps 3 through 8.
9. Read the revised file and compare it with the original record. Fix any lost meaning, then repeat the checks.
10. Finish only when the checks report no banned words or long sentences and the meaning remains intact.
11. Apply this procedure to `notes/a.md`, then `notes/b.md`, then `notes/c.md`. Finish each file before the next.
