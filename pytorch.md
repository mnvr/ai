# PyTorch

## Installation

```sh
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

The `--index-url` is required because the standard Python Package Index (PyPI) does not host pre-compiled binary packages (wheels) for PyTorch on all platforms and configurations.

```py
import torch

print(torch.rand(5, 3))
```

Prints a random 5x3 tensor.
