# Procedure: fix banned words and long sentences in one notes file

Scope: the target file is one file under `notes/`. The tools are `read_file`, `write_file`, `check_file`. Do one file at a time.

1. Run `read_file` on the target path. Print or note the full content.
2. Run `check_file` on the target path. The report lists two finding types: sentences over 25 words, and banned words (boosters and uncalibrated hedges, for example "clearly", "very", "might", "perhaps").
3. Build a fix list from the report. Enter one line per finding: the exact sentence or word, and the planned change. If the report lists no findings, stop here. The file is clean.
4. For each banned word on the fix list, remove it or replace it with a factual word. Do not add new amplifiers. Keep the meaning: if the booster carried a confidence claim, keep the claim only when the file itself supports it with evidence.
5. For each long sentence on the fix list, split it at a clause boundary. Write two or more sentences that together keep every fact, actor, and time marker from the original. Keep the same order of events.
6. Assemble the new content: same title and same structure as the original, with only the fix-list items changed.
7. Run `write_file` on the target path with the new content.
8. Run `check_file` again on the same path.
9. If the new report still lists findings, go back to step 3 with this new report. Repeat at most three times.
10. Stop when `check_file` reports no banned words and no sentences over 25 words. Do not change the file further.
