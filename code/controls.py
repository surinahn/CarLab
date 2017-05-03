#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# Functions for controlling the claws
# By default, all claws are gripped
# p denotes prime (counter-clockwise)
# 2 means turn twice (180 degrees)

servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096

# Initialise the PWM device using the default address
pwm = PWM(0x40)

# Claw grip channel numbers (edit these as necessary)
fgChan = 0
rgChan = 1
lgChan = 2
bgChan = 3

# Claw rotation channel numbers (edit these as necessary)
frChan = 4
rrChan = 5
lrChan = 6
brChan = 7

# PWM values for gripping
# f claw is red
# r claw is orange
# l claw is blue
# b claw is black

fUngrip = 150
fGrip = 410
rUngrip = 150
rGrip = 400
lUngrip = 150
lGrip = 480
bUngrip = 150
bGrip = 450

# PWM values for turning each side
# CW = clockwise, CCW = counter-clockwise, 2 = 180 degrees (turn twice)

fdefault = 390
fCW = 125
fCCW = 600
rdefault = 370
rCW = 140
rCCW = 630
ldefault = 380
lCW = 125
lCCW = 640
bdefault = 370
bCW = 125
bCCW = 640

# Initialize PWM
# Make sure all claws are gripped and properly rotated
def initialize():
    # Initialise the PWM device using the default address
    pwm = PWM(0x40)
    pwm.setPWMFreq(60) # Set frequency to 60 Hz
    pwm.setPWM(fgChan, fGrip)
    pwm.setPWM(rgChan, rGrip)
    pwm.setPWM(lgChan, lGrip)
    pwm.setPWM(bgChan, bGrip)
    pwm.setPWM(frChan, fdefault)
    pwm.setPWM(rrChan, rdefault)
    pwm.setPWM(lrChan, ldefault)
    pwm.setPWM(brChan, bdefault) 

# Turn front side
# x = 0 means CW, x = 1 means CCW, x = 2 means 180 degrees
def turnF(x):
    if x == 0:
        # Turn claw
        pwm.setPWM(frChan, 0, fCW)
        time.sleep(1)
        # Ungrip claw
        pwm.setPWM(fgChan, 0, fUngrip)
        time.sleep(1)
        # Turn claw back
        pwm.setPWM(frChan, 0, fdefault)
        time.sleep(1)
        # Grip claw
        pwm.setPWM(fgChan, 0, fGrip)
        time.sleep(1)
    elif x == 1:
        # Turn Claw
        pwm.setPWM(frChan, 0, fCCW)
        time.sleep(1)
        # Ungrip claw
        pwm.setPWM(fgChan, 0, fUngrip)
        time.sleep(1)
        # Turn claw back
        pwm.setPWM(frChan, 0, fdefault)
        time.sleep(1)
        # Grip claw
        pwm.setPWM(fgChan, 0, fGrip)
        time.sleep(1)
    elif x == 2:
        # Turn claw
        pwm.setPWM(frChan, 0, fCW)
        time.sleep(1)
        # Ungrip claw
        pwm.setPWM(fgChan, 0, fUngrip)
        time.sleep(1)
        # Turn claw back
        pwm.setPWM(frChan, 0, fdefault)
        time.sleep(1)
        # Grip claw
        pwm.setPWM(fgChan, 0, fGrip)
        time.sleep(1)
        # Turn claw
        pwm.setPWM(frChan, 0, fCW)
        time.sleep(1)
        # Ungrip claw
        pwm.setPWM(fgChan, 0, fUngrip)
        time.sleep(1)
        # Turn claw back
        pwm.setPWM(frChan, 0, fdefault)
        time.sleep(1)
        # Grip claw
        pwm.setPWM(fgChan, 0, fGrip)
        time.sleep(1)

# Turn right side
def turnR(x):
    if x == 0:
        # Turn claw
        pwm.setPWM(rrChan, 0, rCW)
        time.sleep(1)
        # Ungrip claw
        pwm.setPWM(rgChan, 0, rUngrip)
        time.sleep(1)
        # Turn claw back
        pwm.setPWM(rrChan, 0, rdefault)
        time.sleep(1)
        # Grip claw
        pwm.setPWM(rgChan, 0, rGrip)
        time.sleep(1)
    elif x == 1:
        # Turn Claw
        pwm.setPWM(rrChan, 0, rCCW)
        time.sleep(1)
        # Ungrip claw
        pwm.setPWM(rgChan, 0, rUngrip)
        time.sleep(1)
        # Turn claw back
        pwm.setPWM(rrChan, 0, rdefault)
        time.sleep(1)
        # Grip claw
        pwm.setPWM(rgChan, 0, rGrip)
        time.sleep(1)
    elif x == 2:
        # Turn claw
        pwm.setPWM(rrChan, 0, rCW)
        time.sleep(1)
        # Ungrip claw
        pwm.setPWM(rgChan, 0, rUngrip)
        time.sleep(1)
        # Turn claw back
        pwm.setPWM(rrChan, 0, rdefault)
        time.sleep(1)
        # Grip claw
        pwm.setPWM(rgChan, 0, rGrip)
        time.sleep(1)
        # Turn claw
        pwm.setPWM(rrChan, 0, rCW)
        time.sleep(1)
        # Ungrip claw
        pwm.setPWM(rgChan, 0, rUngrip)
        time.sleep(1)
        # Turn claw back
        pwm.setPWM(rrChan, 0, rdefault)
        time.sleep(1)
        # Grip claw
        pwm.setPWM(rgChan, 0, rGrip)
        time.sleep(1)

# Turn left side
def turnL(x):
    if x == 0:
        # Turn claw
        pwm.setPWM(lrChan, 0, lCW)
        time.sleep(1)
        # Ungrip claw
        pwm.setPWM(lgChan, 0, lUngrip)
        time.sleep(1)
        # Turn claw back
        pwm.setPWM(lrChan, 0, ldefault)
        time.sleep(1)
        # Grip claw
        pwm.setPWM(lgChan, 0, lGrip)
        time.sleep(1)
    elif x == 1:
        # Turn Claw
        pwm.setPWM(lrChan, 0, lCCW)
        time.sleep(1)
        # Ungrip claw
        pwm.setPWM(lgChan, 0, lUngrip)
        time.sleep(1)
        # Turn claw back
        pwm.setPWM(lrChan, 0, ldefault)
        time.sleep(1)
        # Grip claw
        pwm.setPWM(lgChan, 0, lGrip)
        time.sleep(1)
    elif x == 2:
        # Turn claw
        pwm.setPWM(lrChan, 0, lCW)
        time.sleep(1)
        # Ungrip claw
        pwm.setPWM(lgChan, 0, lUngrip)
        time.sleep(1)
        # Turn claw back
        pwm.setPWM(lrChan, 0, ldefault)
        time.sleep(1)
        # Grip claw
        pwm.setPWM(lgChan, 0, lGrip)
        time.sleep(1)
        # Turn claw
        pwm.setPWM(lrChan, 0, lCW)
        time.sleep(1)
        # Ungrip claw
        pwm.setPWM(lgChan, 0, lUngrip)
        time.sleep(1)
        # Turn claw back
        pwm.setPWM(lrChan, 0, ldefault)
        time.sleep(1)
        # Grip claw
        pwm.setPWM(lgChan, 0, lGrip)
        time.sleep(1)

# Turn back side
def turnB(x):
    if x == 0:
        # Turn claw
        pwm.setPWM(brChan, 0, bCW)
        time.sleep(1)
        # Ungrip claw
        pwm.setPWM(bgChan, 0, bUngrip)
        time.sleep(1)
        # Turn claw back
        pwm.setPWM(brChan, 0, bdefault)
        time.sleep(1)
        # Grip claw
        pwm.setPWM(bgChan, 0, bGrip)
        time.sleep(1)
    elif x == 1:
        # Turn Claw
        pwm.setPWM(brChan, 0, bCCW)
        time.sleep(1)
        # Ungrip claw
        pwm.setPWM(bgChan, 0, bUngrip)
        time.sleep(1)
        # Turn claw back
        pwm.setPWM(brChan, 0, bdefault)
        time.sleep(1)
        # Grip claw
        pwm.setPWM(bgChan, 0, bGrip)
        time.sleep(1)
    elif x == 2:
        # Turn claw
        pwm.setPWM(brChan, 0, bCW)
        time.sleep(1)
        # Ungrip claw
        pwm.setPWM(bgChan, 0, bUngrip)
        time.sleep(1)
        # Turn claw back
        pwm.setPWM(brChan, 0, bdefault)
        time.sleep(1)
        # Grip claw
        pwm.setPWM(bgChan, 0, bGrip)
        time.sleep(1)
        # Turn claw
        pwm.setPWM(brChan, 0, bCW)
        time.sleep(1)
        # Ungrip claw
        pwm.setPWM(bgChan, 0, bUngrip)
        time.sleep(1)
        # Turn claw back
        pwm.setPWM(brChan, 0, bdefault)
        time.sleep(1)
        # Grip claw
        pwm.setPWM(bgChan, 0, bGrip)
        time.sleep(1)

'''
# Turn up side
def turnU(x):
    # Ungrip front claw
    # Ungrip back claw
    # Ungrip left claw
    # Turn right claw 90 degrees CCW (up side is now on front)

    # Grip left claw
    # Ungrip right claw
    # Turn right claw 90 degrees CW

    # Grip front claw
    # Turn front claw 90 degrees CW
    # Ungrip front claw
    # Turn front claw 90 degrees CCW

    # Turn left claw 90 degrees CCW (up side is now back to up)
    # Grip right claw
    # Ungrip left claw
    # Turn left claw 90 degrees CW

    # Grip left claw
    # Grip front claw
    # Grip back claw

# Turn down side
def turnD(x):
'''
