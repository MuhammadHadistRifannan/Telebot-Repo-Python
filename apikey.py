import os
from dotenv import load_dotenv

load_dotenv() #for load .env api key file 

TELE_API = os.getenv("TELE_API")
GEMINI_API = os.getenv("GEMINI_API")
IDENTITY_BOT = os.getenv("IDENTITYBOT")
CREDENTIAL_FILE = os.getenv("SPREADSHEET_FILE")