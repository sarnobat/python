#!/usr/bin/env python3
import numpy as np
import ctypes
import objc
from Cocoa import *
from Metal import *

# -------------------------------
# 1) GPU kernel as a multiline string
# -------------------------------
metal_source = """
#include <metal_stdlib>
using namespace metal;

kernel void multiply_by_factor(
    device const float* in       [[ buffer(0) ]],
    device float* out            [[ buffer(1) ]],
    constant float& factor       [[ buffer(2) ]],
    uint id                      [[ thread_position_in_grid ]]
){
    out[id] = in[id] * factor;
}
"""

# -------------------------------
# 2) Host-side Python data
# -------------------------------
input_list = [
    0, 1, 0, 1, 1, 0, 0, 1,
    1, 1, 0, 0, 1, 0, 1, 0
]
factor = np.array([3], dtype=np.float32)

inp = np.array(input_list, dtype=np.float32)
out = np.zeros_like(inp)

# -------------------------------
# 3) Metal setup
# -------------------------------
device = MTLCreateSystemDefaultDevice()
if device is None:
    raise RuntimeError("No Metal device found. Are you on Apple Silicon?")

# Compile the kernel
library, error = device.newLibraryWithSource_options_error_(metal_source, None, None)
if library is None:
    raise RuntimeError(f"Metal compile error: {error}")

kernel = library.newFunctionWithName_("multiply_by_factor")
pipeline, error = device.newComputePipelineStateWithFunction_error_(kernel, None)
if pipeline is None:
    raise RuntimeError(f"Pipeline creation error: {error}")

command_queue = device.newCommandQueue()
command_buffer = command_queue.commandBuffer()
encoder = command_buffer.computeCommandEncoder()

# -------------------------------
# 4) GPU buffers
# -------------------------------
in_buf  = device.newBufferWithBytes_length_options_(inp,  inp.nbytes, 0)
out_buf = device.newBufferWithBytes_length_options_(out, out.nbytes, 0)
fac_buf = device.newBufferWithBytes_length_options_(factor, factor.nbytes, 0)

encoder.setComputePipelineState_(pipeline)
encoder.setBuffer_offset_atIndex_(in_buf,  0, 0)
encoder.setBuffer_offset_atIndex_(out_buf, 0, 1)
encoder.setBuffer_offset_atIndex_(fac_buf, 0, 2)

# -------------------------------
# 5) Dispatch GPU kernel
# -------------------------------
threads = MTLSizeMake(len(inp), 1, 1)
encoder.dispatchThreads_threadsPerThreadgroup_(threads, MTLSizeMake(1,1,1))
encoder.endEncoding()

command_buffer.commit()
command_buffer.waitUntilCompleted()

# -------------------------------
# 6) Read results back (PyObjC-safe)
# -------------------------------
length = out_buf.length()
ptr = out_buf.contents()
buf_ptr = ctypes.cast(ptr, ctypes.POINTER(ctypes.c_float))
result = np.ctypeslib.as_array(buf_ptr, shape=(len(inp),))

# -------------------------------
# 7) Print
# -------------------------------
print("Input:  ", input_list)
print("Output: ", result.astype(int).tolist())
