# Procedure: fix banned words and long sentences in one notes file

This procedure fixes two defect types that the check tool reports. The two types are banned words and sentences over 25 words. The banned word list lives in the check tool, so the tool output is the source of truth. Keep the meaning of the file during every edit.

## Steps

1. Read the target file with `read_file`. Note its meaning in one clause before any edit.
2. Run `check_file` on the file path. Read the reported banned words and the reported long sentences.
3. Fix banned words first. Replace each banned word with a plain word, or delete it when the sentence works without it. Do not add banned words in the replacement.
   - Test: after the edit, `check_file` reports zero banned words.
4. Fix long sentences next. Split each reported sentence at a clause boundary. Keep the meaning in both halves. Add a close link word such as "then" or "so" when the link carries meaning.
   - Test: after the edit, `check_file` reports zero sentences over 25 words.
5. Write the fixed content with `write_file` to the same path.
6. Run `check_file` again on the path. Confirm zero banned words and zero long sentences.
7. If step 6 reports a defect, repeat steps 3 to 6 until the report is clean. Do not exceed five repeat cycles per file.
8. Record done when the report is clean. Stop.

## Constraint

- The report from `check_file` is the single pass criterion. No edit is final until a run after the edit is clean.
- Meaning check: after the final clean run, read the file once more. Keep the file until its one-clause summary at step 1 still holds.
