import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(23,GPIO.IN)

GPIO.output(16,GPIO.input(23))