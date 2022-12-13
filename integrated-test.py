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
GpioPinsIndex = [18, 23, 24, 25]
GpioPinsLead = [17, 27, 22, 10]

leadMotor = RpiMotorLib.BYJMotor("Lead", "Nema")
indexMotor = RpiMotorLib.BYJMotor("Index", "Nema")
time.sleep(0.5)

# DC motor
in1 = 14
in2 = 15
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)


#set both motor pins low
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

# # state 1 --> state 4 (270 degree ccw turn)
index1to4 = 275
indexMotor.motor_run(GpioPinsIndex , 0.01, degToStep(index1to4), True, False, "half", .05)

#stall stepper
GPIO.output(18,GPIO.HIGH)
GPIO.output(23,GPIO.HIGH)

# move lead screw up for capping
leadStroke = 2100
leadMotor.motor_run(GpioPinsLead , 0.001, degToStep(leadStroke), False, False, "half", .05)

# activate capping motor and check current levels
# turn DC motor on
GPIO.output(in2,GPIO.HIGH)

SHUNT_OHMS = 0.1
ina = INA219(SHUNT_OHMS, busnum=1)
ina.configure()

threshold = -500
index = 0
above_count = 0
while True:
    try:
        current_level = ina.current()
        print("Bus Current: %.3f mA" % current_level)
        # print(current_level, "mA")
        if current_level < threshold and index > 200:
            above_count +=1
            print("reached threshold")
        if above_count > 3:
            break
    except DeviceRangeError as e:
        # Current out of device range with specified shunt resistor
        print(e)
    index +=1

# turn off capping motor
GPIO.output(in2,GPIO.LOW)

# move lead screw down
leadMotor.motor_run(GpioPinsLead , 0.001, degToStep(leadStroke), True, False, "half", .05)

# unlock stepper motor
GPIO.output(17,GPIO.LOW)
GPIO.output(27,GPIO.LOW)

# Move from state 4 --> state 2 (180 cw turn)
index4to2 = 180
indexMotor.motor_run(GpioPinsIndex , 0.01, degToStep(index4to2), False, False, "half", .05)


# from time import sleep  
# GPIO.setmode(GPIO.BOARD)  

# This is for the kicker
print("beginning of kicker code")
GPIO.setup(20,GPIO.OUT)  
pwm=GPIO.PWM(20,50)  
pwm.start(0)  
print("starting kicker for loop")
for i in range(0,181):
    sig=(i/18)+2  
    pwm.ChangeDutyCycle(sig)  
    print("here")
    time.sleep(0.01)  
for i in range(180,-1,-1):  
    sig=(i/18)+2  
    pwm.ChangeDutyCycle(sig)  
    time.sleep(0.01)  
pwm.stop()  


# Move from state 2 --> state 1 (90 cw turn)
index2to1 = 90
indexMotor.motor_run(GpioPinsIndex , 0.01, degToStep(index2to1), False, False, "half", .05)

#stall stepper
GPIO.output(18,GPIO.HIGH)
GPIO.output(23,GPIO.HIGH)


#what does it need to be able to do

# start at state 1
# move 270 to state 4
# stall stepper motor so that it locks against wall
# move lead screw up for capping
# activate capping motor -- check current
# unlock stepper motor
# move lead screw down
# move to state (180 cw)
