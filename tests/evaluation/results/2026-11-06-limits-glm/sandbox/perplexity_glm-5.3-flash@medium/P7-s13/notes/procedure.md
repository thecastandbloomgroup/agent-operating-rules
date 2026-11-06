# Procedure to fix banned words and long sentences

Use this procedure on one notes file at a time. Run it with the sandbox tools only.

1. Run `check_file` on the file path. Read its report.
2. If the report lists no banned words and no long sentences, stop. The file passes.
3. Read the file with `read_file`. Plan the fixes:
   a. For each long sentence: split it at a clause boundary. Keep every fact that the original sentence has.
   b. For each banned word: replace it with a plain word or delete it, so the meaning stays the same.
4. Write the fixed file with `write_file`. Never add new facts. Never remove old facts.
5. Run `check_file` again on the file path.
6. If the report still lists a banned word or a long sentence, go back to step 3.
7. When the second report is clean, check the meaning: compare the old and new text fact by fact. If a fact was lost, go back to step 3.
8. Record in the notes file header that it passed the check.
