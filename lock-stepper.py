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
# GpioPins = [17, 27, 22, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)


# GPIO.output(17,GPIO.LOW)
# GPIO.output(27,GPIO.LOW)
# GPIO.output(22,GPIO.LOW)
# GPIO.output(10,GPIO.LOW)


GPIO.output(18,GPIO.HIGH)
GPIO.output(23,GPIO.HIGH)
GPIO.output(24,GPIO.LOW)
GPIO.output(25,GPIO.LOW)

# while True:
#     print("hi")

# Declare an named instance of class pass a name and type of motor
# mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "Nema")
# time.sleep(0.5)

# call the function pass the parameters
# numDegrees = 180
# #17,27, 22, 10
# #True is counterclockwise
# mymotortest.motor_run(GpioPins , 0.001, degToStep(numDegrees), False, False, "half", .05)




