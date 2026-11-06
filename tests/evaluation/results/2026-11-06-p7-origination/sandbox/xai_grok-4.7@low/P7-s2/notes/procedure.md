# Procedure: fix banned words and long sentences

Any agent can follow these steps on one notes file. The tools are `read_file`, `check_file`, and `write_file`.

1. Call `read_file` on the notes file. Keep the heading and the meaning of every sentence.
2. Call `check_file` on the same path. Record each sentence over 25 words and each banned word.
3. Split each sentence over 25 words into two or more sentences. Keep the same facts.
4. Replace each banned word with a plain word, or delete it when it adds no fact. Do not add a new claim.
5. Call `write_file` with the full revised text. Do not edit any other file in this step.
6. Call `check_file` again. If it still reports a long sentence or a banned word, return to step 3.
7. Stop when `check_file` reports no long sentence and no banned word.
