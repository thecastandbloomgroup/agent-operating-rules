# Procedure: fix banned words and long sentences in one notes file

This procedure uses the tools `read_file`, `write_file`, and `check_file`.
Follow the steps in order. Do one file at a time.

1. Read the target file with `read_file`. Record its purpose and its meaning.
2. Run `check_file` on the target file. Record the reported long sentences and the reported banned words.
3. Fix each banned word first, one sentence at a time:
   - Replace words that amplify without evidence (for example "clearly", "very") with a fact or a number, or drop the word. Log the replacement.
   - Write the replacement in the present tense, in the active voice, with common words.
4. Fix each long sentence, one at a time:
   - Find each sentence with more than 25 words.
   - Split it into two or more sentences at the clearest join. Keep the meaning.
   - Reword so each new sentence has 25 words or fewer, with at most one subordinate clause.
5. Write the full fixed content back to the target file with `write_file`. Change nothing else.
6. Run `check_file` on the target file again.
7. If step 6 still reports banned words or long sentences, repeat steps 3 to 6 with the reported items only. The list MUST be empty before this loop ends.
8. Compare the fixed file with the version from step 1. Confirm each fact in the original still appears in the fixed file. Wait for this confirmation before step 9.
9. Move to the next file. Stop when no files remain.
