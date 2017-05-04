#!/usr/bin/python

import kociemba
from controls import *
from read_cube import *
import time
import subprocess


# Initialize the claws
initialize()

# Close claws
userInput = ''
while userInput != 'c':
    userInput = raw_input("Press c when ready to grip: ")
close()

turnR(0)
turnU(0)
turnR(1)
turnU(1)
turnR(1)
turnF(0)
turnR(2)
turnU(1)
turnR(1)
turnU(1)
turnR(0)
turnU(0)
turnR(1)
turnF(1)

seq = ''

print('Inspecting yellow...')
seq += read() 
inspect()

print('Inspecting orange...')
seq += read() 
inspect()

print('Inspecting white...')
seq += read() 
inspect()

print('Inspecting pink...')
seq += read() 
inspect()

print('Inspecting blue...')
seq += read() 
inspect()

print('Inspecting green...')
seq += read() 
inspect()

############################
#     INSPECTION PHASE     #
############################

'''
# Read input cube configuration from pixy cam
subprocess.call(['./read_cube.sh'])
subprocess.call("process_cube.py cleaned.txt", shell=True)

# (Inspect each side by rotating it)
# Camera is looking down on the cube (at the Yellow face)
# Front = Orange, Right = Blue, Left = Green, Up = Yellow, Down = White, Back = Pink

# What if the claws interfere with the camera vision? 

# Capture the up (yellow) face
print('Inspecting yellow...')

# Rotate the cube CW with right claw 

# Capture the front (orange) face
print('Inspecting orange...')

# Rotate the cube CW with right claw 

# Capture the down (white) face
print('Inspecting white...')

# Rotate the cube CW with right claw 

# Capture the back (pink) face
print('Inspecting pink...')

# Capture the right (blue) face
print('Inspecting blue...')

# Capture the left (green) face
print('Inspecting green...')

# Return to original orientation
print('Done Inspecting!\n')



############################
#       SOLVING PHASE      #
############################

# Convert the cube configuration into kociemba format
config = 'DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD'
print("Input Configuration: ")
print(config)
print('\n')

# Pass the cube configuration into the kociemba solver
solution = kociemba.solve(config)
print("Solution: ")
print(solution)
print('\n')

# Solve the cube
print("Solving the cube...")
moves = solution.split()

for m in moves:
    print(m)
    time.sleep(1)
'''


