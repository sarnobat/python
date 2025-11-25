# Prepend your pyenv shims to PATH
PATH := /Users/sarnobat/.pyenv/shims:$(PATH)

all:
	#python3 multiply_nopytorch.py
	python3 multiply.py 4

install:
	python3 -m pip install torch
	python3 -m pip install pyobjc

diff:
	# not as useful as I was hoping
# 	cp multiply.py /tmp/ && perl -i -pe 's{^#}{// }' /tmp/multiply.py
# 	/Volumes/apps/Apps/DiffMerge.app/Contents/MacOS/DiffMerge /Volumes/git/github/depot_parent/c/19_cuda_metal_gpu/multiply_metal.m 
	cp multiply.py /Volumes/git/github/depot_parent/c/19_cuda_metal_gpu/multiply_metal.m  /tmp/ && perl -i -pe 's{^\s*[#/]+\s*}{// }' /tmp/multiply_metal.m /tmp/multiply.py
	/Volumes/apps/Apps/DiffMerge.app/Contents/MacOS/DiffMerge /tmp/multiply_metal.m /tmp/multiply.py
