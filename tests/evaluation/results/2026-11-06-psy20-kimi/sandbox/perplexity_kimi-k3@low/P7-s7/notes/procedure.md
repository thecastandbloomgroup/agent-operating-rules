# Procedure: fix banned words and long sentences in one notes file

1. Read the file with read_file.
2. Run check_file on the file path to get the list of sentences over 25 words and the banned words.
3. For each banned word, remove it or replace it with a neutral word. Keep the original meaning. If the word makes a claim, replace it with the measured fact or drop the claim.
4. For each sentence over 25 words, split it into two or more sentences. Keep each part under 25 words.
5. Write the new text back with write_file. Keep the heading and the meaning of the file.
6. Run check_file again on the path. Confirm zero banned words and zero sentences over 25 words.
7. If check_file still reports issues, repeat steps 3 to 6 until the file passes.
