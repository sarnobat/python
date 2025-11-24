import sys
import ctypes
import subprocess
from pathlib import Path

##
## ---- Call shared library ----
##
lib_path = Path(__file__).parent / "libhello.dylib"  # path to lib in same directory as script
lib = ctypes.CDLL(str(lib_path))                     # load the shared library at runtime
lib.greet.argtypes = [ctypes.c_char_p]               # declare greet() argument types for ctypes

print("[trace]\ttest.py calling dylib", file=sys.stderr)
lib.greet(b"Sridhar3")                                # call greet() with a bytes (C char*) argument

##
## ---- Call native executable ----
##
exe_path = Path(__file__).parent / "hello"

print("[trace]\ttest.py calling executable", file=sys.stderr)

result = subprocess.run(
    [str(exe_path), "Chinnu"],   # shell command + arg, executed without a shell
    capture_output=True,         # capture stdout and stderr instead of printing to console
    text=True                    # return stdout/stderr as strings instead of bytes
)

# Print executable output exactly as produced
sys.stdout.write(result.stdout)
sys.stderr.write(result.stderr)
