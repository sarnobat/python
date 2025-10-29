# --- Configuration ---
PFX        := /tmp/pyout
PYMAJMIN   := 3.12
PYTHON     := $(PFX)/bin/python$(PYMAJMIN)
NUITKA     := $(PYTHON) -m nuitka

# The source script and output binary
SCRIPT     := hello.py
OUTBIN     := hello_embedded

# Static library name (copied for clarity and caching)
LIBA       := libpython$(PYMAJMIN).a

# --- Targets ---

all: $(OUTBIN)
	@echo "Built with Nuitka successfully:"
	@./$(OUTBIN)

# Build the Nuitka binary using the locally copied static lib
$(OUTBIN): $(SCRIPT) $(PYTHON) $(LIBA)
	$(NUITKA) --onefile \
	           --output-filename=$(OUTBIN) \
	           --static-libpython=yes \
	           --remove-output \
	           $(SCRIPT)

# Copy static lib from built Python into current dir
$(LIBA): $(PYTHON)
	@echo "Copying static libpython from $(PFX) ..."
	cp -f $(PFX)/lib/libpython$(PYMAJMIN).a $(LIBA)
	@echo "Done: $(LIBA)"

# Build static Python (if missing)
$(PYTHON):
	@echo "Building static Python under $(PFX)..."
	@mkdir -p $(PFX)
	@cd /tmp && { \
		ls Python-$(PYMAJMIN).5.tgz || \
		curl -LO https://www.python.org/ftp/python/$(PYMAJMIN).5/Python-$(PYMAJMIN).5.tgz; \
		tar xf Python-$(PYMAJMIN).5.tgz; \
		cd Python-$(PYMAJMIN).5; \
		./configure \
			--prefix="$(PFX)" \
			--disable-shared \
			--without-ensurepip \
			--enable-optimizations; \
		make -j$$(sysctl -n hw.ncpu); \
		make install; \
	}

# Clean generated artifacts
clean:
	rm -rf $(OUTBIN) $(LIBA) build dist *.build *.dist *.bin __pycache__
