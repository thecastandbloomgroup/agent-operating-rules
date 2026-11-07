# Procedure for Editing Notes

Follow these steps to fix banned words and long sentences in a note file:

1. Run `check_file` on the target note file to list violations.
2. Read the file with `read_file` to review context.
3. Remove or replace every booster, uncalibrated hedge, and banned phrase.
4. Split any sentence that exceeds 25 words into shorter sentences.
5. Save the updated text to the file with `write_file`.
6. Run `check_file` on the file again to confirm that zero violations remain.
