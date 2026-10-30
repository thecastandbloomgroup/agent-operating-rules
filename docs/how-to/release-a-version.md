# How to release a new version

The version is in three places:

- `version.json`
- the version line at the top of `sources/model-operating-rules.md`
- a section of `CHANGELOG.md`

`task build` fails when they differ, or when the major version is not 0.

## Choose the version

The version follows Semantic Versioning 2.0.0 (<https://semver.org/spec/v2.0.0.html>). The major version stays at 0. Major version 0 is initial development, so any release MAY break the rules file, the scripts or the tests. Use this rule to pick the next version:

- A breaking change raises the minor version and sets the patch to 0, for example 0.3.2 to 0.4.0.
- Each other change raises the patch version, for example 0.3.0 to 0.3.1.

A change breaks when a user must change something to keep the same result. Examples: a new heading name in the rules, a moved output folder, or a new expected answer in the evaluation tests.

## Map each commit to the changelog

Each commit subject is a Conventional Commit 1.0.0 (<https://www.conventionalcommits.org/en/v1.0.0/>). `task commits` checks the subjects of the branch, and the review stage runs it. The type of each commit gives the section of the changelog:

| Commit type                                       | Section of the changelog                        |
| ------------------------------------------------- | ----------------------------------------------- |
| `feat`                                            | Added                                           |
| `fix`                                             | Fixed                                           |
| any type with `!`, or a `BREAKING CHANGE:` footer | Changed, with **Breaking:** first               |
| `refactor`, `perf`                                | Changed, when a user can see the change         |
| `docs`, `test`, `build`, `ci`, `style`, `chore`   | none, unless a user can see the change          |
| `revert`                                          | Removed, or the section of the change it undoes |

Use Deprecated, Removed and Security from Keep a Changelog 1.1.0 (<https://keepachangelog.com/en/1.1.0/>) when a change fits them.

## Steps

1. List the commits since the last tag: `git log --oneline v<last version>..HEAD`.
2. Choose the new version with the rule above.
3. Change `version.json`. It holds the parts of the version, not one string.
4. Change the version line of `sources/model-operating-rules.md`, for example `Version 0.4, 2026-11-02.` Leave out a patch part of 0. So version 0.4.0 is `Version 0.4`, and version 0.4.1 is `Version 0.4.1`.
5. In `CHANGELOG.md`, move the entries of `[Unreleased]` into a new section `## [<version>] - <date>`. Add an entry for each commit with the map above, and add the compare link of the version at the end of the file.
6. Run `task ci`, and fix each failure.
7. Merge the change through a merge request, as the [make a change](make-a-change.md) page shows. The package job of the pipeline makes `dist/agent-operating-rules-<version>.zip`.
8. Tag the merged commit with `git tag -a v<version> -m v<version>`, and push the tag with `git push origin v<version>`. The compare links of the changelog use the tags.
