# Procedure: fix banned words and long sentences in one notes file

1. Read the file with the read_file tool.
2. Run check_file on the file path to list banned words and sentences over 25 words.
3. Remove each banned word, or replace it with a factual statement that keeps the meaning.
4. Split each long sentence into two or more sentences. Keep each sentence at 25 words or fewer.
5. Write the new content with the write_file tool.
6. Run check_file again. If it still reports problems, repeat steps 3 to 5.
7. Stop when check_file reports no banned words and no long sentences.
