# Procedure: fix one notes file

Goal: remove banned words and sentences over 25 words from one file. Keep every fact.

Tools: `read_file`, `check_file`, `write_file`.

## Steps

1. Read the target file with `read_file`. Note the title and every fact it states.
2. Run `check_file` on the same path. It lists the sentences over 25 words and the banned words. These two lists are the work list.
3. For each banned word, remove it or replace it with a specific fact or a number. Do not replace it with a weaker word that changes the claim.
4. For each sentence over 25 words, split it at a join word such as "and", "so that", "when", or "until". Put the events in the same order as the original. Keep each new sentence at 25 words or fewer.
5. Write the fixed file with `write_file` to the same path. Keep the original title and every fact from step 1.
6. Run `check_file` on the path again. If it still reports a banned word or a long sentence, repeat steps 3 to 5 for the remaining items.
7. Confirm the meaning: every fact from step 1 must appear in the fixed file. Stop when both checks pass with no change to any fact.

## Rules for word choice

- One word, one meaning. Use the same term for the same thing as the original file.
- Active voice, present tense. No em dash or en dash.
- Remove amplifiers such as "clearly" and "very" instead of keeping them.
