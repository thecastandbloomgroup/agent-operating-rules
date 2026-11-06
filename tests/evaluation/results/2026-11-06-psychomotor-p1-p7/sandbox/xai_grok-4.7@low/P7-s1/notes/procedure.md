# Procedure: fix one notes file

Use these steps on one notes file. Use the tools named below. Keep the meaning of the file.

1. Call read_file with the path of the notes file.
2. Call check_file with the same path.
3. Read the report. Note each banned word. Note each sentence over 25 words.
4. If the report lists no banned words and no long sentences, stop.
5. Rewrite the full text. Keep the meaning of each sentence.
6. Replace each banned word with a plain word, or delete it when it adds no fact.
7. Split each sentence over 25 words into two or more sentences.
8. Do not add new claims. Do not drop facts from the original text.
9. Call write_file with the same path and the full new text.
10. Call check_file again on the same path.
11. If the report still lists banned words or long sentences, return to step 5.
12. Stop when check_file reports no banned words and no sentences over 25 words.
