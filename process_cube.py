import os, sys, subprocess
import numpy as np

base_x = 110
base_y = 50

side = 50
offset = 30

data = open(sys.argv[1], "r")

blocks = []
for i in range(0,9): 
	sigs = [0,0,0,0,0,0]
	blocks.append(sigs)

hits = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]

def contains(sig, mid_x, mid_y, x, y): 
	offset_x = mid_x-x; 
	offset_y = mid_y-y; 
	print str(sig) + ":" + str(mid_x) + ":" +str(mid_y)
	if offset_x < 0 or offset_y < 0: 
		return False 
	if offset_x < offset and offset_y < offset: 
		print str(sig) + ":" + str(offset_x) + ":" +str(offset_y)
	return (offset_x < offset and offset_y < offset)

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

			mid_x = base_x+(i+.5)*side
			mid_y = base_y+(j+.5)*side

			if w*h > 100: 
				if contains(sig, mid_x, mid_y, x, y):
					blocks[num][sig-1] += 1

print blocks