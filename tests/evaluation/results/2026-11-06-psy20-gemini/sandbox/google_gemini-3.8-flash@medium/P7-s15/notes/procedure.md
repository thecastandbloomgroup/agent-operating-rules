# Procedure to Fix Banned Words and Long Sentences

Follow these steps to remediate one notes file:

1. Run `check_file` on the target path to find rule failures.
2. Read the file with `read_file` to inspect the source text.
3. Remove or replace every banned word identified by `check_file`.
4. Split any sentence that exceeds 25 words into shorter sentences.
5. Save the updated text to the target path with `write_file`.
6. Run `check_file` again to verify that all checks pass.
