#!/usr/bin/env bash
# Give the GitLab evaluate job a Doppler service token that reads the config
# dev of cast-and-bloom. The token goes from Doppler straight into the GitLab
# variable DOPPLER_TOKEN through a pipe, so it never shows on the screen or in
# the shell history. Run it from main/bin.
set -euo pipefail

PROJECT=cast-and-bloom
CONFIG=dev
TOKEN_NAME=gitlab-ci-evaluate
GITLAB_PROJECT=thecastandbloomgroup/private/agent-operating-rules

if ! doppler secrets --project "$PROJECT" --config "$CONFIG" --only-names | grep -q PERPLEXITY_TOKEN; then
  echo "PERPLEXITY_TOKEN is not in $PROJECT/$CONFIG. Add it in the Doppler dashboard, then run this again." >&2
  exit 1
fi

if glab variable get DOPPLER_TOKEN --repo "$GITLAB_PROJECT" >/dev/null 2>&1; then
  echo "DOPPLER_TOKEN is already set in GitLab. Delete it first to replace it." >&2
  exit 1
fi

if ! doppler configs tokens create "$TOKEN_NAME" --project "$PROJECT" --config "$CONFIG" --plain |
  glab variable create DOPPLER_TOKEN --repo "$GITLAB_PROJECT" --protected --masked --hidden --raw >/dev/null; then
  echo "GitLab did not take the token. Revoking it in Doppler." >&2
  slug=$(doppler configs tokens --project "$PROJECT" --config "$CONFIG" --json |
    python3 -c 'import json, sys; print(next(t["slug"] for t in json.load(sys.stdin) if t["name"] == sys.argv[1]))' "$TOKEN_NAME")
  doppler configs tokens revoke --slug "$slug" --project "$PROJECT" --config "$CONFIG" >/dev/null || true
  exit 1
fi

echo "DOPPLER_TOKEN is set in GitLab: protected, masked and hidden."
