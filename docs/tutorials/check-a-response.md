# Check the first response of a model

In this tutorial you install the rules on one model. Then you send one prompt and test the response with a script. It takes about 15 minutes.

You need:

- Python 3.10 or later.
- An account with one LLM provider that accepts a system prompt.

## 1. Install the rules

Open the settings of your model. Find the field for the system prompt. Paste the full text of `sources/model-operating-rules.md` into that field. Save the settings.

## 2. Send one prompt

Open `tests/evaluation/evaluation-tests.md`. Copy prompt C1 from Section 1. Send it to the model in a new conversation.

## 3. Save the response

Make a folder for the model in `tests/evaluation/results/`, for example `tests/evaluation/results/model-a/`. Save the response as `C1.md` in that folder.

## 4. Test the response

Run this command from the root of the repository:

```sh
python3 bin/deterministic-tests.py --check tests/evaluation/results/model-a/C1.md
```

The script prints one JSON report. The list `failures` names each test that the response fails. An empty list means that the response passes each deterministic test. The exit code is 0 for a pass and 1 for a fail.

## 5. Read the report

Look at `long_sentences`, `dashes` and `banned` first. Each entry gives the line number and the start of the text. So you can find each problem in the response. The [deterministic tests](../reference/deterministic-tests.md) page explains each field.

## Next step

The deterministic tests do not grade the judgment rules of Sections 6.4 and 6.5. Two graders score those with a rubric. Follow [record an evaluation run](../how-to/record-an-evaluation-run.md).
