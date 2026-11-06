# Procedure: Fix banned words and long sentences

1. Read the target notes file with `functions.read_file`.
2. Run `functions.check_file` on the target file before any edits.
3. Record each flagged word and each sentence over 25 words.
4. Identify the facts, limits, conditions, and requests that each flagged passage contains.
5. Replace banned words with plain words that keep the same meaning.
6. Remove empty emphasis without changing the strength of a factual claim.
7. Replace vague uncertainty with a precise condition when the source supports that condition.
8. Do not invent facts, probabilities, evidence, or promises.
9. Split long sentences at clause boundaries, keeping each sentence at 25 words or fewer.
10. Keep instructions at 20 words or fewer per sentence.
11. Keep all facts, limits, conditions, requests, and links between ideas.
12. Write the revised file with `functions.write_file`.
13. Run `functions.check_file` on the revised file.
14. If the check reports any banned words or long sentences, repeat steps 4 through 13.
15. Read the revised file and compare its meaning with the original text from step 1.
16. Correct any lost or changed meaning, then repeat the check.
17. Finish only when the check reports no banned words or long sentences and the meaning remains intact.
18. Complete each target file before you start the next target file.
