
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
p = GPIO.PWM(16, 50)
p.start(5)

p.ChangeDutyCycle(3.5)
time.sleep(2)
p.ChangeDutyCycle(0)
time.sleep(2)
p.ChangeDutyCycle(5) # may need to be adjusted
time.sleep(2)
p.ChangeDutyCycle(0)
time.sleep(2)
p.ChangeDutyCycle(6.5)
time.sleep(2)
p.ChangeDutyCycle(6.8) # may need to be adjusted
time.sleep(2)

# import RPi.GPIO as GPIO
# import servo

# GPIO.setmode(GPIO.BCM)

# s=servo.ContinuousServo(16,700,1500,2300,50)

# s.speed(25)











# from gpiozero import Servo
# from gpiozero import AngularServo
# from time import sleep

# servo = Servo(38)
# # min_angle=-180, max_angle=180
# try:
#     servo.value = 0.0
#     sleep(.1)
#     servo.value = 1

# except KeyboardInterrupt:
# 	print("Program stopped")


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