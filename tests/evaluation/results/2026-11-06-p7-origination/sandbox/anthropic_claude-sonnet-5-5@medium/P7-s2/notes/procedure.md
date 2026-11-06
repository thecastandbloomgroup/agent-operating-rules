# Procedure: fix banned words and long sentences in one notes file

Use these steps for one file at a time. Repeat them for each file.

1. Call read_file on the file. Keep the original text in your context.
2. Call check_file on the same path. Write down each banned word and each long sentence it reports.
3. Rewrite the file. Replace each banned word with a plain word or delete it. Keep the meaning.
4. Split each long sentence into two or more short sentences. Keep each one under 20 words. Keep the facts and the order.
5. Do not add new facts. Do not remove facts. Do not use the em dash or the en dash.
6. Call write_file with the full new text. The call replaces the old file.
7. Call check_file on the same path again.
8. If check_file still reports a problem, go to Step 3. Fix only the reported items.
9. Stop when check_file reports no banned words and no long sentences.
10. Go to the next file. Do not start it until Step 9 is true for the current file.
