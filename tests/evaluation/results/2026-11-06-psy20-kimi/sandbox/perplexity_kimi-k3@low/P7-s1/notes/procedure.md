# Fix banned words and long sentences in a notes file

1. Run the check tool on the target file to get the list of banned words and sentences over 25 words.
2. If no issues are reported, stop and move to the next file.
3. For each banned word, remove it or replace it with a plain word that keeps the meaning.
4. For each sentence over 25 words, split it into two or more short sentences that keep the original meaning.
5. Write the fixed content back to the file in full.
6. Run the check tool again on the file.
7. If issues remain, repeat steps 3 to 6. Otherwise the file is done.
