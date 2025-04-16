import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [8,11,7,1,0,5,12,6]
GPIO.setup(dac,GPIO.OUT)
def dec2bin(a,n):
    return [int(elem) for elem in bin(a)[2:].zfill(8)]

try:
    while True:
        T =input()
        if not T.isdigit():
            print('intput zeloe')
            continue
        t = int(T)/256/2
        for i in range(256):
            GPIO.output(dac,dec2bin(i,8))
            print("{:.4f}".format(int(i)/256*3.3))
            time.sleep(t)
        for i in range(255,-1,-1):
            GPIO.output(dac,dec2bin(i,8))
            print("{:.4f}".format(int(i)/256*3.3))
            time.sleep(t)

finally:
    GPIO.output(dac,0)
    GPIO.cleanup()