import ctypes

lib = ctypes.CDLL("./libhello.dylib")
lib.hello()
