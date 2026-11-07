# Procedure for Note Remediation

Follow these numbered steps to fix banned words and long sentences in a target note file:

1. Read the target file with `read_file`.
2. Inspect the file with `check_file` to list rule violations.
3. Remove or replace banned words identified by `check_file` while preserving technical meaning.
4. Split any sentence that exceeds 25 words into two or more short sentences.
5. Save the updated text to the file with `write_file`.
6. Run `check_file` on the target file to verify that zero failures remain.
