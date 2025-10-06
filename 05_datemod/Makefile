build:	doy	dm

doy:
	cython --embed -3 dayofyear.py
	
	gcc -Os dayofyear.c \
	  `python-config --cflags --embed --ldflags` \
	  -Wl,-rpath,/Applications/Xcode.app/Contents/Developer/Library/Frameworks \
	  -o doy

dm:
	cython --embed -3 datemod.py

	gcc -Os datemod.c \
	  `python-config --cflags --embed --ldflags` \
	  -Wl,-rpath,/Applications/Xcode.app/Contents/Developer/Library/Frameworks \
	  -o dm

clean:
	rm -v dm 
	rm -v doy