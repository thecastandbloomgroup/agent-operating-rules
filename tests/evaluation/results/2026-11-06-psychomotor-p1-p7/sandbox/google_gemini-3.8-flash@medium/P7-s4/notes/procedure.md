# Procedure for Fixing Notes

This procedure describes how to fix style violations in notes files.

1. Run `check_file` on the target note file to list violations.
2. Read the file with `read_file` to inspect the text.
3. Remove or replace banned words such as boosters without changing meaning.
4. Split any sentence longer than 25 words into shorter sentences.
5. Save the updated text to the file with `write_file`.
6. Run `check_file` again to verify that all checks pass.
