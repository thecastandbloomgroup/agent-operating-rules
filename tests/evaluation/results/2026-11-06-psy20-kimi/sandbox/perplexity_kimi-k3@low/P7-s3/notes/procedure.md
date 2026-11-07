# Procedure: fix banned words and long sentences in a notes file

1. Run `check_file` on the target file with the tools. Note each banned word and each sentence over 25 words.
2. Read the file with `read_file` to get the full text.
3. For each banned word, remove it or replace it. Keep the meaning of the sentence.
4. For each sentence over 25 words, split it into two or more sentences. Keep the meaning and the order of ideas.
5. Write the fixed text with `write_file`. Replace the whole file.
6. Run `check_file` again. If it still reports problems, repeat steps 3 to 5 until the file is clean.
