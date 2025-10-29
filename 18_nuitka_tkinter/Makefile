TARGET_STATIC := hello.static

$(TARGET_STATIC):
    python3 -m nuitka --onefile --static-libpython=no \
		--tcl-library-dir=`brew --prefix tcl-tk`/lib \
		--enable-plugin=tk-inter --output-filename=$(TARGET_STATIC) hello.py

libpython.a:
	cp /private/tmp/pyout/lib/libpython3.12.a .
	
	