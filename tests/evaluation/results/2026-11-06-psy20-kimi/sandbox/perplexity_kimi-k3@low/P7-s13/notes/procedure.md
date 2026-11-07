# Procedure: fix banned words and long sentences in a notes file

Tools: read_file, write_file, check_file (all take a sandbox-relative path).

1. Run check_file on the file. Note its banned words and its sentences over 25 words.
2. Run read_file on the file. Keep the output.
3. For each banned word, remove it or replace it with a plain word that keeps the meaning.
4. For each sentence over 25 words, split it into two or more sentences. Each new sentence must keep one idea from the original.
5. Check that the rewrite keeps the title, the facts, and the order of the original.
6. Run write_file on the path with the rewritten text.
7. Run check_file on the file again.
8. If check_file still reports banned words or long sentences, repeat from step 3.
9. Stop when check_file reports no problems.
