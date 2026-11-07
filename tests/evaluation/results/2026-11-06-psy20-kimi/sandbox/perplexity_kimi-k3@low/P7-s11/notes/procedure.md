# Fix procedure

1. Run the check on the file with check_file.
2. Read the reported banned words. Replace each banned word or delete it. Keep the meaning.
3. Read the reported sentences over 25 words. Split each into two or more short sentences. Keep the meaning.
4. Write the fixed file with write_file.
5. Run check_file again on the same file. Repeat steps 2 to 4 until no banned words and no long sentences stay.
