import os, sys, subprocess

def read():
	subprocess.call(['./read_cube.sh'])
	subprocess.call("sudo python process_cube.py cleaned.txt > seq.txt", shell=True)
	file = open('seq.txt', 'r')
	seq = file.readline()
	file.close() 
        return seq 
