# Procedure: fix banned words and long sentences in one notes file

Tools: list_files, read_file, check_file, write_file.

1. Call list_files. Confirm that the target file exists.
2. Call check_file on the target. Record each long sentence and each banned word.
3. Call read_file on the target. Keep the full text.
4. Split each sentence over 25 words into shorter sentences. Keep one idea in each sentence.
5. Replace each banned word with a plain word or a number. If the word only adds force, delete it.
6. Keep facts, numbers, names, and order. Do not add new claims.
7. Remove the em dash and the en dash. Use a comma, colon, period, or parentheses.
8. Call write_file with the full new text. The call replaces the old file.
9. Call check_file on the target again.
10. If the report shows any long sentence or banned word, go to Step 4. Repeat until the report is clean.
11. Compare the new text with the old text. Confirm that the meaning is the same.
12. Move to the next file only after Step 9 reports no issue.
