
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
p = GPIO.PWM(16, 50)
p.start(5)
p.ChangeDutyCycle(0)
BEAM_PIN = 26

def break_beam_callback(channel):
    if GPIO.input(BEAM_PIN):
        print("not broken")
    else:
        print("broken")

GPIO.setmode(GPIO.BCM)
GPIO.setup(BEAM_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# I think that this might need to be in a loop once input goes away


GPIO.add_event_detect(BEAM_PIN, GPIO.BOTH, callback=break_beam_callback)

while True:
    pass
# message = input("Press enter to quit\n\n")
# GPIO.cleanup()