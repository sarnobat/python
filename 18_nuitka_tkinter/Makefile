# ------------------------------------------------------------
# Optimized static Python + Nuitka single-file build
# ------------------------------------------------------------

PYMAJMIN := 3.12
PYVER    := 3.12.5
PFX      := /tmp/pyout
PYTHON   := $(PFX)/bin/python$(PYMAJMIN)
LIBA     := $(PFX)/lib/libpython$(PYMAJMIN).a
INCDIR   := $(PFX)/include/python$(PYMAJMIN)
PYCONFIG := $(PFX)/bin/python$(PYMAJMIN)-config

OUTBIN   := hello_embedded
SCRIPT   := hello.py
LIBSTATIC := libpython.a

PYTHON_SRC := /tmp/Python-$(PYVER)
PYTHON_TGZ := /tmp/Python-$(PYVER).tgz

.PHONY: $(OUTBIN)
.PHONY: $(LIBSTATIC)

# ------------------------------------------------------------
# Step 1: Build static Python (only if missing)
# ------------------------------------------------------------

$(PYTHON):
	@if [ -f "$(LIBA)" ]; then \
		echo "Static libpython already exists — skipping Python rebuild."; \
	else \
		echo "Building static Python under $(PFX)..."; \
		mkdir -p $(PFX); \
		if [ ! -d "$(PYTHON_SRC)" ]; then \
			echo "Preparing Python source in $(PYTHON_SRC)..."; \
			if [ ! -f "$(PYTHON_TGZ)" ]; then \
				curl -L -o "$(PYTHON_TGZ)" "https://www.python.org/ftp/python/$(PYVER)/Python-$(PYVER).tgz"; \
			fi; \
			cd /tmp && tar xf "$(PYTHON_TGZ)"; \
		fi; \
		cd "$(PYTHON_SRC)" && { \
			ulimit -n 1024 \
			&& ./configure \
				--prefix="$(PFX)" \
				--disable-shared \
				--without-ensurepip \
				--enable-optimizations \
				--with-lto \
				--without-tests; \
			make -j$$(sysctl -n hw.ncpu) PROFILE_TASK= install; \
		}; \
	fi

# ------------------------------------------------------------
# Step 2: Install pip + Nuitka if missing
# ------------------------------------------------------------

$(PFX)/.nuitka_installed: $(PYTHON)
	@echo "Checking for pip and Nuitka in $(PFX)..."
	@if ! $(PYTHON) -m pip -V >/dev/null 2>&1; then \
		echo "Bootstrapping pip into static Python..."; \
		curl -sS https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py; \
		$(PYTHON) /tmp/get-pip.py; \
	fi
	@if ! $(PYTHON) -m nuitka --version >/dev/null 2>&1; then \
		echo "Installing Nuitka..."; \
		$(PYTHON) -m pip install --no-cache-dir nuitka; \
	fi
	@touch $(PFX)/.nuitka_installed

# ------------------------------------------------------------
# Step 3: Copy libpython.a locally (if not already copied)
# ------------------------------------------------------------


$(LIBSTATIC): $(LIBA)
	@if [ ! -f "$(LIBSTATIC)" ]; then \
		echo "Copying $(LIBA) → $(LIBSTATIC)"; \
		cp -v $(LIBA) .; \
		cp -v $(LIBA) $(LIBSTATIC); \
	else \
		echo "$(LIBSTATIC) already exists — skipping copy."; \
	fi

# ------------------------------------------------------------
# Step 4: Build single-file binary with Nuitka
# ------------------------------------------------------------

$(OUTBIN): $(SCRIPT) $(PFX)/.nuitka_installed $(LIBSTATIC)
	@echo "Building $(OUTBIN) using Nuitka (single-file, static libpython + _tkinter)..."
	$(PFX)/bin/python3 -m nuitka --onefile --static-libpython=yes \
		--clang --remove-output \
		--enable-plugin=tk-inter \
		--tcl-library-dir=/tmp/tcltk-static/lib \
		--tk-library-dir=/tmp/tcltk-static/lib \
		--output-filename=$@ $<
	@strip -x $(OUTBIN) || true
	@echo "Built successfully: $(OUTBIN)"


# 
# $(OUTBIN): $(SCRIPT) $(PFX)/.nuitka_installed $(LIBSTATIC)
# 	@echo "Building $(OUTBIN) using Nuitka (single-file, static libpython)..."
# 	$(PYTHON) -m nuitka --onefile --static-libpython=yes \
# 		--clang --remove-output --output-filename=$@ $<
# 	@strip -x $(OUTBIN) || true
# 	@echo "Built successfully: $(OUTBIN)"

# ------------------------------------------------------------
# Step 5: Run & maintenance
# ------------------------------------------------------------

all: #$(OUTBIN)
	@echo "I can't get this working for static. But Makefile.dynamic works"
# 	@./$(OUTBIN)

clean:
	rm -rf __pycache__ build dist *.bin *build
	@echo "Preserved Python sources and libpython under /tmp."

distclean: clean
	rm -rf $(PFX) $(PFX)/.nuitka_installed
	@echo "Preserved $(PYTHON_SRC) and $(PYTHON_TGZ) (not redownloaded next time)."

update-nuitka:
	@$(PYTHON) -m pip install --upgrade nuitka
