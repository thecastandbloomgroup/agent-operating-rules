# Procedure: fix banned words and long sentences in one notes file

Use these steps for one file at a time. Replace PATH with the file path.

1. Call read_file on PATH. Save the full text.
2. Call check_file on PATH. Save the list of long sentences and banned words.
3. Stop if the report shows no long sentence and no banned word. The file is done.
4. Write a short list of the facts in the file. Use it in Step 7 to check the meaning.
5. Split each long sentence into two or more sentences. Each new sentence must have 20 words or fewer.
6. Replace each banned word with a plain word of the same meaning. If the word adds no meaning, delete it.
7. Compare the new text with the fact list from Step 4. Add back any fact that you lost.
8. Call write_file on PATH with the full new text. Do not write part of the file.
9. Call check_file on PATH again.
10. If the report still shows a problem, go to Step 5. Repeat until the report is clean.
11. Do not start the next file until the report for this file is clean.

Rules for every step:

- Do not use the em dash or the en dash. Use a comma, a colon, or a period.
- Do not add new facts. Do not remove facts.
- Keep headings, lists, and numbers as they are.
