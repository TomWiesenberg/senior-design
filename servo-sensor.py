
import RPi.GPIO as GPIO
import time
from time import sleep
from gpiozero import Servo
from gpiozero import AngularServo


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

GPIO.setmode(GPIO.BCM)
servo = Servo(16)
up_val = 0.34
down_val = 0.75
# p.start(5)
# p.ChangeDutyCycle(0)
BEAM_PIN = 26
state = 1
print("state ", state)
def break_beam_callback(channel):
    # print(GPIO.input(BEAM_PIN))
    state = GPIO.input(BEAM_PIN)
    print("state ", state)

    # if GPIO.input(BEAM_PIN):
    #     print("not broken")
    #     try:
    servo.value = down_val
    sleep(0.5)
    servo.value = up_val
    sleep(0.1)
    servo.value = down_val
    sleep(2)
    #     except KeyboardInterrupt:
    #         print("Program stopped")
    # else:
    #     sleep(5)
    #     print("broken")
       

GPIO.setmode(GPIO.BCM)
GPIO.setup(BEAM_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# I think that this might need to be in a loop once input goes away


GPIO.add_event_detect(BEAM_PIN, GPIO.BOTH, callback=break_beam_callback)

while True:
    pass
# message = input("Press enter to quit\n\n")
# GPIO.cleanup()