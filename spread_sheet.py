import gspread
from google.oauth2.service_account import Credentials

def init_spreadsheet(credential_api):
    SCOPE = ['https://www.googleapis.com/auth/spreadsheets' , 'https://www.googleapis.com/auth/drive']
    credential = Credentials.from_service_account_file(credential_api , scopes=SCOPE)
    return credential

def get_spreadsheet(credential):
    gc = gspread.authorize(credential)
    return gc