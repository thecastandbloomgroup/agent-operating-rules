# Procedure: fix banned words and long sentences

1. Read the target notes file with `functions.read_file`.
2. Record its facts, qualifications, instructions, and intended meaning before you edit.
3. Run `functions.check_file` on the target file to locate banned words and sentences over 25 words.
4. Replace each banned word with plain wording that preserves its meaning, or remove it if it adds no meaning.
5. Preserve uncertainty and factual claims; do not invent evidence, probabilities, or confidence levels.
6. Split long descriptions into sentences of at most 25 words.
7. Split instructions into sentences of at most 20 words, with one instruction per sentence.
8. Compare the revised text with the original to verify facts, scope, qualifications, and instructions remain intact.
9. Save the full revised file with `functions.write_file`.
10. Run `functions.check_file` again on the saved file.
11. If the check reports a banned word or long sentence, revise the text and repeat steps 8 through 10.
12. Read the saved file and confirm its meaning matches the original before you continue to the next file.
