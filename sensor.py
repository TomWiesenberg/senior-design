
import RPi.GPIO as GPIO

BEAM_PIN = 26

def break_beam_callback(channel):
    if GPIO.input(BEAM_PIN):
        print("not broken")
    else:
        print("broken")

GPIO.setmode(GPIO.BCM)
GPIO.setup(BEAM_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(BEAM_PIN, GPIO.BOTH, callback=break_beam_callback)

while True:
    pass
GPIO.cleanup()