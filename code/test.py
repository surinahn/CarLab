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

pwm.setPWM(2, 0, 480)


pwm.setPWM(6,0,140)


time.sleep(1)

pwm.setPWM(6, 0, 370)

time.sleep(1)

pwm.setPWM(6, 0, 630)

time.sleep(1)

pwm.setPWM(6, 0, 370)




