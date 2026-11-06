# Procedure: fix banned words and long sentences in one notes file

Use this procedure on one file at a time. Replace PATH with the file path.

1. Call list_files. Confirm that PATH exists.
2. Call read_file on PATH. Keep the original text in your context.
3. Call check_file on PATH. Note each banned word and each sentence over 25 words.
4. Write the new text. Replace each banned word with a plain word or delete it. Keep the facts the same.
5. Split each long sentence into two or more short sentences. Keep each sentence under 20 words. Do not drop any fact.
6. Keep the headings, lists, and order of the original.
7. Call write_file on PATH with the full new text. This replaces the old content.
8. Call check_file on PATH again. If it reports any banned word or long sentence, go to Step 4.
9. Compare the new text with the original from Step 2. Confirm that the meaning is the same.
10. Go to the next file only when Step 8 reports zero problems.
