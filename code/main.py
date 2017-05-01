#!/usr/bin/python

import kociemba
from controls import *
import time


# Initialize the claws
initialize()

############################
#     INSPECTION PHASE     #
############################

# Read input cube configuration from pixy cam
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


