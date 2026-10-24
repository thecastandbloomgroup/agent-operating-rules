# How to set up the GitHub mirror

The mirror job of the pipeline pushes `main` to the public repository `thecastandbloomgroup/agent-operating-rules` on GitHub. It runs only on `main`, after every other stage passes. Do these steps one time.

## Before you start

You need the GitHub CLI `gh` and the GitLab CLI `glab`, each signed in to an account that can change the repository settings. You also need `ssh-keygen`.

## Steps

1. Create an empty public repository on GitHub with the name above. Do not add a README, because the first push needs an empty repository.
2. Make a key pair with no passphrase: `ssh-keygen -t ed25519 -N '' -f ~/.ssh/agent-operating-rules-mirror`.
3. Add the public key to the GitHub repository as a deploy key with write access. The deploy key can push to this one repository only.
4. Add the private key to the GitLab project as a CI variable with the name `GITHUB_MIRROR_KEY`. Set its type to File, and make it protected. Then only the protected branch `main` gets the key.
5. Run the pipeline on `main`. The mirror job prints the result of `git push`.

## Change or remove the key

Delete the deploy key on GitHub, and delete the variable on GitLab. Then the mirror job fails, and no other job changes. Do the steps 2 to 4 again for a new key.

## Why the job checks the host key of GitHub

The file `.github-known-hosts` holds the public host key that GitHub publishes. So ssh refuses a server that is not GitHub.
