import torch

# Use MPS GPU if available
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
print("Using:", device)

# Literal data: no loops, no random generation
input_list = [
    0, 1, 0, 1, 1, 0, 0, 1,
    1, 1, 0, 0, 1, 0, 1, 0
]

factor = 3

# Move list to MPS GPU
x = torch.tensor(input_list, dtype=torch.float32, device=device)

# GPU-parallel multiply
y = x * factor    # runs on Apple GPU (MPS)

# Bring back to CPU for printing
output_list = y.to("cpu").tolist()

print("Input: ", input_list)
print("Output:", output_list)
