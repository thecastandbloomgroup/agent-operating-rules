# Procedure: fix banned words and long sentences in one notes file

Use the sandbox tools: list_files, read_file, check_file, write_file.

1. Run list_files to find the notes file. Confirm the path.
2. Run read_file on the notes file. Save the content.
3. Run check_file on the notes file. Record every banned word and every sentence over 25 words.
4. For each banned word, rewrite the sentence without it. Keep the meaning. Examples: delete "clearly" and "very", or replace them with a fact.
5. For each sentence over 25 words, split it into shorter sentences. Each new sentence MUST have 25 words or fewer. Keep the meaning.
6. Run write_file with the new content. Keep the heading and the paragraph structure.
7. Run check_file on the notes file again.
8. If check_file reports problems, go to step 4. Fix the reported lines.
9. If check_file reports no problems, stop. The file is done.
