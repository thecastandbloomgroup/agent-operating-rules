# Procedure: fix one notes file

Use this procedure for one file at a time. Replace PATH with the file path.

1. Run check_file on PATH. Save the list of banned words and long sentences.
2. Run read_file on PATH. Keep the full text in view.
3. Find each banned word in the text. Replace it with a plain word, or delete it.
4. Delete a banned word that adds no fact. Do not add a new fact.
5. Find each sentence that the check reports. Split it into two or more short sentences.
6. Keep each new sentence under 20 words. Use one idea in each sentence.
7. Keep the meaning, the numbers, the names, and the order of the facts.
8. Do not use the em dash or the en dash. Use a comma, a colon, or a period.
9. Run write_file on PATH with the full new text. The tool replaces the old content.
10. Run check_file on PATH again. Compare the result with the list from Step 1.
11. If the check still reports a problem, go to Step 3. Repeat until the report is clean.
12. Run read_file on PATH one last time. Confirm that the meaning is the same.
13. Do not start the next file until Step 12 is done for this file.
