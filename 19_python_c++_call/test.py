import sys
import ctypes
import subprocess
from pathlib import Path

#base = Path(__file__).parent

# ---- Call shared library ----
lib_path = Path(__file__).parent / "libhello.dylib"
lib = ctypes.CDLL(str(lib_path))
lib.greet.argtypes = [ctypes.c_char_p]

print("[trace]\ttest.py calling dylib", file=sys.stderr)
lib.greet(b"Sridhar")

# ---- Call native executable ----
exe_path = Path(__file__).parent / "hello"

print("[trace]\ttest.py calling executable", file=sys.stderr)

result = subprocess.run(
    [str(exe_path), "Sridhar"],
    capture_output=True,
    text=True
)

# Print executable output exactly as produced
sys.stdout.write(result.stdout)
sys.stderr.write(result.stderr)
