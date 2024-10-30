import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint as pp
import time
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

def auth():
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive",
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)
    client = gspread.authorize(creds)

    sheet = client.open("CPS Google Sheets").sheet1
    return sheet

def insert_data(data,sheet):
    # Get all records and determine the next empty row
    existing_data = sheet.get_all_records()
    next_row = len(existing_data) + 2  # +2 for headers and the next row

    # Insert the data into the next blank row
    sheet.insert_row(data, next_row)
    print("The row has been added at row:", next_row)

 

if __name__ == "__main__":
    load_dotenv()
    sheet = auth()
    def job():
        print("Getting Weight Data")
        weight_data = get_weight()
        print(f"Weight {weight_data}, Type: {type(weight_data)}")
        if type(weight_data) == list:
            weight_data = weight_data[0]
        print("Getting Gas Data")
        gas_data = get_gasdata()
        print(f"Gas {gas_data}")
        print("Getting Distance Data")
        dist = measure_distance()
        print(f"Distance {dist}")
        print(f"Value {[weight_data,gas_data,dist]}")

        now = datetime.now()
        # Format the date to dd-mm-yyyy
        formatted_date = now.strftime("%d-%m-%Y")
        curr_time = time.strftime("%H:%M:%S", time.localtime())
        print("Inserting Row")
        data = [weight_data,gas_data,dist,formatted_date,curr_time]
        insert_data(data,sheet)
        print("Done Upload")
    try:
        schedule.every(0.1).minutes.do(job)

    except Exception as e:
        print(e)

    while True:
        schedule.run_pending()
        time.sleep(1)