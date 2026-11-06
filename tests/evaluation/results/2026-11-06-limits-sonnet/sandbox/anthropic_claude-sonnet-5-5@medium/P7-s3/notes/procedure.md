# Procedure: fix banned words and long sentences in one notes file

This procedure uses four tools: list_files, read_file, check_file, and write_file.

1. Call list_files. Confirm that the target file exists.
2. Call check_file on the target path. Record the banned words and the long sentences in the report.
3. Call read_file on the target path. Read the full text.
4. Write down the meaning of each flagged sentence in plain words. Keep facts, numbers, names, and order.
5. Rewrite each flagged sentence. Remove each banned word or replace it with a plain word.
6. Split each sentence over 20 words into two or more short sentences. Use one idea per sentence.
7. Do not add new facts. Do not delete facts. Do not use em dashes or en dashes.
8. Call write_file with the full new text of the file. The call replaces the old content.
9. Call check_file on the same path again.
10. If the report still lists a banned word or a long sentence, go to Step 5 and fix only those items. Then repeat Steps 8 and 9.
11. Stop when the report lists zero banned words and zero long sentences.
12. Compare the new text with the old text. Confirm that the meaning is the same.
