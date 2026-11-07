# Procedure

Use these steps to fix banned words and long sentences in one notes file. Follow them in order. Use only the listed tools.

1. Call read_file with the path of the notes file.
2. Call check_file with that same path.
3. Record each banned word from the report.
4. Record each sentence that the report marks as over 25 words.
5. Rewrite the full text. Remove each banned word. Split each long sentence into sentences of 25 words or fewer.
6. Keep the original meaning. Do not add facts that the file does not state.
7. Call write_file with the same path and the full rewritten text.
8. Call check_file with that path again.
9. If the report still lists a banned word or a long sentence, repeat steps 5 to 8.
10. Stop when the report lists no banned words and no sentences over 25 words.
