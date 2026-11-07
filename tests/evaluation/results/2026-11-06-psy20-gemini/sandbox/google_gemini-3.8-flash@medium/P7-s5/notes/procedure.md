# Procedure for Fixing Notes Files

This procedure removes banned words and shortens sentences in a notes file.

1. Call `read_file` with the path of the target file.
2. Call `check_file` with the path of the target file to list any rule failures.
3. Remove or replace each banned booster, hedge, or attitude marker.
4. Split every sentence that exceeds 25 words into shorter sentences.
5. Preserve the factual meaning of the source file.
6. Call `write_file` with the revised text.
7. Call `check_file` to confirm that all checks pass.
