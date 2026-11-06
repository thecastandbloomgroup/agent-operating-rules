# Procedure: fix the banned words and long sentences of one notes file

This procedure fixes one file in the sandbox. Use these tools: `list_files`, `read_file`, `check_file`, `write_file`. Apply the steps to exactly one file per run. Keep the meaning of the file in every edit.

## Steps

1. **Read the file.** Run `read_file` on the target path. Note its meaning in one sentence. You keep this meaning fixed for all later edits.
2. **Run the check.** Run `check_file` on the same path. It reports two issue kinds: sentences over 25 words, and banned words.
3. **Fix the banned words first.** For each banned word in the report, choose a plain word that keeps the meaning. Rework the sentence, because the report often counts words again after this change.
   - "very <adjective>" becomes the adjective alone, or a stronger plain adjective.
   - "clearly" becomes "more than" with a number, or it becomes "the tests show that". Use the phrase that does not add a claim.
   - "obviously", "definitely", "clearly" as hedges: delete them. They add no information.
4. **Fix each long sentence.** For every sentence over 25 words in the report, split it at a natural break. Make the new sentences each 25 words or fewer. Keep one idea per sentence. Join the ideas with "then", "so", or "because" across sentences, not with "and" inside one long sentence.
5. **Write the file back.** Run `write_file` with the full fixed content. Do not change the title or the meaning.
6. **Verify.** Run `check_file` on the same path again. Pass means: zero long sentences and zero banned words. Fail means: return to step 3.
7. **Log the result.** Record the path, the edits made, and the pass or fail state of step 6.
