import time 
import RPi.GPIO as GPIO

# This code snippet is for Version 1.2 

# import the library
from RpiMotorLib import RpiMotorLib


def degToStep(degrees):
    #7.2 degrees per step sequence
    steps = degrees/7.2
    return steps

GpioPinsIndex = [18, 23, 24, 25]
GpioPins = [17, 27, 22, 10]

# Declare an named instance of class pass a name and type of motor
mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "Nema")
indexMotor = RpiMotorLib.BYJMotor("Index", "Nema")
time.sleep(0.5)

# call the function pass the parameters
numDegrees = 2100
# numDegrees = 280
#17,27, 22, 10
#True is counterclockwise
#True is down
mymotortest.motor_run(GpioPins , 0.001, degToStep(numDegrees), True, False, "half", .05)

import time 
import RPi.GPIO as GPIO

# This code snippet is for Version 1.2 

# import the library
from RpiMotorLib import RpiMotorLib


def degToStep(degrees):
    #7.2 degrees per step sequence
    steps = degrees/7.2
    return steps

# GpioPins = [18, 23, 24, 25]
GpioPins = [17, 27, 22, 10]

# Declare an named instance of class pass a name and type of motor
mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "Nema")
time.sleep(0.5)

# call the function pass the parameters
numDegrees = 2100
# numDegrees = 280
#17,27, 22, 10
#True is counterclockwise
#True is down
mymotortest.motor_run(GpioPins , 0.001, degToStep(numDegrees), True, False, "half", .05)

# # state 4 --> state 1 (270 degree cw turn)
index1to4 = 275
indexMotor.motor_run(GpioPinsIndex , 0.01, degToStep(index1to4), False, False, "half", .05)

#stall indexing stepper
GPIO.output(18,GPIO.HIGH)
GPIO.output(23,GPIO.HIGH)

