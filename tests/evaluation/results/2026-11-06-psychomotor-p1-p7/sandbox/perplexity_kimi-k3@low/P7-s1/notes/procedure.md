# Procedure: fix banned words and long sentences in one notes file

1. Read the target file with the read_file tool.
2. Run check_file on the file path. Record the banned words and the sentences over 25 words.
3. For each banned word, replace it with a neutral word that keeps the sentence meaning.
4. For each sentence over 25 words, split it into two or more sentences. Keep every fact from the original sentence.
5. Write the corrected text to the file with the write_file tool.
6. Run check_file again on the file. If it still reports issues, return to step 3.
7. When check_file reports no remaining issues, stop. The file is done.
