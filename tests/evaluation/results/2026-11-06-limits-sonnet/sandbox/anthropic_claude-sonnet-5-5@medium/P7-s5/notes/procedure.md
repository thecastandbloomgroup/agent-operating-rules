# Procedure: fix banned words and long sentences in one notes file

Use these steps for one file. Repeat them for each file, in the order given.

1. Read the file with read_file. Save the full text.
2. Run check_file on the file. Record the banned words and the long sentences.
3. Stop if the report shows no banned words and no long sentences. The file is done.
4. Edit the text in memory. Replace each banned word with a plain word, or delete it. Keep the meaning.
5. Split each sentence over the limit into two or more short sentences. Keep one idea in each sentence.
6. Do not add new facts. Do not remove facts. Do not use dashes. Use a comma, colon, or period instead.
7. Write the full new text with write_file to the same path. The write replaces the old content.
8. Run check_file again on the same path.
9. If the report still lists a problem, go to Step 4. Repeat until the report is clean.
10. Go to the next file. Start at Step 1.
