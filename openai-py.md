# OpenAI Python SDK

Install the OAI SDK

```sh
pip install openai
```

## Pre-flight check

**`pre-flight.py`**

```py
from openai import OpenAI

client = OpenAI(
  base_url="https://ente.services.ai.azure.com/openai/v1"
)

print(client.models.list())
```

```sh
python3 pre-flight.py
```

## Hello, World!

**`responses-hello.py`** and onwards.

## Env vars

The SDK automatically uses

- `OPENAI_API_KEY`
- `OPENAI_BASE_URL`

```sh
export OPENAI_API_KEY=xxx
export OPENAI_BASE_URL=https://ente.services.ai.azure.com/openai/v1
```

```py
from openai import OpenAI

client = OpenAI()

print(client.models.list())
```

> [!NOTE]
>
> Setting both causes codex to also use these instead of using the subscription (it is fine to set the API key tho, that alone when present does not cause codex to override the sub).
