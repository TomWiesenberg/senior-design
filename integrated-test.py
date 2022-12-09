import time 
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
from ina219 import INA219
from ina219 import DeviceRangeError

def degToStep(degrees):
    #7.2 degrees per step sequence
    steps = degrees/7.2
    return steps

#  Pin initialization
# lead screws
GpioPinsLead = [18, 23, 24, 25]
GpioPinsIndex = [17, 27, 22, 10]

leadMotor = RpiMotorLib.BYJMotor("Lead", "Nema")
indexMotor = RpiMotorLib.BYJMotor("Index", "Nema")
time.sleep(0.5)

# DC motor
in1 = 14
in2 = 15
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(20, GPIO.IN)


#set both motor pins low
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

# # state 1 --> state 4 (270 degree ccw turn)
index1to4 = 270
indexMotor.motor_run(GpioPinsIndex , 0.01, degToStep(index1to4), True, False, "half", .05)

#stall stepper
GPIO.output(17,GPIO.HIGH)
GPIO.output(27,GPIO.HIGH)

# move lead screw up for capping
leadStroke = 2150
leadMotor.motor_run(GpioPinsLead , 0.001, degToStep(leadStroke), False, False, "half", .05)

# activate capping motor and check current levels
# turn DC motor on
GPIO.output(in1,GPIO.HIGH)

SHUNT_OHMS = 0.1
ina = INA219(SHUNT_OHMS, busnum=1)
ina.configure()

threshold = -400
index = 0
while True:
    try:
        current_level = ina.current()
        print("Bus Current: %.3f mA" % current_level)
        # print(current_level, "mA")
        if current_level < threshold and index > 200:
            GPIO.output(in1,GPIO.LOW)
            print("reached threshold")
            break
    except DeviceRangeError as e:
        # Current out of device range with specified shunt resistor
        print(e)
    index +=1

# move lead screw down
leadMotor.motor_run(GpioPinsLead , 0.001, degToStep(leadStroke), True, False, "half", .05)

# unlock stepper motor
GPIO.output(17,GPIO.LOW)
GPIO.output(27,GPIO.LOW)

# Move from state 4 --> state 2 (180 cw turn)
index4to2 = 180
indexMotor.motor_run(GpioPinsIndex , 0.01, degToStep(index4to2), False, False, "half", .05)




#what does it need to be able to do

# start at state 1
# move 270 to state 4
# stall stepper motor so that it locks against wall
# move lead screw up for capping
# activate capping motor -- check current
# unlock stepper motor
# move lead screw down
# move to state (180 cw)