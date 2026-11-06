# Procedure: fix banned words and long sentences in one notes file

1. Call read_file on the file. Save the full text.
2. Call check_file on the same path. Record each banned word and each long sentence.
3. Stop if the report shows no banned words and no long sentences.
4. Rewrite each banned word. Use a plain word, or delete the word if the sentence keeps its meaning.
5. Split each long sentence into shorter sentences. Keep each sentence at 20 words or fewer.
6. Check that the new text keeps every fact, number, name, and instruction of the old text.
7. Call write_file with the full new text. The call replaces the old file.
8. Call check_file again on the same path.
9. If the report still shows a problem, go back to Step 4. Repeat until the report is clean.
10. Call read_file once more. Confirm that the meaning is the same.
