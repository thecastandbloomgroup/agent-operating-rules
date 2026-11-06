# Procedure

Use these steps to fix banned words and long sentences in one notes file. Keep the meaning of the file.

1. Read the target file with read_file. Pass the path of that notes file.
2. Split the text into sentences. Count the words in each sentence.
3. Mark each sentence that has more than 25 words.
4. Run check_file on the same path. Record each banned word and each long sentence that it reports.
5. Rewrite the full file. Split each long sentence into two or more sentences. Remove each banned word, or replace it with a plain word that keeps the meaning.
6. Write the full new text with write_file. Use the same path.
7. Run check_file on that path again.
8. If the check still reports a banned word or a long sentence, repeat from step 5. Stop when the check reports no hits.
