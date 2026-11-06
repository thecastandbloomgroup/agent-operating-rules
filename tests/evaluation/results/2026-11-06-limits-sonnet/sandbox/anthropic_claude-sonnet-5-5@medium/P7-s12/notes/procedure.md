# Procedure: fix banned words and long sentences in one notes file

1. Call list_files. Confirm that the target file exists.
2. Call read_file on the target file. Keep the text as the source of meaning.
3. Call check_file on the target file. Write down each long sentence and each banned word.
4. Edit the text in your head. Split each long sentence into two or more short sentences.
5. Replace each banned word with a plain word, or delete it. Keep the facts the same.
6. Do not add new facts. Do not remove facts. Do not use the em dash or the en dash.
7. Call write_file with the full new text. The new text replaces the old file.
8. Call check_file on the target file again.
9. If check_file reports any problem, go to Step 4. Repeat until the report is clean.
10. Call read_file once more. Confirm that the meaning matches the source from Step 2.
