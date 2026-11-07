# Procedure for one notes file

1. Select one target notes file. Complete this procedure before you select another file.
2. Read the target with `functions.read_file`. Record its facts, names, numbers, conditions, claims, and degree of certainty.
3. Run `functions.check_file` on the target. Record every banned word and sentence that exceeds the tool's limit.
4. Review all sentences for length. Use at most 20 words per sentence, which also meets the tool's 25-word limit.
5. Replace banned words with permitted words that keep the same meaning. Remove a word only when it adds no meaning.
6. Split long sentences at natural boundaries. Keep each condition, exception, cause, comparison, and reference with the claim it qualifies.
7. Compare the draft with the original. Check that every fact and qualification remains, without new claims or changes in certainty.
8. Write the complete revised target with `functions.write_file`. Do not change other notes files during this step.
9. Run `functions.check_file` again. If it reports any banned word or long sentence, repeat steps 5 through 9.
10. Read the saved target with `functions.read_file`. Confirm that its meaning matches the original and each sentence meets step 4.
11. If the final review requires an edit, repeat steps 7 through 10. Finish only after all checks pass.
12. Report the target path, edits, and final check result. If a faithful revision is not possible, report the unresolved conflict.
