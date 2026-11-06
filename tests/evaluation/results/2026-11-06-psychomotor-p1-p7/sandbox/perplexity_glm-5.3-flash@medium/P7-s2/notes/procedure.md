# Procedure: fix one notes file

## Goal

Remove banned words and sentences over 25 words from one file. Keep the meaning. The tools are: `list_files`, `read_file`, `write_file`, and `check_file`.

The checker reports two failure kinds:

1. Banned words (boosters, hedges, attitude markers, filler).
2. Sentences over 25 words, including a Flesch-Kincaid grade over 10.

## Steps

1. Run `check_file` on the target path. Record the reported banned words and the count of long sentences. If both lists are empty, the file passes, so stop here.
2. Run `read_file` on the same path. Read the full text before any edit.
3. Fix each long sentence first. Split it into two or more sentences at a clause boundary. Keep every fact: the cause, the order of events, and the result. Rewrite in the active voice and use the present tense for facts.
4. Fix each banned word next. Delete the word when the sentence keeps its meaning without it. Replace it with the measurer or fact behind the claim when the sentence needs the point. Do not swap one booster for another.
5. Check the meaning against the original text. Each original fact still appears once, and no new claim is added.
6. Run `write_file` with the revised text.
7. Run `check_file` again on the same path. If it still reports a banned word or a long sentence, repeat steps 3 to 6 on the new report. The pass condition is a report with no failures.
8. Record one line per file in your reply: the path, the fixes that were made, and the final check result.
