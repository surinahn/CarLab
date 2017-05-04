import os, sys, subprocess

def read():
	subprocess.call(['./read_cube.sh'])
	subprocess.call(['python process_cube.py cleaned.txt > seq.txt'])
