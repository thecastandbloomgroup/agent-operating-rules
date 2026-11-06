# Procedure: Fix Banned Words and Long Sentences

Follow these steps to clean a file with the sandbox tools.

1. Call `read_file` on the target path to inspect the current text.
2. Call `check_file` on the target path to list long sentences and banned words.
3. Identify every banned word that `check_file` reports.
4. Remove each booster, or replace it with a neutral factual statement.
5. Identify every sentence with more than 20 words in instructions or 25 words in descriptions.
6. Split each long sentence into two or more short sentences.
7. Use the active voice and simple connectives such as "then" or "because".
8. Preserve the original meaning and numbers of the text.
9. Call `write_file` to save the revised text to the target path.
10. Call `check_file` again to verify that zero failures remain.
11. If failures remain, repeat step 4 through step 10 until the file passes.
