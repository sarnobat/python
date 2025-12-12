# run:	build
# 	open media/videos/hello_world/480p15/HelloWorld.mp4
# 	
# build:	
# 	ln -sf media/videos/hello_world/480p15/HelloWorld.mp4
# 	manim --quality l hello_world.py HelloWorld

# Makefile for Manim animations (v0.19+)
# Keeps only final MP4s in output/, deletes media/ after rendering
# Creates symlinks in the current folder for easy access

MANIM = manim
FLAGS = -ql  # low quality: 480p15
OUTPUT = output

# List of scripts and their scene names
# Format: script.py SceneClass
SCRIPTS = hello_world.py HelloWorld \
          remove_first.py RemoveFirstElement \
          tree.py SubsetTree

.PHONY: all render play clean

# Default target: render and play
play: all
	@echo "Playing selected videos..."
	# Open the final MP4s from output/ or symlinks
# 	open HelloWorld.mp4
# 	open RemoveFirstElement.mp4
	open SubsetTree.mp4

all: render

render:
	@echo "Rendering all Manim scenes..."
	@mkdir -p $(OUTPUT)
	@set -- $(SCRIPTS); \
	while [ "$$#" -gt 0 ]; do \
		script=$$1; \
		scene=$$2; \
		shift 2; \
		echo "Rendering $$script -> $$scene"; \
		$(MANIM) $(FLAGS) $$script $$scene; \
		# Find the rendered MP4 and copy it to output/ \
		VIDEO_PATH=$$(find media/videos -type f -name "$$scene.mp4" | head -n 1); \
		if [ -f "$$VIDEO_PATH" ]; then \
			cp "$$VIDEO_PATH" $(OUTPUT)/; \
		fi; \
	done
	@echo "Deleting entire media/ folder..."
	@rm -rf media
	@echo "Creating symlinks to MP4s in current folder..."
	@ln -srf $(OUTPUT)/*.mp4 .

clean:
	@echo "Removing output/ folder and symlinks..."
	rm -rf $(OUTPUT) *.mp4

help:
	manim render --help