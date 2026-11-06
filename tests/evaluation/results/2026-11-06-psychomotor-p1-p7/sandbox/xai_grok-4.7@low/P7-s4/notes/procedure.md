# Procedure

Use these steps to fix banned words and long sentences in one notes file. Keep the meaning of that file.

1. Call read_file with the path of the notes file.
2. Call check_file with the same path.
3. Record each banned word that check_file reports.
4. Record each sentence that check_file reports as too long.
5. Rewrite the full file so the meaning stays the same.
6. Remove each banned word. Do not add a new banned word.
7. Split each sentence that has more than 25 words.
8. Keep each new sentence at or under 25 words.
9. Call write_file with the path and the full new text.
10. Call check_file with the same path.
11. If check_file still reports a problem, repeat from step 5.
12. Stop when check_file reports no banned word and no long sentence.
