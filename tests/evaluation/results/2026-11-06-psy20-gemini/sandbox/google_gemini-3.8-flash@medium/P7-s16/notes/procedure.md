# Procedure for Fixing Notes Files

1. Run `check_file` on the target note path to find banned words and long sentences.
2. Run `read_file` to read the complete text of the note.
3. Edit the text to remove banned words and split sentences over 25 words into shorter sentences.
4. Keep the original factual meaning of the file without adding claims.
5. Run `write_file` with the revised text to overwrite the target file.
6. Run `check_file` on the target path to verify zero failures remain.
