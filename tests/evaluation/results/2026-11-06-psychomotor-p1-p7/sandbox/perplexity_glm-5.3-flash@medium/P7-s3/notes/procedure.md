# Procedure: fix banned words and long sentences in one notes file

Use these tools: `read_file`, `check_file`, `write_file`.

## Steps

1. Read the file with `read_file`. Note each sentence and its meaning.
2. Run `check_file` on the file. Two reports come back: sentences over 25 words and banned words.
3. For each banned word, write a replacement that keeps the meaning:
   - A booster such as "clearly" or "very": delete it, or state the measured fact instead.
   - A hedge such as "might" or "perhaps": state a probability, for example "70% likely", or state the fact.
4. For each sentence over 25 words, split it at clause boundaries. Rules:
   - Keep every clause, so the meaning stays whole.
   - Use active voice. Put an agent on the verb.
   - One idea per sentence. Use the present tense for facts.
5. Write the fixed full file with `write_file`.
6. Run `check_file` again. If the report shows a violation, go to step 3 and fix it.
7. Stop when `check_file` reports no banned words and no sentences over 25 words.

## Meaning check

Before step 5, list each fact in the file. After step 5, list the facts again. The two lists MUST match.
