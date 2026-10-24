# How to release a new version

The version is in two places: `version.json`, and the version line at the top of `sources/model-operating-rules.md`. `task build` fails when the two differ.

1. Choose the new version with Semantic Versioning 2.0.0 (https://semver.org/spec/v2.0.0.html).
2. Change `version.json`. It holds the parts of the version, not one string.
3. Change the version line of `sources/model-operating-rules.md`, for example `Version 2.2, 2026-11-02.` Leave out a patch part of 0. So version 2.2.0 is `Version 2.2`, and version 2.2.1 is `Version 2.2.1`.
4. Run `task ci`, and fix each failure.
5. Commit the change and push it. The package job of the pipeline makes `dist/agent-operating-rules-<version>.zip`.
