# Procedure for fixing notes files

1. Run `check_file` on the target note path to identify violations.
2. Read the file with `read_file` to review the full text.
3. Remove or replace banned words such as boosters without changing the factual meaning.
4. Split any sentence that contains more than 25 words into two or more short sentences.
5. Save the updated text to the file with `write_file`.
6. Run `check_file` again to verify that all checks pass.
