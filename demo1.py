#spin 270
#solenoid push
#lead screw comes up
#start tightening
#lead screw comes down
#solenoid loosenes
#spin 270 other direction

import time 
import RPi.GPIO as GPIO

# import the library
from RpiMotorLib import RpiMotorLib

def degToStep(degrees):
    #7.2 degrees per step sequence
    steps = degrees/7.2
    return steps

GpioPinsLead = [18, 23, 24, 25]
GpioPinsIndex = [17, 27, 22, 10]

in1 = 14
in2 = 15
solenoid1 = 3
solenoid2 = 4

GPIO.setmode(GPIO.BCM)

#pin initilization
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(20, GPIO.IN)
GPIO.setup(solenoid1, GPIO.OUT)
GPIO.setup(solenoid2, GPIO.OUT)

#set both motor pins low
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(solenoid1,GPIO.LOW)
GPIO.output(solenoid2,GPIO.LOW)


# Declare an named instance of class pass a name and type of motor
leadMotor = RpiMotorLib.BYJMotor("Lead", "Nema")
indexMotor = RpiMotorLib.BYJMotor("Index", "Nema")
time.sleep(0.5)

# call the function pass the parameters
numDegrees = 270
#17,27, 22, 10
##need to check direction
# indexMotor.motor_run(GpioPinsIndex , 0.01, degToStep(numDegrees), False, False, "half", .05)
# time.sleep(0.5)

# #solenoid push
# # GPIO.output(solenoid2,GPIO.HIGH)
# # time.sleep(0.5)

numDegrees2 = 2800
## need to check direction
leadMotor.motor_run(GpioPinsLead , 0.001, degToStep(numDegrees2), True, False, "half", .05)
time.sleep(0.5)

# ##start tightening
# #set 1 pin high
# GPIO.output(in1,GPIO.HIGH)
# while True:
#     voltage = GPIO.input(20)
#     print("voltage: ", voltage)
#     if (voltage == 1):
#         GPIO.output(in1,GPIO.LOW)
#         break
# time.sleep(0.5)

# ## need to check direction
# # leadMotor.motor_run(GpioPinsLead , 0.001, degToStep(numDegrees), True, False, "half", .05)
# time.sleep(0.5)

# #solenoid loosens
# GPIO.output(solenoid1, GPIO.LOW)
# GPIO.output(solenoid2,GPIO.HIGH)


# #spin 270 other direction -- direction needs to be checked
# indexMotor.motor_run(GpioPinsIndex , 0.01, degToStep(numDegrees), True, False, "half", .05)
