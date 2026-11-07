# Procedure

Fix banned words and long sentences in one notes file. Keep the meaning.

Tools: list_files, read_file, write_file, check_file.

Banned words: clearly, obviously, very, extremely, significantly, definitely, undoubtedly, of course, critical, powerful, robust, might, perhaps, somewhat, arguably, it seems, could potentially, may or may not, to some extent, generally speaking.

A long sentence has more than 25 words.

1. Call read_file on the notes file.
2. Rewrite the file in full. Remove each banned word. Split each sentence that has more than 25 words. Keep the meaning.
3. Call write_file with the full new text.
4. Call check_file on the same path.
5. If check_file reports a banned word or a sentence over 25 words, repeat steps 2 to 4. Stop when check_file reports none.
