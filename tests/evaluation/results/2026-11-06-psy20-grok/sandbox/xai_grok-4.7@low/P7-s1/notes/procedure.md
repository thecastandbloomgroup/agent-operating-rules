# Procedure: fix one notes file

Use these steps for one notes file. The tools are read_file, check_file, and write_file.

1. Call read_file with the file path. Keep the meaning of the text.
2. Call check_file with the same path. Note each banned word and each sentence over 25 words.
3. Call write_file with the full new text. Remove each banned word. Split each long sentence. Do not add new claims.
4. Call check_file again on the same path.
5. If check_file still reports a banned word or a long sentence, repeat steps 3 and 4. Stop when the report is clean.
