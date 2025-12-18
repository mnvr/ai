# Continuation

Base models that provide raw token completion and continuation instead of having an assistant persona trained-in.

1. llama-server + "/completion"
2. llama-completion + "-no-cnv"

Needs a base model (e.g. "ggml-org/gemma-3-1b-pt-GGUF", "ggml-org/gemma-3-270m-GGUF").

```sh
llama-completion -hf ggml-org/gemma-3-1b-pt-GGUF --seed 24 --p "I am a" -n 24
```

or

```sh
llama-server -hf ggml-org/gemma-3-1b-pt-GGUF
```

```sh
curl 'http://localhost:8080/completions' -d '{"seed": 24, "prompt": "I am a", "n_predict": 24}' \
    | jq -r '.content'
```

Seed is optional.

Without capping the number of output tokens the model can get into a infinite generation mode with generic unconstrained prompts like the example above. Longer prompts help the model stop (for some seeds):

```sh
llama-completion -hf ggml-org/gemma-3-1b-pt-GGUF -s 1337 -p "a haiku about a topic I find hard to write a haiku about. hope you like it:"
```
