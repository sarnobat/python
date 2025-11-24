# ---- Configuration ----
CXX      := clang++
CXXFLAGS := -std=c++17 -O2 -fPIC
TARGET   := libhello.dylib
EXE      := hello
PYTHON   := python3

# ---- Default target ----
all: $(TARGET) $(EXE) run

# ---- Build shared library ----
$(TARGET): hello.cpp
	$(CXX) $(CXXFLAGS) -shared -o $@ $<

# ---- Build executable ----
$(EXE): hello.cpp
	$(CXX) $(CXXFLAGS) -o $@ $<

# ---- Run Python script ----
run: $(TARGET)
	$(PYTHON) test.py

# ---- Clean ----
clean:
	rm -f $(TARGET) $(EXE)
