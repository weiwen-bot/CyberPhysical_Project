import RPi.GPIO as GPIO
import time


# Define the pin connected to the MQ135 DO
mq135_digital_pin = 27
GPIO.setmode(GPIO.BCM)
# Set up the pin as input
GPIO.setup(mq135_digital_pin, GPIO.IN)
try:
    while True:
        gas_detected = GPIO.input(mq135_digital_pin)
        if gas_detected:
            print("Gas Levels Are Normal.")
        else:
            
            print("High Gas Levels Detected!")
finally:
    print("Cleaning up")
    GPIO.cleanup()