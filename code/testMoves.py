from controls import *
import time


# Initialize the claws

initialize()

# Close claws
userInput = ''
while userInput != 'c':
    userInput = raw_input("Press c when ready to grip: ")

close()

# R_Ungrip() 
# L_Ungrip()
# sleep(.75)

#     # Rotate entire cube with F and B 
# while True: 
# 	F_n_CCW()
# 	B_n_CW()
# 	sleep(3)
# 	F_n_CW()
# 	B_n_CCW()
# 	sleep(3)

# print "0"
# rotate0()
# sleep(2)
# print "1" 
# rotate1()
# sleep(2)
# print "2" 
# rotate2()
# sleep(2)
# print "1" 
# rotate1()
# sleep(2)
# print "2" 
# rotate2()
# sleep(2)
# print "1" 
# rotate1()
# sleep(2)
# print "2" 
# rotate2()
# sleep(2)
# print "1" 
# rotate1()
# sleep(2)

turnR(0)
turnF(2)
turnR(2)
turnB(2)
turnL(2)
turnU(2)
turnD(2)
