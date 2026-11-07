# Procedure: edit one notes file

1. Read the target file with `functions.read_file`.
2. Run `functions.check_file` on the target file before any edit.
3. Record the reported banned words and sentences over 25 words.
4. Preserve the file's facts, names, numbers, conditions, and level of certainty.
5. Replace each banned word with plain text that preserves its meaning.
6. Split each reported long sentence into shorter sentences at a natural boundary.
7. Keep each sentence at 20 words or fewer to provide a margin below the checker limit.
8. Compare the draft with the original for lost facts or changed meaning.
9. Write the complete revised file with `functions.write_file`.
10. Run `functions.check_file` on the revised file.
11. If the checker reports any issue, repeat steps 5 through 10 until no issues remain.
12. Read the revised file and compare it with the original once more.
13. Fix any change in meaning, then repeat the check after each edit.
14. Finish this file before you read or edit the next target file.
