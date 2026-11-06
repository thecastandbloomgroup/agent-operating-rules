# Procedure: fix banned words and long sentences in one notes file

Use these steps for one file at a time. Replace PATH with the file path.

1. Call list_files. Confirm that PATH exists.
2. Call read_file on PATH. Keep the text as the source of meaning.
3. Call check_file on PATH. Write down each banned word and each long sentence.
4. Rewrite each long sentence as two or more sentences. Keep each new sentence at 20 words or fewer.
5. Replace each banned word with a plain word of the same meaning. If the word adds no meaning, delete it.
6. Replace each em dash and en dash with a comma, a colon, or a period.
7. Check that every fact, number, and name from the source text stays in the new text.
8. Call write_file on PATH with the full new text. The call replaces the old content.
9. Call check_file on PATH again.
10. If the report lists a banned word or a long sentence, go back to Step 4. Stop after three rounds and report what remains.
11. Move to the next file only when the report is clean.
