# Procedure: Fix Banned Words and Long Sentences

Follow these steps to remediate style issues in a markdown file.

1. Call `check_file` with the path of the target file.
2. Read the tool report to identify banned words and long sentences.
3. Call `read_file` to inspect the full text of the file.
4. Remove or replace banned words without altering the underlying meaning.
5. Split any sentence that exceeds twenty-five words into shorter sentences.
6. Check that every sentence stays below the Flesch-Kincaid grade threshold of ten.
7. Call `write_file` with the updated content.
8. Call `check_file` on the target file again.
9. Verify that `check_file` returns zero failures.
