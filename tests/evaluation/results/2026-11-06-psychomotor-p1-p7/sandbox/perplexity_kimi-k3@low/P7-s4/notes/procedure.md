# Procedure: fix banned words and long sentences in one notes file

Tools available: read_file, write_file, check_file.

1. Run read_file on the target notes file to get its current content.
2. Run check_file on the target notes file. It reports banned words and sentences over 25 words.
3. Rewrite the content: replace each banned word with a neutral synonym, and split each long sentence into shorter sentences of 25 words or fewer. Keep the meaning unchanged.
4. Run write_file on the target notes file with the rewritten content.
5. Run check_file again on the target notes file to confirm no banned words and no sentences over 25 words remain.
6. If check_file still reports problems, return to step 3. Otherwise stop.
