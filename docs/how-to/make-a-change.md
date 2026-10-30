# How to make a change

The branch `main` takes changes only through a merge request. Nobody can push to it. GitLab merges a request only when its pipeline passes. Then the push mirror copies `main` to GitHub.

## Before you start

You need `git`, Task, uv, and the GitLab CLI `glab`, signed in to the project. The [run the checks](run-the-checks.md) page lists the versions.

## Steps

1. Update `main`, and make a branch from it:

   ```sh
   git switch main
   git pull --ff-only
   git switch -c <branch>
   ```

2. Make the change, and run `task ci`. Fix each failure.

3. Commit the change. The subject of each commit MUST be a Conventional Commit, for example `fix(checks): find the References list under any heading`. The [release guide](release-a-version.md) lists the types. Check the subjects:

   ```sh
   task commits
   ```

   Push the branch:

   ```sh
   git push -u origin <branch>
   ```

4. Open a merge request to `main`:

   ```sh
   glab mr create --target-branch main --remove-source-branch --fill
   ```

5. Wait for the pipeline of the merge request. When it fails, fix the change, commit, and push again.

6. Merge the request with `glab mr merge`. GitLab uses a fast-forward merge, so `main` gets the commit that the pipeline tested.

## When the merge stops

GitLab refuses a fast-forward merge when `main` has a new commit. Rebase the branch on `main`, then push it again:

```sh
git fetch origin
git rebase origin/main
git push --force-with-lease
```

The new push starts a new pipeline. Merge when it passes.
