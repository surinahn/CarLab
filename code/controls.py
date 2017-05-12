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
fGrip = 430
rUngrip = 320
rGrip = 415
lUngrip = 400
lGrip = 490
bUngrip = 320
bGrip = 480

# PWM values for turning each side
# CW = clockwise, CCW = counter-clockwise, 2 = 180 degrees (turn twice)

fdefault = 370
fCW = 125
fCCW = 635
rdefault = 390
rCW = 125
rCCW = 640
#rCCW = 632
ldefault = 380
lCW = 125
#lCCW = 645
lCCW = 648
bdefault = 370
#bCW = 117
bCW = 112
#bCCW = 640
bCCW = 622

fnCCW = fCCW - 16
bnCW = bCW + 21

fnCW = fCW + 30 - 15
bnCCW = bCCW - 30 + 10

lnCW = lCW + 20
rnCCW = rCCW - 20

lnCCW = lCCW - 20
rnCW = rCW + 20

#DEFAULTS
def F_Default():
    pwm.setPWM(frChan, 0, fdefault)

def B_Default():
    pwm.setPWM(brChan, 0, bdefault)

def L_Default():
    pwm.setPWM(lrChan, 0, ldefault)

def R_Default():
    pwm.setPWM(rrChan, 0, rdefault)

#CLOCKWISE WITH FRICTION 
def F_CW():
    pwm.setPWM(frChan, 0, fCW)

def B_CW():
    pwm.setPWM(brChan, 0, bCW)

def L_CW():
    pwm.setPWM(lrChan, 0, lCW)

def R_CW():
    pwm.setPWM(rrChan, 0, rCW)

#COUNTERCLOCKWISE WITH FRICTION
def F_CCW():
    pwm.setPWM(frChan, 0, fCCW)

def B_CCW():
    pwm.setPWM(brChan, 0, bCCW)

def L_CCW():
    pwm.setPWM(lrChan, 0, lCCW)

def R_CCW():
    pwm.setPWM(rrChan, 0, rCCW)
    
#CLOCKWISE NO FRICTION
def F_n_CW():
    pwm.setPWM(frChan, 0, fnCW)

def B_n_CW():
    pwm.setPWM(brChan, 0, bnCW)

def L_n_CW():
    pwm.setPWM(lrChan, 0, lnCW)

def R_n_CW():
    pwm.setPWM(rrChan, 0, rnCW)

#COUNTERCLOCKWISE NO FRICTION
def F_n_CCW():
    pwm.setPWM(frChan, 0, fnCCW)

def B_n_CCW():
    pwm.setPWM(brChan, 0, bnCCW)

def L_n_CCW():
    pwm.setPWM(lrChan, 0, lnCCW)

def R_n_CCW():
    pwm.setPWM(rrChan, 0, rnCCW)

#GRIP
def F_Grip():
    pwm.setPWM(fgChan, 0, fGrip)

def B_Grip():
    pwm.setPWM(bgChan, 0, bGrip)

def L_Grip():
    pwm.setPWM(lgChan, 0, lGrip)

def R_Grip():
    pwm.setPWM(rgChan, 0, rGrip)

#UNGRIP
def F_Ungrip():
    pwm.setPWM(fgChan, 0, fUngrip)

def B_Ungrip():
    pwm.setPWM(bgChan, 0, bUngrip)

def L_Ungrip():
    pwm.setPWM(lgChan, 0, lUngrip)

def R_Ungrip():
    pwm.setPWM(rgChan, 0, rUngrip)

#OPEN ALL THE WAY
def F_Open():
    pwm.setPWM(fgChan, 0, servoMin)

def B_Open():
    pwm.setPWM(bgChan, 0, servoMin)

def L_Open():
    pwm.setPWM(lgChan, 0, servoMin)

def R_Open():
    pwm.setPWM(rgChan, 0, servoMin)

#CLOSE ALL THE WAY
def F_Close():
    pwm.setPWM(fgChan, 0, fGrip+20)

def B_Close():
    pwm.setPWM(bgChan, 0, bGrip+20)

def L_Close():
    pwm.setPWM(lgChan, 0, lGrip+20)

def R_Close():
    pwm.setPWM(rgChan, 0, rGrip+20)

def insert_cube():
    pwm.setPWM(fgChan, 0, fGrip-80)
    pwm.setPWM(rgChan, 0, rGrip-80)
    pwm.setPWM(lgChan, 0, lGrip-80)
    pwm.setPWM(bgChan, 0, bGrip-80)

def sleep(t):
    time.sleep(t)

# Initialize PWM
# Make sure all claws are gripped and properly rotated
def initialize():
    # Initialise the PWM device using the default address
    pwm = PWM(0x40)
    pwm.setPWMFreq(60) # Set frequency to 60 Hz

    print "Hello, I'm Ruby the Rubik's Cube Robot!"
    print '\n'

    F_Open()
    B_Open()
    L_Open()
    R_Open()
    sleep(2)
    
    F_Close()
    B_Close()
    sleep(0.5)
    F_Default()
    B_Default()
    sleep(1)

    L_Close()
    R_Close()
    sleep(0.5)
    L_Default()
    R_Default()
    sleep(1)

    insert_cube()
    

def close():
    F_Grip()
    B_Grip()
    R_Grip()
    L_Grip()

    F_Default()
    B_Default()
    R_Default()
    L_Default()
    sleep(1)

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
        F_CW() 
        sleep(0.75)
        # Ungrip claw
        F_Ungrip() 
        sleep(0.75)
        # Turn claw back
        F_Default() 
        sleep(0.75)
        # Grip claw
        F_Grip() 
        sleep(0.75)
    elif x == 1:
        # Turn claw
        F_CCW() 
        sleep(0.75)
        # Ungrip claw
        F_Ungrip() 
        sleep(0.75)
        # Turn claw back
        F_Default() 
        sleep(0.75)
        # Grip claw
        F_Grip() 
        sleep(0.75)
    elif x == 2:
        # Ungrip claw
        F_Ungrip() 
        sleep(0.75)
        # Turn claw
        F_n_CCW() 
        sleep(0.75)
        # Grip claw
        F_Grip() 
        sleep(0.75)
        # Turn claw
        F_Default()
        sleep(0.5)
        F_CW() 
        sleep(0.75)
        # Ungrip claw
        F_Ungrip() 
        sleep(0.75)
        # Turn claw back
        F_Default() 
        sleep(0.75)
        # Grip claw
        F_Grip() 
        sleep(0.75)

# Turn right side
def turnR(x):
    
    if x == 0:
        # Turn claw
        R_CW() 
        sleep(0.75)
        # Ungrip claw
        R_Ungrip() 
        sleep(0.75)
        # Turn claw back
        R_Default() 
        sleep(0.75)
        # Grip claw
        R_Grip() 
        sleep(0.75)
    elif x == 1:
        # Turn claw
        R_CCW() 
        sleep(0.75)
        # Ungrip claw
        R_Ungrip() 
        sleep(0.75)
        # Turn claw back
        R_Default() 
        sleep(0.75)
        # Grip claw
        R_Grip() 
        sleep(0.75)
    elif x == 2:
        # Ungrip claw
        R_Ungrip() 
        sleep(0.75)
        # Turn claw
        #R_n_CCW()
        pwm.setPWM(rrChan, 0, rnCCW+10) 
        sleep(0.75)
        # Grip claw
        R_Grip() 
        sleep(0.75)
        # Turn claw
        R_Default()
        sleep(0.5)
        R_CW() 
        sleep(0.75)
        # Ungrip claw
        R_Ungrip() 
        sleep(0.75)
        # Turn claw back
        R_Default() 
        sleep(0.75)
        # Grip claw
        R_Grip() 
        sleep(0.75)

# Turn left side
def turnL(x):
    
    if x == 0:
        # Turn claw
        L_CW() 
        sleep(0.75)
        # Ungrip claw
        L_Ungrip() 
        sleep(0.75)
        # Turn claw back
        L_Default() 
        sleep(0.75)
        # Grip claw
        L_Grip() 
        sleep(0.75)
    elif x == 1:
        # Turn claw
        L_CCW() 
        sleep(0.75)
        # Ungrip claw
        L_Ungrip() 
        sleep(0.75)
        # Turn claw back
        L_Default() 
        sleep(0.75)
        # Grip claw
        L_Grip() 
        sleep(0.75)
    elif x == 2:
        # Ungrip claw
        L_Ungrip() 
        sleep(0.75)
        # Turn claw
        L_n_CCW() 
        sleep(0.75)
        # Grip claw
        L_Grip() 
        sleep(0.75)
        # Turn claw
        L_Default()
        sleep(0.5)
        L_CW() 
        sleep(0.75)
        # Ungrip claw
        L_Ungrip() 
        sleep(0.75)
        # Turn claw back
        L_Default() 
        sleep(0.75)
        # Grip claw
        L_Grip() 
        sleep(0.75)

# Turn back side
def turnB(x):
    if x == 0:
        # Turn claw
        B_CW() 
        sleep(0.75)
        # Ungrip claw
        B_Ungrip() 
        sleep(0.75)
        # Turn claw back
        B_Default() 
        sleep(0.75)
        # Grip claw
        B_Grip() 
        sleep(0.75)
    elif x == 1:
        # Turn claw
        B_CCW() 
        sleep(0.75)
        # Ungrip claw
        B_Ungrip() 
        sleep(0.75)
        # Turn claw back
        B_Default() 
        sleep(0.75)
        # Grip claw
        B_Grip() 
        sleep(0.75)
    elif x == 2:
        # Ungrip claw
        B_Ungrip() 
        sleep(0.75)
        # Turn claw
        B_n_CCW() 
        sleep(0.75)
        # Grip claw
        B_Grip() 
        sleep(0.75)
        # Turn claw
        #B_CW()
        B_Default()
        sleep(0.5)
        B_CW()
        sleep(0.75)
        # Ungrip claw
        B_Ungrip() 
        sleep(0.75)
        # Turn claw back
        B_Default() 
        sleep(0.75)
        # Grip claw
        B_Grip() 
        sleep(0.75)

# Turn up side
def turnU(x):
    if x == 0:
        # Ungrip front and back claws
        F_Ungrip()
        B_Ungrip()
        sleep(0.75)
        # Rotate entire cube with left/right claws
        R_n_CCW()
        L_n_CW()
        sleep(0.75)
        # Grip front and back claws
        F_Grip()
        sleep(0.5)
        B_Grip()
        sleep(0.75)
        # Get left and right claws out of the way
        R_Ungrip()
        L_Ungrip()
        sleep(0.75)
        R_Default()
        L_Default()
        sleep(0.75)
        R_Grip()
        L_Grip()
        sleep(0.75)
        # Turn up side with front claw
        F_CW()
        sleep(0.75)
        # Ungrip front and back claws
        B_Ungrip()
        F_Ungrip()
        sleep(0.75)
        # Turn front claw back
        F_Default()
        sleep(0.75)
        # Rotate entire cube back
        R_n_CW()
        L_n_CCW()
        sleep(0.75)
        # Grip front and back claws
        B_Grip()
        sleep(0.5)
        F_Grip()
        sleep(0.75)
        # Ungrip left and right claws  and turn them back to default
        R_Ungrip()
        L_Ungrip()
        sleep(0.75)
        R_Default()
        L_Default()
        sleep(0.75)
        R_Grip()
        L_Grip()
        sleep(0.75)
        
        
    elif x == 1:
        # Ungrip front and back claws
        F_Ungrip()
        B_Ungrip()
        sleep(0.75)
        # Rotate entire cube with left/right claws
        R_n_CCW()
        L_n_CW()
        sleep(0.75)
        # Grip front and back claws
        F_Grip()
        sleep(0.5)
        B_Grip()
        sleep(0.75)
        # Get left and right claws out of the way
        R_Ungrip()
        L_Ungrip()
        sleep(0.75)
        R_Default()
        L_Default()
        sleep(0.75)
        R_Grip()
        L_Grip()
        sleep(0.75)
        # Turn up side with front claw
        F_CCW()
        sleep(0.75)
        # Ungrip front and back claws
        B_Ungrip()
        F_Ungrip()
        sleep(0.75)
        # Turn front claw back
        F_Default()
        sleep(0.75)
        # Rotate entire cube back
        R_n_CW()
        L_n_CCW()
        sleep(0.75)
        # Grip front and back claws
        B_Grip()
        sleep(0.5)
        F_Grip()
        sleep(0.75)
        # Ungrip left and right claws  and turn them back to default
        R_Ungrip()
        L_Ungrip()
        sleep(0.75)
        R_Default()
        L_Default()
        sleep(0.75)
        R_Grip()
        L_Grip()
        sleep(0.75)
        
    elif x == 2:
        # Ungrip front and back claws
        F_Ungrip()
        B_Ungrip()
        sleep(0.75)
        # Rotate entire cube with left/right claws
        R_n_CCW()
        L_n_CW()
        sleep(0.75)
        # Grip front and back claws
        F_Grip()
        sleep(0.5)
        B_Grip()
        sleep(0.75)
        # Get left and right claws out of the way
        R_Ungrip()
        L_Ungrip()
        sleep(0.75)
        R_Default()
        L_Default()
        sleep(0.75)
        R_Grip()
        L_Grip()
        sleep(0.75)
        # Turn up side with front claw
        F_Ungrip()
        sleep(0.75)
        F_n_CCW()
        sleep(0.75)
        F_Grip()
        sleep(0.75)
        F_Default()
        sleep(0.5)
        F_CW()
        sleep(0.75)
        # Ungrip front and back claws
        B_Ungrip()
        F_Ungrip()
        sleep(0.75)
        # Turn front claw back
        F_Default()
        sleep(0.75)
        # Rotate entire cube back
        R_n_CW()
        L_n_CCW()
        sleep(0.75)
        # Grip front and back claws
        B_Grip()
        sleep(0.5)
        F_Grip()
        sleep(0.75)
        # Ungrip left and right claws  and turn them back to default
        R_Ungrip()
        L_Ungrip()
        sleep(0.75)
        R_Default()
        L_Default()
        sleep(0.75)
        R_Grip()
        L_Grip()
        sleep(0.75)
        

# Turn down side
def turnD(x):
    if x == 0:
        # Ungrip front and back claws
        F_Ungrip()
        B_Ungrip()
        sleep(0.75)
        # Rotate entire cube with left/right claws
        R_n_CCW()
        L_n_CW()
        sleep(0.75)
        # Grip front and back claws
        F_Grip()
        sleep(0.5)
        B_Grip()
        sleep(0.75)
        # Get left and right claws out of the way
        R_Ungrip()
        L_Ungrip()
        sleep(0.75)
        R_Default()
        L_Default()
        sleep(0.75)
        R_Grip()
        L_Grip()
        sleep(0.75)
        # Turn up side with back claw
        B_CW()
        sleep(0.75)
        # Ungrip front and back claws
        B_Ungrip()
        F_Ungrip()
        sleep(0.75)
        # Turn back claw back
        B_Default()
        sleep(0.75)
        # Rotate entire cube back
        R_n_CW()
        L_n_CCW()
        sleep(0.75)
        # Grip front and back claws
        B_Grip()
        sleep(0.5)
        F_Grip()
        sleep(0.75)
        # Ungrip left and right claws  and turn them back to default
        R_Ungrip()
        L_Ungrip()
        sleep(0.75)
        R_Default()
        L_Default()
        sleep(0.75)
        R_Grip()
        L_Grip()
        sleep(0.75)
        
        
    elif x == 1:
        # Ungrip front and back claws
        F_Ungrip()
        B_Ungrip()
        sleep(0.75)
        # Rotate entire cube with left/right claws
        R_n_CCW()
        L_n_CW()
        sleep(0.75)
        # Grip front and back claws
        F_Grip()
        sleep(0.5)
        B_Grip()
        sleep(0.75)
        # Get left and right claws out of the way
        R_Ungrip()
        L_Ungrip()
        sleep(0.75)
        R_Default()
        L_Default()
        sleep(0.75)
        R_Grip()
        L_Grip()
        sleep(0.75)
        # Turn up side with back claw
        B_CCW()
        sleep(0.75)
        # Ungrip front and back claws
        B_Ungrip()
        F_Ungrip()
        sleep(0.75)
        # Turn back claw back
        B_Default()
        sleep(0.75)
        # Rotate entire cube back
        R_n_CW()
        L_n_CCW()
        sleep(0.75)
        # Grip front and back claws
        B_Grip()
        sleep(0.5)
        F_Grip()
        sleep(0.75)
        # Ungrip left and right claws  and turn them back to default
        R_Ungrip()
        L_Ungrip()
        sleep(0.75)
        R_Default()
        L_Default()
        sleep(0.75)
        R_Grip()
        L_Grip()
        sleep(0.75)
        
    elif x == 2:
        # Ungrip front and back claws
        F_Ungrip()
        B_Ungrip()
        sleep(0.75)
        # Rotate entire cube with left/right claws
        R_n_CCW()
        L_n_CW()
        sleep(0.75)
        # Grip front and back claws
        F_Grip()
        sleep(0.5)
        B_Grip()
        sleep(0.75)
        # Get left and right claws out of the way
        R_Ungrip()
        L_Ungrip()
        sleep(0.75)
        R_Default()
        L_Default()
        sleep(0.75)
        R_Grip()
        L_Grip()
        sleep(0.75)
        # Turn up side with back claw
        B_Ungrip()
        sleep(0.75)
        B_n_CCW()
        sleep(0.75)
        B_Grip()
        sleep(0.75)
        B_Default()
        sleep(0.5)
        B_CW()
        sleep(0.75)
        # Ungrip front and back claws
        B_Ungrip()
        F_Ungrip()
        sleep(0.75)
        # Turn back claw back
        B_Default()
        sleep(0.75)
        # Rotate entire cube back
        R_n_CW()
        L_n_CCW()
        sleep(0.75)
        # Grip front and back claws
        B_Grip()
        sleep(0.5)
        F_Grip()
        sleep(0.75)
        # Ungrip left and right claws  and turn them back to default
        R_Ungrip()
        L_Ungrip()
        sleep(0.75)
        R_Default()
        L_Default()
        sleep(0.75)
        R_Grip()
        L_Grip()
        sleep(0.75)

def rotate0():
    # Ungrip R and L and turn them to grip hoizontally
    R_Ungrip()
    L_Ungrip()
    sleep(.75)
    R_n_CW()
    L_n_CCW()
    sleep(.75)
    R_Grip()
    L_Grip()

    #move F and B out of the way 
    sleep(.75)
    F_Open()
    B_Open()
    sleep(.5)

def rotate1():
    #Grip vertically with F and B
    B_Grip()
    sleep(.5)
    F_Grip()
    sleep(.75)

    #get R and L out of the way 
    R_Ungrip()
    L_Ungrip()
    sleep(.75)
    R_Default()
    L_Default()
    sleep(.75) 
    
    # Rotate entire cube with F and B 
    F_n_CCW()
    B_n_CW()
    sleep(.75)

    R_Grip() 
    sleep(.5)
    L_Grip() 
    sleep(.75)

    R_Open()
    L_Open() 



def rotate2():
    #Grip Vertically with R and L
    L_Grip() 
    sleep(.5)
    R_Grip() 
    sleep(.5)


    #Ungrip B and F and get them out of the way
    F_Ungrip()
    B_Ungrip()
    sleep(.75)
    F_Default()
    B_Default()
    sleep(.75)

    #Rotate cube with R and L
    R_n_CW()
    L_n_CCW()
    sleep(.75)



