# Procedure for Editing Notes Files

Follow these steps to remove banned words and shorten long sentences in any target file.

1. Inspect the target file with `check_file`.
2. Inspect the current text of the file with `read_file`.
3. Remove every booster, uncalibrated hedge, and forbidden marker.
4. Split every sentence that contains more than 25 words into shorter sentences.
5. Keep the original meaning and technical facts of the source text.
6. Save the revised text to the target file with `write_file`.
7. Run `check_file` on the target file to verify zero failures remain.
8. If any failure remains, repeat steps 2 to 7.
