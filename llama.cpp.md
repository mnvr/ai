# llama.cpp

C/C++ binary to run inference, even on CPUs.

See [README](https://github.com/ggml-org/llama.cpp/) for prebuilt binaries and GPU builds. For a simple CPU build:

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
