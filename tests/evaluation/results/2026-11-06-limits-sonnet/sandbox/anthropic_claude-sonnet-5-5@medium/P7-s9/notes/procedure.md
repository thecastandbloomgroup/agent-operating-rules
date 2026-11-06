# Procedure: fix banned words and long sentences in one notes file

1. Call list_files. Confirm that the target file exists.
2. Call read_file on the target file. Keep the text as the source of meaning.
3. Call check_file on the target file. Record each banned word and each long sentence.
4. Rewrite each long sentence as two or more sentences. Each new sentence has 20 words or fewer.
5. Replace each banned word with a plain word or a number. If the word only adds emphasis, delete it.
6. Keep every fact, name, number, and date. Do not add new claims.
7. Call write_file with the full new text. The new text replaces the old file.
8. Call check_file on the target file again.
9. If check_file still reports a problem, go to Step 4. Repeat until the report is empty.
10. Move to the next file only after Step 9 ends with an empty report.
