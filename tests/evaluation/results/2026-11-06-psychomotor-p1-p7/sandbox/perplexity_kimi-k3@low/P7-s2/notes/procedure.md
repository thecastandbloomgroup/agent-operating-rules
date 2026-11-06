# Procedure: fix banned words and long sentences in one notes file

Tools: read_file, check_file, write_file. Run this procedure on one file at a time.

1. Run check_file on the target file. Note the banned words and the sentences over 25 words that it reports.
2. Run read_file on the target file.
3. Remove or replace each banned word. Replace it only when a replacement keeps the meaning. Otherwise delete it.
4. Split each sentence over 25 words into two or more sentences. Keep every fact. Do not change the order of events.
5. Keep the title and the structure of the file. Do not add new content.
6. Run write_file to save the revised text in full.
7. Run check_file again on the file. Confirm it reports no banned words and no sentences over 25 words.
8. If check_file still reports problems, go back to step 3. Otherwise the file is done.
