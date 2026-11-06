# Procedure: Fix banned words and long sentences in one notes file

This procedure makes one notes file pass the `check_file` tool. Keep the meaning of the file.

## Inputs

1. `path`: the notes file to fix, for example `notes/a.md`.

## Steps

1. Run `read_file` with `path`. Read the full text.
2. Run `check_file` with `path`. Write down the reported failures.
3. For each reported banned word, do one of these edits:
   a. Delete the word. Example: "clearly faster" becomes "faster".
   b. Replace it with a number or a measured fact. Example: "very simple" becomes "three steps".
4. For each sentence with more than 25 words, split it at a clause boundary. Each part keeps its own subject and verb. Move connective words, for example "until" or "so that", to the start of the next part when the link must stay clear.
5. Run `check_file` with `path` again.
6. If the check is clean, stop. If it still fails, fix each reported failure and repeat Steps 3 to 5.
7. Verify the meaning: run `read_file` with `path`. Confirm each fixed file states the same facts as the original, with no fact added, removed, or changed.
