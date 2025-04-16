import RPi.GPIO as GPIO
import sys
GPIO.setmode(GPIO.BCM)
dac = [8,11,7,1,0,5,12,6]
GPIO.setup(dac,GPIO.OUT)
def dec2bin(a,n):
    return [int(elem) for elem in bin(a)[2:].zfill(8)]

try:
    while True:
        a = input()
        if a == 'q':
            sys.exit()
        elif a.isdigit() and 0 <= int(a) <=255 and int(a)%1 == 0:
            GPIO.output(dac,dec2bin(int(a),8))
            print("{:.4f}".format(int(a)/256*3.3))
        elif not a.isdigit():
            print("input number 0-255!!")
        else:
            print("more number input (0<=   or <= 255 )")

except ValueError:
    print('input number 0-255 (cheloe)')
except KeyboardInterrupt:
    print('done')
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()
