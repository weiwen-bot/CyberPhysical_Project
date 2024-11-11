from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from googleapiclient.http import MediaFileUpload,MediaIoBaseDownload
import io
import os
from loadcell import get_weight
from mq135 import get_gasdata
from ultrasonic import measure_distance
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime

import schedule
import time

import RPi.GPIO as GPIO
from hx711 import HX711
import time




# Function to read weight


        # Set up GPIO mode
GPIO.setmode(GPIO.BCM)

DT_PIN = 5   # Connect to Pin 29 (GPIO 5)
SCK_PIN = 6  # Connect to Pin 31 (GPIO 6)

# Initialize HX711
hx = HX711(dout_pin=DT_PIN, pd_sck_pin=SCK_PIN)
###########
hx.zero()

reading = hx.get_data_mean(readings=100)
# reading = hx.get_data_mean(readings=100)

# scale = reading/ 200
# hx.set_scale_ratio(scale)

#     # Get the average weight over 5 readings
# weight = hx.get_weight_mean()

# finally:
#     GPIO.cleanup()

if __name__ == "__main__":
    while True:
        weight = hx.get_weight_mean()
        print("Weight data ",weight)