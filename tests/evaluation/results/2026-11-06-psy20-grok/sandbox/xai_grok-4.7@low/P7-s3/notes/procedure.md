# Procedure

Fix banned words and long sentences in one notes file. Keep the meaning.

1. Read the file with read_file. Note each sentence and its meaning.
2. Find banned words from Section 4.4. Replace each one with a plain fact or delete it. Do not add a new claim.
3. Split each sentence over 25 words. Keep one idea per sentence. Keep the original meaning.
4. Write the full file with write_file. Do not change headings or facts.
5. Run check_file on that path. If it reports a hit, repeat steps 2 to 5 on the same file.
6. Stop when check_file reports no banned words and no sentence over 25 words.
