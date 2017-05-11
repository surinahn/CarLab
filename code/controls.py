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
fGrip = 440
rUngrip = 320
rGrip = 425
lUngrip = 400
lGrip = 500
bUngrip = 320
bGrip = 490

# PWM values for turning each side
# CW = clockwise, CCW = counter-clockwise, 2 = 180 degrees (turn twice)

fdefault = 370
fCW = 125
fCCW = 630
rdefault = 390
rCW = 125
rCCW = 640
#rCCW = 632
ldefault = 380
lCW = 125
#lCCW = 645
lCCW = 650
bdefault = 370
#bCW = 117
bCW = 112
#bCCW = 640
bCCW = 630

fnCCW = fCCW - 16
bnCW = bCW + 21

fnCW = fCW + 30 - 15
bnCCW = bCCW - 30 + 10

lnCW = lCW + 20
rnCCW = rCCW - 20

lnCCW = lCCW - 20
rnCW = rCW + 20 

#DEFAULTS
def fdefault():
    pwm.setPWM(frChan, 0, fdefault)

def bdefault():
    pwm.setPWM(brChan, 0, bdefault)

def ldefault():
    pwm.setPWM(lrChan, 0, ldefault)

def rdefault():
    pwm.setPWM(rrChan, 0, rdefault)

#CLOCKWISE WITH FRICTION 
def fCW():
    pwm.setPWM(frChan, 0, fCW)

def bCW():
    pwm.setPWM(brChan, 0, bCW)

def lCW():
    pwm.setPWM(lrChan, 0, lCW)

def rCW():
    pwm.setPWM(rrChan, 0, rCW)

#COUNTERCLOCKWISE WITH FRICTION
def fCCW():
    pwm.setPWM(frChan, 0, fCCW)

def bCCW():
    pwm.setPWM(brChan, 0, bCCW)

def lCCW():
    pwm.setPWM(lrChan, 0, lCCW)

def rCCW():
    pwm.setPWM(rrChan, 0, rCCW)
    
#CLOCKWISE NO FRICTION
def fnCW():
    pwm.setPWM(frChan, 0, fnCW)

def bnCW():
    pwm.setPWM(brChan, 0, bnCW)

def lnCW():
    pwm.setPWM(lrChan, 0, lnCW)

def rnCW():
    pwm.setPWM(rrChan, 0, rnCW)

#COUNTERCLOCKWISE NO FRICTION
def fnCCW():
    pwm.setPWM(frChan, 0, fnCCW)

def bnCCW():
    pwm.setPWM(brChan, 0, bnCCW)

def lnCCW():
    pwm.setPWM(lrChan, 0, lnCCW)

def rnCCW():
    pwm.setPWM(rrChan, 0, rnCCW)

#GRIP
def fGrip():
    pwm.setPWM(fgChan, 0, fGrip)

def bGrip():
    pwm.setPWM(bgChan, 0, bGrip)

def lGrip():
    pwm.setPWM(lgChan, 0, lGrip)

def rGrip():
    pwm.setPWM(rgChan, 0, rGrip)

#UNGRIP
def fUnGrip():
    pwm.setPWM(fgChan, 0, fUngrip)

def bUnGrip():
    pwm.setPWM(bgChan, 0, bUngrip)

def lUnGrip():
    pwm.setPWM(lgChan, 0, lUngrip)

def rUnGrip():
    pwm.setPWM(rgChan, 0, rUngrip)

#OPEN ALL THE WAY
def fOpen():
    pwm.setPWM(fgChan, 0, servoMin)

def bOpen():
    pwm.setPWM(bgChan, 0, servoMin)

def lOpen():
    pwm.setPWM(lgChan, 0, servoMin)

def rOpen():
    pwm.setPWM(rgChan, 0, servoMin)

#CLOSE ALL THE WAY
def fClose():
    pwm.setPWM(fgChan, 0, fGrip+20)

def bClose():
    pwm.setPWM(bgChan, 0, fGrip+20)

def lClose():
    pwm.setPWM(lgChan, 0, fGrip+20)

def rClose():
    pwm.setPWM(rgChan, 0, fGrip+20)

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
    pwm.setPWM(fgChan, 0, fGrip+20)
    pwm.setPWM(rgChan, 0, rGrip+20)
    pwm.setPWM(lgChan, 0, lGrip+20)
    pwm.setPWM(bgChan, 0, bGrip+10)
    time.sleep(1)
    pwm.setPWM(frChan, 0, fdefault)
    pwm.setPWM(brChan, 0, bdefault)
    time.sleep(1)
    pwm.setPWM(rrChan, 0, rdefault)
    pwm.setPWM(lrChan, 0, ldefault)
    time.sleep(1)
    pwm.setPWM(fgChan, 0, fGrip-80)
    pwm.setPWM(rgChan, 0, rGrip-80)
    pwm.setPWM(lgChan, 0, lGrip-80)
    pwm.setPWM(bgChan, 0, bGrip-80)
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

def openrl():
    pwm.setPWM(rgChan, 0, servoMin)
    pwm.setPWM(lgChan, 0, servoMin)

def openbf():
    pwm.setPWM(bgChan, 0, servoMin)
    pwm.setPWM(fgChan, 0, servoMin)
    

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
    pwm.setPWM(brChan, 0, bCW+30)
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
    # Get right claw out of the way
    pwm.setPWM(rgChan, 0, rUngrip)
    time.sleep(0.75)
    pwm.setPWM(rrChan, 0, rdefault+30)
    time.sleep(0.75)
    pwm.setPWM(rgChan, 0, rGrip)
    time.sleep(0.75)
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
    pwm.setPWM(rgChan, 0, rUngrip)
    time.sleep(0.75)
    pwm.setPWM(rrChan, 0, rdefault)
    time.sleep(0.75)
    pwm.setPWM(rgChan, 0, rGrip)

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
        pwm.setPWM(lgChan, 0, lGrip)
        time.sleep(0.75)

        # Get back claw out of the way
        pwm.setPWM(bgChan, 0, bUngrip)
        time.sleep(0.75)
        
        # Turn right claw CW
        pwm.setPWM(rrChan, 0, rCW)
        time.sleep(0.75)

        # Put back claw back
        pwm.setPWM(bgChan, 0, bGrip)
        time.sleep(0.75)
        
        # Ungrip right claw
        pwm.setPWM(rgChan, 0, rUngrip)
        time.sleep(0.75)
        # Turn right claw back
        pwm.setPWM(rrChan, 0, rdefault)
        pwm.setPWM(lgChan, 0, lUngrip)
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
        pwm.setPWM(lgChan, 0, lGrip)
        time.sleep(0.75)
        # Get back claw out of the way
        pwm.setPWM(bgChan, 0, bUngrip)
        time.sleep(0.75)
        # Turn right claw CCW
        pwm.setPWM(rrChan, 0, rCCW+10)
        time.sleep(0.75)
        # Put back claw back
        pwm.setPWM(bgChan, 0, bGrip)
        time.sleep(0.75)
        # Ungrip right claw
        pwm.setPWM(rgChan, 0, rUngrip)
        time.sleep(0.75)
        # Turn right claw back
        pwm.setPWM(rrChan, 0, rdefault)
        pwm.setPWM(lgChan, 0, lUngrip)
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
        pwm.setPWM(lgChan, 0, lGrip)
        time.sleep(0.75)
        # Get back claw out of the way
        pwm.setPWM(bgChan, 0, bUngrip)
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
        # Put back claw back
        pwm.setPWM(bgChan, 0, bGrip)
        time.sleep(0.75)
        # Ungrip right claw
        pwm.setPWM(rgChan, 0, rUngrip)
        time.sleep(0.75)
        # Turn right claw back
        pwm.setPWM(rrChan, 0, rdefault)
        pwm.setPWM(lgChan, 0, lUngrip)
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

def rotate1():
    # Rotate front and back claws 
    pwm.setPWM(frChan, 0, fnCCW)
    pwm.setPWM(brChan, 0, bnCW)
    time.sleep(1)

    pwm.setPWM(rrChan, 0, rCW)
    pwm.setPWM(lrChan, 0, lCCW)
    time.sleep(1)

    # Grip right and left claws 
    pwm.setPWM(rgChan, 0, rGrip)
    pwm.setPWM(lgChan, 0, lGrip)
    time.sleep(1)

    # Ungrip front and back claws 
    pwm.setPWM(fgChan, 0, servoMin)
    pwm.setPWM(bgChan, 0, servoMin)
    time.sleep(1)

    openbf()


def rotate2():
    pwm.setPWM(fgChan, 0, fGrip)
    pwm.setPWM(bgChan, 0, bGrip)
    time.sleep(1)

    pwm.setPWM(rgChan, 0, rUngrip)
    pwm.setPWM(lgChan, 0, lUngrip)

    pwm.setPWM(rrChan, 0, rdefault)
    pwm.setPWM(lrChan, 0, ldefault)
    time.sleep(1)

    pwm.setPWM(rgChan, 0, rGrip)
    pwm.setPWM(lgChan, 0, lGrip)
    time.sleep(1)

    # Rotate front and back claws
    openbf()
    pwm.setPWM(frChan, 0, fCW+10)
    pwm.setPWM(brChan, 0, bCCW-10)
    time.sleep(1)
    pwm.setPWM(rrChan, 0, rnCW)
    pwm.setPWM(lrChan, 0, lnCCW)
    time.sleep(1)

def rotate3():
    pwm.setPWM(fgChan, 0, fGrip)
    pwm.setPWM(bgChan, 0, bGrip)
    time.sleep(1)

    openrl()
    pwm.setPWM(rrChan, 0, rdefault)
    pwm.setPWM(lrChan, 0, ldefault)
    time.sleep(1)

    pwm.setPWM(frChan, 0, fdefault)
    pwm.setPWM(brChan, 0, bdefault)
    time.sleep(1)

def rotate4():
    pwm.setPWM(rgChan, 0, rGrip)
    pwm.setPWM(lgChan, 0, lGrip)
    time.sleep(1)

    openbf()
    time.sleep(1)
    pwm.setPWM(frChan, 0, fCW)
    pwm.setPWM(brChan, 0, bCCW)
    time.sleep(1)

    pwm.setPWM(rrChan, 0, rnCW)
    pwm.setPWM(lrChan, 0, lnCCW)
    time.sleep(1)

    pwm.setPWM(fgChan, 0, fGrip)
    pwm.setPWM(bgChan, 0, bGrip)
    time.sleep(1)

    openrl()
    pwm.setPWM(rrChan, 0, rdefault)
    pwm.setPWM(lrChan, 0, ldefault)
    time.sleep(1)

    pwm.setPWM(rgChan, 0, rGrip)
    pwm.setPWM(lgChan, 0, lGrip)
    time.sleep(1)

    openbf()
    pwm.setPWM(frChan, 0, fdefault)
    pwm.setPWM(brChan, 0, bdefault)
    time.sleep(1)

    pwm.setPWM(fgChan, 0, fGrip)
    pwm.setPWM(bgChan, 0, bGrip)
    time.sleep(1)
