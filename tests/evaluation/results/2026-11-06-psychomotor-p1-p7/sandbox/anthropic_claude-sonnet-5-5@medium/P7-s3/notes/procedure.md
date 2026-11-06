# Procedure: fix banned words and long sentences in one notes file

Use these steps for one file. Repeat them for each file, in the order given.

1. Read the file with read_file. Keep the full text in view.
2. Run check_file on the same path. Write down each long sentence and each banned word that the tool reports.
3. Rewrite each long sentence as two or more short sentences. Keep each sentence under 20 words.
4. Replace each banned word with a plain word of the same meaning. If the word adds no meaning, delete it.
5. Keep every fact, number, name, and list item. Do not add new facts.
6. Write the full new text with write_file to the same path. The tool replaces the old content.
7. Run check_file on the path again.
8. If the tool still reports a problem, go to Step 3. Stop when the report is empty.
9. Do not start the next file until the check of the current file is clean.
