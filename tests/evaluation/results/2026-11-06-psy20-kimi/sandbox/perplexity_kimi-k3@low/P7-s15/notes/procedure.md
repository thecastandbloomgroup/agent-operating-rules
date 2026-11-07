# Procedure: clean one notes file

1. Read the file with read_file.
2. Run check_file on the file to list banned words and sentences over 25 words.
3. Rewrite each banned word: delete it or replace it with a plain synonym. Keep the meaning.
4. Split each sentence over 25 words into two or more short sentences. Keep the meaning.
5. Write the new text with write_file.
6. Run check_file again on the file.
7. If the check still lists problems, repeat steps 3 to 6 until the check is clean.
