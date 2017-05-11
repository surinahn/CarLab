from controls import *
import time


# Initialize the claws

initialize()

# Close claws
userInput = ''
while userInput != 'c':
    userInput = raw_input("Press c when ready to grip: ")

close()

turnR(0)
#turnU(0)
#turnD(1)
#turnU(2)
#turnL(1)
#turnR(1)

'''
pwm.setPWM(fgChan, 0, fUngrip)
pwm.setPWM(bgChan, 0, bUngrip)
time.sleep(0.75)
pwm.setPWM(frChan, 0, fCW)
pwm.setPWM(brChan, 0, bCCW)
time.sleep(0.75)
pwm.setPWM(rrChan, 0, rCW)
pwm.setPWM(lrChan, 0, lCCW)
time.sleep(0.75)
pwm.setPWM(fgChan, 0, fGrip)
pwm.setPWM(bgChan, 0, bGrip)
time.sleep(0.75)
pwm.setPWM(rgChan, 0, rUngrip)
pwm.setPWM(lgChan, 0, lUngrip)
time.sleep(0.75)
pwm.setPWM(rrChan, 0, rdefault)
pwm.setPWM(lrChan, 0, ldefault)
time.sleep(0.75)
pwm.setPWM(lgChan, 0, lGrip)
#pwm.setPWM(rgChan, 0, rGrip)
time.sleep(0.75)
pwm.setPWM(brChan, 0, bdefault)
'''

