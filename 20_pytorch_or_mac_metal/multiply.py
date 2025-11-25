from typing import List
from torch import Tensor
import torch
import sys
# --------------------------------------------------
# Use MPS GPU if available
device: torch.device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
print("Using:", device)

# -------------------------------------------------- Input
# Literal data: no loops
input_list = [
    0, 1, 0, 1, 1, 0, 0, 1,
    1, 1, 0, 0, 1, 0, 1, 0
]
# -------------------------------------------------- Factor
# Get factor from command line, default to 3
factor = int(sys.argv[1]) if len(sys.argv) > 1 else 3

# Move to GPU
x: Tensor = torch.tensor(input_list, dtype=torch.float32, device=device)

# -------------------------------------------------- Kernel
# GPU parallel multiply
y: Tensor = x * factor
# -------------------------------------------------- Result
# Convert to int before printing
# (-) Move the tensor from GPU memory to CPU memory
#     (because most Python operations (like list() or printing) cannot directly access GPU memory.)
# (-) Change the data type of the tensor from float32 to int32.
#     (because your original tensor is floating-point because GPU operations often prefer floats, but you want integer outputs like your Python list of 0s and 1s multiplied by the factor.)
output_list: List[int] = y.to("cpu").to(torch.int32).tolist()
# --------------------------------------------------
print("Input: ", input_list)
print("Factor:", factor)
print("Output:", output_list)
# --------------------------------------------------