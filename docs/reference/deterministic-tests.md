# Deterministic tests

`bin/deterministic-tests.py` tests one Markdown file against the rules that have a fixed expected result. It reads the banned words from `sources/banned-words.txt`.

```sh
python3 bin/deterministic-tests.py FILE [--instructions] [--check]
```

| Option           | Effect                                                                          |
| ---------------- | ------------------------------------------------------------------------------- |
| `--instructions` | Use the limit of 20 words for each sentence. Without it, the limit is 25 words. |
| `--check`        | Add the list `failures` to the report. Exit with 1 when the list has an entry.  |

Without `--check`, the script prints the report and exits with 0.

## Report fields

| Field                             | Content                                                                                               | A failure with `--check` when |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------- |
| `long_sentences`                  | Line, word count and start of each sentence over the limit (4.1.1)                                    | the list has an entry         |
| `dashes`                          | Each line with an em dash or an en dash (4.3.1)                                                       | the list has an entry         |
| `banned`, `banned_total`          | The hits of each category of `banned-words.txt` (4.2.3, 4.2.6, 4.4)                                   | the total is more than 0      |
| `nominalizations`                 | Each noun phrase that has a verb form (4.2.4)                                                         | the list has an entry         |
| `gerund_nouns`                    | Each gerund used as a noun (4.1.6)                                                                    | the list has an entry         |
| `passive_count`, `passive_sample` | The count of passive forms, and up to 8 of them (4.1.2)                                               | never                         |
| `fk_grade`, `flesch_ease`         | The Flesch-Kincaid grade and reading ease (4.1.7). Both are `null` for a page with no prose sentence. | the grade is more than 10     |
| `citation_order_ok`               | The citations are numbered in order of first use (5.4.1)                                              | false                         |
| `multi_citation_lines`            | Each line with more than one citation (5.4.1)                                                         | the list has an entry         |
| `refs_blank_line_separated`       | A blank line separates the reference entries (5.4.1)                                                  | false                         |
| `refs_untagged`                   | Each reference with no P, S, T or U tag (5.4.5)                                                       | the list has an entry         |
| `refs_uncited`                    | Each reference that the text does not cite                                                            | the list has an entry         |
| `cites_unlisted`                  | Each citation with no reference entry                                                                 | the list has an entry         |

The passive voice is a count and never a failure, because rule 4.1.2 allows it when the agent is unknown or irrelevant.

The grade reads only the prose sentences that the sentence test reads. So a table row does not count as one long sentence.

## Exemptions

The script skips headings, code blocks, table rows, and lines that start with `[` or `<`. A banned word in quotes is not a hit, so a page can name a banned word as an example. The script reads `very likely` and `very unlikely` as IPCC terms, not as boosters.
