# Procedure

Any agent can fix banned words and long sentences in one notes file. Use these tools. Keep the meaning of the file.

1. Call list_files. Confirm the target file is present.
2. Call read_file on the target path. Copy the current text.
3. Find each booster that Section 4.4 bans. The checker names them in its report.
4. Remove or replace that word so the claim stays true.
5. Split each sentence that has more than 25 words. Keep the same facts.
6. Call write_file with the full new text. Do not change facts that were already correct.
7. Call check_file on the same path. If it reports a hit, return to step 3.
8. Stop when check_file reports no banned words and no sentence over 25 words.
