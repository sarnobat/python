# run:	build
# 	open media/videos/hello_world/480p15/HelloWorld.mp4
# 	
# build:	
# 	ln -sf media/videos/hello_world/480p15/HelloWorld.mp4
# 	manim --quality l hello_world.py HelloWorld

# Makefile for Manim animations (v0.19+), POSIX-compatible

MANIM = manim
FLAGS = -pql

# List of scripts and their scene names
# Format: script.py SceneClass
SCRIPTS = hello_world.py HelloWorld \
          remove_first.py RemoveFirstElement

.PHONY: all clean

all:
	@echo "Rendering all Manim scenes..."
	@set -- $(SCRIPTS); \
	while [ "$$#" -gt 0 ]; do \
		script=$$1; \
		scene=$$2; \
		shift 2; \
		echo "Rendering $$script -> $$scene"; \
		$(MANIM) $(FLAGS) $$script $$scene; \
	done

clean:
	rm -rf media

help:
	manim render --help