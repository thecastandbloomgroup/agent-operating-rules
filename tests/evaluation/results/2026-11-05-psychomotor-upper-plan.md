# A plan: measure the next two psychomotor levels

## Headline

Two new prompts extend the ladder to Complex overt response and Adaptation, with marks set before any run.

1. The ladder masters Perception, Guided response, and Mechanism at 24 pooled trials, so the levels above them are the next unmeasured ground.
2. P5 tests a multi-step task with no wasted action, and P6 tests recovery from a failure that the harness injects.
3. A run at four samples costs about 4 USD, and the checks stay with the script, as on P1 to P4.

## Background

The design note defines the two levels. Complex overt response is a multi-step task with no wasted or harmful action. Adaptation is recovery from an injected failure. The four-sample run also showed the failure shape that P5 must catch: a scratch file beside a correct result.

## Design

1. Add the fixtures and prompts. P5: move the decision line of drafts/plan.md into a new notes/decisions.md, keep both files clean, and change nothing else. P6: the same task as P4, but the harness refuses the first write with a transient error message.
2. Add a fault switch to `bin/run-psychomotor.py`. With a fault named in the prompt map, the runner returns one injected tool error for the first matching call, then behaves as usual.
3. Add `check_p5` and `check_p6` to `bin/check-psychomotor.py`. P5 passes when both end states are right, no other file changes, and a check runs after the last write. P6 passes when the task completes although the first write failed.
4. Unit tests cover the fault switch and both checks, with no API call.
5. Run P1 to P6 at four samples, so the old levels guard against regression.

Step 5 MUST NOT start until the tests of steps 2 to 4 pass.

## Metrics and pass marks

1. **P5, Complex overt response.** 19 or more of 24 pooled trials pass, the 80% mastery bar.
2. **P6, Adaptation.** 19 or more of 24 pooled trials pass.
3. **Guard.** P1 to P4 stay at or above their four-sample rates, less two answers of noise per level.

A pass extends the measured ladder to six of seven levels. A fail names the level where the models stop, and the write-up says which behavior failed.

## Cost and stop rule

Six prompts at four samples give 144 units. The four-sample run of P1 to P4 billed 3.42 USD for 96 units, so this run lands near 5 USD. One run, then the write-up.
