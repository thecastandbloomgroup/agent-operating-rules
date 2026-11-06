# Procedure: fix banned words and long sentences in one notes file

Follow these steps in order for one file. Repeat the loop until Step 5 passes.

1. **Read the file.** Use `read_file` with the file path.
2. **Run the checks.** Use `check_file` on the same path. The tool lists:
      - Sentences with more than 25 words.
      - Banned words. Examples: "clearly", "very", "obviously", "extremely", "significantly" without a number, "perhaps", "somewhat".
3. **Apply the rules, in this order:**
      1. **Split long sentences.** Keep every clause. Split a sentence of more than 25 words into two or more sentences.
   2. **Remove banned words.** Delete the banned word if the sentence keeps its meaning. Otherwise replace it with a measured or plain word. Example: "clearly faster" becomes "faster", "in two seconds".
   3. **Keep the meaning.** Do not add new claims. Do not drop facts, numbers, or causes.
4. **Write the file.** Use `write_file` with the full fixed content at the same path.
5. **Verify.** Use `check_file` again. Pass means the tool reports zero banned words and zero long sentences. If the check fails, go back to Step 3.

## Notes for step 3

- One fact still needs one sentence. Splitting never deletes a fact.
- Replace, then read the result aloud in your head. The sentence must state the same claim as before, with the same qualifiers left out only when they are the banned word.
