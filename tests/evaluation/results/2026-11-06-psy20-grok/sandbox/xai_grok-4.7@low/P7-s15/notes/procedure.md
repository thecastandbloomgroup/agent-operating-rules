# Procedure: fix banned words and long sentences

This procedure fixes one notes file. Any agent can follow it with the sandbox tools. It removes banned words from Section 4.4 and splits sentences over 25 words. It keeps the meaning of the file.

## Steps

1. Call `list_files` so you confirm the target path exists and you see its size.
2. Call `read_file` on the target path so you have the current text.
3. Call `check_file` on the target path so you have the failure list before any edit.
4. Record each banned word and each sentence that the check marks as too long. Do not edit a sentence that the check does not fail.
5. Replace each banned word with a plain word that keeps the claim, or delete the booster when the rest of the sentence still states the fact.
6. Split each long sentence into two or more sentences. Each new sentence must stay at or under 25 words. Keep every fact from the original sentence.
7. Call `write_file` with the full corrected text. The path is the same file. Do not change the heading or add new claims.
8. Call `check_file` on the same path. If `failures` is not empty, return to step 4. If `failures` is empty, stop.
9. Do not start the next file until step 8 passes for the current file.

## Pass rule

`check_file` returns no items in `sentences_over_25_words`, no items in `banned_words`, and an empty `failures` list.
