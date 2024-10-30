import RPi.GPIO as GPIO
import time

def get_gasdata():
# Set up GPIO mode
    GPIO.setmode(GPIO.BCM)

    # Define the pin connected to the MQ135 DO
    mq135_digital_pin = 17

    # Set up the pin as input
    GPIO.setup(mq135_digital_pin, GPIO.IN)

    try:
        while True:
            gas_detected = GPIO.input(mq135_digital_pin)
            if gas_detected==GPIO.HIGH:
                return("High Gas Levels Detected!")
            else:
                return("Gas Levels Are Normal.")
    except Exception as e:
        
        print(f"Gas Error {e}")
    finally:
        GPIO.cleanup()
