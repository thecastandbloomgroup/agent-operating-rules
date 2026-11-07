# Procedure: fix banned words and long sentences

1. Read the target file with `read_file` before you change it.
2. Run `check_file` on the target file to find banned words and sentences over 25 words.
3. Record the facts, numbers, conditions, and intent that the revised file must keep.
4. Replace each banned word with plain, precise text, or remove it when it adds no meaning.
5. Split each sentence over 25 words into shorter sentences. Keep instructions at 20 words or fewer.
6. Keep the original meaning, including limits, uncertainty, duties, and links between ideas.
7. Write the complete revised file with `write_file`.
8. Run `check_file` again. Repeat steps 4 through 8 until no banned words or long sentences remain.
9. Read the revised file. Compare it with the original facts and intent recorded in step 3.
10. Correct any lost meaning and repeat the checks after each change.
11. Finish one target file before you start the next file in the requested order.
