# Procedure

1. Read the target notes file with `read_file`. Keep its path and full text.
2. Run `check_file` on that path before edits. Use the reported banned words and sentences over 25 words as the baseline.
3. Record the facts, names, numbers, conditions, and links between ideas that each flagged passage must keep.
4. Replace each banned word with plain text that keeps its meaning. Remove it only if it adds no meaning.
5. Split each long sentence into shorter sentences. Keep each sentence at 25 words or fewer, and each instruction at 20 words or fewer.
6. Read the revised text beside the original. Check that each fact, condition, and link from Step 3 remains.
7. Use `write_file` to save the full revised text at the same path. Do not change other files.
8. Run `check_file` on the saved file. If any banned words or long sentences remain, repeat Steps 3 through 8.
9. Read the saved file with `read_file`. Compare it with the original again to confirm that the meaning remains.
10. Finish this file only when the checks report no banned words or long sentences and the meaning check passes.
11. Apply Steps 1 through 10 to `notes/a.md`, then `notes/b.md`, then `notes/c.md`. Finish each file before the next.
