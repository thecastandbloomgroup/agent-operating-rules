# Procedure to fix banned words and long sentences

Follow these steps to remediate one notes file:

1. Run `check_file` on the target file path.
2. Read the full content with `read_file`.
3. If `check_file` reports banned words, remove them or replace them with objective terms.
4. If `check_file` reports sentences over 25 words or Flesch-Kincaid failure, split each long sentence into shorter sentences.
5. Preserve the original meaning of the text during rewrites.
6. Write the updated text to the file with `write_file`.
7. Run `check_file` again to verify that all checks pass.
