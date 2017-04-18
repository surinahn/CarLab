import os, sys, subprocess
import numpy as np

base_x = 100
base_y = 80

side = 40 
error = 30

data = open(sys.argv[1], "r")

blocks = []
for i in range(0,9): 
	sigs = [0,0,0,0,0,0]
	blocks.append(sigs)

hits = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]

def contains(mid_x, mid_y, x, y, w, h): 
	return (mid_x-x <error and mid_y-y < error and h*w>100)

for line in data.readlines(): 
	split = line.split() 
	split = [int(s) for s in split]
	sig = split[0]
	x = split[1]
	y = split[2]
	w = split[3]
	h = split[4]

	for j in range(0,3): 
		for i in range(0,3): 
			num = j*3 + i 

			mid_x = base_x+i*side
			mid_y = base_y+j*side

			if contains(mid_x, mid_y, x, y, w, h):
				blocks[num][sig-1] += 1

print blocks