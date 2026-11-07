# Procedure: repair one notes file

1. Read the target file with `functions.read_file`. Record its facts, claims, limits, and intent before any edits.
2. Run `functions.check_file` on the target file. Use its banned-word list and sentence reports as the initial test.
3. Replace each banned word with plain text that keeps the claim's meaning and strength. Do not add evidence or certainty.
4. Split each reported long sentence into shorter sentences. Keep the links between causes, conditions, contrasts, and results.
5. Keep each sentence at 20 words or fewer where practical. Keep all facts, names, numbers, and qualifications.
6. Write the revised file with `functions.write_file`. Keep its existing structure unless a sentence split requires a change.
7. Run `functions.check_file` again. If any banned words or long sentences remain, repeat steps 3 through 7.
8. Read the revised file with `functions.read_file`. Compare it with the original text from step 1 for meaning and omissions.
9. If the comparison finds a change in meaning, repair it. Repeat the checks and comparison until both pass.
10. Report the file's result. Finish this file before starting the next requested file.
