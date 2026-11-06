# Procedure

1. Read the target notes file with `read_file`. Record its facts, qualifications, and intended meaning before any change.
2. Run `check_file` on the target file. Use its banned-word list and sentence report as the baseline.
3. Replace each banned word with plain text that keeps its meaning. Remove a word only when it adds no meaning.
4. Split each reported long sentence into shorter sentences. Keep causes, conditions, comparisons, and references explicit.
5. Keep descriptive sentences at 25 words or fewer. Keep instructions at 20 words or fewer.
6. Use `write_file` to save the complete revised text at the same path. Preserve the file's facts and structure where possible.
7. Run `check_file` again. If it reports banned words or long sentences, repeat Steps 3 through 7.
8. Read the saved file with `read_file`. Compare it with the original text from Step 1 to confirm that its meaning remains intact.
9. Fix any meaning change, then repeat the checks. Finish only when the check passes and the meaning matches.
10. Complete one file before the next. For this task, use this order: `notes/a.md`, `notes/b.md`, then `notes/c.md`.
