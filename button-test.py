import time 
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
from ina219 import INA219
from ina219 import DeviceRangeError

# button 
GPIO.setmode(GPIO.BCM)
buttonPin = 12
GPIO.setup(buttonPin, GPIO.IN)
i = 0
while True:
    #print(GPIO.input(buttonPin))
    
    if GPIO.input(buttonPin) == GPIO.HIGH:
        print(i)
        print("button was pressed")
        i += 1