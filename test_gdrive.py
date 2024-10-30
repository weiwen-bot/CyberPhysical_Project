from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from googleapiclient.http import MediaFileUpload,MediaIoBaseDownload
import io
import os

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
    uploadFile(drive_service,"test.csv")

    
