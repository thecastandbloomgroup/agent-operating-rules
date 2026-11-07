# Procedure

Use these steps to fix banned words and long sentences in one notes file. Keep the meaning of the file.

1. Call read_file with the path of the notes file.
2. Call check_file with the same path.
3. Record each banned word that the check reports.
4. Record each sentence that the check reports as longer than 25 words.
5. Call write_file with the same path and the full new text.
6. Remove each banned word. Do not add a new booster or hedge.
7. Split each long sentence into sentences of 25 words or fewer.
8. Keep the same facts, numbers, names, and order of events.
9. Call check_file again with the same path.
10. If the check still reports a banned word or a long sentence, repeat from step 5.
11. Stop when the check reports no banned words and no long sentences.
