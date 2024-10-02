import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

try:
    while True:
        # Read the digital output (HIGH or LOW)
        if GPIO.input(17):
            print("TRUE")
        else:
            print("FALSE")
        
        sleep(1)


finally:
    print("Cleaning up")
    GPIO.cleanup()


# vcc - 2
# GND - 6
# DO - 17