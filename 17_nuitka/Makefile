# Minimal Nuitka Makefile
PYTHON := python3
SRC    := hello.py
TARGET := hello.dynamic
TARGET_STATIC := hello.static

all: $(TARGET)	$(TARGET_STATIC).static

$(TARGET): $(SRC)
	$(PYTHON) -m nuitka --static-libpython=no \
		--output-filename=$(TARGET) \
		$(SRC)

$(TARGET_STATIC):
	python3 -m nuitka --onefile --static-libpython=no --output-filename=$(TARGET_STATIC) hello.py

clean:
	rm -rf $(SRC:.py=.build) $(SRC:.py=.dist)
