# Procedure: fix banned words and long sentences in one notes file

Tools: list_files, read_file, check_file, write_file.

## Steps

1. Read the target file with read_file.
2. Run check_file on the file. Note every banned word and every sentence over 25 words.
3. Rewrite the text:
   - Remove each banned word. If it carried meaning (for example "two seconds"), keep the fact. If it was an intensifier with no measure (for example "clearly", "very"), delete it.
   - Split each sentence over 25 words into shorter sentences of 25 words or fewer.
   - Keep the headings and all facts. Do not add new claims.
4. Write the rewritten text with write_file, replacing the old content.
5. Run check_file again on the file.
6. If check_file still reports a banned word or a long sentence, return to step 3.
7. Stop when check_file reports no problems.
