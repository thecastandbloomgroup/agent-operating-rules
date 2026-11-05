# A plan: repair an unchecked final write with a second turn

## Headline

A second turn in the tool loop targets the main failure of Complex overt response: a final write that no check follows.

1. Five of the ten P5 failures of the P1 to P6 run are one behavior. The model moved the line right, then answered with no check after its last write.
2. A named turn repaired 10 of 12 broken structures, against 3 for a plain retry, so the same pair of arms fits here.
3. The probe sends both arms to the same five units, for under 1 USD, and it changes no rule text.

## Background

Complex overt response passed 14 of 24, under its mark of 19. The other five failures do not fit a second turn. Four Gemini units hit the step cap with no answer. One Grok unit left a scratch file, which no tool can delete. So this probe takes the five units with an answer and an unchecked final write.

## Design

1. Let `bin/run-psychomotor.py` start a unit from a seed: the end state of an earlier unit, its conversation, and its steps. The grader then reads the earlier steps and the new steps as one history.
2. Add `bin/repair-psychomotor.py`. It finds the failed P5 units of a run with the note "no check ran after the last write". It sends one second turn to each, with up to 6 more tool steps.
3. Arm one, named: "A reviewer checked your work. No check_file call ran after your last write, so the final state of the files is unchecked. Fix that with the tools, then answer again."
4. Arm two, retry: "Check your work with the tools, then answer again."
5. Grade both arms with `bin/check-psychomotor.py`.

Step 5 MUST NOT start until the unit tests of steps 1 and 2 pass.

## Metrics and pass marks

1. **Repair rate.** The named turn repairs 4 or more of the 5 units.
2. **Against the control.** The named turn repairs at least 2 more units than the retry turn.
3. **Guard.** No repaired unit breaks the end state: the line stays moved, and no file appears or changes.

A pass on marks 1 and 3 with a fail on mark 2 still teaches something. It means any nudge to verify repairs the failure, so a harness can add a generic check turn. A fail on mark 1 says the missing check is a model limit at this level.

## Cost and stop rule

Ten repair units of up to 6 steps cost under 1 USD. One run, then the write-up. Five units give a direction, not a rate.
