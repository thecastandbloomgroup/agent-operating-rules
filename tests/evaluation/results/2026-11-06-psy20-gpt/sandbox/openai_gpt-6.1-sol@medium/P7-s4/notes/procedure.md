# Procedure

1. Read the target file with `functions.read_file`.
2. Run `functions.check_file` on the target file.
3. Record each banned word and each sentence over 25 words from the report.
4. Replace each banned word with plain text that keeps the original meaning.
5. Split each long sentence into shorter sentences that keep all facts, conditions, and links.
6. Keep instructions at 20 words or fewer, and descriptions at 25 words or fewer.
7. Compare the revised text with the original text before saving.
8. Confirm that the revision keeps names, numbers, dates, duties, limits, and the strength of each claim.
9. Save the full revised file with `functions.write_file`.
10. Run `functions.check_file` on the saved file.
11. If the report lists banned words or long sentences, repeat steps 4 through 10.
12. Read the saved file and compare it with the original text once more.
13. Finish the current file before starting the next file.
