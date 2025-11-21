# Completion API

API Docs: <https://platform.openai.com/docs/api-reference/chat/create>

### Minimal

```sh
curl 'https://ente.openai.azure.com/openai/v1/chat/completions' \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o-mini",
    "messages": [
      {
        "role": "user",
        "content": "Tell me a joke"
      }
    ]
  }'
```

### Temperature

Sampling temperature, between 0 and 2, higher is more random. Default 1.

```sh
curl 'https://ente.openai.azure.com/openai/v1/chat/completions' \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o-mini",
    "temperature": 2,
    "messages": [
      {
        "role": "user",
        "content": "Tell me a joke"
      }
    ]
  }'
```

### Logprobs

Return log probabilities of each output token returned in the `content` of `message`. Top logprobs is an integer (0-20) specifying the number of most likely tokens to return at each token position.

```sh
curl 'https://ente.openai.azure.com/openai/v1/chat/completions' \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o-mini",
    "logprobs": true,
    "top_logprobs": 2,
    "messages": [
      {
        "role": "user",
        "content": "Tell me a joke"
      }
    ]
  }'
```

## Works with other models

### Mistral

Docs: <https://docs.mistral.ai/api>

Temperature for Azure deployments seems to be 1 by default.

```sh
curl 'https://ente.openai.azure.com/openai/v1/chat/completions' \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "mistral-small-2503",
    "messages": [
       {
         "role": "user",
         "content": "Tell me a joke"
       }
    ]
  }'
```
