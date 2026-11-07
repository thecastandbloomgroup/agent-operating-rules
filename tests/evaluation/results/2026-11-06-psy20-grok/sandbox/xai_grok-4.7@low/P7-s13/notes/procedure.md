# Procedure: fix banned words and long sentences

Any agent can follow these steps on one notes file. The tools are list_files, read_file, write_file, and check_file.

1. Call list_files so you know the file is in the sandbox.
2. Call read_file on the target path. Copy the full text.
3. Call check_file on the same path. Record each banned word and each sentence over 25 words.
4. Rewrite only the flagged sentences. Keep the facts, numbers, and names.
5. Replace each banned word with a plain word that keeps the claim. Drop the word when no replacement is needed.
6. Split each sentence over 25 words into two or more sentences. Each new sentence must be 25 words or fewer.
7. Do not add new facts. Do not change the heading.
8. Call write_file with the full new text. This replaces the old file.
9. Call check_file again on the same path.
10. If check_file still reports banned words or long sentences, repeat steps 4 to 9. Stop when check_file reports none.
