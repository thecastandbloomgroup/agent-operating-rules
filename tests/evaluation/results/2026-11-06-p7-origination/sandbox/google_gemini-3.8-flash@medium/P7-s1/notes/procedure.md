# Procedure for Fixing Notes Files

Follow these steps to clean a notes file:

1. Read the target file with `read_file`.
2. Inspect the file content for sentence length, structure, and banned language.
3. Run `check_file` on the target file path to see reported failures.
4. Remove banned words such as boosters, uncalibrated hedges, or attitude markers while preserving the factual meaning.
5. Split any sentence longer than 25 words into two or more short sentences.
6. Write the corrected text back to the file with `write_file`.
7. Run `check_file` on the file path to verify that zero failures remain.
8. If failures remain, repeat step 4 through step 7 until `check_file` passes.
