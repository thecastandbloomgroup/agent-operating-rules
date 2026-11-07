# Procedure

1. Read the target notes file with `read_file`.
2. Run `check_file` on the target file before any edits.
3. Review each reported banned word and long sentence in its full context.
4. Replace banned words with plain terms that preserve the original claim, scope, and certainty.
5. Split long sentences at natural breaks without removing facts, conditions, exceptions, or links between ideas.
6. Keep instructions at 20 words or fewer and descriptions at 25 words or fewer.
7. Write the revised text to the same path with `write_file`.
8. Run `check_file` on the revised file.
9. If the check reports banned words or long sentences, repeat steps 3 through 8.
10. Read the revised file and compare it with the original text from step 1.
11. Restore any lost meaning, then repeat the checks after each change.
12. Finish only when the check reports no banned words or long sentences and the comparison confirms the original meaning.
13. Apply these steps to each requested file in the specified order.
