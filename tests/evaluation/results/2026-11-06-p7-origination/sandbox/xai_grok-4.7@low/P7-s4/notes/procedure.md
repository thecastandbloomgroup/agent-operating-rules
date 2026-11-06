# Procedure: fix banned words and long sentences

Use this procedure on one notes file. The tools are list_files, read_file, write_file, and check_file.

1. Call list_files. Confirm the target path is present.
2. Call read_file on the target path. Copy the meaning of each sentence before you edit.
3. Call check_file on the target path. Record each banned word and each sentence over 25 words.
4. Rewrite the file. Remove each banned word. Split each long sentence. Keep the same facts.
5. Call write_file with the full new text. Do not append.
6. Call check_file again. If it still reports a banned word or a long sentence, repeat steps 4 to 6.
7. Stop when check_file reports no banned words and no sentences over 25 words.
