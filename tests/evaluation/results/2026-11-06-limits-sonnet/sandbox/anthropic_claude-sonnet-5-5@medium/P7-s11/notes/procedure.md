# Procedure: fix banned words and long sentences in one notes file

The tools are list_files, read_file, check_file, and write_file.

1. Run list_files. Confirm that the target file exists.
2. Run check_file on the target file. Record each banned word and each sentence over 25 words.
3. Run read_file on the target file. Keep the full text.
4. Rewrite each sentence that the check flagged. Keep the meaning of the sentence.
5. Replace each banned word with a plain word, or delete it. Do not add new facts.
6. Split each long sentence into two or more sentences. Each new sentence has 20 words or fewer.
7. Do not use the em dash or the en dash. Use a comma, a colon, or a period.
8. Run write_file with the full new text. The tool replaces the old content.
9. Run check_file on the same file again.
10. If the check still reports a problem, go to Step 4. Fix only the reported items.
11. Stop when the check reports no banned word and no long sentence.
12. Move to the next file only after Step 11 is true for the current file.
