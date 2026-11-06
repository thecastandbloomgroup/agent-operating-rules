# Procedure: fix banned words and long sentences in one notes file

1. Read the file with the read_file tool. Note its full text.
2. Run the check_file tool on the file. Record each banned word and each sentence over 25 words.
3. For each banned word, replace it:
   - Remove the word if it only adds intensity (for example "very", "clearly").
   - Or replace it with a measured fact if the file contains one (for example a time or a count).
4. For each sentence over 25 words, split it into two or more sentences. Keep the original order of ideas. Keep the meaning.
5. Check punctuation. Replace any em dash or en dash with a comma, colon, or period.
6. Write the new text with the write_file tool. Write the file in full.
7. Run the check_file tool on the file again.
8. If the check still reports a problem, repeat from step 3.
9. Stop when the check reports no banned words and no long sentences.
