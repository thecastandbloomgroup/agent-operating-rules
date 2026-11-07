# Procedure: clean one notes file

1. Read the file.
2. Run check_file on the file.
3. Read the reported list of banned words and the reported long sentences.
4. For each reported banned word, delete it or replace it with a measured fact. Keep the meaning.
5. For each sentence over 25 words, split it into shorter sentences of at most 25 words. Keep the meaning and the order of ideas.
6. Write the corrected file in full.
7. Run check_file on the file again.
8. Repeat steps 4 to 7 until check_file reports no failures.
