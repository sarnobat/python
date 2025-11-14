import ctypes
from pathlib import Path


lib_path = Path(__file__).parent / "libhello.dylib"
lib = ctypes.CDLL(str(lib_path))
lib.greet.argtypes = [ctypes.c_char_p]

print("[trace]	test.py  ")
lib.greet(b"Sridhar")
