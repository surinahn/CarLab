from controls import *
import time


# Initialize the claws
pwm.setPWM(lgChan, 0, lGrip)
pwm.setPWM(rgChan, 0, rGrip)
pwm.setPWM(fgChan, 0, fUngrip)
pwm.setPWM(bgChan, 0, bUngrip+30)
pwm.setPWM(frChan, 0, fnCW)
pwm.setPWM(brChan, 0, bnCCW-20)
pwm.setPWM(rrChan, 0, rnCCW+10)
pwm.setPWM(lrChan, 0, lnCW-10)
pwm.setPWM(fgChan, 0, fGrip-30)
pwm.setPWM(bgChan, 0, bGrip-30) 

initialize()

# Close claws
userInput = ''
while userInput != 'c':
    userInput = raw_input("Press c when ready to grip: ")

close()

#turnR(0)
#turnU(0)
#turnD(1)
#turnU(2)
#turnL(1)
#turnR(1)

pwm.setPWM(fgChan, 0, fUngrip)
pwm.setPWM(bgChan, 0, bUngrip)
time.sleep(0.75)
pwm.setPWM(frChan, 0, fnCW)
pwm.setPWM(brChan, 0, bnCCW)
time.sleep(0.75)
pwm.setPWM(rrChan, 0, rnCW+15)
pwm.setPWM(lrChan, 0, lnCCW-15)
time.sleep(2)

pwm.setPWM(fgChan, 0, fGrip)
pwm.setPWM(bgChan, 0, bGrip)
time.sleep(0.75)
##pwm.setPWM(rgChan, 0, rUngrip)
##pwm.setPWM(lgChan, 0, lUngrip)
##time.sleep(0.75)
##pwm.setPWM(rrChan, 0, rdefault)
##pwm.setPWM(lrChan, 0, ldefault)
##time.sleep(0.75)
##pwm.setPWM(lgChan, 0, lGrip)
#pwm.setPWM(rgChan, 0, rGrip)
##time.sleep(0.75)
##pwm.setPWM(brChan, 0, bdefault)


