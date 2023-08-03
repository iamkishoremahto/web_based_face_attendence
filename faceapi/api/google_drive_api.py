from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload
import json
import ast
def get_service():
    key_file_location = "faceapi/secret_key/secret_key.json"
    api_name = 'drive'
    api_version = 'v3'
    scopes = ['https://www.googleapis.com/auth/drive']
    credentials = service_account.Credentials.from_service_account_file(
        key_file_location)

    scoped_credentials = credentials.with_scopes(scopes)

    # Build the service object.
    service = build(api_name, api_version, credentials=scoped_credentials)

    return service

def get_file_content(service):
    file_id = "1j_-bIB2vGJ0ku-PvraOPBteliE1f3J24"
    request = service.files().get_media(fileId=file_id)
    response = request.execute()
    return ast.literal_eval(response.decode())

def fetch_file_metadata(service, file_id):
  
    file_metadata = service.files().get(fileId=file_id).execute()
    return file_metadata

def update_file_content(service, new_content):
    file_id = "1j_-bIB2vGJ0ku-PvraOPBteliE1f3J24"
    
    updated_file = service.files().update(
        fileId=file_id,
        media_body=new_content,
    ).execute()
    



