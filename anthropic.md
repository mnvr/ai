# Anthropic

Base URL: **https://ente.services.ai.azure.com/anthropic/**

```
export ANTHROPIC_API_KEY=xxx
```

## API

```sh
curl https://ente.services.ai.azure.com/anthropic/v1/messages \
  -H "Content-Type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-opus-4-1",
    "max_tokens": 1000,
    "messages": [
      {
        "role": "user",
        "content": "Tell me a joke"
      }
    ]
  }'
```

## Claude Code

Define the following env vars:

```sh
export ANTHROPIC_API_KEY=the-key-itself
export ANTHROPIC_BASE_URL=https://ente.services.ai.azure.com/anthropic
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-1
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-5
export ANTHROPIC_DEFAULT_HAIKU_MODEL=claude-haiku-4-5
```

Then test with

```sh
claude -p hello
```

Alternatively, you can also put them in `~/.claude/settings.json`

```json
{
  "env": {
    "ANTHROPIC_API_KEY": "the-key-itself",
    "ANTHROPIC_BASE_URL": "https://ente.services.ai.azure.com/anthropic",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "claude-opus-4-1",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "claude-sonnet-4-5",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "claude-haiku-4-5"
  }
}
```
