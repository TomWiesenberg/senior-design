
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.OUT)  
pwm=GPIO.PWM(20,50)  
pwm.start(0)

print("beginning of kicker code")

for j in range(5):
    
    print("starting kicker for loop")
    for i in range(0,181):
        sig=(i/18)+2  
        print("first for loop")
        pwm.ChangeDutyCycle(sig)  
        time.sleep(0.005)  
    for i in range(180,-1,-1):  
        print("second for loop")
        sig=(i/18)+2  
        pwm.ChangeDutyCycle(sig)  
        time.sleep(0.001)  
    pwm.ChangeDutyCycle(0)  
   # pwm.stop()  