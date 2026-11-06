# Procedure: fix banned words and long sentences in one notes file

Use the tools list_files, read_file, check_file, and write_file.

1. Call read_file on the target file. Keep the text as the source of meaning.
2. Call check_file on the target file. Record each banned word and each sentence over 25 words.
3. Edit the text in memory. Replace each banned word with a plain word, or delete it when it adds no meaning.
4. Split each long sentence into two or more sentences. Keep each new sentence under 20 words.
5. Keep all facts, numbers, names, and headings. Do not add new claims.
6. Call write_file with the full new text of the same path.
7. Call check_file on the same path again.
8. If check_file still reports a problem, go to Step 3. Repeat until the report is clean.
9. Start the next file only after Step 7 shows a clean report for the current file.
