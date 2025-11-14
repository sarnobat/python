# ---- Configuration ----
CXX      := clang++
CXXFLAGS := -std=c++17 -O2 -fPIC
TARGET   := libhello.dylib
PYTHON   := python3

# ---- Default target ----
all: $(TARGET)	run

# ---- Build shared library ----
$(TARGET): hello.cpp
	$(CXX) $(CXXFLAGS) -shared -o $@ $<

# ---- Run Python script ----
run: $(TARGET)
	$(PYTHON) test.py

# ---- Clean ----
clean:
	rm -f $(TARGET)
