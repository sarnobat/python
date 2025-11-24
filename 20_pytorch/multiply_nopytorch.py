#!/usr/bin/env python3
import numpy as np
from Cocoa import *
from Metal import *

# Minimal Metal kernel
metal_source = """
#include <metal_stdlib>
using namespace metal;
kernel void add_one(device float* data [[buffer(0)]], uint id [[thread_position_in_grid]]) {
    data[id] += 1;
}
"""

# Input data
data = np.array([0, 1, 2], dtype=np.float32)

# Metal setup
device = MTLCreateSystemDefaultDevice()
library, _ = device.newLibraryWithSource_options_error_(metal_source, None, None)
func = library.newFunctionWithName_("add_one")
pipeline, _ = device.newComputePipelineStateWithFunction_error_(func, None)

queue = device.newCommandQueue()
cmd_buf = queue.commandBuffer()
encoder = cmd_buf.computeCommandEncoder()

# GPU buffer
buf = device.newBufferWithBytes_length_options_(data, data.nbytes, 0)
encoder.setComputePipelineState_(pipeline)
encoder.setBuffer_offset_atIndex_(buf, 0, 0)

threads = MTLSizeMake(len(data), 1, 1)
encoder.dispatchThreads_threadsPerThreadgroup_(threads, MTLSizeMake(1,1,1))
encoder.endEncoding()

cmd_buf.commit()
cmd_buf.waitUntilCompleted()

# COPY buffer to NumPy safely — NO ctypes.cast
out = np.empty_like(data)
buf.getBytes_length_(out.ctypes.data, out.nbytes)

print("Result:", out.tolist())
