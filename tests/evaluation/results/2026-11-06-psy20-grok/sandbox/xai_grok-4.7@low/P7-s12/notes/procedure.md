# Procedure

Fix banned words and long sentences in one notes file. Keep the meaning.

Tools: list_files, read_file, write_file, check_file.

Banned words: clearly, obviously, very, extremely, significantly, definitely, undoubtedly, of course, critical, powerful, robust.

A long sentence has more than 25 words.

## Steps

1. Call list_files and confirm the target notes file is present.
2. Call read_file on that file and copy the full text.
3. Remove each banned word. Keep the same claim. Do not add a new intensifier.
4. Split each sentence over 25 words into two or more sentences. Keep the same facts, order, and actors.
5. Call write_file with the full revised text. This replaces the old file.
6. Call check_file on that path.
7. If check_file still reports a banned word or a sentence over 25 words, repeat steps 3 to 6 once. Stop after that repeat even if a report remains.
8. Do not edit any other file in this pass.
