# Procedure: fix banned words and long sentences

Use this procedure on one notes file. The tools are list_files, read_file, write_file, and check_file.

1. Call read_file on the target path.
2. Mark each word from the banned list in Section 4.4 of the operating rules.
3. Count the words in each sentence. Flag a sentence over 25 words. Flag an instruction over 20 words.
4. Delete each banned word. Keep the same claim.
5. Split each flagged sentence into two or more sentences. Keep the same facts.
6. Call write_file with the full revised text. Do not change the title.
7. Call check_file on the same path.
8. If the check reports a hit, repeat steps 4 to 7. Stop when the check reports no hits.
