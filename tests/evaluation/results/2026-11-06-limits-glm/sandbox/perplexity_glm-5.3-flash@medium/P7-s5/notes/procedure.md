# Procedure: fix banned words and long sentences in one notes file

Use the `check_file`, `read_file`, and `write_file` tools. One file per pass. Keep the meaning of the file.

1. Run `check_file` on the file path. Record the sentences over 25 words and the banned words.
2. If the report is empty, stop. The file is done.
3. Run `read_file` on the same path.
4. Fix each long sentence. Split it into two or more sentences at "and", "when", "so", "but", or a comma. Keep every fact. Keep the order of events.
5. Fix each banned word. Delete an intensifier, or replace it with a number from the text. Replace a hedge with a plain statement of the same fact.
6. Check each new sentence. Count its words. Keep every sentence at 25 words or fewer.
7. Run `check_file` on the path again. The report MUST be empty.
8. If the report is not empty, go to step 3. Do not send the file until the report is empty.
