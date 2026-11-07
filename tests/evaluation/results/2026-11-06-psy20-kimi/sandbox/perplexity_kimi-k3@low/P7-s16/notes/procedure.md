# Procedure: fix banned words and long sentences in one notes file

1. Read the target file with the read_file tool.
2. Run check_file on the file path to get the list of banned words and any sentence over 25 words.
3. For each banned word, remove it or replace it with a fact, such as a number with units. Keep the meaning of the sentence.
4. For each sentence over 25 words, split it at a natural break, for example before a conjunction or at a list boundary. Keep all facts in the same order.
5. Apply steps 3 and 4 to the file with the write_file tool. Replace the full content.
6. Run check_file on the file again. If it still reports a banned word or a long sentence, return to step 3. If it reports none, the file is done.
