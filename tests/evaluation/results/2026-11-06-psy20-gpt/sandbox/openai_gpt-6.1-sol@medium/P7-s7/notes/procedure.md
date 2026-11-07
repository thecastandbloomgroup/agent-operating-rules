# Procedure

1. Read the target notes file with `functions.read_file`.
2. Run `functions.check_file` on the target file before any edits.
3. Record each banned word and each sentence above 25 words from the report.
4. Replace banned words with plain terms that preserve the original meaning.
5. Split long sentences at logical boundaries. Keep each sentence at 25 words or fewer.
6. Preserve all facts, conditions, relationships, and instructions. Do not add claims or remove qualifications.
7. Write the revised file with `functions.write_file`.
8. Run `functions.check_file` again on the revised file.
9. If the report finds banned words or long sentences, repeat steps 4 through 8.
10. Read the revised file again. Compare it with the original text from step 1 for meaning.
11. If the meaning changes, revise the text and repeat steps 7 through 10.
12. Finish only when the checker reports no violations and the meaning remains intact.
13. Complete each target before the next. For this task, use `notes/a.md`, then `notes/b.md`, then `notes/c.md`.
