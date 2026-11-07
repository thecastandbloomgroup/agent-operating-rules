# Procedure

1. Read the target notes file with `functions.read_file`.
2. Run `functions.check_file` on the target file to find banned words and sentences over 25 words.
3. Record each claim, condition, number, and instruction that the edit must keep.
4. Replace banned words with plain terms that keep the meaning. Delete a word only when it adds no meaning.
5. Split long sentences at clause boundaries. Keep each condition linked to its claim or instruction.
6. Keep instructions within 20 words and descriptions within 25 words. Preserve names, numbers, scope, and certainty.
7. Write the complete revised file with `functions.write_file`.
8. Run `functions.check_file` again. If it reports any issue, repeat steps 4 through 8.
9. Read the revised file with `functions.read_file`. Compare its meaning with the original text from step 1.
10. Correct any change in meaning, then repeat steps 7 through 9. Finish only when the checks and comparison pass.
11. Complete one target file before starting the next. For this task, use `notes/a.md`, then `notes/b.md`, then `notes/c.md`.
