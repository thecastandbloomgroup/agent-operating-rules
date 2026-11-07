# Procedure: fix banned words and long sentences

Any agent can follow these steps for one notes file. The tools are `list_files`, `read_file`, `check_file`, and `write_file`.

1. Call `list_files` and confirm the target path exists in the sandbox.
2. Call `read_file` on that path and keep the full text.
3. Call `check_file` on that path and record each banned word and each sentence over 25 words.
4. Rewrite the file in full. Keep the meaning. Replace each banned word with a plain word that does not boost, hedge, or praise. Split each sentence over 25 words so every sentence has 25 words or fewer. Use active voice. Keep one topic per paragraph.
5. Call `write_file` with the full new text. This replaces the old content.
6. Call `check_file` again. If it still reports a banned word or a sentence over 25 words, repeat steps 4 to 6. Stop when `check_file` reports none.
7. Call `read_file` and compare the new text with the old text. Confirm the facts and the request stay the same.

Do these steps for one file before you start the next file.
