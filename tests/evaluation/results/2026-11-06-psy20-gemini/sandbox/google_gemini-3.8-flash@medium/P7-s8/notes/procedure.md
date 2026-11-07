# Procedure to Fix Style Violations in a Notes File

Follow these steps to fix banned words and long sentences in one notes file:

1. Run `check_file` on the target path to find rule violations.
2. Run `read_file` to inspect the full text of the file.
3. Edit the text to remove banned words and split sentences that exceed 25 words.
4. Run `write_file` with the revised text to save the changes.
5. Run `check_file` on the target path to verify zero failures remain.
