# Procedure

Use these steps to fix one notes file. The tools are read_file, check_file, and write_file.

1. Call read_file with the path of the notes file.
2. Call check_file with the same path.
3. Read the report for banned words and for sentences over 25 words.
4. If the report is clean, stop.
5. If the report lists problems, rewrite the full file.
6. Call write_file with the same path and the full new text.
7. Keep the heading and the meaning of the file.
8. Remove each banned word that the report names.
9. Split each sentence over 25 words into shorter sentences.
10. Call check_file again on the same path.
11. Repeat the rewrite until the report is clean.
