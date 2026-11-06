# Procedure: fix banned words and long sentences in one notes file

Use this procedure on one file at a time. The tools are list_files, read_file, write_file, and check_file.

1. Run check_file on the path. Record the banned words and the sentences over 25 words.
2. Run read_file on the same path. Keep the original text for later comparison.
3. Split each long sentence into sentences of 20 words or fewer. Use one idea per sentence.
4. Replace each banned word with a plain word that has the same meaning. If the word adds no meaning, delete it.
5. Do not use the em dash or the en dash. Use a comma, a colon, or a period.
6. Keep every fact, number, name, and heading. Do not add new claims.
7. Run write_file with the full new text. The tool replaces the old file.
8. Run check_file on the path again.
9. If the report still lists an item, go to Step 2 and repeat. Stop when the report lists none.
10. Compare the final text with the original. Confirm that the meaning is the same.
11. Go to the next file only after Step 10 is done.
