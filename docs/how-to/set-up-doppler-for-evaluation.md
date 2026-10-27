# How to set up Doppler for the evaluation

Doppler holds the Perplexity API key as the secret `PERPLEXITY_TOKEN` in the Doppler project `cast-and-bloom`. GitLab holds only a Doppler service token, which can read one Doppler config and change nothing. The evaluate job runs `doppler run --only-secrets PERPLEXITY_TOKEN`, which gives the key to the evaluation task alone. Do these steps one time.

## Before you start

You need:

- A Doppler account with access to the project `cast-and-bloom`, and the Doppler CLI on your machine from <https://docs.doppler.com/docs/install-cli>.
- A Perplexity API key from the API settings of Perplexity. A Pro or Max plan does not include API use, so the API account needs its own credit.
- The Maintainer role on the GitLab project, and the GitLab CLI `glab`.

## Put the key in Doppler

1. Sign in with `doppler login`.
2. In the Doppler dashboard, open the project `cast-and-bloom`, then the config `dev`. Add the secret `PERPLEXITY_TOKEN` with the key as its value. Your machine reads this config.
3. Add the same secret to the config `prd`. GitLab reads this config. You can use a second Perplexity key here, so you can stop one key without the other.

Use the dashboard for the value, not a command line. A command line keeps the key in the history of your shell.

To see that the secret is there without its value, run `doppler secrets --project cast-and-bloom --config prd --only-names`.

## Give GitLab a service token

1. Make a service token that reads the config `prd`:

   ```sh
   doppler configs tokens create gitlab-ci-evaluate --project cast-and-bloom --config prd --plain
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

A 401 error means that the key in Doppler is wrong. A Doppler error about the token means that `DOPPLER_TOKEN` is wrong or not protected. A Doppler error about a missing secret means that `PERPLEXITY_TOKEN` is not in the config `prd`.

## Use Doppler on your machine

1. In the root of the repository, run `doppler setup --project cast-and-bloom --config dev`. Doppler keeps this choice for the folder in your home folder, not in the repository.
2. Run the evaluation through Doppler: `doppler run --only-secrets PERPLEXITY_TOKEN -- task eval:probe`.

## Change a key or a token

- To change the Perplexity key, change the secret in Doppler. GitLab needs no change.
- To change the service token, make a new one and put it in the GitLab variable. Then revoke the old one: `doppler configs tokens revoke gitlab-ci-evaluate --project cast-and-bloom --config prd`.

## What the service token can read

The config `prd` of `cast-and-bloom` holds other secrets, such as Mailgun keys and a GitLab token. A service token reads the whole config, so the GitLab variable can read those secrets too. Two things limit this:

- `--only-secrets PERPLEXITY_TOKEN` puts only the key in the job. The other secrets do not reach the job or its log.
- Only pipelines of `main` get `DOPPLER_TOKEN`, and only a merge request changes `main`.

To limit the token itself, make a Doppler project that holds only `PERPLEXITY_TOKEN`, and make the service token there.

## Why the job uses the Doppler CLI

Doppler can also copy its secrets into GitLab CI/CD variables. That sync needs a GitLab token with the scope `api`, kept in Doppler. That token can change any setting of the project. The sync also puts the Perplexity key itself in GitLab.

With the CLI, GitLab keeps only a token that reads one config. The key stays in Doppler, and each job reads it when it starts. The job installs the CLI from the signed Alpine repository of Doppler, and it checks the SHA-256 sum of the signing key first.

GitLab cannot mask `PERPLEXITY_TOKEN`, because it is not a GitLab variable. So `bin/run-evaluation.py` never prints the key, and no task prints its environment.
