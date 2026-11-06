# Procedure: fix banned words and long sentences in one notes file

Tools: list_files, read_file, check_file, write_file.

1. Run list_files. Confirm that the target file exists.
2. Run check_file on the target path. Save the list of long sentences and banned words.
3. Run read_file on the target path. Read the full text.
4. Stop if check_file reports no long sentences and no banned words. The file needs no change.
5. Find each long sentence in the text. Split it into sentences of 20 words or fewer. Keep one idea in each sentence.
6. Find each banned word in the text. Replace it with a plain word of the same meaning. If the word adds no meaning, delete it.
7. Replace a hedge with a probability or a confidence level only when the source text gives one. Otherwise state the fact without the hedge.
8. Keep all facts, numbers, names, and headings. Do not add new claims.
9. Do not use the em dash or the en dash. Use a comma, a colon, or a period.
10. Run write_file on the same path with the full new text. The write replaces the old content.
11. Run check_file on the same path again.
12. If check_file still reports a problem, repeat Steps 5 to 11 for that problem only. Stop after three rounds.
13. Run read_file once more. Compare the new text with the old text. Confirm that the meaning is the same.
14. Report the result: the count of fixes, and the final check_file output.
