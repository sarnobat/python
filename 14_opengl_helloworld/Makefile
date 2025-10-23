build:
	rsync -a /Volumes/git/src.git/2021/python/opengl/helloworld.py .
	nm -gU /opt/homebrew/lib/libglut.dylib | grep glutCloseFunc
# 	DYLD_LIBRARY_PATH=/opt/homebrew/lib:$$DYLD_LIBRARY_PATH 
	python3 helloworld.py


init:
	pip install PyOpenGL
	brew install --build-from-source freeglut
	brew install glew glfw
	pip3 install glfw

	
