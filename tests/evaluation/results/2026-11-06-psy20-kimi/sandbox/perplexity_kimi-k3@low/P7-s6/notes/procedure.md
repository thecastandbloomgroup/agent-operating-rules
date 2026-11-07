# Procedure: fix banned words and long sentences in one notes file

Use these tools: list_files, read_file, check_file, write_file.

1. Run check_file on the file to get the current list of banned words and long sentences.
2. Run read_file on the file to read the full content.
3. For each banned word, remove the word or replace it with a measured fact that keeps the meaning.
4. For each sentence over the word limit, split it into two or more sentences. Keep every fact from the original.
5. Keep the heading and the structure of the file.
6. Run write_file to replace the content with the fixed version.
7. Run check_file again on the file.
8. If check_file still reports problems, repeat steps 2 to 7 until the report is clean.
