# llama.cpp

C/C++ binary to run inference, on CPUs and GPUs.

# Installing

## macOS

```sh
brew install llama.cpp
```

## Building from source.

See [README](https://github.com/ggml-org/llama.cpp/) for prebuilt binaries and GPU builds. 

For a simple CPU build:

```sh
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp
cmake -B build
cmake --build build -j 6
```

Deps on Fedora:

```sh
dnf install cmake
dnf install libcurl-devel # OR cmake -B build -DLLAMA_CURL=OFF
```

Using:

```sh
llama-cli -hf LiquidAI/LFM2-700M-GGUF # downloads hf user/model
./build/bin/llama-cli -m model.gguf # interactive conversation
llama-server -m model.gguf # OpenAI-compatible API on port 8080
```

For base model semantics, see [completion.md](completion.md).

# Using 

## Local Server

```sh
llama-server -hf ggml-org/gemma-3-270m-it-GGUF
```

## Showing already downloaded models

`--cache-list`

```sh
llama-cli -cl
```

## CLI chat

Requires a instruct tuned model with a chat template.

```sh
llama-cli -hf ggml-org/gemma-3-270m-it-GGUF
```

## Token completion

Works best with a base model.

```sh
llama-completion -hf ggml-org/gemma-3-270m-GGUF -p '// Quicksort in JS:'
```

## Interactive token completion

`--interactive` allows `Ctrl-C` to interrupt the model any time, inject the next token, and resume completion.

By default, the model starts sampling immediately, and the prompt passed via `-p` is ignored. So functionally, the (currently undocumented) `--interactive-first` is needed.

```sh
llama-completion -hf ggml-org/gemma-3-270m-GGUF --interactive-first
```

## Use a specific quantization

The `-hf` flag takes an optional `:quant`. Defaults to `Q4_K_M` or first file.

```sh
llama-completion -hf 'Qwen/Qwen3-32B-GGUF:Q6_K' --interactive-first
```