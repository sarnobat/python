TARGET_STATIC := hello.static
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

# Paths
TCL_VER   := 8.6.13
TK_VER    := 8.6.13
PREFIX    := /tmp/tcltk-static
TCL_SRC   := /tmp/tcl$(TCL_VER)
TK_SRC    := /tmp/tk$(TK_VER)
TCL_TGZ   := /tmp/tcl$(TCL_VER)-src.tar.gz
TK_TGZ    := /tmp/tk$(TK_VER)-src.tar.gz

# Targets
TCL_LIB := $(PREFIX)/lib/libtcl8.6.a
TK_LIB  := $(PREFIX)/lib/libtk8.6.a

$(TARGET_STATIC):		libpython.a	
	python3 -m nuitka --onefile \
	    --static-libpython=no \
	    --enable-plugin=tk-inter \
	    --tcl-library-dir=/opt/homebrew/opt/tcl-tk@8/lib \
	    --tk-library-dir=/opt/homebrew/opt/tcl-tk@8/lib \
	    --output-filename=hello.static \
	    hello.py

tcltk: $(TCL_LIB) $(TK_LIB) copy-libs

copy-libs:
	echo ""

# Download and extract Tcl
$(TCL_SRC):
	mkdir -p /tmp
	cd /tmp && { \
		[ -f "$(TCL_TGZ)" ] || curl -LO https://prdownloads.sourceforge.net/tcl/tcl$(TCL_VER)-src.tar.gz; \
		tar xf "$(TCL_TGZ)"; \
	}

# Download and extract Tk
$(TK_SRC):
	mkdir -p /tmp
	cd /tmp && { \
		[ -f "$(TK_TGZ)" ] || curl -LO https://prdownloads.sourceforge.net/tcl/tk$(TK_VER)-src.tar.gz; \
		tar xf "$(TK_TGZ)"; \
	}

# Build static Tcl
$(TCL_LIB): $(TCL_SRC)
	cd $(TCL_SRC)/unix && \
		./configure --disable-shared --prefix=/tmp/tclbuild && \
		make -j$$(sysctl -n hw.ncpu)

# Build static Tk (depends on Tcl)
$(TK_LIB): $(TK_SRC) $(TCL_LIB)
	cd $(TK_SRC)/unix && \
		./configure --disable-shared --with-tcl=$(TCL_SRC)/unix && \
		make -j$$(sysctl -n hw.ncpu)

libpython.a:
	pwd
	chmod a+w lib*
	cp /private/tmp/pyout/lib/libpython3.12.a .
# 	cp $(TCL_LIB) .
# 	cp $(TK_LIB) .
# 	cp $(TK_SRC)/unix/libtk8.6.a .
	cp $(TCL_SRC)/unix/libtcl8.6.a .

init:
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
		cd "$(PYTHON_SRC)"; \
		ulimit -n 1024 && \
		./configure \
			--prefix=$(PFX) \
			--disable-shared \
			--without-ensurepip \
			--enable-optimizations \
			--with-lto \
			--enable-loadable-sqlite-extensions \
			--with-static-libtk && \
		make -j$$(sysctl -n hw.ncpu) && \
		make install; \
	fi
