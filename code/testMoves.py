from controls import *
import time


# Initialize the claws

initialize()

# Close claws
userInput = ''
while userInput != 'c':
    userInput = raw_input("Press c when ready to grip: ")

close()

##print "0"
##rotate0()
##sleep(2)
##print "1" 
##rotate1()
##sleep(2)
##print "2" 
##rotate2()
##sleep(2)
##print "1" 
##rotate1()
##sleep(2)

turnF(2)
turnR(2)
turnB(2)
turnL(2)
turnU(2)
turnD(2)
