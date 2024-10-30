# import RPi.GPIO as GPIO
import time
import pandas as pd
import os


# Set up GPIO mode
import RPi.GPIO as GPIO

# Function to measure distance
def measure_distance():
    GPIO.setmode(GPIO.BCM)

    # Define GPIO pins
    TRIG = 23  # GPIO pin for Trig
    ECHO = 24  # GPIO pin for Echo

    # Set up the GPIO pins
    GPIO.setup(TRIG, GPIO.OUT)  # Trig pin as output
    GPIO.setup(ECHO, GPIO.IN)   # Echo pin as input

    GPIO.output(TRIG, False)
    time.sleep(2)  # Allow sensor to settle

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    start_time = time.time()
    while GPIO.input(ECHO) == 0:
        start_time = time.time()

    while GPIO.input(ECHO) == 1:
        stop_time = time.time()

    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2  # Distance in cm
    return distance

# Google Drive upload function
# def upload_to_google_drive(file_name):

#     gauth = GoogleAuth()
#     drive = GoogleDrive(gauth)

#     f = drive.CreateFile()
#     f.SetContentFile('document.txt')

#     f.Upload()
#     print('title: %s, mimeType: %s' % (f['title'], f['mimeType']))

#     # read all files, the newly uploaded file will be there
#     file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
#     for file1 in file_list:
#         print('title: %s, id: %s' % (file1['title'], file1['id']))

#     SCOPES = ['https://www.googleapis.com/auth/drive.file']
#     creds = None

#     # Token storage and authentication
#     if os.path.exists('token.json'):
#         creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
#             auth_url, _ = flow.authorization_url()
#             print(f'Please go to this URL: {auth_url}')
#             code = input('Enter the authorization code: ')
#             creds = flow.fetch_token(code=code)
        
#         # Save the credentials for the next run
#         with open('token.json', 'w') as token:
#             token.write(creds.to_json())

#     # Build the service
#     service = build('drive', 'v3', credentials=creds)

#     # File metadata and upload
#     file_metadata = {'name': file_name}
#     media = MediaFileUpload(file_name, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    
#     try:
#         file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
#         print(f'File ID: {file.get("id")} uploaded successfully to Google Drive.')
#     except Exception as e:
#         print(f'An error occurred while uploading the file: {e}')

# # Collecting distance readings
# distance_readings = []

# try:
#     # for i in range(10):  # Measure 10 times
#     #     distance = measure_distance()
#     #     print(f"Distance: {distance:.2f} cm")
#     #     distance_readings.append(distance)
#     #     time.sleep(1)

#     # Create a DataFrame and save to Excel
#     # df = pd.DataFrame(distance_readings, columns=["Distance (cm)"])
#     df = pd.DataFrame()
#     excel_file_name = 'ultrasonic_readings.xlsx'
#     df.to_excel(excel_file_name, index=False)
#     print(f'File "{excel_file_name}" created successfully.')

#     # Upload the file to Google Drive
#     upload_to_google_drive(excel_file_name)

# except Exception as e:
#     print(f'An error occurred during measurement: {e}')

# finally:
#     # Cleanup
#     GPIO.cleanup()

