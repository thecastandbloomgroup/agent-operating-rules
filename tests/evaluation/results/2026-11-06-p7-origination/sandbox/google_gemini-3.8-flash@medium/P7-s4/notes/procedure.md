# Procedure for editing notes

This procedure removes banned words and shortens long sentences in a target note file.

1. Call `read_file` with the target file path to inspect the current text.
2. Call `check_file` with the target file path to list specific failures.
3. Edit the text to remove banned words, split sentences over 25 words, and simplify phrasing.
4. Call `write_file` with the target file path and the revised content.
5. Call `check_file` on the target file path to confirm zero failures.
