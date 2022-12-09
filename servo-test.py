from gpiozero import Servo
from gpiozero import AngularServo
from time import sleep

servo = Servo(16)
# min_angle=-180, max_angle=180
try:
    servo.value = 0.0
    sleep(.1)
    servo.value = 1

except KeyboardInterrupt:
	print("Program stopped")