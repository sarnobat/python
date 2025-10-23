build:
	nm -gU /opt/homebrew/lib/libglut.dylib | grep glutCloseFunc
	python3 helloworld.py data.csv


init:
	pip install PyOpenGL
	brew install --build-from-source freeglut
	brew install glew glfw
	pip3 install glfw

	
