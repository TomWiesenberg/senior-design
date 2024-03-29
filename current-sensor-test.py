#!/usr/bin/env python
from ina219 import INA219
from ina219 import DeviceRangeError
import RPi.GPIO as GPIO

SHUNT_OHMS = 0.1


def initialize():
    in1 = 14
    in2 = 15

    GPIO.setmode(GPIO.BCM)

    #pin initilization
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)
    GPIO.setup(20, GPIO.IN)

    #set both motor pins low
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)

    #set 1 pin high
    GPIO.output(in1,GPIO.HIGH)

def read():
    ina = INA219(SHUNT_OHMS, busnum=1)
    ina.configure()

    # print("Bus Voltage: %.3f V" % ina.voltage())
    try:
        print("Bus Current: %.3f mA" % ina.current())
        # print("Power: %.3f mW" % ina.power())
        # print("Shunt voltage: %.3f mV" % ina.shunt_voltage())
    except DeviceRangeError as e:
        # Current out of device range with specified shunt resistor
        print(e)


if __name__ == "__main__":
    initialize()
    while True:
        read()
    