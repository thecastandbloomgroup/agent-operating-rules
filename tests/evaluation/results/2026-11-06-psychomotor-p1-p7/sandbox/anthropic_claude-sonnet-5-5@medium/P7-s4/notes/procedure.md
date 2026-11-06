# Procedure: fix one notes file

1. Run check_file on the path. Save the list of long sentences and banned words.
2. Run read_file on the path. Keep the full text.
3. Find each banned word in the text. Find each sentence over 25 words.
4. Rewrite each banned word. Replace it with a plain word, or delete it if the sentence keeps its meaning.
5. Split each long sentence into two or more short sentences. Keep each fact. Add no new fact.
6. Do not use the em dash or the en dash. Use a comma, a colon, or a period.
7. Run write_file on the same path. Send the full new text.
8. Run check_file on the path again.
9. If the check still reports a problem, go to Step 3. Repeat until the report is empty.
10. Run read_file once more. Confirm that the meaning is the same as the original.
11. Start the next file only after Step 10 is done.
