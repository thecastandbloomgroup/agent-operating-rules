# Procedure: fix banned words and long sentences in a notes file

1. Run both read_file and check_file on the target file in parallel, for example read_file("notes/a.md") and check_file("notes/a.md").
2. From the check_file report, list the banned words and the sentences over 25 words.
3. Rewrite each banned word with a neutral term, or remove it when the sentence has a concrete measure.
4. Split each sentence over 25 words into two or more sentences of at most 25 words, keeping the original meaning and order.
5. Write the revised text with write_file, replacing the file in full.
6. Run check_file again. If it still reports problems, repeat steps 3 to 6 until the report is clean.
7. Confirm the meaning matches the original before moving to the next file.
