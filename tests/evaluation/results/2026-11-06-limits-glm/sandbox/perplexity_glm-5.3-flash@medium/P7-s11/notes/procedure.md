# Procedure: fix one notes file

Use this procedure on one notes file. The tools are check_file, read_file, and write_file. The checks are sentence length and banned words. A check_file run lists both.

## Steps

1. Read the file. Note each meaning that the file states.
2. Run check_file on the file path.
3. Read every finding. Split each step so that one item gets one fix.
4. Fix banned words first. Replace each one with a plain word of the same meaning, or delete it when no meaning is lost.
5. Fix long sentences next. For each sentence over the limit, do all of these:
   a. Find the main point. Keep it in the first new sentence.
   b. Move each extra clause into its own sentence, in the original order.
   c. Replace joined clauses with words such as "because", "so", or "then" only when the link is the point.
6. Keep every fact, number, cause, and condition from the original text. Do not add new facts. Do not drop a fact.
7. Run check_file again. If it reports any finding, repeat from Step 4.
8. Write the fixed text back with write_file. Cite no changes to other files.

## Limits

- One check_file run reports one file only. Run it per file.
- The fix must not change the meaning. When a split can change the meaning, keep the original clause order. Mark the risk in a follow-up note at the end of the file.
