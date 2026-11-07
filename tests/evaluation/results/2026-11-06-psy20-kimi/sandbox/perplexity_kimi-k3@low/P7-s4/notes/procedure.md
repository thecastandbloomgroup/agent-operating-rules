# How to fix one notes file

Tools: read_file, write_file, check_file.

1. Call read_file on the notes file to get its current content.
2. Call check_file on the notes file to list the banned words and the sentences over the word limit.
3. Rewrite the content: remove each banned word or replace it with a number or measure, and split each long sentence into two or more short sentences.
4. Keep the meaning of the file the same.
5. Call write_file with the new content in full.
6. Call check_file again to confirm that no banned words or long sentences remain.
7. If check_file still reports a problem, go to step 3.
