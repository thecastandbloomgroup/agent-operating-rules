# Procedure: fix banned words and long sentences in one notes file

1. Run check_file on the file. Note each banned word and each sentence over 25 words.
2. Read the file to see the full text.
3. Rewrite each flagged sentence:
   a. Remove the banned word, or replace it with a factual term or a number.
   b. Split any sentence over 25 words into two or more sentences under the limit.
4. Keep the meaning of the file. Do not add or remove facts.
5. Write the fixed text to the file with write_file.
6. Run check_file again on the file.
7. Confirm zero banned words and zero sentences over 25 words. If not, go back to Step 3.
