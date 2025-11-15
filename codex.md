# Configuring Codex

Modify `~/.codex/config.toml`

```toml
model = "gpt-5.1-codex"

[profiles.api]
model_provider = "azure"
# Optional (use a specific model for this profile)
# model = "gpt-5.1"

[profiles.pro]
model_provider = "azure"
model = "gpt-5-pro"
model_reasoning_effort = "high"

[model_providers.azure]
name = "API"
base_url = "https://ente.openai.azure.com/openai/v1"
env_key = "OPENAI_API_KEY"
```

Then use with

```sh
codex --profile api
codex --profile api --model gpt-5.1
codex --profile pro
```
