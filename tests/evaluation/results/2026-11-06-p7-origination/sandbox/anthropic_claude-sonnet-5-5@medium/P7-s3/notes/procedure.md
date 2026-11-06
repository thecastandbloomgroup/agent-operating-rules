# Procedure: fix one notes file

Use this procedure on one file at a time. The tools are list_files, read_file, check_file, and write_file.

1. Call list_files. Confirm that the target file exists.
2. Call read_file on the target. Keep the text as the source of meaning.
3. Call check_file on the target. Record each banned word and each sentence over 25 words.
4. Rewrite each flagged sentence. Keep the facts, the numbers, and the names. Replace each banned word with a plain word, or delete it when it adds no fact.
5. Split each long sentence into two or more short sentences. Keep each sentence under 20 words.
6. Do not add new facts. Do not remove facts. Do not use dashes. Use a comma, colon, or period instead.
7. Call write_file with the full new text. The tool replaces the old content, so include every unchanged line.
8. Call check_file on the target again.
9. If check_file reports any flag, go to Step 4. Stop after three rounds and report what remains.
10. Compare the new text with the source from Step 2. Confirm that the meaning is the same.
11. Move to the next file only after Step 8 reports no flag.
