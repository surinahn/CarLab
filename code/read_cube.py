import subprocess

def read(): 
	seq = subprocess.call(['./read_cube.sh'])
	return seq 