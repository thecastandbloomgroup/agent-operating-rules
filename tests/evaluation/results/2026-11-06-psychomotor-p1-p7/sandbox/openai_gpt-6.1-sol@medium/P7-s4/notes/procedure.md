# Procedure

1. Read the target notes file with `read_file`. Keep a copy of its text for the meaning check.
2. Run `check_file` on the target file. Record each banned word and each sentence over 25 words.
3. Replace each banned word with a plain term that keeps its meaning. Remove it only if it adds no meaning.
4. Split each long sentence into short sentences. Keep all facts, names, numbers, conditions, and links between ideas.
5. Compare the draft with the original text. Restore any lost meaning without adding banned words or long sentences.
6. Save the full draft to the same path with `write_file`.
7. Run `check_file` on the saved file. If any issue remains, repeat steps 3 through 7.
8. Read the saved file with `read_file`. Compare it with the original text once more for meaning.
9. If the meaning changes, fix the text and repeat steps 6 through 8. Finish only when meaning stays intact and no check issues remain.
10. Complete all steps for one file before you start the next file. Use the order the user gives.
