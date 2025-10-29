# Minimal Nuitka Makefile
PYTHON := python3
SRC    := hello.py
TARGET_DYNAMIC := hello.dynamic
TARGET_STATIC := hello.static

all: $(TARGET)	$(TARGET_STATIC).static

$(TARGET_DYNAMIC): $(SRC)
	$(PYTHON) -m nuitka --static-libpython=no \
		--output-filename=$(TARGET_DYNAMIC) \
		$(SRC)

$(TARGET_STATIC):
	python3 -m nuitka --onefile --static-libpython=no --output-filename=$(TARGET_STATIC) hello.py

clean:
	rm -rf $(SRC:.py=.build) $(SRC:.py=.dist)
