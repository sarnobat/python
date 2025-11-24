import torch
import sys

# Use MPS GPU if available
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
print("Using:", device)

# Literal data: no loops
input_list = [
    0, 1, 0, 1, 1, 0, 0, 1,
    1, 1, 0, 0, 1, 0, 1, 0
]

# Get factor from command line, default to 3
factor = int(sys.argv[1]) if len(sys.argv) > 1 else 3

# Move to GPU
x = torch.tensor(input_list, dtype=torch.float32, device=device)

# GPU parallel multiply
y = x * factor

# Convert to int before printing
output_list = y.to("cpu").to(torch.int32).tolist()

print("Input: ", input_list)
print("Factor:", factor)
print("Output:", output_list)
