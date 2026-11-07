# Procedure for fixing notes

Follow these steps to fix long sentences and banned words in a notes file.

1. Call `check_file` on the target path to find rule violations.
2. Call `read_file` to inspect the content of the target file.
3. Remove or replace all banned booster words and hedges.
4. Split every sentence that contains more than 25 words into shorter sentences.
5. Call `write_file` to save the updated text.
6. Call `check_file` again to verify that zero failures remain.
