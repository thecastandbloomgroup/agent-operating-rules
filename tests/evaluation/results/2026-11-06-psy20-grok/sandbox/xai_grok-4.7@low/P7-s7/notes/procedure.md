# Procedure

Any agent can follow these steps to fix banned words and long sentences in one notes file. The tools are list_files, read_file, write_file, and check_file.

1. Call list_files so you know the notes path exists and its size.
2. Call read_file on that notes path and keep the full text.
3. Find banned words named in Section 4.4. These are boosters and hedges that amplify or weaken a claim without evidence.
4. Replace each banned word with a plain fact, a number, or delete it. Do not change the claim.
5. Split every sentence over 25 words into two or more sentences. Keep the same facts.
6. Keep the heading, the topic, and the meaning of the file.
7. Call write_file with the full revised text. This replaces the old file.
8. Call check_file on the same path.
9. If check_file still reports a banned word or a sentence over 25 words, repeat from step 4.
10. Stop when check_file reports no banned words and no sentence over 25 words.
