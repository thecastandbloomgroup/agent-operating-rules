# Procedure

1. Read the target notes file with `read_file`.
2. Run `check_file` on that file to find banned words and sentences over 25 words.
3. Read each flagged passage in context. Identify the facts, conditions, and links that must stay.
4. Replace banned words with plain terms, or remove them when they add no meaning.
5. Split long sentences at clause boundaries. Keep each sentence at 25 words or fewer.
6. Keep instructions at 20 words or fewer. Preserve facts, names, numbers, dates, conditions, and the strength of each claim.
7. Write the full revised file with `write_file`. Keep its headings and order unless a change helps preserve meaning.
8. Run `check_file` again. If it reports a fault, repeat Steps 3 through 8 until no faults remain.
9. Read the revised file. Compare it with the original text from Step 1 to check that the meaning stays the same.
10. If the comparison finds a change in meaning, fix it and repeat Steps 8 and 9.
11. Finish the current file before you start the next file. Report the final check results.
