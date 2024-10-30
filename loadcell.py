import RPi.GPIO as GPIO
from hx711 import HX711
import time




# Function to read weight
def get_weight():

        # Set up GPIO mode
    GPIO.setmode(GPIO.BCM)

    # Define the pins for DT and SCK (connect these to the Raspberry Pi)
    DT_PIN = 5   # Connect to Pin 29 (GPIO 5)
    SCK_PIN = 6  # Connect to Pin 31 (GPIO 6)

    # Initialize HX711
    hx = HX711(dout_pin=DT_PIN, pd_sck_pin=SCK_PIN)
    # List all attributes and methods
    print(dir(hx))

    # Get help on a specific function (if you think it might be named differently)
    help(hx.getweightmean)  # Replace with the actual function name you are trying to use

    # Reset the HX711 and tare the scale
    hx.reset()   # Reset the HX711
    print(hx)
    hx.tare()    # Tare the scale (set baseline to 0)

    try:
        # Get the average weight over 5 readings
        weight = hx.get_weight_mean(5)
        return weight
    except Exception as e:
        print(f"Error reading weight: {e}")
        return None
    finally:
        GPIO.cleanup()

# try:
#     while True:
#         # Read and print the weight
#         weight = get_weight()
#         if weight is not None:
#             print(f"Weight: {weight:.2f} grams")
#         else:
#             print("Failed to read weight.")
#         time.sleep(1)  # Wait for 1 second before the next reading

# except KeyboardInterrupt:
#     print("Measurement stopped by user.")

# finally:
#     # Clean up GPIO pins before exiting
#     GPIO.cleanup()
