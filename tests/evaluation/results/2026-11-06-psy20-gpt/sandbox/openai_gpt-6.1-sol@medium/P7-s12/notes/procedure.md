# Procedure: fix banned words and long sentences

1. Read the target notes file with `functions.read_file` before you edit it.
2. Run `functions.check_file` on the target path to find banned words and sentences over 25 words.
3. Record the facts, claims, conditions, numbers, names, and links that the edit must preserve.
4. Replace each banned word with a neutral phrase that preserves the claim and its level of certainty.
5. Split long sentences at natural breaks, and keep each description within 25 words.
6. Keep instructions within 20 words, and give each instruction its own sentence.
7. Preserve cause, contrast, scope, conditions, and sequence when you split sentences.
8. Remove empty emphasis without removing facts, warnings, or limits.
9. Write the complete revised file to its original path with `functions.write_file`.
10. Run `functions.check_file` on the revised file.
11. Compare the revised file with the original text from step 1 to check that it retains the meaning.
12. If the check reports a problem, revise the text and repeat steps 9 through 11.
13. Finish only when the check reports no banned words or long sentences and the meaning remains intact.
14. Repeat this procedure for each requested file, in the requested order.
