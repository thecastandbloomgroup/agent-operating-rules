# Procedure for Editing Notes

Follow these steps to fix banned words and long sentences in one file.

1. Call `read_file` with the path of the target file.
2. Read the text and identify words banned by Section 4.4.
3. Identify sentences longer than 25 words in descriptions or 20 words in instructions.
4. Rewrite sentences to remove banned words while keeping the original meaning.
5. Split long sentences into shorter sentences under the word limits.
6. Check that the revised text remains in the active voice and present tense.
7. Call `write_file` with the path and the updated content.
8. Call `check_file` with the path of the file to verify compliance.
9. If `check_file` reports failures, repeat steps 4 through 8 until it passes.
