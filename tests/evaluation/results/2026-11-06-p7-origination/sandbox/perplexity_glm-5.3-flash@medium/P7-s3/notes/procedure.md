# Procedure: fix banned words and long sentences in one notes file

## Steps

1. Run `check_file` on the file. Read the two failure lists: sentences over 25 words, and banned words.
2. Split each long sentence. Find the points where one idea ends and the next starts. Break the sentence there. Keep the original words where possible, so the meaning stays.
3. Fix each banned word. Replace amplifiers such as "clearly" with the evidence itself, or remove them. Markers such as "very" are banned amplifiers.
4. Check the style rules as you edit. Use the active voice and the present tense. Use a comma or a period instead of dashes. Do not use gerunds when a verb form exists. Keep the Flesch-Kincaid grade at 10 or lower.
5. Run `check_file` on the file again. Confirm both failure lists are empty.
6. Read the file and the original once more. Confirm the meaning did not change.
