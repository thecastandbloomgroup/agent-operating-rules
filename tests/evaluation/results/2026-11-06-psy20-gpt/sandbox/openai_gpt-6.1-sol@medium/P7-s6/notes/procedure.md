# Procedure

1. Read the target notes file with `functions.read_file`.
2. Run `functions.check_file` on the target file.
3. Review every reported banned word and sentence over 25 words.
4. Replace banned words with plain terms that preserve the original meaning.
5. Split long sentences into shorter sentences, each with no more than 25 words.
6. Preserve facts, names, numbers, conditions, and the links between ideas.
7. Write the full revised file with `functions.write_file`.
8. Run `functions.check_file` on the revised file.
9. If the check reports any issue, repeat steps 3 through 8.
10. Read the revised file and compare it with the original text from step 1.
11. Restore any lost meaning, then repeat the check until it reports no issues.
12. Finish the current file before you start the next file in the requested order.
