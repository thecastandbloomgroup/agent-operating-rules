# Procedure: fix banned words and long sentences

Use this procedure on one notes file. The tools are read_file, check_file, and write_file.

A long sentence has more than 25 words. check_file reports long sentences and banned words.

1. Call read_file with the path of the notes file. Keep the heading and the meaning.
2. Call check_file with the same path. Record each banned word and each sentence over 25 words.
3. Call write_file with the same path. Remove each banned word. Split each long sentence into sentences of 25 words or fewer. Do not add new facts.
4. Call check_file again. If it still reports a banned word or a long sentence, repeat step 3. Stop when both lists are empty.
