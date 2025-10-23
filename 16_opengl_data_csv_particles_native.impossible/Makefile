# Paths and versions
PFX       := /tmp/pyout
PYMAJMIN  := 3.12
INCDIR    := $(PFX)/include/python$(PYMAJMIN)
LIBA      := $(PFX)/lib/libpython$(PYMAJMIN).a
PYCONFIG  := $(PFX)/bin/python$(PYMAJMIN)-config

PY_SRC    := helloworld.py
PY_HEADER := helloworld_py.h
TARGET    := particles
C_SRC     := main.c

all: $(TARGET)

# Convert Python script to C header
$(PY_HEADER): $(PY_SRC)
	xxd -i $< > $@

# Build the executable
$(TARGET): $(C_SRC) $(PY_HEADER)
	clang -std=c11 -O2 -Wall \
	      -mmacosx-version-min=14.7 \
	      -I$(INCDIR) -I/opt/homebrew/include \
	      $(C_SRC) $(LIBA) \
	      $$($(PYCONFIG) --embed --ldflags) \
	      -L/opt/homebrew/lib -lglfw -framework OpenGL -lm \
	      -o $@

# Optional: build libpython3.12.a if not already present
$(LIBA):
	cd /tmp/Python-3.12.5 && \
	./configure --prefix=$(PFX) --disable-shared --without-ensurepip --enable-optimizations && \
	make && make install

# Optional: download Python source
/tmp/Python-3.12.5:
	cd /tmp && \
	{ test -f Python-3.12.5.tgz || curl -LO https://www.python.org/ftp/python/3.12.5/Python-3.12.5.tgz; } && \
	tar xf Python-3.12.5.tgz

clean:
	rm -f $(TARGET) $(PY_HEADER)
