# Procedure: fix banned words and long sentences in one notes file

1. Call read_file on the target file. Keep the text as the source of meaning.
2. Call check_file on the target file. Record each banned word and each long sentence that the tool reports.
3. Stop if the report is empty. The file needs no change.
4. Rewrite each long sentence as two or more short sentences. Keep each sentence under 20 words.
5. Replace each banned word with a plain word of the same meaning. If the word adds no meaning, delete it.
6. Do not add facts. Do not remove facts. Do not use the em dash or the en dash.
7. Call write_file with the full new text. The call replaces the old content.
8. Call check_file on the target file again.
9. If the report still lists a problem, go to Step 4. Repeat until the report is empty.
10. Read the new text once. Confirm that it keeps the meaning of the old text.
