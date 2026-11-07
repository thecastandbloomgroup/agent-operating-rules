# Procedure

1. Read the target notes file with `read_file` and record its facts, conditions, and intended meaning.
2. Run `check_file` on the target file before you edit it.
3. Read each reported sentence in context and identify each reported banned word.
4. Replace banned words with plain terms that preserve the meaning. Remove a word only when it adds no meaning.
5. Split long sentences at logical boundaries. Keep descriptions within 25 words and instructions within 20 words.
6. Keep each fact, qualification, relationship, and instruction. Preserve the file's structure where possible.
7. Write the complete revised file with `write_file`.
8. Run `check_file` on the revised file. If it reports banned words or long sentences, repeat steps 3 through 8.
9. Read the revised file and compare it with the original meaning recorded in step 1. Restore any missing meaning and repeat the checks.
10. Finish only when the checks report no banned words or long sentences and the comparison confirms the original meaning.
11. Apply these steps to one file at a time. Finish `notes/a.md`, then `notes/b.md`, then `notes/c.md`.
