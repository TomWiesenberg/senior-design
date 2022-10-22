import time 
import RPi.GPIO as GPIO

# This code snippet is for Version 1.2 

# import the library
from RpiMotorLib import RpiMotorLib


def degToStep(degrees):
    #7.2 degrees per step sequence
    steps = degrees/7.2
    return steps

GpioPins = [18, 23, 24, 25]

# Declare an named instance of class pass a name and type of motor
mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "Nema")
time.sleep(0.5)

# call the function pass the parameters
numDegrees = 360
mymotortest.motor_run(GpioPins , 0.001, degToStep(numDegrees), False, False, "half", .05)




