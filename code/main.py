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


############################
#     INSPECTION PHASE     #
############################


# Read input cube configuration from pixy cam

# (Inspect each side by rotating it)
# Camera is looking down on the cube (at the Yellow face)
# Front = Orange, Right = Blue, Left = Green, Up = Yellow, Down = White, Back = Pink

seq = ''

print('Inspecting yellow...')
inspect() 
seq += read()

#rotateZ()
#print('Inspecting blue...')
#inspect()
#seq += read()

#rotateX()
##print('Inspecting orange...')
##seq += read() 
##inspect()

## rotateZ()
##print('Inspecting white...')
##seq += read() 
##inspect()

## rotateX()
##print('Inspecting green...')
##seq += read() 
##inspect()

## rotateZ()
##print('Inspecting pink...')
##seq += read() 
##inspect()

# Return to original orientation
## rotateX()
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

'''

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

