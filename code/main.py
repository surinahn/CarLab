#!/usr/bin/python

import kociemba
from controls import *
import time


# Initialize the claws
initialize()

# Read input cube configuration from pixy cam

# Convert the cube configuration into kociemba format
config = 'DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD'
print("Input Configuration: ")
print(config)
print('\n')

# Pass the cube configuration into the kociemba solver
solution = kociemba.solve(config)
print("Solution: ")
print(solution)

# Solve the cube
turnF()
