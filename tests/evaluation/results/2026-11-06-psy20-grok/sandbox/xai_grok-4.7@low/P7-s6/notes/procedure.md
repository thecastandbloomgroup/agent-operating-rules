# Procedure

Use this procedure on one notes file. The tools are read_file, check_file, and write_file.

1. Call read_file with the file path. Keep the returned text.
2. Call check_file with the same path. Record each banned word. Record each sentence over 25 words.
3. Call write_file with the same path and the full new text. Keep the heading and the facts. Remove each banned word. Split each sentence over 25 words. Do not add facts.
4. Call check_file again on the same path. If a banned word or a long sentence remains, repeat step 3. Stop when the report is clean.
