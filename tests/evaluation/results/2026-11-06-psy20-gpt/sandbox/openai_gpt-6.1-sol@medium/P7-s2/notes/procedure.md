# Procedure: Fix banned words and long sentences

1. Use `read_file` to read the target notes file before you change it.
2. Use `check_file` on the target file to find banned words and sentences over 25 words.
3. Record the facts, claims, conditions, and uncertainty that the revised file must retain.
4. Replace each banned word with neutral text that keeps its meaning.
5. Remove empty emphasis only when the claim keeps its meaning without it.
6. Split long sentences at clause boundaries and keep the links between their ideas.
7. Keep each sentence at 20 words or fewer to cover both instructions and descriptions.
8. Keep names, numbers, units, dates, duties, exceptions, and the strength of each claim.
9. Use `write_file` to save the complete revised file at its original path.
10. Use `check_file` again and fix every reported banned word or long sentence.
11. Use `read_file` to compare the saved text with the original facts and claims recorded in step 3.
12. Repeat steps 4 through 11 until the checks pass and the meaning stays intact.
13. Finish one file before you start the next file in the requested order.
