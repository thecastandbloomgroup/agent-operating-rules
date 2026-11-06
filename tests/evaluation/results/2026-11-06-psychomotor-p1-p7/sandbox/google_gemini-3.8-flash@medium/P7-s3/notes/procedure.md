# Procedure for Cleaning Notes Files

Follow these steps to clean banned words and long sentences from a notes file.

1. Call `read_file` with the target file path.
2. Call `check_file` with the target file path to see the reported issues.
3. Identify banned words from the check output.
4. Remove or replace each banned word without changing the meaning.
5. Identify sentences that exceed the word limit from the check output.
6. Split each long sentence into two or more short sentences.
7. Verify that every instruction sentence has at most 20 words.
8. Verify that every descriptive sentence has at most 25 words.
9. Verify that the Flesch-Kincaid grade stays at or below 10.
10. Call `write_file` to save the updated text to the target file path.
11. Call `check_file` again on the target file path.
12. Repeat the editing process if any failure remains.
