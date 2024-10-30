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


def setupauth():
        # Setup the Drive v3 API
        SCOPES = 'https://www.googleapis.com/auth/drive.file'
        store = file.Storage('credentials.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('client_secrets.json', SCOPES)
            creds = tools.run_flow(flow, store)
        drive_service = build('drive', 'v3', http=creds.authorize(Http()))
        return drive_service

def uploadFile(drive_service,filename):
    file_metadata = {
    'name': filename,
    'mimeType': '*/*',
    'parents':[FOLDER_ID]
    }
    media = MediaFileUpload(filename,
                            mimetype='*/*',
                            resumable=True)
    file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print ('File ID: ' + file.get('id'))


if __name__ == "__main__":
    load_dotenv()
    FOLDER_ID = os.getenv('FOLDER_ID')
    drive_service = setupauth()

    try:
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
        columns = ['Weight','Gas','Dist']
        print(f"Value {[weight_data,gas_data,dist]}")
        print("Storing DF")
        df = pd.DataFrame([weight_data,gas_data,dist], columns = columns)
        print(df,"DFFFFFF")
        print("DF Done")
        filename = "data.csv"
        df.to_csv(filename,index=False)
        print("Uploading File")
        uploadFile(drive_service,filename)
        print("Done Upload")
    except Exception as e:
        print(e)
    
    

    
