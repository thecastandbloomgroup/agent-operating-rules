# Procedure: fix banned words and long sentences in one notes file

Goal: bring one Markdown file to zero banned words and zero sentences over 25 words, and keep its meaning.

Tools used: `read_file`, `check_file`, `write_file`.

## Steps

1. Read the file with `read_file`. Note its title, topic, and meaning. Do not change the meaning at any later step.
2. Run `check_file` on the file path. It lists every sentence over 25 words and every banned word.
3. Make a change plan from the report:
   - For each banned word, pick a plain word with the same meaning. Do not add intensifiers in their place.
   - For each long sentence, find the break point at a clause boundary. Split it into two or more sentences. Keep every fact. Move no fact between clauses unless the order of events stays true.
4. If the report is empty, stop. The file is done.
5. Write the fixed text with `write_file`. Replace the whole file. Keep the title and paragraph order the same.
6. Run `check_file` on the same path again.
7. If the report is still not empty, repeat steps 3 to 6. One new side effect of an edit can be another banned word or a new long sentence.
8. When the report is empty, compare the new text with the old meaning one final time. Keep the fix only if every fact from step 1 is still present.
