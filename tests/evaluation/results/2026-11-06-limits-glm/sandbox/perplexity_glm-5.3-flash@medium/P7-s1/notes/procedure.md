# Procedure: Fix banned words and long sentences in one notes file

Use this procedure with these tools: `list_files`, `read_file`, `write_file`, `check_file`.
Work on one file per pass. Keep the meaning of each sentence.

1. List every file in the sandbox with `list_files`, so you know what exists.
2. Read the target file with `read_file`. Find every banned word and every sentence over 25 words.
   - Banned word groups: amplifiers without evidence (examples: clearly, very, obviously, simply, critical), hedges without a probability (examples: might, perhaps, arguably), and filler phrases.
   - Mark every match: line and word.
3. Edit one item at a time. Write the fixed text with `write_file`.
   - Banned word: delete the word or replace it with a number or a fact, then keep the sentence under 25 words.
   - Long sentence: split it at a clause boundary. Each result must be a full sentence. Keep the order of events. Keep every fact.
4. Run `check_file` on the file. It reports long sentences and banned words.
5. Repeat steps 2 to 4 until `check_file` reports no problems.
6. Read the final file once more. Compare it with the original facts:
   - Every fact from the original is present.
   - No new fact was added.
7. Record the fix per file: matches found, how each was fixed, and the final `check_file` result.
