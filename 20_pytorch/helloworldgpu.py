# install: /Users/sarnobat/.pyenv/shims//python3 -m pip install torch

import torch

device = "mps"

x = torch.arange(10_000_000, device=device, dtype=torch.float32)
y = x * 2
print(y[:10])
