# Procedure

1. Read the target notes file with `functions.read_file`.
2. Run `functions.check_file` on the target file to locate banned words and sentences over 25 words.
3. Read each flagged passage in context before you edit it.
4. Replace banned words with plain, precise words, or remove them when they add no meaning.
5. Preserve facts, conditions, uncertainty, names, numbers, and the strength of each claim.
6. Split long sentences at natural breaks, and keep each sentence at 25 words or fewer.
7. Keep instructions at 20 words or fewer per sentence.
8. Preserve the order of ideas and links between causes, contrasts, and results.
9. Write the full revised file with `functions.write_file`.
10. Run `functions.check_file` again on the revised file.
11. If the check reports any issues, repeat steps 3 through 10 until none remain.
12. Read the revised file and compare it with the original text from step 1.
13. Restore any lost meaning, then repeat the check if you change the file.
14. Finish one target file before you start the next file in the requested order.
