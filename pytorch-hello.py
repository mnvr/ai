import torch

print("Torch:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())

x = torch.rand(5, 3)
print(x)
