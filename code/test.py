#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Test Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x40)

servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096


pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

time.sleep(2)
pwm.setPWM(4, 0, 400)
pwm.setPWM(0, 0, servoMin)
pwm.setPWM(1, 0, servoMin)
time.sleep(2)
pwm.setPWM(0, 0, servoMin+350)
pwm.setPWM(1, 0, servoMin+280)
time.sleep(2)
pwm.setPWM(4, 0, servoMin)
time.sleep(2)
pwm.setPWM(4, 0, servoMax)


'''
time.sleep(1)
pwm.setPWM(4, 0, servoMin)
time.sleep(1)
pwm.setPWM(4, 0, servoMin + 300)
'''



