# Procedure: fix banned words and long sentences in a notes file

1. Read the notes file with read_file.
2. Run check_file on the file. Note each banned word and each sentence over 25 words.
3. For each banned word, replace it with a neutral word or delete it. Keep the meaning.
4. For each sentence over 25 words, split it into two or more shorter sentences. Keep the meaning.
5. Write the fixed file with write_file.
6. Run check_file again. If it reports issues, repeat steps 3 to 5.
7. Stop when check_file reports no banned words and no long sentences.
