# Procedure: fix one notes file

1. Run check_file on the path. Record each banned word and each long sentence.
2. Run read_file on the same path. Keep the original text in view.
3. Replace each banned word with a plain word, or delete it when it adds no fact.
4. Split each sentence over 20 words into shorter sentences. Keep one idea in each sentence.
5. Keep all facts, numbers, names, and headings. Do not add new claims.
6. Run write_file with the full new text. This replaces the old file.
7. Run check_file again on the path.
8. If the report shows any banned word or long sentence, go back to Step 3. Stop after three rounds.
9. Compare the new text with the original from Step 2. Confirm that the meaning is the same.
10. Move to the next file only when Step 7 reports no problem.
