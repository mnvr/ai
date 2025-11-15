# Zero to OpenAI API in 30 minutes

API Endpoint: https://ente.openai.azure.com/openai/

Source this in your bashrc or before running the commands.

```sh
export OPENAI_API_KEY=xxx
```

OpenAI's SDK uses the env var named OPEN_AI_KEY by default.

## Pre-flight check

```sh
curl 'https://ente.openai.azure.com/openai/v1/models' -H "Authorization: Bearer $OPENAI_API_KEY"
```

API Reference: https://platform.openai.com/docs/api-reference/

## Hello World

```sh
curl 'https://ente.openai.azure.com/openai/v1/responses' \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"model": "gpt-5.1", "input": "Hello, world!"}'
```

## Text input

```sh
curl 'https://ente.openai.azure.com/openai/v1/responses' \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gpt-5.1",
    "input": [
      {
        "role": "user",
        "content": [
          {"type": "input_text", "text": "Tell me a joke"}
        ]
      }
    ]
  }'
```
