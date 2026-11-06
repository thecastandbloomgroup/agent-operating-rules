# Procedure

1. Read the target notes file with `read_file`. Record its facts, intent, conditions, and key terms before any edits.
2. Run `check_file` on the target path. Use its banned-word and sentence reports to locate each issue.
3. Replace banned words with plain terms that keep the meaning. Remove filler only when it adds no meaning.
4. Split each long sentence into shorter sentences. Keep each fact, condition, link, and required action. Aim for at most 20 words per sentence.
5. Use `write_file` to save the full revised file at the same path. Do not change other notes files.
6. Run `check_file` again. If it reports any banned words or long sentences, repeat Steps 3 through 6.
7. Read the saved file with `read_file`. Compare it with the original text from Step 1. Restore any lost meaning, then repeat the checks.
8. Finish only when the checker reports no issues and the meaning remains intact. Report the result without claims beyond the checks.
9. Apply Steps 1 through 8 to `notes/a.md`, then `notes/b.md`, then `notes/c.md`. Finish each file before the next one.
