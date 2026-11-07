# Procedure to Fix Notes Files

Follow these steps to fix banned words and long sentences in a notes file.

1. Call `read_file` on the target file to read its text.
2. Call `check_file` on the target file to list rule violations.
3. Remove or replace all banned words reported by `check_file`.
4. Split any sentence longer than 25 words into shorter sentences.
5. Keep the original meaning and facts of the note intact.
6. Call `write_file` to save the revised text to the target file.
7. Call `check_file` on the target file to verify zero failures remain.
8. If failures remain, repeat step 3 through step 7 until `check_file` passes.
