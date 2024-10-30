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
    baseline = 34705 -1800 -930
    raw_data = sum(hx.get_raw_data(100))/100
    agg_weight = (raw_data) + baseline

    # known_weight_reading = -34500 - baseline
    print(f"RAW VALUE NOT SCALED {raw_data/(raw_data/220)}")


    scaling_factor = -0.36

    try:
        # Get the average weight over 5 readings
        weight = agg_weight * scaling_factor
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
