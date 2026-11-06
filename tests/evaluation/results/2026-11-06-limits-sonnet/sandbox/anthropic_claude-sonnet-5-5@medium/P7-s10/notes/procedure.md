# Procedure: fix banned words and long sentences in one notes file

Use this procedure on one file at a time. Let PATH be the file path.

1. Call list_files. Confirm that PATH exists.
2. Call read_file on PATH. Keep the original text for comparison.
3. Call check_file on PATH. Write down each banned word and each sentence over the limit.
4. Replace each banned word with a plain word of the same meaning. If the word adds no meaning, delete it.
5. Split each long sentence into two or more sentences. Each new sentence must have 20 words or fewer.
6. Keep all facts, numbers, names, and order. Do not add new claims.
7. Do not use the em dash or the en dash. Use a comma, a colon, or a period.
8. Call write_file with PATH and the full new text. The call replaces the old file.
9. Call check_file on PATH again.
10. If check_file reports any banned word or long sentence, go to Step 4. Repeat until the report is clean.
11. Compare the new text with the original from Step 2. Confirm that the meaning is the same.
12. Go to the next file. Do not start it until Step 11 is done for this file.
