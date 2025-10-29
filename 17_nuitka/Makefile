# Minimal Nuitka Makefile
PYTHON := python3
SRC    := hello.py
TARGET := hello.dynamic

all: $(TARGET)

$(TARGET): $(SRC)
	$(PYTHON) -m nuitka --static-libpython=no $(SRC)

clean:
	rm -rf $(TARGET) $(SRC:.py=.build) $(SRC:.py=.dist)
