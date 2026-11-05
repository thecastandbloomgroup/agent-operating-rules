# A plan: repair dropped structure with a named second turn

## Headline

A second turn that names the dropped part targets Organization, because wording and position are exhausted there.

1. The sequence run left 12 answers with a broken structure, 6 of them on A3, and all 12 on three models.
2. The pilots showed that feedback lifts an answer only when it names the failed part, and that a plain retry often makes answers worse.
3. The probe sends both turn forms to the same 12 answers, so each arm has the same base, for about 1.5 USD.

## Background

Two wording levers failed on A3. The precedence line in Section 0 scored 12 of 18. The same line at the end of the file also scored 12 of 18. The structure columns of the script checks already name the dropped part of each answer. Examples: a heading used, or a self-test out of place. So the harness can write the feedback, and no judge is needed.

## Design

1. Add a mode `structure` to `bin/second-turn.py`. It reads the structure columns of `script-checks.csv` and writes one line that names each broken part. Unit tests cover the message, and the mode calls no API in them.
2. Send two second turns to each of the 12 broken answers of the sequence run: one `structure` turn and one `retry` turn, as its control.
3. Score both second-answer sets with `bin/script-checks.py`.

Step 2 MUST NOT start until the tests of step 1 pass.

## Metrics and pass marks

1. **Repair rate.** The structure turn repairs 9 or more of the 12 broken answers.
2. **Against the control.** The structure turn repairs at least 3 more answers than the retry turn.
3. **Guard.** No repaired answer loses its domain labels: labels with a reason do not fall in the repaired set.

A pass makes the structure turn the standing repair step of harness use, documented on the install page. It changes no rule text. A fail leaves Organization as a model limit, and the write-up says so.

## Cost and stop rule

Twenty-four second turns at the second-turn estimate cost about 1.5 USD. One run, then the write-up. The run waits for the mode of step 1.
