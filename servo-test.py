
import RPi.GPIO as GPIO
import time
from time import sleep
from gpiozero import AngularServo

# # with servo logo facing you...
# # duty of 3.5-6.8 is cw rotation where 3.5 is fast and 6.8 is slow
# # duty of 7.5-11.5 is ccw rotation where 7.5 is slow and 11.5 is fast
# def set_speed(percent, direction):
#     frac = percent / 100
#     if percent == 0:
#         duty = 0
#     elif direction == "cw":
#         duty = 6.8 - ((6.8 - 3.5) * frac)
#     elif direction == "ccw":
#         duty = 7.5 + ((11.5 - 7.5) * frac)
#     return duty

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(16, GPIO.OUT)
# p = GPIO.PWM(16, 50)
# p.start(5)

# # p.ChangeDutyCycle(set_speed(25, "cw"))
# # time.sleep(2)
# # # p.ChangeDutyCycle(set_speed(75, "cw"))
# # # time.sleep(2)
# # p.ChangeDutyCycle(set_speed(100, "cw"))
# # time.sleep(2)
# # p.ChangeDutyCycle(0)
# # time.sleep(2)
# p.ChangeDutyCycle(set_speed(20, "cw"))
# time.sleep(0.1)
# p.ChangeDutyCycle(set_speed(0, "cw"))

# # p.ChangeDutyCycle(set_speed(75, "ccw"))
# # time.sleep(2)
# # p.ChangeDutyCycle(14)
# # time.sleep(2)

# # p.ChangeDutyCycle(11.5)
# # time.sleep(2)
# # p.ChangeDutyCycle(0)
# # time.sleep(2)
# # p.ChangeDutyCycle(5) # may need to be adjusted
# # time.sleep(2)
# # p.ChangeDutyCycle(0)
# # time.sleep(2)
# # p.ChangeDutyCycle(6.5)
# # time.sleep(2)
# # p.ChangeDutyCycle(6.8) # may need to be adjusted
# # time.sleep(2)





# # import RPi.GPIO as GPIO
# # import servo

# # GPIO.setmode(GPIO.BCM)

# # s=servo.ContinuousServo(16,700,1500,2300,50)

# # s.speed(25)











# # from gpiozero import Servo
# # from gpiozero import AngularServo
# # from time import sleep

# # servo = Servo(38)
# # # min_angle=-180, max_angle=180
# # try:
# #     servo.value = 0.0
# #     sleep(.1)
# #     servo.value = 1

# # except KeyboardInterrupt:
# # 	print("Program stopped")


#### Kelly's code
# import RPi.GPIO as gp  
# from time import sleep  
# gp.setmode(gp.BOARD)  

# # This is for the kicker
# gp.setup(38,gp.OUT)  
# pwm=gp.PWM(38,50)  
# pwm.start(0)  
# for i in range(0,181):
#     sig=(i/18)+2  
#     pwm.ChangeDutyCycle(sig)  
#     print("here")
#     sleep(0.01)  
# for i in range(180,-1,-1):  
#     sig=(i/18)+2  
#     pwm.ChangeDutyCycle(sig)  
#     sleep(0.01)  
# pwm.stop()  
# gp.cleanup()

# servo = AngularServo(20, min_angle=-90, max_angle=90)

# try:
#     while True:
#         print(servo.angle)
#         servo.min()
#         time.sleep(1)
#         print(servo.angle)
#         servo.max()
#         time.sleep(1)
# except KeyboardInterrupt:
#     print("Program stopped")

from gpiozero import Servo
import RPi.GPIO as GPIO
import time
from time import sleep
from gpiozero import AngularServo
# from time import sleep

servo = Servo(16)
up_val = 0.34
down_val = 0.75

try:
    servo.value = down_val
    while True:
        sleep(0.5)
        servo.value = up_val
        sleep(0.1)
        servo.value = down_val
        sleep(2)
except KeyboardInterrupt:
	print("Program stopped")