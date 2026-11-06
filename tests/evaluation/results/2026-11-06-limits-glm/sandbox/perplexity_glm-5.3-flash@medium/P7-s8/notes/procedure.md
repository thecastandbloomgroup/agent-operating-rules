# Procedure: fix banned words and long sentences in one notes file

This procedure fixes one file of the notes folder with two tools: `check_file` and `write_file`. The goal is a file with no banned words and no sentence over 25 words that keeps its meaning.

Steps:

1. Read the file with `check_file`. The report lists each sentence over 25 words and each banned word. If the report shows no problem, stop here.
2. Read the file with `read_file`. This gives the full text needed to preserve the meaning.
3. For each banned word, replace it with a plain word or delete it. Do not add a new claim: keep the meaning. Examples: "very simple" becomes "simple"; "clearly faster" becomes "faster".
4. For each sentence over 25 words, split it at a natural break. Put a period at the break. Use a connective word, such as "then" or "however", when the link matters. Keep every fact.
5. Write the new text with `write_file`. Write the whole file, not a fragment.
6. Run `check_file` again. It must report no long sentences and no banned words.
7. If the report still shows problems, repeat steps 3 to 6. Fix one problem per pass. The loop ends when the report is clean.
