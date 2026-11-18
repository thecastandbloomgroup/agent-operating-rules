# Results: the combined rule cuts against released rules 0.10, run the same day

## Headline

The combined cuts pass all four marks of the [plan](2026-11-18-rule-cuts-form-plan.md), against released rules 0.10 run the same day.

1. Answers with a false self-test line fell from 58.7% to 6.3%, so the fall of 52.4 points is far over the mark of 20.
2. Each of the seven script checks stayed within 10 points of the control, and the input tokens fell by 21.1%.
3. The two arms cost 7.01 USD, under the cap of 10 USD.

The machine-readable result is [2026-11-18-rule-cuts-form-result.json](2026-11-18-rule-cuts-form-result.json), written by `bin/score-arms.py`.

## Background

The person approved this one form-only run on 2026-11-18, to decide on the cuts. The plan and its marks were merged before the first paid call. Both arms ran on 2026-11-18 with the same six models, and no call failed.

## Results

| Mark | Control | Candidate | Difference, 95% interval | Pass |
| --- | --- | --- | --- | --- |
| False self-test lines fall by 20 points or more | 58.7% | 6.3% | -52.4 (-61.2 to -42.0) | yes |
| No long sentence, within 10 points | 46.8% | 38.1% | -8.7 (-20.5 to +3.4) | yes |
| No banned word, within 10 points | 84.9% | 82.5% | -2.4 (-11.6 to +6.8) | yes |
| No dash, within 10 points | 99.2% | 98.4% | -0.8 (-4.9 to +3.0) | yes |
| No first person outside End, within 10 points | 96.0% | 92.9% | -3.2 (-9.5 to +2.8) | yes |
| Structure, within 10 points | 88.1% | 88.9% | +0.8 (-7.3 to +8.9) | yes |
| Every action labelled, within 10 points | 84.9% | 88.9% | +4.0 (-4.5 to +12.5) | yes |
| Every label with a reason, within 10 points | 76.2% | 80.2% | +4.0 (-6.3 to +14.1) | yes |
| Input tokens fall by 10% or more | 5,726 | 4,517 | -21.1% | yes |
| Both arms under 10 USD | 3.76 USD | 3.26 USD | 7.01 USD | yes |

Each arm has 126 answers. The intervals are Newcombe intervals of the difference of two rates.

## Agreement with the run of 2026-11-07

The run of 2026-11-07 gave the same picture. False lines fell from 59.5% to 7.1%, and the input tokens fell by 21.5%.

One check moved. The share with no long sentence fell by 8.7 points, against a rise of 0.8 points on 2026-11-07. The point value passes the mark of 10, but the interval reaches -20.5 points. So a fall in this check of up to 20 points cannot be ruled out at this sample size.

## Limits

The run has no judge, so it does not measure the quality of judgment. A pass means only that no script check fell by more than its mark, and that the two costs fell.

## Next

The person decides on the cuts from this result. If the person approves them, the cuts ship from the kit, and no file in `sources/` changes here.
