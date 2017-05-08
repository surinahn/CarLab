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

#turnF(0)
#turnF(1)
#turnR(0)
#turnR(1)
#turnL(0)
#turnL(1)
#turnB(0)
#turnB(1)
#turnU(0)
#turnU(1)
#turnD(0)
#turnD(1)


seq = ''

inspect() 
print('Inspecting yellow...')
subprocess.call(['./read_cube.sh'])
subprocess.call("sudo python process_cube.py cleaned.txt > seq.txt", shell=True)
#rotate()

#print('Inspecting orange...')
##inspect()
##seq += read() 
##
##print('Inspecting white...')
##seq += read() 
##inspect()
##
##print('Inspecting pink...')
##seq += read() 
##inspect()
##
##print('Inspecting blue...')
##seq += read() 
##inspect()
##
##print('Inspecting green...')
##seq += read() 
##inspect()

############################
#     INSPECTION PHASE     #
############################


# Read input cube configuration from pixy cam


'''
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
    if m == 'F':
        turnF(0)
    elif m == "F'":
        turnF(1)
    elif m == "F2":
        turnF(2)
    elif m == 'R':
        turnR(0)
    elif m == "R'":
        turnR(1)
    elif m == "R2":
        turnR(2)
    elif m == 'L':
        turnL(0)
    elif m == "L'":
        turnL(1)
    elif m == "L2":
        turnL(2)
    elif m == 'B':
        turnB(0)
    elif m == "B'":
        turnB(1)
    elif m == "B2":
        turnB(2)
    elif m == 'U':
        turnU(0)
    elif m == "U'":
        turnU(1)
    elif m == "U2":
        turnU(2)
    elif m == 'D':
        turnD(0)
    elif m == "D'":
        turnD(1)
    elif m == "D2":
        turnD(2)
'''

