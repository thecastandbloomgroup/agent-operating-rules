# Procedure: fix banned words and long sentences

## Fix policy

Correct prose keeps its meaning without intensifiers, so the first attempt for each banned word is deletion, not generic neutralization. If the claim still stands without the word, delete it. If it does not, replace the word with the specific value: a number, a comparison, or a state from the material. Verify the substitute is a direct quote or a numeric fact from the material. Do not invent values. This keeps meaning intact while meeting the style rules.

## Fix list

The checks run on one file cover two failure types:

1. Sentences over the word limit. Instructions: 20 words. Descriptions: 25 words.
2. Banned words: boosters and uncalibrated hedges. Examples: clearly, very, might, perhaps, obviously, significantly.

## Steps for one file

1. Read the target file.
2. Run `check_file` on the target file. Record every line it reports.
3. For each reported banned word, decide: delete it, or replace it with a specific value from the material. Use the fix policy above.
4. For each reported long sentence, classify it: does it contain one instruction or more than one fact?
   4a. If it lists steps, split at each step boundary so each result is its own sentence.
   4b. If it gives background that leads to one fact, extract the background into its own sentence first.
   4c. Do not lose any detail, including conditions, durations, and sequence.
5. Run `check_file` again on the target file. Expect a clean result and no word limit violations. The fix list over the first run must be MECE: each reported item maps to exactly one fix type.
6. If a banned word or a long sentence survives, go to step 3. Merge the whole fixed text back into the file only after step 5 passes.
7. Stop the check-report loop. A file that reports no banned words and no long sentences is done. Do not polish further.
