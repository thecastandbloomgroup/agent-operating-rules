# Procedure: Fix Banned Words and Long Sentences

Follow these numbered steps to fix one notes file:

1. Run the check tool on the target file path with `check_file`.
2. Read the full content of the target file with `read_file`.
3. Inspect the check report for banned words, long sentences, and readability failures.
4. Remove banned booster words, hedges, and prohibited phrases while preserving the core meaning.
5. Split any sentence that contains more than 25 words into two or more shorter sentences.
6. Write the updated text to the target file path with `write_file`.
7. Run `check_file` on the target file again to verify that zero failures remain.
