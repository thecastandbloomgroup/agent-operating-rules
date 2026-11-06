# A plan: a narrow note that says only where the answer goes

## Headline

A narrow note says only where the answer goes. It tests the cause of the Gemini loop with no hint about any fail of a prompt.

1. The full sandbox note ended the loop: Gemini passed 24 of 24 on P1 to P3, against 11 of 24 in the control.
2. However, its sentence "Do not write any other file" names a fail of P2 and P5, so it cannot be the default.
3. The narrow note keeps only the sentence that names no fail. If it works alone, it can be the default.

## Background

The [sandbox note results](2026-11-06-sandbox-note-results.md) found the effect and the problem with its text. `bin/run-psychomotor.py --answer-note` adds only the narrow sentence after the prompt.

## Design

1. Probe arm: Gemini 3.8 Flash on P1, P2, and P3, 8 samples, with `--answer-note`: 24 units.
2. Control arm: the same 24 units with no note, at the same time.
3. Guard arm: Sonnet 5.5 on P1, P2, and P3, 4 samples, with `--answer-note`: 12 units.
4. P5 arm: all six providers on P5, 4 samples, with `--answer-note`: 24 units. The [P1 to P7 run](2026-11-06-psychomotor-p1-p7-results.md) of the same day is its baseline, at 18 of 24.

## Metrics and pass marks

1. **Baseline.** The control has 4 or more of 24 Gemini units at the cap.
2. **Cap.** The probe has 2 or fewer of 24 Gemini units at the cap.
3. **Passes.** Gemini passes in the probe are at least its passes in the control.
4. **Guard.** Sonnet passes 11 or more of 12.
5. **No give-away on P5.** No provider passes P5 2 or more units above the P1 to P7 run. A larger rise would mean that the note helps on more than the loop.
6. **Cost.** All four arms cost under 4 USD.

The note can become the default when marks 1 to 5 pass.

## Cost and stop rule

84 units at about 0.03 USD each cost about 2.5 USD. One round, then the write-up.
