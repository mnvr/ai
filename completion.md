# Continuation

Base models that provide raw token completion and continuation instead of having an assistant persona trained-in.

## Using llama.cpp

1. llama-server + "/completion"
2. llama-completion + "-no-cnv"

Needs a base model (e.g. "ggml-org/gemma-3-1b-pt-GGUF", "ggml-org/gemma-3-270m-GGUF").

```sh
llama-completion -hf ggml-org/gemma-3-1b-pt-GGUF --seed 24 -p "I am a" -n 24
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

`--interactive` mode - `Ctrl-C` to interrupt the model any time, inject the next token, and resume completion.

```sh
llama-completion -hf ggml-org/gemma-3-1b-pt-GGUF -p "Once upon a time" -i
```

llama-completion [has a lot of parameters](https://github.com/ggml-org/llama.cpp/blob/master/tools/completion/README.md) controlling which tokens are sampled.

## Using Transformers

```py
from transformers import pipeline, set_seed
generator = pipeline('text-generation', model='gpt2')
set_seed(1773)
seqs = generator("Hello!", max_new_tokens=20, num_return_sequences=5)
print(*[s['generated_text'] for s in seqs], sep='\n')
```

`num_return_sequences` is great for rolling multiple dies in one go.

See also [transformers.md](transformers.md)
