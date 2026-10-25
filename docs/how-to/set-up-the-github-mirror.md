# How to set up the GitHub mirror

The push mirror of GitLab copies the protected branch `main` to the public repository `thecastandbloomgroup/agent-operating-rules` on GitHub. No CI job pushes, so the mirror uses no CI minutes. Do these steps one time.

## Before you start

You need the Maintainer role on the GitLab project. You need the GitHub CLI `gh` and the GitLab CLI `glab`, each signed in to an account that can change the repository settings.

The GitLab project ID is `88006393`. The API page of GitLab is <https://docs.gitlab.com/api/remote_mirrors/>.

## Steps in the GitLab UI

1. Create an empty public repository on GitHub with the name above. Do not add a README, because the first push needs an empty repository.
2. In the GitLab project, open **Settings**, then **Repository**, then **Mirroring repositories**.
3. For **Git repository URL**, enter `ssh://git@github.com/thecastandbloomgroup/agent-operating-rules.git`. GitLab refuses the short form `git@github.com:...`.
4. For **Mirror direction**, select **Push**.
5. Select **Detect host keys**. Compare each fingerprint with the list at <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints>. Stop when one differs.
6. For **Authentication method**, select **SSH public key**.
7. Select **Mirror only protected branches**, then select **Mirror repository**.
8. Select **Copy SSH public key** on the new mirror. Add the key to the GitHub repository as a deploy key with write access.
9. Select **Update now**. The mirror shows the time of the last good update, or the error.

## Steps with the API

The steps make the mirror with `enabled` false, because GitHub refuses each push until it has the key.

1. Get the host keys of GitHub, and compare their fingerprints with the list above:

   ```sh
   gh api meta --jq '.ssh_keys[]' | sed 's/^/github.com /' > github-host-keys
   ssh-keygen -lf github-host-keys
   ```

2. Make the mirror. The file `mirror.json` holds the URL, the auth method `ssh_public_key`, `enabled` false, `only_protected_branches` true, and each line of `github-host-keys` in the list `host_keys`:

   ```sh
   glab api -X POST projects/88006393/remote_mirrors -H 'Content-Type: application/json' --input mirror.json
   ```

3. Get the public key of the mirror, and add it to GitHub as a deploy key with write access. Use the mirror `id` from step 2:

   ```sh
   key=$(glab api projects/88006393/remote_mirrors/<id>/public_key | jq -r .public_key)
   gh api -X POST repos/thecastandbloomgroup/agent-operating-rules/keys -f title='GitLab push mirror' -f key="$key" -F read_only=false
   ```

4. Turn the mirror on, and push one time:

   ```sh
   glab api -X PUT projects/88006393/remote_mirrors/<id> -F enabled=true
   glab api -X POST projects/88006393/remote_mirrors/<id>/sync
   ```

5. Check the result. `update_status` is `finished` and `last_error` is empty after a good push:

   ```sh
   glab api projects/88006393/remote_mirrors/<id>
   ```

## Keep untested commits off GitHub

The mirror pushes each new commit of `main` in about one minute. It does not wait for the pipeline. So `main` must get only commits that passed CI. Set these in the GitLab project:

1. In **Settings**, then **Repository**, then **Protected branches**, set **Allowed to push and merge** of `main` to **No one**. Keep **Allowed to merge** at **Maintainers**.
2. In **Settings**, then **Merge requests**, set **Merge method** to **Fast-forward merge**. Then `main` gets the same commit that the pipeline of the merge request tested.
3. In the same page, select **Pipelines must succeed**.

## Change the key or the host keys

GitLab keeps the private key of the mirror in its database, and only a Maintainer sees the mirror settings. To get a new key, delete the mirror and make it again. Then delete the old deploy key on GitHub.

When GitHub changes a host key, the mirror fails with a host key error. Get the new keys and check their fingerprints, as in step 1 of the API steps. Then send them in `host_keys` with `PUT` to the mirror.
