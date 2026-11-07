# Procedure: Fix banned words and long sentences

1. Read the target notes file with `read_file`. Record its facts, numbers, names, conditions, and degree of certainty.
2. Run `check_file` on the target file. Use its report to locate banned words and sentences over 25 words.
3. Replace each banned word with a permitted phrase that keeps the claim. Remove a word only when it adds no meaning.
4. Split each long sentence at a natural boundary. Keep causes, contrasts, conditions, and references explicit. Keep each instruction at 20 words or fewer. Keep each description at 25 words or fewer.
5. Compare the draft with the original. Check that every fact, number, name, condition, and degree of certainty remains intact.
6. Write the revised file with `write_file`. Change only the target file.
7. Run `check_file` again. If it reports banned words or long sentences, repeat steps 3 through 7.
8. Read the revised file with `read_file`. Compare it with the original from step 1. Correct any change in meaning, then repeat the checks.
9. Finish only when the report has no banned words or long sentences and the meaning check passes.
10. For several files, finish all steps for one file before starting the next. Follow the requested file order.
