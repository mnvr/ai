# OpenAI Python SDK

Requirements:

- Python 3

Some distros remove venv from the default install; need something like `python3-venv`.

```sh
python3 -m venv .venv && source .venv/bin/activate
```

Install the OAI SDK

```sh
pip install openai
```

## Pre-flight check

**`pre-flight.py`**

```py
from openai import OpenAI

client = OpenAI(
  base_url="https://ente.openai.azure.com/openai/v1"
)

print(client.models.list())
```

```sh
python3 pre-flight.py
```

## Hello, World!

**`hello.py`** and onwards.
