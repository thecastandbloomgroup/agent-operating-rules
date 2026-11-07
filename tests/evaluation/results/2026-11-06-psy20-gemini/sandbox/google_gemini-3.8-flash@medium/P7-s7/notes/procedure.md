# Procedure for Fixing Notes Files

Follow these steps to fix banned words, long sentences, and readability issues in a file.

1. Call `read_file` with the path of the target file to inspect its content.
2. Call `check_file` with the path of the target file to list all violations.
3. Rewrite sentences with banned words by removing booster words or replacing uncalibrated hedges.
4. Split any sentence longer than 20 words in instructions or 25 words in descriptions into shorter sentences.
5. Use active voice and simple phrasing to ensure the Flesch-Kincaid grade does not exceed 10.
6. Call `write_file` with the target file path and the updated content.
7. Call `check_file` on the target file to verify that zero failures remain.
8. If failures remain, repeat step 3 through step 7 until `check_file` passes.
