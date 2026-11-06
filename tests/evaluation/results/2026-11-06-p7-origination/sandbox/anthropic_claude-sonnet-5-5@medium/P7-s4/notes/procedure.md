# Procedure: fix banned words and long sentences in one notes file

Use this procedure on one file at a time. The tools are list_files, read_file, check_file, and write_file.

1. Call read_file on the target file. Keep the original text in view.
2. Call check_file on the same path. Record each banned word and each long sentence.
3. Rewrite each flagged sentence. Replace each banned word with a plain word, or delete it if it adds no fact.
4. Split each sentence over 20 words into shorter sentences. Keep one idea in each sentence.
5. Keep the meaning. Keep all names, numbers, dates, and headings the same. Do not add new facts.
6. Call write_file with the full new text. The call replaces the old file.
7. Call check_file again on the same path.
8. If the report still lists a banned word or a long sentence, go to Step 3. Stop after three passes.
9. Read the file once more. Confirm that the facts match the original text.
10. Move to the next file only when the report is clean.
