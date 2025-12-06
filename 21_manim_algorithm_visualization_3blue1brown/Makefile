# run:	build
# 	open media/videos/hello_world/480p15/HelloWorld.mp4
# 	
# build:	
# 	ln -sf media/videos/hello_world/480p15/HelloWorld.mp4
# 	manim --quality l hello_world.py HelloWorld

# Makefile for Manim animations (v0.19+)
# Render, clean temporary files, and optionally play videos

MANIM = manim
FLAGS = -ql  # low quality rendering; change to -qm or -pqh for higher quality

# List of scripts and their scene names
# Format: script.py SceneClass
SCRIPTS = hello_world.py HelloWorld \
          remove_first.py RemoveFirstElement

.PHONY: all render play clean


# Play selected videos
play:	all
	@echo "Playing selected videos..."
	# Uncomment the scenes you want to play:
	# open media/videos/hello_world/1080p60/HelloWorld.mp4
	open media/videos/remove_first/1080p60/RemoveFirstElement.mp4

# Default target: render all
all: render

# Render all scenes
render:
	@echo "Rendering all Manim scenes..."
	@set -- $(SCRIPTS); \
	while [ "$$#" -gt 0 ]; do \
		script=$$1; \
		scene=$$2; \
		shift 2; \
		echo "Rendering $$script -> $$scene"; \
		$(MANIM) $(FLAGS) $$script $$scene; \
		# Remove all partial movie files and lock files \
		find media -type d -name partial_movie_files -exec rm -rf {} +; \
		find media -type f -name '*.lock' -exec rm -f {} +; \
	done


# Clean all generated media
clean:
	@echo "Removing all rendered media..."
	rm -rf media

help:
	manim render --help