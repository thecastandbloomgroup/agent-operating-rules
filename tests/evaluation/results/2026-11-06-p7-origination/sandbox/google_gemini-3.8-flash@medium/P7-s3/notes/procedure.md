# Procedure for fixing style violations

This procedure describes how to fix long sentences and banned words in a notes file.

1. Call `check_file` with the path of the target file to list any violations.
2. Read the contents of the file with `read_file`.
3. If `check_file` reports banned words, remove or replace each banned word while keeping the original meaning.
4. If `check_file` reports sentences over the limit, split each long sentence into shorter sentences.
5. Write the updated text back to the file with `write_file`.
6. Call `check_file` on the file again to verify that zero failures remain.
