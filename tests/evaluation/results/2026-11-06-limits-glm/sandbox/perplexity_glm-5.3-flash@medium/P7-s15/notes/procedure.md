# Procedure: fix banned words and long sentences in one notes file

This procedure fixes one file. Run it once per file. Keep the meaning of the file in every edit.

1. Read the file with `read_file`.
2. Run `check_file` on the file. Note each problem it reports: banned words and sentences over 25 words.
3. Draft a fix for every banned word. Replace it with a plain word or delete it. Do not remove facts.
4. Draft a fix for every long sentence. Split it at a clause boundary. Each part must keep the same facts in order.
5. Write the fixed text with `write_file`.
6. Run `check_file` on the new file.
7. Repeat steps 3 to 6 until `check_file` reports no problems.
