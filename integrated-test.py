import time 
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
from ina219 import INA219
from ina219 import DeviceRangeError
from gpiozero import Servo
from gpiozero import AngularServo

def degToStep(degrees):
    #7.2 degrees per step sequence
    steps = degrees/7.2
    return steps

# with servo logo facing you...
# duty of 3.5-6.8 is cw rotation where 3.5 is fast and 6.8 is slow
# duty of 7.5-11.5 is ccw rotation where 7.5 is slow and 11.5 is fast
def set_speed(percent, direction):
    frac = percent / 100
    if percent == 0:
        duty = 0
    elif direction == "cw":
        duty = 6.8 - ((6.8 - 3.5) * frac)
    elif direction == "ccw":
        duty = 7.5 + ((11.5 - 7.5) * frac)
    return duty

def release_cap():
    servo.value = down_val
    time.sleep(0.5)
    servo.value = up_val
    time.sleep(0.1)
    servo.value = down_val
    # time.sleep(2)

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
# red LED
GPIO.setup(6, GPIO.OUT)
GPIO.output(6,GPIO.LOW)
# green LED
GPIO.setup(5, GPIO.OUT)
GPIO.output(5,GPIO.LOW)
buttonPin = 12
# button 
GPIO.setup(buttonPin, GPIO.IN)
# initialize cap servo
GPIO.setup(16, GPIO.OUT)

# kicker pin initialization
GPIO.setup(20,GPIO.OUT)  
pwm=GPIO.PWM(20,50)  

# initialize cap servo
servo = Servo(16)
# up_val = 0.34
# down_val = 0.75
up_val = 0.1
down_val = 0.9

# beam sensor initialization
BEAM_PIN = 26
GPIO.setup(BEAM_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

## MAIN LOOP
while True:
    # Turn red LED on
    GPIO.output(6, GPIO.HIGH)
    GPIO.output(5,GPIO.LOW)

    # release first cap
    release_cap()
    print("released first cap")
    # cap releasing loop
    releaseDelayTime = 5
    slideTime = 3
    start = time.time()
    while GPIO.input(BEAM_PIN):
        end = time.time()
        print(end - start)
        if (end - start) > releaseDelayTime:
            print("releasing cap now")
            release_cap()
            start = time.time()
    print("beam broken")
    
    time.sleep(slideTime)
    
    # Turn green LED on
    GPIO.output(6, GPIO.LOW)
    GPIO.output(5,GPIO.HIGH)

    # waiting for button
    while not GPIO.input(buttonPin):
        pass

    # # state 1 --> state 4 (270 degree ccw turn)
    indexingSpeed = 0.01

    index1to4 = 270
    indexMotor.motor_run(GpioPinsIndex , indexingSpeed, degToStep(index1to4), True, False, "half", .05)
    #stall stepper
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(23,GPIO.HIGH)
    # move lead screw up for capping
    leadStroke = 2400
    leadMotor.motor_run(GpioPinsLead , 0.001, degToStep(leadStroke), False, False, "half", .05)
    # activate capping motor and check current levels
    # turn DC motor on
    GPIO.output(in1,GPIO.HIGH)
    SHUNT_OHMS = 0.1

    # time.sleep(0.5)
    threshold = -500
    index = 0
    above_count = 0
    boosted = 0
    while True:
        try:
            ina = INA219(SHUNT_OHMS, busnum=1)
            ina.configure()
            current_level = ina.current()
            #print("Bus Current: %.3f mA" % current_level)

            # Current threshold reached
            if current_level < threshold and index > 200:
                above_count +=1
                print("reached threshold")
            # Capped!
            if above_count > 3:
                break
            # Misalignment, try raising lead screw slightly
            if (index > 1500) and (current_level > threshold) and (boosted < 2):
                boosted += 1
                index = 0
                # turn off capping motor
                GPIO.output(in1,GPIO.LOW)
                time.sleep(0.5)
                print("too low boosting up")
                boostStroke = 60
                leadMotor.motor_run(GpioPinsLead , 0.001, degToStep(boostStroke), False, False, "half", .05)
                time.sleep(0.5)
                # turn DC motor on
                GPIO.output(in1,GPIO.HIGH)

            
        except IOError as e:
            # Current out of device range with specified shunt resistor
            print(e)
            pass
            #break

        index +=1
    # turn off capping motor
    GPIO.output(in1,GPIO.LOW)

    # increment leadStroke based on boosts
    leadStroke = leadStroke + (boosted * 60)
    # move lead screw down
    leadMotor.motor_run(GpioPinsLead , 0.001, degToStep(leadStroke), True, False, "half", .05)
    # unlock stepper motor
    GPIO.output(17,GPIO.LOW)
    GPIO.output(27,GPIO.LOW)
    # Move from state 4 --> state 2 (180 cw turn)
    index4to2 = 180
    indexMotor.motor_run(GpioPinsIndex , indexingSpeed, degToStep(index4to2), False, False, "half", .05)
    # from time import sleep  
    # GPIO.setmode(GPIO.BOARD)  
    # This is for the kicker
    print("beginning of kicker code")

    pwm.start(0)  
    print("starting kicker for loop")
    for i in range(0,181):
        sig=(i/18)+2  
        pwm.ChangeDutyCycle(sig)  
        time.sleep(0.005)  
    for i in range(180,-1,-1):  
        sig=(i/18)+2  
        pwm.ChangeDutyCycle(sig)  
        time.sleep(0.001)  
    #pwm.stop()  
    # Move from state 2 --> state 1 (90 cw turn)
    index2to1 = 90
    indexMotor.motor_run(GpioPinsIndex , indexingSpeed, degToStep(index2to1), False, False, "half", .05)

    #stall stepper
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(23,GPIO.HIGH)
    # time.sleep(5)


    #what does it need to be able to do

    # start at state 1
    # move 270 to state 4
    # stall stepper motor so that it locks against wall
    # move lead screw up for capping
    # activate capping motor -- check current
    # unlock stepper motor
    # move lead screw down
    # move to state (180 cw)
    # move to state (180 cw)