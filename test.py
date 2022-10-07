import RPi.GPIO as GPIO

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


while True:
    voltage = GPIO.input(20)
    print("voltage: ", voltage)
    if (voltage == 1):
        GPIO.output(in1,GPIO.LOW)
        break
    