#!/bin/sh

curl 'https://ente.services.ai.azure.com/openai/v1/responses' \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5.1",
    "input": [
      {
        "role": "system",
        "content": [
          {
            "type": "input_text",
            "text": "You are an ancient oracle who speaks in cryptic but wise phrases, always hinting at deeper meanings."
          }
        ]
      },
      {
        "role": "user",
        "content": [
          {
            "type": "input_text",
            "text": "Tell me a joke"
          }
        ]
      }
    ]
  }'

exit 0

curl https://ente.services.ai.azure.com/anthropic/v1/messages \
  -H "Content-Type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-opus-4-1",
    "system": "You are an ancient oracle who speaks in cryptic but wise phrases, always hinting at deeper meanings.",
    "max_tokens": 9999,
    "messages": [ { "role": "user",  "content": "Tell me a joke" } ]
  }'
