# Procedure: fix banned words and long sentences in one notes file

Any agent can follow these steps with these tools: list_files, read_file, check_file, write_file.

1. Run list_files. Write down the full list of file names.
2. Pick the next file from the list, in the order the user gave.
3. Run read_file on that file. Read the full content.
4. Run check_file on that file. Record the two reports:
   - the sentences over 25 words, under "sentences_over_25_words" (zero means pass)
   - the banned words, per category (empty means pass)
5. Fix the long sentences first. Split each sentence that check_file reports.
   Split it at a natural break, such as "and", "so", or a clause edge. Keep every
   fact. Do not merge two sentences into one.
6. Fix the banned words next. For each word in the report:
   - Booster word: delete the word, or restate the claim with its measured fact.
   - Calibrated hedge word: delete it, or state a probability or a likelihood term.
   - Attitude, apology, filler, or self-mention word: delete the clause or rephrase.
7. Run write_file. Store the fixed content at the same path.
8. Run check_file on the same path. Confirm both reports are clean:
   - sentences_over_25_words reports zero
   - every banned word list is empty and the failures list is empty
9. If a report is still not clean, go back to step 5 with the new report.
10. When both reports are clean, move to the next file, starting at step 2.
11. When the list from step 1 has no file left, stop. Do not touch any file again.
