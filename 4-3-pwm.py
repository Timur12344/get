import RPi.GPIO as GPIO
import sys
GPIO.setmode(GPIO.BCM)
dac = [8,11,7,1,0,5,12,6]
GPIO.setup(27,0)
GPIO.setup(dac,GPIO.OUT,initial=GPIO.HIGH)

pwm= GPIO.PWM(27,1000)
try:
        while True:
            DutyCicle = int(input())
            pwm.ChangeDutyCycle(DutyCicle)
            print("{:.2f}".format(DutyCicle*3.3/100))



finally:
    GPIO.output(27,0)
    GPIO.output(dac,0)
    GPIO.cleanup()