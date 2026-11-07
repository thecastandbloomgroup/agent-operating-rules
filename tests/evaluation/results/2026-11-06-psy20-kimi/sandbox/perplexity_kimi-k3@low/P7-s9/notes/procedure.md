# Procedure: fix banned words and long sentences in one notes file

1. Read the file with read_file.
2. Run check_file on the file to get the list of banned words and sentences over 25 words.
3. For each banned word, do one of these steps:
   a. Delete the word when the sentence keeps its meaning without it.
   b. Replace the word with a plain synonym when deleting it changes the meaning.
   c. Replace a claim that amplifies without evidence with a measured statement when the file contains the measure.
4. For each sentence over 25 words, split it into two or more sentences at clause boundaries. Keep each part under the word limit.
5. Keep the file structure the same: title, paragraph order, and facts stay as they were.
6. Write the fixed file with write_file, replacing the whole content.
7. Run check_file again on the file.
8. If check_file still reports issues, repeat steps 3 to 7 until it reports none.
9. Go to the next file and repeat steps 1 to 8.
