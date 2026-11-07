# Procedure for Cleaning Notes Files

Follow these steps to clean a notes file.

1. Run `check_file` on the target file path to see reported failures.
2. Read the file content with `read_file`.
3. Remove or replace banned words identified by `check_file`.
4. Split any sentence that exceeds the word limit.
5. Save the updated text with `write_file`.
6. Run `check_file` again to confirm zero failures.
