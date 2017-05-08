import os, sys, subprocess
import numpy as np

print 'rprksad'
base_x = 120
base_y = 50

side = 50
offset = 40

data = open(sys.argv[1], "r")

blocks = []
for i in range(0,9): 
	sigs = [0,0,0,0,0,0]
	blocks.append(sigs)

letters = ['B','F','U','L','D','R']
hits = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]

def contains(sig, mid_x, mid_y, x, y): 
	offset_x = mid_x-x; 

	offset_y = mid_y-y; 
	if offset_x < 0 or offset_y < 0: 
		return False 
	# if offset_x < offset and offset_y < offset: 
	# 	print str(sig) + ":" + str(offset_x) + ":" +str(offset_y)
	return (offset_x < offset and offset_y < offset)

min_x = 500 
min_y = 500
for i in range(0,500): 
	line = data.readline() 
	split = line.split() 
	split = [int(s) for s in split]
	sig = split[0]
	x = split[1]
	y = split[2]
	w = split[3]
	h = split[4]
	if w*h>400 and x < min_x:
		min_x = x 
	if w*h>400 and y < min_y:
		min_y = y 

base_x = min_x
base_y = min_y
data.seek(0)
print base_x
print base_y

print "begin"
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

			if w*h > 200: 
				if contains(sig, mid_x, mid_y, x, y):
					blocks[num][sig-1] += 1

print blocks
max_indices = [letters[b.index(max(b))] for b in blocks]
print "max_indices"
print max_indices
#process for white
for i in range(0,9): 
	if max(blocks[i]) < 5: 
		max_indices[i] = letters[4]
string = ''.join(max_indices)
print string

