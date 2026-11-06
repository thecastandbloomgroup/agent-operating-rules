# Procedure: fix banned words and long sentences in one notes file

Use these steps on one file at a time. The tools are list_files, read_file, check_file, and write_file.

1. Call list_files. Confirm that the target file exists.
2. Call check_file on the target. Save the list of long sentences and banned words.
3. Call read_file on the target. Read the full text.
4. Write a new text. Split each sentence over 25 words into shorter sentences.
5. Replace each banned word with a plain word. If the word adds no meaning, delete it.
6. Keep every fact, number, name, and list item from the original text.
7. Do not add dashes. Use a comma, a colon, or a period instead.
8. Call write_file with the full new text. The tool replaces the old file.
9. Call check_file on the target again.
10. If check_file reports any problem, go to Step 4 and fix it. Repeat until the report is clean.
11. Compare the new text with the original. Confirm that the meaning is the same.
12. Move to the next file only after Step 11 passes.
