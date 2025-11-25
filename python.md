# Python

## Setup

Requirements:

- Python 3

Some distros remove venv from the default install; need something like `python3-venv`.

```sh
python3 -m venv .venv && source .venv/bin/activate
```

## requirements.txt

There isn't a way in vanilla to both install a package and add it to reqs. Simplest might be to `pip install openai` and then:

```sh
pip freeze | grep openai >>requirements.txt
```

```sh
pip install -r requirements.txt
```

The file can be named anything. Also, to upgrade already installed packages, use `-U`.

```sh
pip install --upgrade -r requirements-nb.txt
```
