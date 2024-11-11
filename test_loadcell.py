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

if __name__ == "__main__":
    while True:
        print("Getting Weight Data")
        weight_data = get_weight()
        print(f"Weight {weight_data}, Type: {type(weight_data)}")
        if type(weight_data) == list:
            weight_data = weight_data[0]
        print(f"Weight {weight_data}")