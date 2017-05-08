#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# Functions for controlling the claws
# By default, all claws are gripped

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

fUngrip = 320
fGrip = 420
rUngrip = 320
rGrip = 410
lUngrip = 400
lGrip = 480
bUngrip = 320
bGrip = 455

# PWM values for turning each side
# CW = clockwise, CCW = counter-clockwise, 2 = 180 degrees (turn twice)

fdefault = 380
fCW = 125
fCCW = 630
rdefault = 370
rCW = 125
rCCW = 640
ldefault = 380
lCW = 125
lCCW = 645
bdefault = 370
bCW = 117
bCCW = 640

fnCCW = fCCW - 16
bnCW = bCW + 16

fnCW = fCW + 30 
bnCCW = bCCW - 30

lnCW = lCW + 20
rnCCW = rCCW - 20

lnCCW = lCCW - 20
rnCW = rCW + 20 


# Initialize PWM
# Make sure all claws are gripped and properly rotated
def initialize():
    # Initialise the PWM device using the default address
    pwm = PWM(0x40)
    pwm.setPWMFreq(60) # Set frequency to 60 Hz

    pwm.setPWM(fgChan, 0, servoMin)
    pwm.setPWM(rgChan, 0, servoMin)
    pwm.setPWM(lgChan, 0, servoMin)
    pwm.setPWM(bgChan, 0, servoMin)
    time.sleep(2)
    pwm.setPWM(fgChan, 0, servoMax)
    pwm.setPWM(rgChan, 0, servoMax)
    pwm.setPWM(lgChan, 0, servoMax)
    pwm.setPWM(bgChan, 0, servoMax)
    time.sleep(1)
    pwm.setPWM(frChan, 0, fdefault)
    pwm.setPWM(brChan, 0, bdefault)
    time.sleep(1)
    pwm.setPWM(rrChan, 0, rdefault)
    pwm.setPWM(lrChan, 0, ldefault)
    time.sleep(1)
    pwm.setPWM(fgChan, 0, fGrip-40)
    pwm.setPWM(rgChan, 0, rGrip-40)
    pwm.setPWM(lgChan, 0, lGrip-40)
    pwm.setPWM(bgChan, 0, bGrip-40)
    time.sleep(1)

def close():
    pwm.setPWM(fgChan, 0, fGrip)
    pwm.setPWM(rgChan, 0, rGrip)
    pwm.setPWM(lgChan, 0, lGrip)
    pwm.setPWM(bgChan, 0, bGrip)
    pwm.setPWM(frChan, 0, fdefault)
    pwm.setPWM(rrChan, 0, rdefault)
    pwm.setPWM(lrChan, 0, ldefault)
    pwm.setPWM(brChan, 0, bdefault)
    time.sleep(1)

def inspect():
    pwm.setPWM(rgChan, 0, servoMin)
    pwm.setPWM(lgChan, 0, servoMin)
    

# Turn front side
# x = 0 means CW, x = 1 means CCW, x = 2 means 180 degrees
def turnF(x):
    if x == 0:
        # Turn claw
        pwm.setPWM(frChan, 0, fCW)
        time.sleep(0.75)
        # Ungrip claw
        pwm.setPWM(fgChan, 0, fUngrip)
        time.sleep(0.75)
        # Turn claw back
        pwm.setPWM(frChan, 0, fdefault)
        time.sleep(0.75)
        # Grip claw
        pwm.setPWM(fgChan, 0, fGrip)
        time.sleep(0.75)
    elif x == 1:
        # Turn Claw
        pwm.setPWM(frChan, 0, fCCW)
        time.sleep(0.75)
        # Ungrip claw
        pwm.setPWM(fgChan, 0, fUngrip)
        time.sleep(0.75)
        # Turn claw back
        pwm.setPWM(frChan, 0, fdefault)
        time.sleep(0.75)
        # Grip claw
        pwm.setPWM(fgChan, 0, fGrip)
        time.sleep(0.75)
    elif x == 2:
        # Turn claw
        pwm.setPWM(frChan, 0, fCW)
        time.sleep(0.75)
        # Ungrip claw
        pwm.setPWM(fgChan, 0, fUngrip)
        time.sleep(0.75)
        # Turn claw back
        pwm.setPWM(frChan, 0, fdefault)
        time.sleep(0.75)
        # Grip claw
        pwm.setPWM(fgChan, 0, fGrip)
        time.sleep(0.75)
        # Turn claw
        pwm.setPWM(frChan, 0, fCW)
        time.sleep(0.75)
        # Ungrip claw
        pwm.setPWM(fgChan, 0, fUngrip)
        time.sleep(0.75)
        # Turn claw back
        pwm.setPWM(frChan, 0, fdefault)
        time.sleep(0.75)
        # Grip claw
        pwm.setPWM(fgChan, 0, fGrip)
        time.sleep(0.75)

# Turn right side
def turnR(x):
    # Get the other claws out of the way
    pwm.setPWM(fgChan, 0, fUngrip)
    pwm.setPWM(bgChan, 0, bUngrip)
    time.sleep(0.75)
    pwm.setPWM(frChan, 0, fCW)
    pwm.setPWM(brChan, 0, bCW)
    time.sleep(0.75)
    pwm.setPWM(fgChan, 0, fGrip)
    pwm.setPWM(bgChan, 0, bGrip)
    time.sleep(0.75)
    
    if x == 0:
        # Turn claw
        pwm.setPWM(rrChan, 0, rCW)
        time.sleep(0.75)
        # Ungrip claw
        pwm.setPWM(rgChan, 0, rUngrip)
        time.sleep(0.75)
        # Turn claw back
        pwm.setPWM(rrChan, 0, rdefault)
        time.sleep(0.75)
        # Grip claw
        pwm.setPWM(rgChan, 0, rGrip)
        time.sleep(0.75)
    elif x == 1:
        # Turn Claw
        pwm.setPWM(rrChan, 0, rCCW)
        time.sleep(0.75)
        # Ungrip claw
        pwm.setPWM(rgChan, 0, rUngrip)
        time.sleep(0.75)
        # Turn claw back
        pwm.setPWM(rrChan, 0, rdefault)
        time.sleep(0.75)
        # Grip claw
        pwm.setPWM(rgChan, 0, rGrip)
        time.sleep(0.75)
    elif x == 2:
        # Turn claw
        pwm.setPWM(rrChan, 0, rCW)
        time.sleep(0.75)
        # Ungrip claw
        pwm.setPWM(rgChan, 0, rUngrip)
        time.sleep(0.75)
        # Turn claw back
        pwm.setPWM(rrChan, 0, rdefault)
        time.sleep(0.75)
        # Grip claw
        pwm.setPWM(rgChan, 0, rGrip)
        time.sleep(0.75)
        # Turn claw
        pwm.setPWM(rrChan, 0, rCW)
        time.sleep(0.75)
        # Ungrip claw
        pwm.setPWM(rgChan, 0, rUngrip)
        time.sleep(0.75)
        # Turn claw back
        pwm.setPWM(rrChan, 0, rdefault)
        time.sleep(0.75)
        # Grip claw
        pwm.setPWM(rgChan, 0, rGrip)
        time.sleep(0.75)

    # Put the other claws back
    pwm.setPWM(fgChan, 0, fUngrip)
    pwm.setPWM(bgChan, 0, bUngrip)
    time.sleep(0.75)
    pwm.setPWM(frChan, 0, fdefault)
    pwm.setPWM(brChan, 0, bdefault)
    time.sleep(0.75)
    pwm.setPWM(fgChan, 0, fGrip)
    pwm.setPWM(bgChan, 0, bGrip)
    time.sleep(0.75)

# Turn left side
def turnL(x):
    # Get the other claws out of the way
    pwm.setPWM(fgChan, 0, fUngrip)
    pwm.setPWM(bgChan, 0, bUngrip)
    time.sleep(0.75)
    pwm.setPWM(frChan, 0, fCW)
    pwm.setPWM(brChan, 0, bCW)
    time.sleep(0.75)
    pwm.setPWM(fgChan, 0, fGrip)
    pwm.setPWM(bgChan, 0, bGrip)
    time.sleep(0.75)
    
    if x == 0:
        # Turn claw
        pwm.setPWM(lrChan, 0, lCW)
        time.sleep(0.75)
        # Ungrip claw
        pwm.setPWM(lgChan, 0, lUngrip)
        time.sleep(0.75)
        # Turn claw back
        pwm.setPWM(lrChan, 0, ldefault)
        time.sleep(0.75)
        # Grip claw
        pwm.setPWM(lgChan, 0, lGrip)
        time.sleep(0.75)
    elif x == 1:
        # Turn Claw
        pwm.setPWM(lrChan, 0, lCCW)
        time.sleep(0.75)
        # Ungrip claw
        pwm.setPWM(lgChan, 0, lUngrip)
        time.sleep(0.75)
        # Turn claw back
        pwm.setPWM(lrChan, 0, ldefault)
        time.sleep(0.75)
        # Grip claw
        pwm.setPWM(lgChan, 0, lGrip)
        time.sleep(0.75)
    elif x == 2:
        # Turn claw
        pwm.setPWM(lrChan, 0, lCW)
        time.sleep(0.75)
        # Ungrip claw
        pwm.setPWM(lgChan, 0, lUngrip)
        time.sleep(0.75)
        # Turn claw back
        pwm.setPWM(lrChan, 0, ldefault)
        time.sleep(0.75)
        # Grip claw
        pwm.setPWM(lgChan, 0, lGrip)
        time.sleep(0.75)
        # Turn claw
        pwm.setPWM(lrChan, 0, lCW)
        time.sleep(0.75)
        # Ungrip claw
        pwm.setPWM(lgChan, 0, lUngrip)
        time.sleep(0.75)
        # Turn claw back
        pwm.setPWM(lrChan, 0, ldefault)
        time.sleep(0.75)
        # Grip claw
        pwm.setPWM(lgChan, 0, lGrip)
        time.sleep(0.75)

    # Put the other claws back
    pwm.setPWM(fgChan, 0, fUngrip)
    pwm.setPWM(bgChan, 0, bUngrip)
    time.sleep(0.75)
    pwm.setPWM(frChan, 0, fdefault)
    pwm.setPWM(brChan, 0, bdefault)
    time.sleep(0.75)
    pwm.setPWM(fgChan, 0, fGrip)
    pwm.setPWM(bgChan, 0, bGrip)
    time.sleep(0.75)

# Turn back side
def turnB(x):
    if x == 0:
        # Turn claw
        pwm.setPWM(brChan, 0, bCW)
        time.sleep(0.75)
        # Ungrip claw
        pwm.setPWM(bgChan, 0, bUngrip)
        time.sleep(0.75)
        # Turn claw back
        pwm.setPWM(brChan, 0, bdefault)
        time.sleep(0.75)
        # Grip claw
        pwm.setPWM(bgChan, 0, bGrip)
        time.sleep(0.75)
    elif x == 1:
        # Turn Claw
        pwm.setPWM(brChan, 0, bCCW)
        time.sleep(0.75)
        # Ungrip claw
        pwm.setPWM(bgChan, 0, bUngrip)
        time.sleep(0.75)
        # Turn claw back
        pwm.setPWM(brChan, 0, bdefault)
        time.sleep(0.75)
        # Grip claw
        pwm.setPWM(bgChan, 0, bGrip)
        time.sleep(0.75)
    elif x == 2:
        # Turn claw
        pwm.setPWM(brChan, 0, bCW)
        time.sleep(0.75)
        # Ungrip claw
        pwm.setPWM(bgChan, 0, bUngrip)
        time.sleep(0.75)
        # Turn claw back
        pwm.setPWM(brChan, 0, bdefault)
        time.sleep(0.75)
        # Grip claw
        pwm.setPWM(bgChan, 0, bGrip)
        time.sleep(0.75)
        # Turn claw
        pwm.setPWM(brChan, 0, bCW)
        time.sleep(0.75)
        # Ungrip claw
        pwm.setPWM(bgChan, 0, bUngrip)
        time.sleep(0.75)
        # Turn claw back
        pwm.setPWM(brChan, 0, bdefault)
        time.sleep(0.75)
        # Grip claw
        pwm.setPWM(bgChan, 0, bGrip)
        time.sleep(0.75)


# Turn up side
def turnU(x):
    if x == 0:
        # Ungrip left and right claws
        pwm.setPWM(rgChan, 0, rUngrip)
        pwm.setPWM(lgChan, 0, lUngrip)
        time.sleep(0.75)
        # Turn front claw CW and back claw CCW (up side is now on right)
        # +30 and -30 are due to less friction 
        pwm.setPWM(frChan, 0, fnCW)
        pwm.setPWM(brChan, 0, bnCCW)
        time.sleep(0.75)
        # Grip right claw
        pwm.setPWM(rgChan, 0, rGrip)
        time.sleep(0.75)
        # Turn right claw CW
        pwm.setPWM(rrChan, 0, rCW)
        time.sleep(0.75)
        # Ungrip right claw
        pwm.setPWM(rgChan, 0, rUngrip)
        time.sleep(0.75)
        # Turn right claw back
        pwm.setPWM(rrChan, 0, rdefault)
        time.sleep(0.75)
        # Turn front and back claws back (up side is now back to normal)
        pwm.setPWM(frChan, 0, fdefault)
        pwm.setPWM(brChan, 0, bdefault)
        time.sleep(0.75)
        # Grip left and right claws 
        pwm.setPWM(rgChan, 0, rGrip)
        pwm.setPWM(lgChan, 0, lGrip)
        time.sleep(0.75)
    elif x == 1:
        # Ungrip left and right claws
        pwm.setPWM(rgChan, 0, rUngrip)
        pwm.setPWM(lgChan, 0, lUngrip)
        time.sleep(0.75)
        # Turn front claw CW and back claw CCW (up side is now on right)
        pwm.setPWM(frChan, 0, fnCW)
        pwm.setPWM(brChan, 0, bnCCW)
        time.sleep(0.75)
        # Grip right claw
        pwm.setPWM(rgChan, 0, rGrip)
        time.sleep(0.75)
        # Turn right claw CCW
        pwm.setPWM(rrChan, 0, rCCW)
        time.sleep(0.75)
        # Ungrip right claw
        pwm.setPWM(rgChan, 0, rUngrip)
        time.sleep(0.75)
        # Turn right claw back
        pwm.setPWM(rrChan, 0, rdefault)
        time.sleep(0.75)
        # Turn front and back claws back (up side is now back to normal)
        pwm.setPWM(frChan, 0, fdefault)
        pwm.setPWM(brChan, 0, bdefault)
        time.sleep(0.75)
        # Grip left and right claws 
        pwm.setPWM(rgChan, 0, rGrip)
        pwm.setPWM(lgChan, 0, lGrip)
        time.sleep(0.75)
    elif x == 2:
        # Ungrip left and right claws
        pwm.setPWM(rgChan, 0, rUngrip)
        pwm.setPWM(lgChan, 0, lUngrip)
        time.sleep(0.75)
        # Turn front claw CW and back claw CCW (up side is now on right)
        pwm.setPWM(frChan, 0, fnCW)
        pwm.setPWM(brChan, 0, bnCCW)
        time.sleep(0.75)
        # Grip right claw
        pwm.setPWM(rgChan, 0, rGrip)
        time.sleep(0.75)
        # Turn right claw CW
        pwm.setPWM(rrChan, 0, rCW)
        time.sleep(0.75)
        # Ungrip right claw
        pwm.setPWM(rgChan, 0, rUngrip)
        time.sleep(0.75)
        # Turn right claw back
        pwm.setPWM(rrChan, 0, rdefault)
        time.sleep(0.75)
        # Grip right claw
        pwm.setPWM(rgChan, 0, rGrip)
        time.sleep(0.75)
        # Turn right claw CW
        pwm.setPWM(rrChan, 0, rCW)
        time.sleep(0.75)
        # Ungrip right claw
        pwm.setPWM(rgChan, 0, rUngrip)
        time.sleep(0.75)
        # Turn right claw back
        pwm.setPWM(rrChan, 0, rdefault)
        time.sleep(0.75)
        # Turn front and back claws back (up side is now back to normal)
        pwm.setPWM(frChan, 0, fdefault)
        pwm.setPWM(brChan, 0, bdefault)
        time.sleep(0.75)
        # Grip left and right claws 
        pwm.setPWM(rgChan, 0, rGrip)
        pwm.setPWM(lgChan, 0, lGrip)
        time.sleep(0.75)

# Turn down side
def turnD(x):
    if x == 0:
        # Ungrip left and right claws
        pwm.setPWM(rgChan, 0, rUngrip)
        pwm.setPWM(lgChan, 0, lUngrip)
        time.sleep(0.75)
        # Turn front claw CCW and back claw CW (down side is now on right)
        pwm.setPWM(frChan, 0, fnCCW)
        pwm.setPWM(brChan, 0, bnCW)
        time.sleep(0.75)
        # Grip right claw
        pwm.setPWM(rgChan, 0, rGrip)
        time.sleep(0.75)
        # Turn right claw CW
        pwm.setPWM(rrChan, 0, rCW)
        time.sleep(0.75)
        # Ungrip right claw
        pwm.setPWM(rgChan, 0, rUngrip)
        time.sleep(0.75)
        # Turn right claw back
        pwm.setPWM(rrChan, 0, rdefault)
        time.sleep(0.75)
        # Turn front and back claws back (up side is now back to normal)
        pwm.setPWM(frChan, 0, fdefault)
        pwm.setPWM(brChan, 0, bdefault)
        time.sleep(0.75)
        # Grip left and right claws 
        pwm.setPWM(rgChan, 0, rGrip)
        pwm.setPWM(lgChan, 0, lGrip)
        time.sleep(0.75)
    elif x == 1:
        # Ungrip left and right claws
        pwm.setPWM(rgChan, 0, rUngrip)
        pwm.setPWM(lgChan, 0, lUngrip)
        time.sleep(0.75)
        # Turn front claw CCW and back claw CW (down side is now on right)
        pwm.setPWM(frChan, 0, fnCCW)
        pwm.setPWM(brChan, 0, bnCW)
        time.sleep(0.75)
        # Grip right claw
        pwm.setPWM(rgChan, 0, rGrip)
        time.sleep(0.75)
        # Turn right claw CW
        pwm.setPWM(rrChan, 0, rCCW)
        time.sleep(0.75)
        # Ungrip right claw
        pwm.setPWM(rgChan, 0, rUngrip)
        time.sleep(0.75)
        # Turn right claw back
        pwm.setPWM(rrChan, 0, rdefault)
        time.sleep(0.75)
        # Turn front and back claws back (up side is now back to normal)
        pwm.setPWM(frChan, 0, fdefault)
        pwm.setPWM(brChan, 0, bdefault)
        time.sleep(0.75)
        # Grip left and right claws 
        pwm.setPWM(rgChan, 0, rGrip)
        pwm.setPWM(lgChan, 0, lGrip)
        time.sleep(0.75)
    elif x == 2:
        # Ungrip left and right claws
        pwm.setPWM(rgChan, 0, rUngrip)
        pwm.setPWM(lgChan, 0, lUngrip)
        time.sleep(0.75)
        # Turn front claw CCW and back claw CW (up side is now on right)
        pwm.setPWM(frChan, 0, fnCCW)
        pwm.setPWM(brChan, 0, bnCW)
        time.sleep(0.75)
        # Grip right claw
        pwm.setPWM(rgChan, 0, rGrip)
        time.sleep(0.75)
        # Turn right claw CW
        pwm.setPWM(rrChan, 0, rCW)
        time.sleep(0.75)
        # Ungrip right claw
        pwm.setPWM(rgChan, 0, rUngrip)
        time.sleep(0.75)
        # Turn right claw back
        pwm.setPWM(rrChan, 0, rdefault)
        time.sleep(0.75)
        # Grip right claw
        pwm.setPWM(rgChan, 0, rGrip)
        time.sleep(0.75)
        # Turn right claw CW
        pwm.setPWM(rrChan, 0, rCW)
        time.sleep(0.75)
        # Ungrip right claw
        pwm.setPWM(rgChan, 0, rUngrip)
        time.sleep(0.75)
        # Turn right claw back
        pwm.setPWM(rrChan, 0, rdefault)
        time.sleep(0.75)
        # Turn front and back claws back (up side is now back to normal)
        pwm.setPWM(frChan, 0, fdefault)
        pwm.setPWM(brChan, 0, bdefault)
        time.sleep(0.75)
        # Grip left and right claws 
        pwm.setPWM(rgChan, 0, rGrip)
        pwm.setPWM(lgChan, 0, lGrip)
        time.sleep(0.75)

def rotateZ():
    # Grip front and back claws
    pwm.setPWM(fgChan, 0, fGrip)
    pwm.setPWM(bgChan, 0, bGrip)
    time.sleep(1)

    # Ungrip right and left claws 
    pwm.setPWM(rgChan, 0, servoMin)
    pwm.setPWM(lgChan, 0, servoMin)
    time.sleep(1)

    # Rotate front and back claws 
    pwm.setPWM(frChan, 0, fnCCW)
    pwm.setPWM(brChan, 0, bnCW)
    time.sleep(1)

    # Grip right and left claws 
    pwm.setPWM(rgChan, 0, rGrip)
    pwm.setPWM(lgChan, 0, lGrip)
    time.sleep(1)

    # Ungrip front and back claws 
    pwm.setPWM(fgChan, 0, servoMin)
    pwm.setPWM(bgChan, 0, servoMin)
    time.sleep(1)

    # Rotate front and back claws
    pwm.setPWM(frChan, 0, fnCW)
    pwm.setPWM(brChan, 0, bnCCW)
    time.sleep(1)

    # Grip front and back claws
    pwm.setPWM(fgChan, 0, fGrip)
    pwm.setPWM(bgChan, 0, bGrip)
    time.sleep(1)


#def rotateX():
    
