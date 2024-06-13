import os
import gspread
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Ensure the path to your gcloud application default credentials file is correct
creds_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

# Scopes required for Google Sheets API
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

# Load credentials from the environment
creds = Credentials.from_authorized_user_file(creds_path, scopes=SCOPES)

# If the credentials are expired, refresh them
if not creds.valid:
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())

# Authorize with gspread
client = gspread.authorize(creds)

# Open the Google Sheet by ID
sheet_id = os.getenv('SHEET_ID')
spreadsheet = client.open_by_key(sheet_id)

# Select the first sheet
worksheet = spreadsheet.sheet1

# Example data to write
data = [
    ["Name", "Age", "City"],
    ["Sajjad", 33, "Rotterdam"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

# Write data to the sheet
worksheet.update('A1', data)

print("Data written successfully.")
