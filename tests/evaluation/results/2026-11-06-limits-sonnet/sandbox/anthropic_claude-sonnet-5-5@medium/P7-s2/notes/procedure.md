# Procedure: fix one notes file

Use this procedure for one file at a time. Replace PATH with the file path.

1. Call read_file with PATH. Keep the full text.
2. Call check_file with PATH. Write down each long sentence and each banned word.
3. Split each sentence over 20 words into two or more short sentences. Keep one idea in each sentence.
4. Replace each banned word with a plain word. If the word adds no fact, delete it.
5. Keep the meaning. Do not add facts. Do not remove facts. Keep numbers, names, and dates.
6. Do not use the em dash or the en dash. Use a comma, a colon, or a period.
7. Call write_file with PATH and the full new text. The call replaces the old text.
8. Call check_file with PATH again.
9. If the report shows a long sentence or a banned word, go to Step 3.
10. Start the next file only when the report shows no long sentence and no banned word.
