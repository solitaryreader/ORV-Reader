import json
import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account  # For service account authentication

# --- Configuration ---
SHARED_FOLDER_ID = '19J6wpAUaxkvlUzZbS6xigD7kzMuya9ie'  # Replace with the actual ID of your shared folder
INDEX_FILE_NAME = 'index-ch.json'
DOWNLOAD_PATH = 'downloads'
CREDENTIALS_FILE = 'scripts/side-stories-processor/credentials.json'  # Path to your client secret or service account key file
# --- End Configuration ---

def load_index(drive_service, index_file_name):
    """Loads the index file from Google Drive if it exists, otherwise returns an empty set."""
    try:
        results = drive_service.files().list(q=f"name='{index_file_name}' and trashed=false",
                                             spaces='drive').execute()
        items = results.get('files',)
        if items:
            # Assuming only one index file exists
            file_id = items[0]['id']
            request = drive_service.files().get_media(fileId=file_id)
            index_content = request.execute().decode('utf-8')
            return set(json.loads(index_content))
        else:
            return set()
    except HttpError as error:
        print(f'An error occurred while loading index: {error}')
        return set()
    except json.JSONDecodeError:
        print(f'Error decoding JSON from {index_file_name}. Starting with an empty index.')
        return set()

def save_index(drive_service, index_file_name, indexed_files):
    """Saves the updated index file to Google Drive."""
    index_content = json.dumps(list(indexed_files), indent=4)
    media = googleapiclient.http.MediaIoBaseUpload(
        io.BytesIO(index_content.encode('utf-8')),
        mimetype='application/json'
    )
    try:
        results = drive_service.files().list(q=f"name='{index_file_name}' and trashed=false",
                                             spaces='drive').execute()
        items = results.get('files',)
        if items:
            # Update existing file
            file_id = items[0]['id']
            updated_file = drive_service.files().update(fileId=file_id, media_body=media).execute()
            print(f"Updated index file: {updated_file.get('name')}, ID: {updated_file.get('id')}")
        else:
            # Create new file
            file_metadata = {'name': index_file_name}
            created_file = drive_service.files().create(body=file_metadata, media_body=media,
                                                        fields='id, name').execute()
            print(f"Created index file: {created_file.get('name')}, ID: {created_file.get('id')}")
    except HttpError as error:
        print(f'An error occurred while saving index: {error}')

def list_shared_folder_files(drive_service, folder_id):
    """Lists all files in the specified shared folder."""
    try:
        results = drive_service.files().list(q=f"'{folder_id}' in parents and trashed=false",
                                             includeItemsFromAllDrives=True,
                                             supportsAllDrives=True,
                                             fields="nextPageToken, files(id, name)").execute()
        items = results.get('files',)
        return {item['name']: item['id'] for item in items}
    except HttpError as error:
        print(f'An error occurred while listing files: {error}')
        return {}

def download_file(drive_service, file_id, file_name, download_path):
    """Downloads a file from Google Drive."""
    try:
        os.makedirs(download_path, exist_ok=True)
        file_path = os.path.join(download_path, file_name)
        request = drive_service.files().get_media(fileId=file_id)
        with open(file_path, 'wb') as fh:
            downloader = googleapiclient.http.MediaIoBaseDownload(fh, request)
            done = False
            while not done:
                status, done = downloader.next_chunk()
                print(f'Download {int(status.progress() * 100)}%.')
        print(f'Downloaded "{file_name}" to "{file_path}"')
        return True
    except HttpError as error:
        print(f'An error occurred while downloading "{file_name}": {error}')
        return False

def main():
    # Authenticate with Google Drive API
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/drive'])
    elif os.path.exists(CREDENTIALS_FILE):
        # Use service account (replace with your preferred authentication method)
        creds = service_account.Credentials.from_service_account_file(
            CREDENTIALS_FILE, scopes=['https://www.googleapis.com/auth/drive'])
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(google.auth.transport.requests.Request())
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        else:
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, ['https://www.googleapis.com/auth/drive'])
            creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

    try:
        service = build('drive', 'v3', credentials=creds)

        # Load the index file
        indexed_files = load_index(service, INDEX_FILE_NAME)
        print(f"Initial indexed files: {indexed_files}")

        # List files in the shared folder
        shared_folder_files = list_shared_folder_files(service, SHARED_FOLDER_ID)
        print(f"Files in shared folder: {shared_folder_files.keys()}")

        # Identify new files
        new_files_to_download = {}
        for file_name, file_id in shared_folder_files.items():
            if file_name not in indexed_files:
                new_files_to_download[file_name] = file_id

        print(f"New files to download: {new_files_to_download.keys()}")

        # Download new files and update the index
        for file_name, file_id in new_files_to_download.items():
            if download_file(service, file_id, file_name, DOWNLOAD_PATH):
                indexed_files.add(file_name)

        # Save the updated index
        save_index(service, INDEX_FILE_NAME, indexed_files)
        print(f"Updated indexed files: {indexed_files}")

    except HttpError as error:
        print(f'An error occurred: {error}')

if __name__ == '__main__':
    import google.auth
    import google_auth_httplib2
    import google_auth_oauthlib.flow
    import googleapiclient.http
    import io

    main()