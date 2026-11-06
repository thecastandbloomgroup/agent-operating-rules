# Procedure: fix banned words and long sentences

Any agent can follow these steps on one notes file. The tools are list_files, read_file, write_file, and check_file.

1. Call list_files so you know the file exists and its size.
2. Call read_file on the notes file. Keep every fact in the text.
3. Find banned words from Section 4.4 of the operating rules. Examples: clearly, obviously, very, extremely.
4. Replace each banned word with a plain fact, or delete it when the sentence stays true.
5. Split every sentence over 25 words. Keep one idea per sentence. Keep the active voice.
6. Do not add new claims. Do not drop a number, a cause, or an order of events.
7. Call write_file with the full corrected text. This replaces the old file.
8. Call check_file on that path.
9. If check_file still reports a banned word or a long sentence, repeat steps 4 to 8.
10. Stop when check_file reports no banned words and no sentence over 25 words.
