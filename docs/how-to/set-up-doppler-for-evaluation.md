# How to set up Doppler for the evaluation

Doppler holds the Perplexity API key. GitLab holds only a Doppler service token, which can read one Doppler config and change nothing. The evaluate job runs `doppler run`, which gives the key to the evaluation task alone. Do these steps one time.

## Before you start

You need:

- A Doppler account, and the Doppler CLI on your machine from <https://docs.doppler.com/docs/install-cli>.
- A Perplexity API key from the API settings of Perplexity. A Pro or Max plan does not include API use, so the API account needs its own credit.
- The Maintainer role on the GitLab project, and the GitLab CLI `glab`.

## Put the key in Doppler

1. Sign in with `doppler login`.
2. Make the project: `doppler projects create agent-operating-rules`. Doppler gives it the configs `dev`, `stg` and `prd`.
3. In the Doppler dashboard, open the project, then the config `prd`. Add the secret `PERPLEXITY_API_KEY` with the key as its value. GitLab reads this config.
4. Add the same secret to the config `dev`. Your machine reads this config. You can use a second Perplexity key here, so you can stop one key without the other.

Use the dashboard for the value, not a command line. A command line keeps the key in the history of your shell.

## Give GitLab a service token

1. Make a service token that reads the config `prd`:

   ```sh
   doppler configs tokens create gitlab-ci --project agent-operating-rules --config prd --plain
   ```

   The command prints the token one time. Copy it.

2. In the GitLab project, open **Settings**, then **CI/CD**, then **Variables**, and select **Add variable**.

3. Set the fields:

   | Field        | Value             |
   | ------------ | ----------------- |
   | Key          | `DOPPLER_TOKEN`   |
   | Value        | the token         |
   | Type         | Variable          |
   | Visibility   | Masked and hidden |
   | Flags        | Protect variable  |
   | Environments | All               |

   A protected variable goes only to pipelines of protected branches, so only `main` gets the token. A masked and hidden variable does not show in job logs or in the settings page.

## Check the setup

1. Open **Build**, then **Pipelines**, and open the last pipeline of `main`.
2. Find the stage **evaluate**. Select the job `evaluate: [anthropic]`.
3. Add two job variables: `PROMPTS` with the value `C1`, and `SAMPLES` with the value `1`. Then select **Run job**.
4. The job sends one prompt to one pair, for about 0.63 USD. When it ends, open the artifact `.eval/<run>/summary.md`. It names the failed calls, if any.

A 401 error means that the key in Doppler is wrong. A Doppler error about the token means that `DOPPLER_TOKEN` is wrong or not protected.

## Use Doppler on your machine

1. In the root of the repository, run `doppler setup --project agent-operating-rules --config dev`. Doppler keeps this choice for the folder in your home folder, not in the repository.
2. Run the evaluation through Doppler: `doppler run -- task eval:probe`.

## Change a key or a token

- To change the Perplexity key, change the secret in Doppler. GitLab needs no change.
- To change the service token, make a new one and put it in the GitLab variable. Then revoke the old one: `doppler configs tokens revoke gitlab-ci --project agent-operating-rules --config prd`.

## Why the job uses the Doppler CLI

Doppler can also copy its secrets into GitLab CI/CD variables. That sync needs a GitLab token with the scope `api`, kept in Doppler. That token can change any setting of the project. The sync also puts the Perplexity key itself in GitLab.

With the CLI, GitLab keeps only a token that reads one config. The key stays in Doppler, and each job reads it when it starts. The job installs the CLI from the signed Alpine repository of Doppler, and it checks the SHA-256 sum of the signing key first.

GitLab cannot mask `PERPLEXITY_API_KEY`, because it is not a GitLab variable. So `bin/run-evaluation.py` never prints the key, and no task prints its environment.
