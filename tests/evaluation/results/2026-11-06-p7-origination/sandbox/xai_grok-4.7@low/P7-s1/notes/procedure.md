# Procedure: fix banned words and long sentences

Use this procedure on one notes file. The tools are list_files, read_file, write_file, and check_file.

1. Call read_file on the notes file. Keep its heading and its meaning.
2. Call check_file on the same path. Record each banned word and each sentence over 25 words.
3. Rewrite the file in full. Remove each banned word. Split each long sentence so that no sentence has more than 25 words. Do not add new facts.
4. Call write_file with the full new text. This replaces the old file.
5. Call check_file again on the same path.
6. If check_file still reports a banned word or a long sentence, repeat steps 3 to 5. Stop when check_file reports none.
