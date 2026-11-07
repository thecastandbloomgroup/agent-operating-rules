# Procedure: fix one notes file

Use these steps on one notes file. Use only read_file, check_file, and write_file.

1. Call read_file with the path of that file. Keep the heading and the facts.
2. Call check_file with the same path. Note each banned word. Note each sentence over 25 words.
3. Rewrite the full file. Delete each banned word. Split each long sentence into shorter sentences. Do not add facts. Do not drop facts.
4. Call write_file with the same path and the full new text.
5. Call check_file again. If it still lists a banned word or a long sentence, go back to step 3. Stop when the report is clean.
