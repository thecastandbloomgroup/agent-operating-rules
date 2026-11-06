# Procedure: Fix banned words and long sentences in one notes file

Numbered steps. Any agent can follow them with these tools: list_files, read_file, write_file, check_file. Do not change the meaning of the file.

1. Pick one notes file from the list. Call list_files to see every file and its size.
2. Call read_file on that file. Find words that only add force and carry no evidence, for example "very", "extremely", and "obviously". Delete them or replace them with a number. Keep every fact.
3. Count the words in each sentence. One sentence must not exceed 25 words in a description. One sentence must not exceed 20 words in an instruction. If a sentence is over the limit, split it into two or more sentences at a natural break. Keep each fact in one part.
4. Call write_file to replace the file with the fixed text. Keep the title line and every fact that was there before.
5. Call check_file on the same file.
6. Read the check_file report. If it still lists a banned word or a long sentence, go back to Step 2 and fix only the items in the report. Then repeat Steps 4 and 5.
7. When the report is clean, move to the next notes file. Do not start one file until the previous one is clean.
8. Stop after every notes file in the list is clean.
