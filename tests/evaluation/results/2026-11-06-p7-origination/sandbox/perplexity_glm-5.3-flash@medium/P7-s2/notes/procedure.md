# Procedure: fix banned words and long sentences in one notes file

This procedure fixes one file at a time. Any agent with the `check_file`, `read_file`, and `write_file` tools can run it. It keeps the meaning of the file.

## Rules the fix applies

1. Split every sentence with more than 25 words into two or more sentences. Keep all facts from the original sentence. Do not drop or add facts.
2. Remove banned words, or replace them with a word that keeps the meaning. Known banned words:
   - clearly
   - obviously
   - very
   - extremely
   - significantly
   - definitely
   - undoubtedly
   - of course
   - critical (as an intensifier)
   - powerful
   - robust
   - might
   - perhaps
   - somewhat
   - arguably
   - seems
3. Keep the file title and the paragraph order unchanged.

## Steps

1. Run `check_file` on the target file. Read the two report parts: sentences over 25 words, and banned words.
2. Run `read_file` on the target file. Read the full text.
3. Draft a new text in memory:
   - For each reported long sentence: split it at the strongest link between two facts. Write two or more short sentences.
   - For each reported banned word: remove it or replace it. Remove only if the claim still holds without the word. Replace only with a plain word.
4. Run `check_file` on the draft idea only if the tool can check text without a file. If it cannot go to step 5.
5. Run `write_file` on the target file with the new text.
6. Run `check_file` on the target file again.
7. Verify the report shows no long sentences and no banned words. If the report lists an issue again, repeat steps 3 to 6 for that issue only.
8. Verify the meaning is unchanged: every fact in the original text appears in the new text. If a fact is missing, add it in a short sentence and run step 6 again.

## Stop condition

Stop when `check_file` reports no long sentences and no banned words, and every original fact is present.
