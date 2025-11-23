# Python

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
