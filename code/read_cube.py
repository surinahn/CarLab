import os, sys, subprocess

def read():
        #subprocess.call(['./read_cube.sh'])
	#subprocess.call("sudo python process_cube.py cleaned.txt > seq.txt", shell=True)
	#file = open('seq.txt', 'r')
	#seq = file.readline()
	#file.close()
        
        process1 = subprocess.Popen('./read_cube.sh', shell=True)
        process1.wait()
	process = subprocess.Popen(['sudo python process_cube.py cleaned.txt'], shell=True, stdout=subprocess.PIPE)
        process.wait()
        seq = process.communicate()
        seq = seq[0]
        seq = seq[0:9]
        return seq 
